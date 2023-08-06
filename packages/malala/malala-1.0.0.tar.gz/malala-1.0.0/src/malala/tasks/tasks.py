import asyncio


class TaskManager:
    @staticmethod
    async def cancel_tasks(iterable) -> None:
        for task in iterable:
            task.cancel()

    @staticmethod
    async def monitor_event_loop(event_loop, timeout=10) -> set:
        async def _monitor(event_loop):
            while True:
                tasks = asyncio.all_tasks(event_loop)
                for task in tasks:
                    print(f"> {task.get_name()}, {task.get_coro()}")
                print(f"----------------------------------")
                await asyncio.sleep(timeout)

        task = asyncio.create_task(_monitor(event_loop), name="watchmen")
        return {task}
