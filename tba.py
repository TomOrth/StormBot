import json
import discord
from discord.ext import commands
import aiohttp
URL = 'http://www.thebluealliance.com/api/v2/'
HEADER_KEY = '?X-TBA-App-Id='
HEADER_VAL = 'frcTom:discord-bot:1'

description = "Gets team awards"
memeDesc = '''Used to generate a meme using a RESTful api
              Pass a template, top text, and bottom text
              
              Templates: tenguy, afraid, older, aag, tried, biw,
              blb, kermit, bd, ch, cbg, wonka, cb, keanu, dsm,live,
              ants, doge, alwaysonbeat, ermg, fwp, fa, fbf, fmr, fry,
              ggg, hipster, icanhas, crazypills, regret, boat, sohappy,
              captain, inigo, iw, ackbar, happening, joker, ive, ll, 
              morpheus, badchoice, mmm, jetpack, red, mordor, oprah,
              oag, remembers, philosoraptor, jw, sad-obama, sad-clinton,
              sadfrog, sad-bush, sad-boehner, sarcasticbear, dwight, sb,
              ss, sf, dodgson, money, sohot, awesome-awkward, awesome,
              awkward-awesome, fetch, success, ski, officespace,
              interesting, toohigh, bs, both, winter, xy, buzz, yodawg,
              yuno, yallgot, bad, elf, chosen'''
bot = commands.Bot(command_prefix="&", description=description)
data = ""
token = open("token.txt", "rb").read().decode("utf-8")


@bot.event
async def on_ready():
    print("Running bot")
    print(bot.user.name)
    print('-------')

@bot.command(description="pass team number to display awards for a given team")
async def awards(team : int):
    data = "" 
    with aiohttp.ClientSession() as session:
        async with session.get(URL + "team/frc" + str(team) + "/history/awards" + HEADER_KEY + HEADER_VAL) as resp:
            jData = json.loads(await resp.text())
            for i in range(len(jData)):
                data += "Event Key: " + jData[i]["event_key"] + ", Award Name: " + jData[i]["name"] + "\n"
    await bot.say(data)

@bot.command(description=memeDesc)
async def meme(template : str, upper : str, lower : str):
    await bot.say("http://memegen.link/" + template + "/" + upper + "/" + lower + ".jpg")

if __name__ == '__main__':
    bot.run(token[0:59])

