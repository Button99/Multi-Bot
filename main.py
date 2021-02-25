import discord
import os
import urllib.parse, urllib.request, re

# from StayOpen import StayOpen python program to keep up the bot 24/7

client= discord.Client()

@client.event
async def on_ready():
  print("Logged in as {0.user}". format(client))

@client.event
async def on_message(message):
  if(message.author == client.user):
    return
  
  msg= message.content

  if(msg.startswith("$find")):
    try:
      search= msg.split("$find", 1)[1]

      queryString= urllib.parse.urlencode({
          "search_query": search
      })

      html_content= urllib.request.urlopen(
          "http://www.youtube.com/results?" + queryString
      )

      searchResults= re.findall(r"watch\?v=(\S{11})", html_content.read().decode())
    
      await message.channel.send("http://www.youtube.com/watch?v="+ searchResults[0])

    except IndexError as e:
      await message.channel.send("Cant find something :( try again")


# StayOpen()
# Token auth 
client.run(os.getenv("TOKEN"))