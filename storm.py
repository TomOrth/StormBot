
from tba import TBA
import discord
URL = 'http://www.thebluealliance.com/api/v3'
HEADER_KEY = '?X-TBA-App-Id='
HEADER_VAL = 'frcTom:discord-bot:1'

client = discord.Client()
prefix = "TBA"
token = open("token.txt", "rb").read().decode("utf-8")
req = TBA()
@client.event
async def on_ready():
    print('Connected!')
    print('Username: ' + client.user.name)
    print('ID: ' + client.user.id)

@client.event
async def on_message(message):
	if (prefix + " TEAM ") in message.content:
		result = message.content.split(" ")
		await client.send_message(message.channel, req.getTeamName(result[2]))
	if (prefix + " LOCATION ") in message.content:
		result = message.content.split(" ")
		await client.send_message(message.channel, req.getTeamLocation(result[2]))
	if (prefix + " ROBOT ") in message.content:
		result = message.content.split(" ")
		await client.send_message(message.channel, req.getRobot(result[2], result[3]))
	if (prefix + " AWARDS ") in message.content:
		result = message.content.split(" ")
		await client.send_message(message.channel, req.getAwards(result[2]))
	if ("water game") in message.content:
		await client.send_message(message.channel, "confirmed")

client.run(token[0:59])
