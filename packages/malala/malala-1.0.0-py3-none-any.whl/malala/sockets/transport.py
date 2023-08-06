import json
from asyncio import StreamReader, StreamWriter
from typing import AsyncGenerator
from ..constants.sockets import B_DELIM, S_DELIM


class Transport:
    @staticmethod
    async def recv_bytes(reader: StreamReader) -> AsyncGenerator[bytes, None]:
        async for _bytes in reader:
            yield _bytes

    @staticmethod
    async def recv_str(reader: StreamReader) -> AsyncGenerator[str, None]:
        async for _bytes in reader:
            yield _bytes.decode().split(S_DELIM)[0]

    @staticmethod
    async def recv_json(reader: StreamReader) -> AsyncGenerator[dict, None]:
        async for _bytes in reader:
            yield json.loads(_bytes.decode().split(S_DELIM)[0])

    @staticmethod
    async def send_bytes(_bytes: bytes, writer: StreamWriter) -> None:
        writer.write(_bytes + B_DELIM)
        await writer.drain()

    @staticmethod
    async def send_str(_str: str, writer: StreamWriter) -> None:
        writer.write(_str.encode() + B_DELIM)
        await writer.drain()

    @staticmethod
    async def send_json(_json: dict, writer: StreamWriter) -> None:
        writer.write(json.dumps(_json).encode() + B_DELIM)
        await writer.drain()
