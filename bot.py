import discord
from discord.ext import commands, tasks
from random import randint, choice
from time import sleep
client = discord.Client(intents = discord.Intents.all())

@client.event
async def on_ready():
    print('{0.user} Active'.format(client))
    check_vc.start();

@tasks.loop(seconds=300)
async def check_vc():
    if(randint(0,5) == 1): # randomly
        guild = client.get_guild(810395486874894348)
        if(guild is None):
            print("server not found")
            return;
        print(guild)
        print(len(guild.members))
        print(guild.member_count)
        for m in guild.members:
            print(m)
            if(not(m.voice is None)):
                print("is in voice")
                voice_channel = m.voice.channel;
                vc = await voice_channel.connect()
                vc.play(discord.FFmpegPCMAudio('C:\\Users\\Amir\\Desktop\\Serious-Programming\\Stuff\\Bots\\BadToTheBone\\audio.mp3'), after=lambda e: print('done', e))
                # Sleep while audio is playing.
                while vc.is_playing():
                    sleep(.1)
                await vc.disconnect()
                break;

client.run('MTA3NDkyNTUxNzA3MDkzNDA2Ng.G49lCY.FK3aV0IKJSmU92WT3HZUt9LuAeBBFuulhPciZM')