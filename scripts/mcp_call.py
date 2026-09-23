#!/usr/bin/env python3
"""星河文场 MCP 客户端调用工具"""

import os
import sys
import io
import json
import base64
import argparse
from pathlib import Path
from typing import Optional, Dict, Any
from urllib import request, error


def get_default_token() -> str:
    """获取 MCP API Token"""
    token = os.getenv("MCP_TOKEN", "").strip()
    if token:
        return token

    # 检查本地 .cursor/mcp.json
    cursor_mcp_path = Path.cwd() / ".cursor" / "mcp.json"
    if cursor_mcp_path.exists():
        try:
            data = json.loads(cursor_mcp_path.read_text(encoding="utf-8"))
            servers = data.get("mcpServers", {})
            for s in servers.values():
                url = s.get("url", "")
                if "token=" in url:
                    return url.split("token=")[-1].split("&")[0].strip()
        except Exception:
            pass

    # 检查本地 .env 文件
    env_path = Path.cwd() / ".env"
    if env_path.exists():
        try:
            for line in env_path.read_text(encoding="utf-8").splitlines():
                if line.startswith("MCP_TOKEN="):
                    return line.split("=", 1)[1].strip().strip('"').strip("'")
        except Exception:
            pass

    return ""


def compress_image_bytes(data_bytes: bytes, image_type: str, max_width: int = 1600, quality: int = 85) -> tuple[bytes, str]:
    """压缩图片并转换为 JPEG 格式"""
    try:
        from PIL import Image
        img = Image.open(io.BytesIO(data_bytes))

        # 封面尺寸与正文插图尺寸处理
        if image_type == "cover":
            # 封面标准分辨率 900x383
            if img.width > 900 or img.height > 383:
                img = img.resize((900, 383), Image.Resampling.LANCZOS)
        else:
            # 正文插图限制最大宽度
            if img.width > max_width:
                height = int(img.height * (max_width / img.width))
                img = img.resize((max_width, height), Image.Resampling.LANCZOS)

        # 转换色彩模式
        if img.mode in ("RGBA", "P"):
            bg = Image.new("RGB", img.size, (255, 255, 255))
            if img.mode == "RGBA":
                bg.paste(img, mask=img.split()[3])
            else:
                bg.paste(img)
            img = bg
        elif img.mode != "RGB":
            img = img.convert("RGB")

        out = io.BytesIO()
        img.save(out, format="JPEG", quality=quality, optimize=True)
        return out.getvalue(), "image/jpeg"
    except Exception:
        # 降级返回原始数据
        return data_bytes, "image/png"


def send_mcp_request(url: str, token: str, method: str, params: Dict[str, Any]) -> Dict[str, Any]:
    """向 MCP 服务端发送 JSON-RPC 请求"""
    endpoint = url.rstrip("/")
    if not endpoint.endswith("/messages") and not endpoint.endswith("/mcp"):
        endpoint = f"{endpoint}/messages"

    query_char = "&" if "?" in endpoint else "?"
    full_url = f"{endpoint}{query_char}token={token}"

    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": method,
        "params": params
    }

    req = request.Request(
        full_url,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        },
        method="POST"
    )

    try:
        with request.urlopen(req, timeout=30) as resp:
            resp_bytes = resp.read()
            return json.loads(resp_bytes.decode("utf-8"))
    except error.HTTPError as e:
        err_msg = e.read().decode("utf-8", errors="ignore")
        raise RuntimeError(f"HTTP 错误 ({e.code}): {err_msg}")
    except Exception as e:
        raise RuntimeError(f"请求失败: {e}")


def handle_upload_image_cli(args: argparse.Namespace) -> int:
    """处理图片上传子命令"""
    image_path = Path(args.file)
    if not image_path.exists():
        print(f"❌ 错误：文件不存在: {image_path}", file=sys.stderr)
        return 1

    token = args.token or get_default_token()
    if not token:
        print("❌ 错误：缺少 MCP Token。请通过 --token 或环境变量 MCP_TOKEN 指定。", file=sys.stderr)
        return 1

    raw_bytes = image_path.read_bytes()
    image_type = args.type.lower()

    # 压缩图片
    if not args.no_compress:
        data_bytes, mime_type = compress_image_bytes(raw_bytes, image_type=image_type)
    else:
        data_bytes = raw_bytes
        ext = image_path.suffix.lower().lstrip(".")
        mime_type = f"image/{ext}" if ext else "image/png"

    b64_str = base64.b64encode(data_bytes).decode("ascii")
    data_uri = f"data:{mime_type};base64,{b64_str}"

    filename = args.filename or image_path.name
    if not args.no_compress and not filename.lower().endswith(".jpg"):
        filename = f"{Path(filename).stem}.jpg"

    params = {
        "name": "upload_image",
        "arguments": {
            "image_data": data_uri,
            "image_type": image_type,
            "filename": filename
        }
    }

    try:
        res = send_mcp_request(args.url, token, "tools/call", params)
    except Exception as e:
        print(f"❌ 上传失败: {e}", file=sys.stderr)
        return 1

    if res.get("error"):
        print(f"❌ MCP 错误: {json.dumps(res['error'], ensure_ascii=False)}", file=sys.stderr)
        return 1

    result_data = res.get("result", {})
    if result_data.get("isError"):
        print(f"❌ 工具执行错误: {json.dumps(result_data, ensure_ascii=False)}", file=sys.stderr)
        return 1

    # 解析返回文本中的 JSON 数据
    contents = result_data.get("content", [])
    output_url = ""
    for c in contents:
        if c.get("type") == "text":
            try:
                parsed = json.loads(c.get("text", "{}"))
                output_url = parsed.get("url", "")
            except Exception:
                pass

    if args.json:
        print(json.dumps(result_data, ensure_ascii=False, indent=2))
    elif output_url:
        print(output_url)
    else:
        print(json.dumps(result_data, ensure_ascii=False))

    return 0


def handle_call_cli(args: argparse.Namespace) -> int:
    """通用工具调用子命令"""
    token = args.token or get_default_token()
    if not token:
        print("❌ 错误：缺少 MCP Token。请通过 --token 或环境变量 MCP_TOKEN 指定。", file=sys.stderr)
        return 1

    arguments = {}
    if args.arguments:
        try:
            arguments = json.loads(args.arguments)
        except Exception as e:
            print(f"❌ 错误：arguments 必须为合法 JSON 字符串: {e}", file=sys.stderr)
            return 1

    params = {
        "name": args.tool_name,
        "arguments": arguments
    }

    try:
        res = send_mcp_request(args.url, token, "tools/call", params)
    except Exception as e:
        print(f"❌ 请求失败: {e}", file=sys.stderr)
        return 1

    print(json.dumps(res, ensure_ascii=False, indent=2))
    return 0


def main():
    parser = argparse.ArgumentParser(description="星河文场 MCP 命令行客户端")
    parser.add_argument("--url", "-u", default=os.getenv("MCP_URL", "https://mp.soulsrc.com/mcp"), help="MCP 服务端地址")
    parser.add_argument("--token", "-k", default="", help="MCP API Token")

    subparsers = parser.add_subparsers(dest="command", help="子命令")

    # upload-image 子命令
    upload_parser = subparsers.add_parser("upload-image", help="上传图片至平台图床")
    upload_parser.add_argument("--file", "-f", required=True, help="本地图片路径")
    upload_parser.add_argument("--type", "-t", choices=["cover", "illustration"], default="cover", help="图片类型")
    upload_parser.add_argument("--filename", "-n", default="", help="保存文件名提示")
    upload_parser.add_argument("--no-compress", action="store_true", help="禁用自动压缩")
    upload_parser.add_argument("--json", action="store_true", help="输出完整 JSON 结果")

    # call 子命令
    call_parser = subparsers.add_parser("call", help="调用指定 MCP 工具")
    call_parser.add_argument("tool_name", help="工具名称")
    call_parser.add_argument("arguments", nargs="?", default="{}", help="工具入参 JSON 字符串")

    args = parser.parse_args()

    if args.command == "upload-image":
        sys.exit(handle_upload_image_cli(args))
    elif args.command == "call":
        sys.exit(handle_call_cli(args))
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
