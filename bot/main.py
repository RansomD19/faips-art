import json
import nextcord
from nextcord.ext import commands, tasks
from dotenv import load_dotenv
import os
import json


def write_json(new_data, filename='img.json'):
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        file_data["gallery_data"].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent=4)


load_dotenv()
TOKEN = os.getenv("dsc_token")

bot = commands.Bot(command_prefix='.')


@bot.event
async def on_ready():
    print('ready')


@bot.command(aliases=['verify'])
async def test(ctx):
    channel = bot.get_channel(878585302053183498)

    pins = await channel.pins()
    art = pins[0].attachments[0]  # the work of art
    artist = pins[0].author  # the artist

    added_data = {"name": str(artist),
                  "image": str(art),
                  "avatar": str(artist.display_avatar)
                  }

    write_json(added_data)
    # for pin in pins:
    # if pin.attachments != []:
    # print(pin.attachments[0])


bot.run(TOKEN)
