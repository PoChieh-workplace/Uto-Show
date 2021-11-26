# load our local env so we dont have the token in public
import asyncio
from dotenv import load_dotenv
import psutil,os,discord
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from discord import TextChannel
from youtube_dl import YoutubeDL
import json

load_dotenv()

client = commands.Bot(command_prefix='.')

players = {}


def upjson():
    with open('music.json','r',encoding='utf8') as jfile:
        jata = json.load(jfile)


@client.event  # check if bot is ready
async def on_ready():
    print('Bot online')


@client.command()
async def join(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        await ctx.send(f'✅ | 嗨嗨 {channel.name}')

@client.command()
async def play(ctx, url):
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
    FFMPEG_OPTIONS = {
        'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    voice = get(client.voice_clients, guild=ctx.guild)
    channel = ctx.message.author.voice.channel
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    upjson()
    if not voice.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['url']
        voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        await ctx.send(f'✅ | 開始撥放 {url}')

    else:
        await ctx.send("🔧 | 清單式播放仍在開發")
        return


@client.command()
async def resume(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if not voice.is_playing():
        voice.resume()
        await ctx.send('▶️ | 繼續')


# command to pause voice if it is playing
@client.command()
async def pause(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        voice.pause()
        await ctx.send('⏸️ | 暫停')
    else:
        await ctx.send('❌ | 沒有歌可以停止')


# command to stop voice
@client.command()
async def stop(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        voice.stop()
        await ctx.send('⏹️ | 已停止')
    else:
        await ctx.send('❌ | 沒有歌可以停止')

@client.command()
async def disconnect(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)
    
    if voice and voice.is_connected():
        if voice.is_playing():
            voice.stop()
        await voice.disconnect()
        await ctx.send('👋🏻 | 掰掰')
    else:
        await ctx.send('😗 | 我沒有在語音裡')

@client.command(aliases=['memory'])
async def ram(ctx):
    def my_ram():
        process = psutil.Process(os.getpid())
        return (psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)

    memoryEmbed = discord.Embed(title="🔧 | 記憶體使用量", description=f"已使用 `{my_ram()}` MB", color=0x0000ff)
    await ctx.send(embed=memoryEmbed)







client.run("ODM4Nzk1NDAxMDY5ODU0NzUw.YJATFw.87s3pvdSdctDylHHpaKYkOeDgJY")