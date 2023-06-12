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
    check_vc.start()

@tasks.loop(seconds=300)
async def check_vc():
    for guild in client.guilds:
        if guild is None:
            print("Server not found")

            continue

        print(guild.name)

        if random.randint(0, 5) == 1: # 1 in 6 chance
            print("    Checking channels in server: " + guild.name)
            inhabitedChannels = []
            for channel in guild.voice_channels: # loop through channels in server

                if len(channel.members) > 0: # if it has people in it, add it to a list
                    print("           " + channel.name + " has " + str(len(channel.members)) + " members")
                    inhabitedChannels.append(channel)
            
            if len(inhabitedChannels) > 0: # if at least one of the channels has people
                channel: discord.guild.VoiceChannel = random.choice(inhabitedChannels) # pick a random inhabited channel
                
                print("Joining channel: " + channel.name + " in guild " + guild.name)
                vc = await channel.connect(timeout=5, reconnect=False) # join it
                
                print("Connected. Playing...")
                vc.play(discord.FFmpegPCMAudio(random.choice(sounds))) # play the sound

                # Sleep while audio is playing.
                while vc.is_playing():
                    sleep(.1)
                
                print("Finished playing")
                await vc.disconnect() # then disconnect when done
    print("Done")
    print("")

client.run(secrets.token)
