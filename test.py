import random
import asyncio
import secrets


async def waiter(id, count):
    print(f'{id}: came')
    for _ in range(count):
        print(f'{id}: work')
        r = random.random() * 2
        await asyncio.sleep(r)
        print(f'{id}: sleept: {r}')
    print(f'{id} done')


def looper(n, shifts=5):
    waiters = [waiter(i, shifts) for i in range(n)]
    wait_tasks = asyncio.wait(waiters)
    ioloop = asyncio.get_event_loop()
    ioloop.run_until_complete(wait_tasks)
    ioloop.close()


if __name__ == '__main__':
    print(secrets.SOME_SECRET)
