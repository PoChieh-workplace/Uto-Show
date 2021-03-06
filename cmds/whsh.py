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
            [Button(style=ButtonStyle.blue,id="whsh1",emoji="ð",label=f"{guname}ä¼ºæå°å¼"),
            Button(style=ButtonStyle.blue,id="whsh2",emoji="ð¤",label="ææ³éè«æ©å¨äºº")],
            [Button(style=ButtonStyle.blue,id="whsh3",emoji="â¤ï¸âð¥",label=f"çµ¦äº{guname}éè«é£çµ"),
            Button(style=ButtonStyle.blue,id="whsh4",emoji="â",label="å¶ä»")]
        ]
        whshlead = [
            [Button(style=ButtonStyle.blue,id="signin", label="ð¥è¨»åçµ"),
            Button(style=ButtonStyle.blue,id="whshlove", label="ðæè¹æè¯")],
            [Button(style=ButtonStyle.blue,id="whshannouce", label="ð¢å®£å³æè¯"),
            Button(style=ButtonStyle.blue,id="whshfuck", label="ðé åæè¯")],
            [Button(style=ButtonStyle.blue,id="whshmusic", label="ð¶ðððððð¶"),
            Button(style=ButtonStyle.red,id="whshleadall", label="ðæè¦ææ")]
        ]

        whsh2text = ("ð¬è«å°æ©å¨äººéè«é£çµè²¼çµ¦ç®¡ç®¡ï¼ä¸¦ç©è«èå¿ç­å¾å¯©æ ¸ï¼\nð¤è¥è¦éè«èªè£½æ©å¨äººï¼è«éå ä¸æ©å¨äººç¨å¼ç¢¼")
        invitembed = discord.Embed(title=f"{guname}éè«é£çµ", description="https://discord.gg/dghmdEhDvv", color=0xb494ff)
        whsh4text = ("âæ­¡è¿è <@&910351390122078239> æåºå¦ï¼å¯ä»¥æ¯é»å­ï¼ä¹å¯ä»¥æ¯å¶ä»æ³èªªçè©±")


        signintext = ("å¯ å¨ <#911520540756410429> ä¸­ é¸ æ æ³ è¦ ç ä¸» é¡ ð§ ,\næåææä¾ç¸å°æçé »é,\nä½¿ç¨æ¹å¼ï¼åªè¦é»æèº«åçµå°æçç¬¦èå³å¯æ°å¢â\nå¦æåæé¸æï¼åé»æä¸æ¬¡ç¬¦èå³å¯åªé¤â")
        lovetext = ("<#910384305518297098> çºå¿åç³»çµ±ï¼ä½¿ç¨æä»¤å¦ä¸ï¼\n\n1. ð¬ ç´æ¥å¨ ðæè¹æè¯ ä¸çè¨\n\nç£çé·ææ¿æçè¨ï¼\nä½ææå é»è¦å»¶é² ç¢ç0.1ç§é²é ­çé¢¨éª :suiwtf: ï¼\nèä¸å¦æéç¼è(æ)å¨é²è¡æ´æ°æï¼\nä½ å°±æå®å¨é²é ­ :stupid:\n\n\n2.ð¬  ç§è <@871569806439088208> æ\nå¶ä»æ <@871569806439088208> å¨çä¼ºæå¨ï¼\nä½¿ç¨æä»¤ï¼\n\ncf (çè¨)  æ  *cf (çè¨) \nâ è½é¿åé²é ­é¢¨éªç å³éè¨æ¯è³çé¢\n\n\ncfset (æ±ç¨±)  æ *cfset (æ±ç¨±) æ *cs (æ±ç¨±)\n:thonk: å¦ææ±ç¨±ä¸æå¤æ¼ï¼å¯æ´æ¹ä½ çå¿ç¨±\nè¥æ­¤æä»¤ä¸å¡«æ±ç¨±ï¼æä»¥é¨æ©æ¸å­æ¿ä»£\n p.s.æç¸ä¿¡ä½ ä¸æå¨æè¹çé¢ç¨æ­¤æä»¤(éç¶å¯ä»¥ç¨\n\ncfsearch  æ  *cfsearch æ  *cfs\næ¥è©¢ç¶åä½¿ç¨æ±ç¨±\n\n\nBetaçï¼å¦æbugè«ä½¿ç¨ \ntalkauthor (é¯èª¤å§å®¹)  æä»¤åå ±æï¼è¬è¬ä½ ")
        annoucetext = ("<#912637208991793162> å¯å®£å³è¨± **é¤äºææ¶å:underage:ç¸éä»¥å¤**çä»»ä½å§å®¹ï¼å¯ä»¥æ¯ åç æ æå­èªªæ\nä¹å¯ä½¿ç¨æç¥¨æä»¤ :inbox_tray: ï¼\nä½¿ç¨æ¹å¼ï¼ `&poll <æ¨é¡> <é¸é 1> <é¸é 2> [é¸é 3]...`\nè³å°éè¦å©åé¸é  æå¤18åé¸é \né¸é ä¸å¯éè¤ï¼å¦æé¸é ä¸­æ ç©ºç½éµä½¿ç¨ è«å ä¸ `""`\nex: \n```\n&poll æä¸»å¦ä½ å¾å¸¥ è¶å¸¥ éæ¯å¾å¸¥\n&poll ä»å¤©çæ©é¤åä»éº¼? \"è¥¿ç çå¥¶\" è ç±ç```")
        whshfuck = ("<#910471209525854238> ð»éç¼ä¸­ï¼\nä¹å¾å°æå¨æ­¤æ´æ° facebooké æ¯æè¯è²¼æï¼\næ­£å¨ç­å¾å°ç·¨æäºæ¬é")
        musictext = "å¯æ¼ <#910386094846136341> é»æ­ï¼\né³æ¨æä»¤ `&p ç¶²å(ééµå­)`"
        whshleadall = ("éç¼èä¸æ³å¯«äºï¼QQæ±å¹«")

        embed=discord.Embed(title="ä¼ºæå¼å°", description="**è«åæå¯ä»¥å¹«ä½ çéº¼**ï¼è«é»é¸ä¸æ¹æéðð»", color=0xff0000)
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
                            await interaction.respond(content=f"ä¼ºæå¼å°",components = whshlead)
                        else:
                            await interaction.respond(content=f"â| æ­¤æä»¤ä¸æ¯ç¨æ¼æ­¤")
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
        await ctx.send(f"â| æåæ´æå¿åidçº{tmpid}")
    @cfset.error
    async def cfset_error(self,ctx,error):
        if(isinstance(error,commands.errors.MissingRequiredArgument)):
            with open('return.json','r',encoding='utf8') as jfile:
                nid = json.load(jfile)
            tmpid = int(10000*random.random())
            nid['nickid'][ctx.author.name]=tmpid
            with open('return.json','w',encoding='utf8') as jfile:
                json.dump(nid,jfile,indent=4)
            await ctx.send(f"â| æåæ´æå¿åidçº{tmpid}")

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
                    await ctx.message.add_reaction('â')
                else:
                    try:
                        await ctx.message.delete()
                    except:
                        pass
                await channel.send('`'+str(x)+'` èªªï¼'+tmp)
    @commands.command(aliases=['gcf'])
    async def getcf(self,ctx):
        autor = self.bot.get_user(561731559493861398)
        if(autor==ctx.author):
            with open('return.json','r',encoding='utf8') as jfile:
                nid = json.load(jfile)
            x = nid['nickid']
            await ctx.send(f"```{x}```")
        else:
            await ctx.send("â| ä½ æ²ææ¬éä½¿ç¨æ­¤æä»¤")

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
        await ctx.send(f"â|ä½ çå¿åæ±ç¨±çºï¼{x}")
def setup(bot):
    bot.add_cog(WHSH(bot))