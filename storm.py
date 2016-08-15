from tba import TBA
import discord
URL = 'http://www.thebluealliance.com/api/v3'
HEADER_KEY = '?X-TBA-App-Id='
HEADER_VAL = 'frcTom:discord-bot:1'

client = discord.Client()
commandPrefix = "%"
prefix = "TBA"
token = open("token.txt", "rb").read().decode("utf-8")
req = TBA()
spammers = []
result = []
def isMod(roles):
    mod = False
    for x in range(len(roles)):
        if(roles[x].name == "Mods" or roles[x].name == "Admins" or roles[x].name == "Helpers"):
            mod = True
    return mod

@client.event
async def on_ready():
    print('Connected!')
    print('Username: ' + client.user.name)
    print('ID: ' + client.user.id)

@client.event
async def on_message(message):
    if(message.author.mention in spammers):
        await client.delete_message(message)
    if(message.content.startswith(commandPrefix + "block") and isMod(message.author.roles)):
        result = message.content.split(" ")
        spammers.append(result[1])
    if(message.content.startswith(commandPrefix + "unblock") and isMod(message.author.roles)):
        result = message.content.split(" ")
        spammers.remove(result[1])
        message.content = message.content.upper()
    if (prefix + " NAME ") in message.content:
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
        await client.send_message(message.channel, "Team " + result[2] + ":\n" + req.getAwards(result[2])) 
    if ("water game") in message.content:
        await client.send_message(message.channel, "confirmed")
    if (message.content.startswith(commandPrefix + "meme")):
        result = message.content.split(" ")
        await client.send_message(message.channel, "http://memegen.link/" + result[1] + "/" + result[2] + "/" + result[3] + ".jpg")
    if (message.content.startswith(commandPrefix + "eval")):
        result = message.content[6:len(message.content)]
        try:
            evaled = eval(result)
            if(evaled is not None or evaled is not "None"):
                await client.send_message(message.channel, evaled)
        except SyntaxError:
            exec(result)
    if (message.content.startswith(commandPrefix + "warn")):
        if (isMod(message.author.roles)):
            result = message.content.split(" ")
            await client.send_message(message.channel, result[1] + ": You have been warned for breaking a server rule!")
        else:
            await client.send_message(message.channel, "Your not a mod so no")
    if (message.content.startswith(commandPrefix + "mute")):
        if(isMod(message.author.roles)):
            result = message.content.split(" ")
            await client.add_roles(discord.utils.get(message.server.members, mention=result[1]), discord.utils.get(message.server.roles, name="muted"))
            await client.send_message(message.channel, result[1] + " you have been muted")
        else:
            await client.send_message(message.channel, "Your not a mod so no")
    if (message.content.startswith(commandPrefix + "unmute")):
       if(isMod(message.author.roles)):
           result = message.content.split(" ")
           await client.remove_roles(discord.utils.get(message.server.members, mention=result[1]), discord.utils.get(message.server.roles, name="muted"))
           await client.send_message(message.channel, result[1] + " you have been unmuted")
       else:
           await client.send_message(message.channel, "Your not a mod so no")

client.run(token[0:59])
