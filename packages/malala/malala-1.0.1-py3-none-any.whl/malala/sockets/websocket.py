import asyncio
import json
from typing import AsyncGenerator, Any
from ..constants.time import ONE_MIN


class WebSocket:
    @staticmethod
    async def _recv_raw(
        session: Any, uri: str, timeout: int = None
    ) -> AsyncGenerator[Any, None]:
        sleep_func, counter = lambda x: 2**x * 0.01, 0
        while True:
            try:
                counter = 0
                async with session.ws_connect(
                    uri, receive_timeout=timeout, heartbeat=ONE_MIN
                ) as ws:
                    async for msg in ws:
                        yield msg

            except Exception as e:
                sleep_time = sleep_func(counter)
                print(f"Error: {e}")
                print(f"Retrying in {sleep_time} seconds...")
                counter += 1
                # raise if sleep time reaches 12 seconds
                if sleep_time > 12:
                    raise e
                await asyncio.sleep(sleep_time)

    @staticmethod
    async def recv_str(
        session: Any, uri: str, timeout: int = None
    ) -> AsyncGenerator[str, None]:
        async for msg in WebSocket._recv_raw(session, uri, timeout):
            yield msg.data

    @staticmethod
    async def recv_json(
        session: Any, uri: str, timeout: int = None
    ) -> AsyncGenerator[dict, None]:
        async for msg in WebSocket._recv_raw(session, uri, timeout):
            yield json.loads(msg.data)

    @staticmethod
    async def send_str(session: Any, uri: str, payload: str) -> None:
        async with session.ws_connect(uri, heartbeat=ONE_MIN) as ws:
            await ws.send_str(payload)

    @staticmethod
    async def send_json(session: Any, uri: str, payload: dict) -> None:
        async with session.ws_connect(uri, heartbeat=ONE_MIN) as ws:
            await ws.send_json(payload)
