from twitchio.ext import commands
import asyncio
import random

class Bot(commands.Bot):
    """ Twitch IO PART """

    def __init__(self, token, loop=None, channels=['gunlinux']):
        loop = loop or asyncio.get_event_loop()
        super().__init__(token=token, prefix='!',
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
