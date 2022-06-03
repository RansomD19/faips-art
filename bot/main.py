import discord
import mysql.connector
from discord.ext import commands

token = "OTgxMjA5ODY2NjcwNjAwMjYy.GMebX4.1HR3tkrcEIlXB5cPY-XTwS6xiqOG2nd5bE1_So"
client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    print("Bot ready")
    global ping
    ping = f"{format(round(client.latency, 1))}ms"
    print(ping)


@client.command()
async def ping(ctx):
    ping = f"{format(round(client.latency, 1))}ms"
    print(ping)
    await ctx.send(ping)

# @client.event
# async def on_private_channel_pins_update(channel=817405524684308514, last_pin=None):
#     pins_list = await pins()
#     await channel.send()


@client.command()
async def test(ctx, index):
    channel = client.get_channel(817405524684308514)
    pins = await channel.pins()
    pins_count = len(pins)
    print(pins_count)
    await channel.send(f"{pins[int(index)].attachments.url} \n {pins[int(index)]}\n{pins_count}")


client.run(token)
