import asyncio
import os
from asyncio import StreamReader, StreamWriter
from typing import Callable, Tuple, Any
from ..constants.sockets import BUFFER_SIZE


class UnixSocket:
    @staticmethod
    async def start_server(
        handler: Callable[[StreamReader, StreamWriter], Any], path: str
    ) -> asyncio.AbstractServer:
        if os.path.exists(path):
            os.remove(path)

        return await asyncio.start_unix_server(handler, path, limit=BUFFER_SIZE)

    @staticmethod
    async def open_conn(path: str) -> Tuple[StreamReader, StreamWriter]:
        return await asyncio.open_unix_connection(path, limit=BUFFER_SIZE)

    @staticmethod
    async def close_conn(writer: StreamWriter) -> None:
        writer.close()
