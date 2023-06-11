import os
import random
import discord
from discord.ext import commands, tasks
from time import sleep
import secrets

# TODO: Make intents more specific
client = discord.Client(intents = discord.Intents.all())

dirname = os.path.dirname(os.path.realpath(__file__))

sounds = [
    os.path.join(dirname, "sounds", sound)
    for sound in os.listdir(os.path.join(dirname, "sounds"))
]

print(f"{len(sounds)} sounds found!")

@client.event
async def on_ready():
    print('{0.user} active'.format(client))
    check_vc.start();

@tasks.loop(seconds=300)
async def check_vc():
        for guild in client.guilds:
            if guild is None:
                print("Server not found")

                continue

            if random.randint(0, 5) == 1: # 1 in 6 chance
                print(guild)
                print(len(guild.members))
                print(guild.member_count)

                for member in guild.members:
                    print(member)

                    if member.voice is not None:
                        print("Member is in voice channel")

                        vc = await member.voice.channel.connect()
                        
                        def after_playing():
                            print("Finished playing")
                            vc.disconnect()
                        
                        vc.play(discord.FFmpegPCMAudio(random.choice(sounds)), after=lambda _: after_playing())

                        break

client.run(secrets.token)
