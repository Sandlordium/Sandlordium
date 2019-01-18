from keep_alive import keep_alive
import discord
client = discord.Client()
import os
import random as rand



@client.event
async def on_ready():
    print("Sandbot is doing sandy things")
    print(client.user)

@client.event
async def on_message(message):
     if message.author == client.user:
        return
     if message.content == "Sand":
        await client.send_message(message.channel, "Sand")
     if message.content == "sand":
       await client.send_message(message.channel, "sand")
     if message.content == "+help":
       await client.send_message(message.channel, "```Sand = Sand, sand = sand, SAND = SAND, !picsand = pic of sand, and +help for help. Need some cool facts about sand? !sandfact. Want this bot on your own server? !invite for the link. Have any suggestions? Join my discord to suggest them here: https://discord.gg/ArrY3Jr```")

     if message.content == "!picsand":
       num = rand.randint(1, 5)
       if num == 1:
         await client.send_message(message.channel, "https://cdn.discordapp.com/attachments/535277257724526606/535517859535781889/1547747796206660062895632131693.jpg")
       if num == 2:
         await client.send_message(message.channel, "https://cdn.discordapp.com/attachments/535277257724526606/535517722386104321/15477477539757057786695983493433.jpg")
       if num == 3:
         await client.send_message(message.channel, "https://cdn.discordapp.com/attachments/535288818694225920/535389865932750848/image0.jpg")
       if num == 4:
         await client.send_message(message.channel, "https://i.redd.it/7azfkec6sve11.jpg")
       if num == 5:
         await client.send_message(message.channel, "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/Libya_4608_Idehan_Ubari_Dunes_Luca_Galuzzi_2007.jpg/1200px-Libya_4608_Idehan_Ubari_Dunes_Luca_Galuzzi_2007.jpg")

     if message.content == "SAND":
       await client.send_message(message.channel, "SAND")
     if message.content == "!invite":
       await client.send_message(message.channel, "https://discordapp.com/api/oauth2/authorize?scope=bot&client_id=535276186528645131")

     if message.content == "!suggestion":
       await client.send_message(message.channel, "Feel free to add any suggestions in #suggestion or if you have any issues head on over to the github page to open an issue here: https://github.com/samuelfuller01/Sandbot/issues.")
       
     if message.content == "what is sand?":
       await client.send_message(message.channel, "```Sand is a granular material composed of finely divided rock and mineral particles. It is defined by size, being finer than gravel and coarser than silt. Sand can also refer to a textural class of soil or soil type; i.e., a soil containing more than 85 percent sand-sized particles by mass. Source: https://en.wikipedia.org/wiki/Sand```")
     if message.content == "What is sand?":
       await client.send_message(message.channel, "```Sand is a granular material composed of finely divided rock and mineral particles. It is defined by size, being finer than gravel and coarser than silt. Sand can also refer to a textural class of soil or soil type; i.e., a soil containing more than 85 percent sand-sized particles by mass. Source: https://en.wikipedia.org/wiki/Sand```")
     if message.content == "What is sand":
       await client.send_message(message.channel, "```Sand is a granular material composed of finely divided rock and mineral particles. It is defined by size, being finer than gravel and coarser than silt. Sand can also refer to a textural class of soil or soil type; i.e., a soil containing more than 85 percent sand-sized particles by mass. Source: https://en.wikipedia.org/wiki/Sand```")
     if message.content == "what is sand":
       await client.send_message(message.channel, "```Sand is a granular material composed of finely divided rock and mineral particles. It is defined by size, being finer than gravel and coarser than silt. Sand can also refer to a textural class of soil or soil type; i.e., a soil containing more than 85 percent sand-sized particles by mass. Source: https://en.wikipedia.org/wiki/Sand```")

     if message.content == "!sandfact":
       num2 = rand.randint(1, 9)
       if num2 == 1:
        await client.send_message(message.channel, "Sand is a group of rocks and minerals that have eroded into fine, minuscule grains; and large quantities of the substance is often found on coastlines and in desert areas.")
       if num2 == 2:
         await client.send_message(message.channel,"Sand can be composed of a variety of items, including particles of calcium carbonate, coral, quartz and shellfish.")
       if num2 == 3:
         await client.send_message(message.channel, "Sand can be composed of a variety of items, including particles of calcium carbonate, coral, quartz and shellfish.")
       if num2 == 4:
         await client.send_message(message.channel, "A sand grain can be defined as a particle that is between 0.06 and 2 millimetres (0.002 and 0.08 of an inch) in diameter, and is smaller than a piece of gravel but larger than a speck of silt.")
       if num2 == 5:
         await client.send_message(message.channel, "The colour of sand varies greatly, depending on its location and the rocks and minerals that make up the particles, although it is commonly observed to be white, brown, tan, cream, red, grey or black.")
       if num2 == 6:
         await client.send_message(message.channel, "The unique shape of a piece of sand can help determine its source and age, while more pronounced angles often indicate a more recently formed grain.")
       if num2 == 7: 
         await client.send_message(message.channel, "Sand is one of the primary components of soil, and the ratio of sand to clay and silt, partly determines the quality of the soil.")
       if num2 == 8:
         await client.send_message(message.channel, "Dry sand can be dangerous if inhaled")
       if num2 == 9:
         await client.send_message(message.channel, "Sand has many applications and is used for concrete and brick making; is the main ingredient in glass making; and is often used for entertainment purposes, especially by children to play in, or make __**sand castles**__ or other structures, due to its ability to be shaped when damp.")
    
     

    

keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
