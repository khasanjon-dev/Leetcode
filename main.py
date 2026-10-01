import asyncio

async def task_a():
    print("A: started")

    await asyncio.sleep(3)

    print("A: finished")


async def task_b():
    print("B: started")

    await asyncio.sleep(1)

    print("B: finished")


async def main():
    await asyncio.gather(
        task_a(),
        task_b(),
    )


asyncio.run(main())