import requests
import json
import discord
from discord.ext import commands
import aiohttp
URL = 'http://www.thebluealliance.com/api/v2/'
HEADER_KEY = '?X-TBA-App-Id='
HEADER_VAL = 'frcTom:discord-bot:1'

description = '''Gets team awards'''

bot = commands.Bot(command_prefix="&", description=description)

data = ""
@bot.event
async def on_ready():
    print("Running bot")
    print(bot.user.name)
    print('-------')

@bot.command()
async def info(cmd="desc"):
    if(cmd == "desc"):
        await bot.say("StormBot allows for more expansion of the TBA api that the FRCBot does not have.  Also will have more commands added to it.")
    elif(cmd == "awards"):
        await bot.say("Usage: &awards num\n prints out all awards for a given team number")

@bot.command()
async def awards(team : int):
    data = "" 
    with aiohttp.ClientSession() as session:
        async with session.get(URL + "team/frc" + str(team) + "/history/awards" + HEADER_KEY + HEADER_VAL) as resp:
            jData = json.loads(await resp.text())
            for i in range(len(jData)):
                data += "Event Key: " + jData[i]["event_key"] + ", Award Name: " + jData[i]["name"] + "\n"
    await bot.say(data)

bot.run("token")
