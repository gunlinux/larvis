from twitchio.ext import commands
from secrets import ACCESS_TOKEN
import random
import asyncio


class Bot(commands.Bot):

    def __init__(self, loop=None, channels=['gunlinux']):
        loop = loop or asyncio.get_event_loop()
        super().__init__(token=ACCESS_TOKEN, prefix='!',
                         initial_channels=channels, loop=loop)

    async def event_ready(self):
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')

    @commands.command()
    async def hello(self, ctx: commands.Context):
        # Send a hello back!
        print(f'Hello {ctx.author.name}!')
        await ctx.send(f'Hello {ctx.author.name}!')

    @commands.command()
    async def flipcoin(self, ctx: commands.Context):
        print('TOSS THE COIN')
        await ctx.send('Кидаю монетку')
        # Send a hello back!
        await asyncio.sleep(2)
        rez = 'орла' if random.randint(0, 1) else 'решку'
        await ctx.send(f'Монета легла на {rez}!')


async def wtf():
    print('started wtf')
    while(True):
        await asyncio.sleep(3)
        print('sleep more')


if __name__ == '__main__':
    ioloop = asyncio.get_event_loop()
    bot = Bot(loop=ioloop)
    ioloop.create_task(wtf())
    bot.run()
