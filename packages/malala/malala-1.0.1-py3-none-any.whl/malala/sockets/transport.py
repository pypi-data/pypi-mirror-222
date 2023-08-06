import json
from asyncio import StreamReader, StreamWriter
from typing import AsyncGenerator
from ..constants.sockets import DELIM


class Transport:
    @staticmethod
    async def recv_bytes(reader: StreamReader) -> AsyncGenerator[bytes, None]:
        async for _bytes in reader:
            yield _bytes[0:len(_bytes)-1]

    @staticmethod
    async def recv_str(reader: StreamReader) -> AsyncGenerator[str, None]:
        async for _bytes in reader:
            yield _bytes.decode()

    @staticmethod
    async def recv_json(reader: StreamReader) -> AsyncGenerator[dict, None]:
        async for _bytes in reader:
            yield json.loads(_bytes.decode())

    @staticmethod
    async def send_bytes(_bytes: bytes, writer: StreamWriter) -> None:
        writer.write(_bytes + DELIM)
        await writer.drain()

    @staticmethod
    async def send_str(_str: str, writer: StreamWriter) -> None:
        writer.write(_str.encode() + DELIM)
        await writer.drain()

    @staticmethod
    async def send_json(_json: dict, writer: StreamWriter) -> None:
        writer.write(json.dumps(_json).encode() + DELIM)
        await writer.drain()
