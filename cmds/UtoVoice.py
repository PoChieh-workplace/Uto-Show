
import asyncio
import youtube_dl
import discord
from discord.ext import commands
#import pafy

intents = discord.Intents.default()
intents.members = True

class UtoVoice(commands.Cog):
    '''
    def __init__(self, bot):
        self.bot = bot 
        self.song_queue = {}
        self.setup()

    def setup(self):
        for guild in self.bot.guilds:
            self.song_queue[guild.id] = []

    async def check_queue(self, ctx):
        if len(self.song_queue[ctx.guild.id]) > 0:
            await self.play_song(ctx, self.song_queue[ctx.guild.id][0])
            self.song_queue[ctx.guild.id].pop(0)

    async def search_song(self, amount, song, get_url=False):
        info = await self.bot.loop.run_in_executor(None, lambda: youtube_dl.YoutubeDL({"format" : "bestaudio", "quiet" : True}).extract_info(f"ytsearch{amount}:{song}", download=False, ie_key="YoutubeSearch"))
        if len(info["entries"]) == 0: return None

        return [entry["webpage_url"] for entry in info["entries"]] if get_url else info

    async def play_song(self, ctx, song):
        #url = pafy.new(song).getbestaudio().url
        ctx.voice_client.play(discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(url)), after=lambda error: self.bot.loop.create_task(self.check_queue(ctx)))
        ctx.voice_client.source.volume = 0.5

    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice is None:
            return await ctx.send("❌| 你不再語音裡面")

        if ctx.voice_client is not None:
            await ctx.voice_client.disconnect()

        await ctx.author.voice.channel.connect()

    @commands.command()
    async def leave(self, ctx):
        if ctx.voice_client is not None:
            return await ctx.voice_client.disconnect()

        await ctx.send("I am not connected to a voice channel.")

    @commands.command()
    async def play(self, ctx, *, song=None):
        if song is None:
            return await ctx.send("❌| 請輸入關鍵字")

        if ctx.voice_client is None:
            if ctx.author.voice is None:
                return await ctx.send("❌| 你不再語音裡面")
            else:
                if ctx.voice_client is not None:
                    await ctx.voice_client.disconnect()
                    await ctx.author.voice.channel.connect()
        # handle song where song isn't url
        if not ("youtube.com/watch?" in song or "https://youtu.be/" in song):
            await ctx.send(f"🔍正在搜尋 `{song}`")

            result = await self.search_song(1, song, get_url=True)

            if result is None:
                return await ctx.send(f"❌| :Shibanervous: 我找不到這首歌，換個關鍵字吧 ouo ，`已回報開發者`")

            song = result[0]

        if ctx.voice_client.source is not None:
            queue_len = len(self.song_queue[ctx.guild.id])

            if queue_len < 10:
                self.song_queue[ctx.guild.id].append(song)
                return await ctx.send(f"✅| 已加入 `{song}` 到清單中第 `{queue_len+1}` 項")

            else:
                return await ctx.send("❌| 我的記憶體快爆了，請稍後再試 :Shibanervous:，`已回報開發者`")

        await self.play_song(ctx, song)
        await ctx.send(f"正在播放：{song}")

    @commands.command()
    async def search(self, ctx, *, song=None):
        if song is None: return await ctx.send("❌| :Shibanervous: 你的關鍵字呢???")

        await ctx.send(f"🔍正在搜尋 `{song}`")

        info = await self.search_song(5, song)

        embed = discord.Embed(title=f"✅| 找到'{song}'了:", description="您可以使用這個連結來播放您想要play的歌曲\n", colour=discord.Colour.red())
        
        amount = 0
        for entry in info["entries"]:
            embed.description += f"[{entry['title']}]({entry['webpage_url']})\n"
            amount += 1
        guild = self.bot.get_guild(871573666637426738)
        autor = guild.get_member(561731559493861398)
        embed.set_footer(text=f"開發者：{autor}",icon_url=autor.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def queue(self, ctx): # display the current guilds queue
        if len(self.song_queue[ctx.guild.id]) == 0:
            return await ctx.send("❌| 沒有歌曲在清單中 :Shibanervous:，`已回報開發者`")

        embed = discord.Embed(title="🎶播放清單🎶", description="", colour=discord.Colour.dark_gold())
        i = 1
        for url in self.song_queue[ctx.guild.id]:
            embed.description += f"{i}) {url}\n"

            i += 1

        guild = self.bot.get_guild(871573666637426738)
        autor = guild.get_member(561731559493861398)
        embed.set_footer(text=f"開發者：{autor}",icon_url=autor.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def skip(self, ctx):
        if ctx.voice_client is None:
            return await ctx.send("❌| 哪來的歌? :Shibanervous:，`已回報開發者`")

        if ctx.author.voice is None:
            return await ctx.send("❌| 你不再語音裡面")

        if ctx.author.voice.channel.id != ctx.voice_client.channel.id:
            return await ctx.send("❌| 你的心沒有我")

        poll = discord.Embed(title=f"投票跳過 by - {ctx.author.name}#{ctx.author.discriminator}", description="**80% 語音裡的成員超過八成即跳過**", colour=discord.Colour.blue())
        poll.add_field(name="給我跳過", value=":white_check_mark:")
        poll.add_field(name="給我留下", value=":no_entry_sign:")
        poll.set_footer(text="15秒後結算")

        poll_msg = await ctx.send(embed=poll) # only returns temporary message, we need to get the cached message to get the reactions
        poll_id = poll_msg.id

        await poll_msg.add_reaction(u"\u2705") # yes
        await poll_msg.add_reaction(u"\U0001F6AB") # no
        
        await asyncio.sleep(15) # 15 seconds to vote

        poll_msg = await ctx.channel.fetch_message(poll_id)
        
        votes = {u"\u2705": 0, u"\U0001F6AB": 0}
        reacted = []

        for reaction in poll_msg.reactions:
            if reaction.emoji in [u"\u2705", u"\U0001F6AB"]:
                async for user in reaction.users():
                    if user.voice.channel.id == ctx.voice_client.channel.id and user.id not in reacted and not user.bot:
                        votes[reaction.emoji] += 1

                        reacted.append(user.id)

        skip = False

        if votes[u"\u2705"] > 0:
            if votes[u"\U0001F6AB"] == 0 or votes[u"\u2705"] / (votes[u"\u2705"] + votes[u"\U0001F6AB"]) > 0.79: # 80% or higher
                skip = True
                embed = discord.Embed(title="✅| 成功跳過", description="", colour=discord.Colour.green())

        if not skip:
            embed = discord.Embed(title="❌| 無法跳過", description="無法跳過本首音樂\n\n投票少於 `8成` ", colour=discord.Colour.red())

        guild = self.bot.get_guild(871573666637426738)
        autor = guild.get_member(561731559493861398)
        embed.set_footer(text=f"開發者：{autor}",icon_url=autor.avatar_url)

        await poll_msg.clear_reactions()
        await poll_msg.edit(embed=embed)

        if skip:
            ctx.voice_client.stop()


    @commands.command()
    async def pause(self, ctx):
        if ctx.voice_client.is_paused():
            return await ctx.send("❌| 無法跳過")

        ctx.voice_client.pause()
        await ctx.send("The current song has been paused.")

    @commands.command()
    async def resume(self, ctx):
        if ctx.voice_client is None:
            return await ctx.send("I am not connected to a voice channel.")

        if not ctx.voice_client.is_paused():
            return await ctx.send("I am already playing a song.")
        
        ctx.voice_client.resume()
        await ctx.send("The current song has been resumed.")
    

    '''
    pass
def setup(bot):
    bot.add_cog(UtoVoice(bot))