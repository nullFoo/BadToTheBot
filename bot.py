import os
import random
import discord
from discord.ext import commands, tasks
from random import randint, choice
from time import sleep
import secrets
client = discord.Client(intents = discord.Intents.all())

dirname = os.path.dirname(os.path.realpath(__file__))

sounds = [
    os.path.join(dirname, "sounds", sound)
    for sound in os.listdir(os.path.join(dirname, "sounds"))
]

print(f"{len(sounds)} sounds found!")

@client.event
async def on_ready():
    print('{0.user} Active'.format(client))
    check_vc.start();

@tasks.loop(seconds=300)
async def check_vc():
        for guild in client.guilds:
            if(guild is None):
                print("server not found")
                return;
            if(randint(0,5) == 1): # randomly
                print(guild)
                print(len(guild.members))
                print(guild.member_count)
                for m in guild.members:
                    print(m)
                    if(not(m.voice is None)):
                        print("is in voice")
                        voice_channel = m.voice.channel;
                        vc = await voice_channel.connect()
                        vc.play(discord.FFmpegPCMAudio(random.choice(sounds)), after=lambda e: print('done', e))
                        # Sleep while audio is playing.
                        while vc.is_playing():
                            sleep(.1)
                        await vc.disconnect()
                        break;

client.run(secrets.token)
