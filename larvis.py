import asyncio
from twitch import Bot
from donation_alerts_api import DonationApi
from secrets import ACCESS_TOKEN, DTOKEN

if __name__ == '__main__':
    ioloop = asyncio.new_event_loop()
    asyncio.set_event_loop(ioloop)
    bot = Bot(token=ACCESS_TOKEN, loop=ioloop)
    donation_api = DonationApi(bot=bot, token=DTOKEN)
    ioloop.create_task(donation_api.start())
    bot.run()
