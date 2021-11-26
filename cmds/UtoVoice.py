from discord.ext import commands
import asyncio
from dotenv import load_dotenv
import discord
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from discord import TextChannel
from youtube_dl import YoutubeDL
from core.classes import Cog_Extension
import json

def upjson():
    with open('music.json','r',encoding='utf8') as jfile:
        jata = json.load(jfile)

class UtoVoice(Cog_Extension):
    load_dotenv()
    players = {}
    @commands.command(aliases=['connect'])
    async def join(self,ctx):
        channel = ctx.message.author.voice.channel
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()
            await ctx.send(f'✅ | 嗨嗨 {channel.name}')

    @commands.command(aliases=['p'])
    async def play(self,ctx, url):
        YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
        FFMPEG_OPTIONS = {
            'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        voice = get(self.bot.voice_clients, guild=ctx.guild)
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


    @commands.command(aliases=['replay','restart'])
    async def resume(self,ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)

        if not voice.is_playing():
            voice.resume()
            await ctx.send('▶️ | 繼續')

    @commands.command(aliases=['ps'])
    async def pause(self,ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)

        if voice.is_playing():
            voice.pause()
            await ctx.send('⏸️ | 暫停')
        else:
            await ctx.send('❌ | 沒有歌可以停止')


    # command to stop voice
    @commands.command(aliases=['sp'])
    async def stop(self,ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)

        if voice.is_playing():
            voice.stop()
            await ctx.send('⏹️ | 已停止')
        else:
            await ctx.send('❌ | 沒有歌可以停止')

    @commands.command(aliases=['leave'])
    async def disconnect(self,ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        
        if voice and voice.is_connected():
            if voice.is_playing():
                voice.stop()
            await voice.disconnect()
            await ctx.send('👋🏻 | 掰掰')
        else:
            await ctx.send('😗 | 我沒有在語音裡')

    
def setup(bot):
    bot.add_cog(UtoVoice(bot))