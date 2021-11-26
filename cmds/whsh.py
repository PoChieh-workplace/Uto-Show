import discord
from discord.ext import commands
from core.classes import Cog_Extension
from discord_components import *
from discord import Client, guild, Embed
import json,random

class WHSH(Cog_Extension):
    @commands.command(aliases=['whsh','whhelp'])
    async def whshhelp(self,ctx):
        guild = self.bot.get_guild(910150769624358914)
        guname = guild.name
        whshhelp1 = [
            [Button(style=ButtonStyle.blue,id="whsh1",emoji="🔍",label=f"{guname}伺服導引"),
            Button(style=ButtonStyle.blue,id="whsh2",emoji="🤖",label="我想邀請機器人")],
            [Button(style=ButtonStyle.blue,id="whsh3",emoji="❤️‍🔥",label=f"給予{guname}邀請連結"),
            Button(style=ButtonStyle.blue,id="whsh4",emoji="❓",label="其他")]
        ]
        whshlead = [
            [Button(style=ButtonStyle.blue,id="signin", label="🥐註冊組"),
            Button(style=ButtonStyle.blue,id="whshlove", label="💓暈船文華")],
            [Button(style=ButtonStyle.blue,id="whshannouce", label="📢宣傳文華"),
            Button(style=ButtonStyle.blue,id="whshfuck", label="🎈靠北文華")],
            [Button(style=ButtonStyle.blue,id="whshmusic", label="🎶𝒎𝒖𝒔𝒊𝒄🎶"),
            Button(style=ButtonStyle.red,id="whshleadall", label="😈我要所有")]
        ]

        whsh2text = ("💬請將機器人邀請連結貼給管管，並煩請耐心等待審核，\n🤖若要邀請自製機器人，請附加上機器人程式碼")
        invitembed = discord.Embed(title=f"{guname}邀請連結", description="https://discord.gg/dghmdEhDvv", color=0xb494ff)
        whsh4text = ("❓歡迎與 <@&910351390122078239> 提出呦，可以是點子，也可以是其他想說的話")


        signintext = ("可 在 <#911520540756410429> 中 選 擇 想 要 的 主 題 🔧 ,\n我們會提供相對應的頻道,\n使用方式：只要點擊身分組對應的符號即可新增✅\n如果反悔選擇，再點擊一次符號即可刪除❌")
        lovetext = ("<#910384305518297098> 為匿名系統，使用指令如下：\n\n1. 💬 直接在 💓暈船文華 上留言\n\n監獄長會替換留言，\n但會有因電腦延遲 產生0.1秒露頭的風險 :suiwtf: ，\n而且如果開發者(我)在進行更新時，\n你就會完全露頭 :stupid:\n\n\n2.💬  私聊 <@871569806439088208> 或\n其他有 <@871569806439088208> 在的伺服器，\n使用指令：\n\ncf (留言)  或  *cf (留言) \n✅ 能避免露頭風險的 傳送訊息至版面\n\n\ncfset (暱稱)  或 *cfset (暱稱) 或 *cs (暱稱)\n:thonk: 如果暱稱不慎外漏，可更改你的匿稱\n若此指令不填暱稱，會以隨機數字替代\n p.s.我相信你不會在暈船版面用此指令(雖然可以用\n\ncfsearch  或  *cfsearch 或  *cfs\n查詢當前使用暱稱\n\n\nBeta版，如有bug請使用 \ntalkauthor (錯誤內容)  指令回報我，謝謝你")
        annoucetext = ("<#912637208991793162> 可宣傳許 **除了有涉及:underage:相關以外**的任何內容，可以是 圖片 或 文字說明\n也可使用投票指令 :inbox_tray: ，\n使用方式： `&poll <標題> <選項1> <選項2> [選項3]...`\n至少需要兩個選項 最多18個選項\n選項不可重複，如果選項中有 空白鍵使用 請冠上 `""`\nex: \n```\n&poll 服主如何 很帥 超帥 還是很帥\n&poll 今天的早餐吃什麼? \"西瓜 牛奶\" 蛋 熱狗```")
        whshfuck = ("<#910471209525854238> 💻開發中，\n之後將會在此更新 facebook靠杯文華貼文，\n正在等待小編授予權限")
        musictext = "可於 <#910386094846136341> 點歌，\n音樂指令 `&p 網址(關鍵字)`"
        whshleadall = ("開發者不想寫了，QQ求幫")

        embed=discord.Embed(title="伺服引導", description="**請問我可以幫你甚麼**，請點選下方按鈕👇🏻", color=0xff0000)
        await ctx.send(
            embed=embed,
            components = whshhelp1
        )
        if not isinstance(ctx.channel, discord.channel.DMChannel):
            while True:
                interaction = await self.bot.wait_for("button_click")
                if interaction.channel == ctx.channel:
                    responceid = interaction.component.id
                    if(responceid == "whsh1"):
                        if(ctx.guild.id==910150769624358914):
                            await interaction.respond(content=f"伺服引導",components = whshlead)
                        else:
                            await interaction.respond(content=f"❌| 此指令不是用於此")
                    if(responceid == "whsh2"):
                        await interaction.respond(content=whsh2text)
                    if(responceid == "whsh3"):
                        await interaction.respond(embed=invitembed)
                    if(responceid == "whsh4"):
                        await interaction.respond(content=whsh4text)
                    if(responceid == "signin"):
                        await interaction.respond(content=signintext)
                    if(responceid == "whshlove"):
                        await interaction.respond(content=lovetext)
                    if(responceid == "whshannouce"):
                        await interaction.respond(content=annoucetext)
                    if(responceid == "whshfuck"):
                        await interaction.respond(content=whshfuck)
                    if(responceid == "whshmusic"):
                        await interaction.respond(content=musictext)
                    if(responceid == "whshleadall"):
                        await interaction.respond(content=whshleadall)

    @commands.command(aliases=['cs'])
    async def cfset(self,ctx,msg):
        with open('return.json','r',encoding='utf8') as jfile:
                nid = json.load(jfile)
        tmpid = msg
        nid['nickid'][ctx.author.name]=tmpid
        with open('return.json','w',encoding='utf8') as jfile:
            json.dump(nid,jfile,indent=4)
        await ctx.send(f"✅| 成功更換匿名id為{tmpid}")
    @cfset.error
    async def cfset_error(self,ctx,error):
        if(isinstance(error,commands.errors.MissingRequiredArgument)):
            with open('return.json','r',encoding='utf8') as jfile:
                nid = json.load(jfile)
            tmpid = int(10000*random.random())
            nid['nickid'][ctx.author.name]=tmpid
            with open('return.json','w',encoding='utf8') as jfile:
                json.dump(nid,jfile,indent=4)
            await ctx.send(f"✅| 成功更換匿名id為{tmpid}")

    @commands.command()
    async def cf(self,ctx,*,msg):
        with open('return.json','r',encoding='utf8') as jfile:
            nid = json.load(jfile)
        guild = self.bot.get_guild(910150769624358914)
        channel = guild.get_channel(910384305518297098)
        #guild = self.bot.get_guild(901812673279303781)
        #channel = guild.get_channel(901812737389244436)
        try:
            x = nid['nickid'][ctx.author.name]
        except:
            tmpid = int(10000*random.random())
            nid['nickid'][ctx.author.name]=tmpid
            x = nid['nickid'][ctx.author.name]
            with open('return.json','w',encoding='utf8') as jfile:
                json.dump(nid,jfile,indent=4)
        if x!=-2:
            tmp = msg
            if(tmp.find('showme')==-1):
                if isinstance(ctx.channel, discord.channel.DMChannel):
                    await ctx.message.add_reaction('✅')
                else:
                    try:
                        await ctx.message.delete()
                    except:
                        pass
                await channel.send('`'+str(x)+'` 說：'+tmp)
    @commands.command(aliases=['gcf'])
    async def getcf(self,ctx):
        autor = self.bot.get_user(561731559493861398)
        if(autor==ctx.author):
            with open('return.json','r',encoding='utf8') as jfile:
                nid = json.load(jfile)
            x = nid['nickid']
            await ctx.send(f"```{x}```")
        else:
            await ctx.send("❌| 你沒有權限使用此指令")

    @commands.command(aliases=['cfs'])
    async def cfsearch(self,ctx):
        with open('return.json','r',encoding='utf8') as jfile:
            nid = json.load(jfile)
        guild = self.bot.get_guild(910150769624358914)
        channel = guild.get_channel(910384305518297098)
        #guild = self.bot.get_guild(901812673279303781)
        #channel = guild.get_channel(901812737389244436)
        try:
            x = nid['nickid'][ctx.author.name]
        except:
            tmpid = int(10000*random.random())
            nid['nickid'][ctx.author.name]=tmpid
            x = nid['nickid'][ctx.author.name]
            with open('return.json','w',encoding='utf8') as jfile:
                json.dump(nid,jfile,indent=4)
        await ctx.send(f"✅|你的匿名暱稱為：{x}")
def setup(bot):
    bot.add_cog(WHSH(bot))