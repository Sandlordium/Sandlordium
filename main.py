from keep_alive import keep_alive
import discord
client = discord.Client()
import os


@client.event
async def on_ready():
    print("I'm in")
    print(client.user)

@client.event
async def on_message(message):
     if message.content.startswith('!sand'):
        msg = 'Sand is love, Sand is life'.format(message)
        await client.send_message(message.channel, msg)
     if message.author == client.user:
        return
     if message.content == "Sand":
        await client.send_message(message.channel, "Sand")
     if message.content == "sand":
       await client.send_message(message.channel, "sand")
     if message.content == "!help":
       await client.send_message(message.channel, "Sand = Sand, sand = sand, SAND = SAND, !sand = Sand is love, Sand is life, !sandpic = pic of sand, and !help for help. Want this bot on your own server? !invite for the link. Have any suggestions? Join my discord to suggest them here: https://discord.gg/ArrY3Jr")
     if message.content == "!sandpic":
       await client.send_message(message.channel, "https://imgur.com/gallery/3yHbF")
     if message.content == "SAND":
       await client.send_message(message.channel, "SAND")
     if message.content == "!invite":
       await client.send_message(message.channel, "https://discordapp.com/api/oauth2/authorize?scope=bot&client_id=535276186528645131")

keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
