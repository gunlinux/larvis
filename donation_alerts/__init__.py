import json
import socketio


class DonationApiSpace(socketio.AsyncClientNamespace):
    def __init__(self,  bot, token, channel="gunlinux"):
        self.bot = bot
        self.channel = channel
        self.token = token
        super().__init__(namespace=None)


    async def sendmsg(self, message):
        print('send message')
        chan = self.bot.get_channel(self.channel)
        await chan.send(message)

    async def on_connect(self):
        print('connect')
        await self.emit("add-user", {"token": self.token, "type": "alert_widget"})

    def on_disconnect(self):
        pass

    async def on_donation(self, data):
        print('donation event')
        data = json.loads(data)
        print(data)
        message = f"""О боги, да {data['username']} задонатил целых {data['amount']} {data['currency']} {data['message']}"""
        await self.sendmsg(message)


class DonationApi(object):
    """ donation alerts """
    def __init__(self, bot, token, channel="gunlinux"):
        self.sio = socketio.AsyncClient()
        self.state = DonationApiSpace(bot=bot, token=token)
        self.sio.register_namespace(self.state) # , bot=bot, token=token, channel=channel))

    async def start(self):
        await self.sio.connect("wss://socket.donationalerts.ru:443",
                          transports="websocket")
