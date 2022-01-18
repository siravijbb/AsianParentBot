my_secret = os.environ['TOKEN']
import discord
from discord import FFmpegPCMAudio
import os
from discord.ext import commands
import nacl
client=discord.Client()
bad_word = ["You are gay","ugly","Your ass hole","sussy","amogus","terk"]
i_ll_send_you_to_jesus = ["sus","je","theP"]
i_ll_send_you_to_jesuse = ["https://tenor.com/view/i-will-send-you-to-jesus-asian-dad-i-will-slap-you-ray_strikes-steven-he-gif-22426705","https://tenor.com/view/steven-he-i-will-send-you-to-jezus-gif-24191118"]
prefix='%'

@client.event
async def on_message(message):
  msg = message.content
  mg=message.channel.send
  if message.author == client.user:
    return
  if any(word in msg for word in bad_word):
    await mg("https://tenor.com/view/steven-he-emotional-damage-steven-he-emotional-damage-gif-23428142")
  if any(word in msg for word in i_ll_send_you_to_jesus):
    await mg(i_ll_send_you_to_jesuse)
async def add(ctx,x:int,y:int):
  await ctx.send(x+y)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
@client.event
async def on_message(msg):
  if msg.author == client.user:
   return
  if msg.content.startswith("hello"):
   await msg.channel.send('hi')

@client.event
async def on_message(msg):
    if (msg.content.startswith(prefix+'join')):
        if (msg.author.voice): 
            channel = msg.author.voice.channel
            await channel.connect()
            await msg.channel.send('Bot joined')
        else: 
            await msg.channel.send("You must be in a voice channel first so I can join it.")

    elif msg.content.startswith(prefix+'dis'): 
        if (msg.guild.voice_client): 
            await msg.guild.voice_client.disconnect() 
            await msg.channel.send('Bot left')
        else: 
            await msg.channel.send("I'm not in a voice channel, use the join command to make me join")
@client.event
async def on_message(msg):
  if(msg.content.startswith(prefix+'attack')):
    if (msg.guild.voice_client):
      #play(source)
      await msg.channel.send("sus")
    else:
      channel = msg.author.voice.channel
      voice =await channel.connect()
      channel = msg.author.voice.channel
      source =FFmpegPCMAudio('jesus.mp3')
      player=voice.play(source)
      await msg.channel.send('Done')
  else:
     await msg.channel.send("")

@client.event

TOKEN = os.environ['TOKEN']
client.run(TOKEN)
