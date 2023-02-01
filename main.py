import discord
import os
from StayOpen import StayOpen
from FindQuote import findQuote
from FindYt import findYt

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if (message.author == client.user):
        return

    msg = message.content

    if (msg.startswith("$find")):
        search = msg.split("$find", 1)[1]
        res = findYt(msg)
        await message.channel.send(res)

    if (msg.startswith("$quote")):
        try:
            msgRes = findQuote()
            await message.channel.send(msgRes)
        except:
            await message.channel.send("Wait a lil bit :/")


StayOpen()
client.run(os.getenv("TOKEN"))
