import asyncio
import os
from twitch import Bot
from donation_alerts import DonationApi


if __name__ == '__main__':
    ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
    DTOKEN = os.environ.get('DTOKEN')
    ioloop = asyncio.new_event_loop()
    asyncio.set_event_loop(ioloop)
    bot = Bot(token=ACCESS_TOKEN, loop=ioloop)
    donation_api = DonationApi(bot=bot, token=DTOKEN)
    ioloop.create_task(donation_api.start())
    bot.run()
