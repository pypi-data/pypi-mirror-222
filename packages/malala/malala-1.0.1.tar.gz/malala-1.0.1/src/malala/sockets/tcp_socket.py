import asyncio
from asyncio import StreamReader, StreamWriter
from typing import Callable, Tuple, Any


class TcpSocket:
    @staticmethod
    async def start_server(
        handler: Callable[[StreamReader, StreamWriter], Any], host: str, port: int
    ) -> asyncio.AbstractServer:
        raise NotImplementedError

    @staticmethod
    async def open_conn(str: str, port: int) -> Tuple[StreamReader, StreamWriter]:
        raise NotImplementedError

    @staticmethod
    async def close_conn(writer: StreamWriter) -> None:
        raise NotImplementedError
