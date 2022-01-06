from twitchio.ext import commands
from secrets import ACCESS_TOKEN, DTOKEN
import random
import asyncio
import json
from donationalerts_api.asyncio_api import sio


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

    @commands.command()
    async def ssend(self, mssg, ctx: commands.Context):
        await ctx.send(mssg)


ioloop = asyncio.get_event_loop()
bot = Bot(loop=ioloop)


@sio.on("connect")
async def on_connect():
    print('connect event')
    await sio.emit("add-user", {"token": DTOKEN,
                   "type": "alert_widget"})


async def sendmsg(mssg, channel="gunlinux"):
    chan = bot.get_channel(channel)
    await chan.send(mssg)


@sio.on("donation")
async def on_message(data):
    print('donation event')
    data = json.loads(data)
    mssg = f"""О боги, да {data['username']} задонатил
целых {data['amount']} {data['currency']} {data['message']}"""
    print(mssg)
    await sendmsg(mssg)


async def donationalerts_connect():
    print('wtf start')
    await sio.connect("wss://socket.donationalerts.ru:443",
                      transports="websocket")


if __name__ == '__main__':
    ioloop.create_task(donationalerts_connect())
    bot.run()
