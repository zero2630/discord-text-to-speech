import asyncio
from discord.ext import commands
from discord import Embed, FFmpegPCMAudio, Intents, Client
import requests
from bs4 import BeautifulSoup
from GetInfo import GetCitate, GetLink
import random
from TextToSpeech import Speak

intents = Intents.all()
bot = commands.Bot(command_prefix='-', intents=intents)

VoiceChannel = None
VoiceClient = None


@bot.command()
async def lightshot(context, times=1):
    if 0<times<11:
        for i in range(times):
            url = 'https://prnt.sc/'+ GetLink()
            await context.send(url)

@bot.command()
async def say(context, *, text:str):
    global VoiceChannel
    global VoiceClient
    VoiceChannel = context.author.voice.channel
    if VoiceChannel is not None:
        VoiceClient = await VoiceChannel.connect()
        Speak(text)
        VoiceClient.play(FFmpegPCMAudio(executable="E:\\discordBot\\ffmpeg-2023-04-30-git-e7c690a046-full_build\\bin\\ffmpeg.exe", source="text.mp3"))
        while VoiceClient.is_playing():
            await asyncio.sleep(0.1)
        await VoiceClient.disconnect()
        VoiceChannel = None
        VoiceClient = None
    else:
        await context.send("Ты не находишся в голосовом канале")

@bot.command()
async def s(context):
    global VoiceClient
    VoiceClient.stop()
    VoiceClient.disconnect()


bot.run('OTc1NzkyNDY0OTk4ODI2MDc0.GRrmKG.O66LCRavuQujCiC0grkbXFDkQNhUb9rGAaK5IU')