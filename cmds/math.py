import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json
import math
with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class React(Cog_Extension):
    @commands.Cog.listener()
    async def on_message(self,msg):
        if msg.content.endswith('=') and msg.author != self.bot.user:
            try:
                a = msg.content
                e = a
                a = a.replace('x','*')
                for i in range(30):
                    if "^" in a:
                        b=""
                        c=""
                        d=""
                        pos=a.find('^')
                        c_long=0
                        for i in range(1,30):
                            if((a[(pos-i)])!="+" and (pos-i)>=0 and (a[(pos-i)])!="-" and (a[(pos-i)])!="*" and (a[(pos-i)])!="/"):
                                c = a[(pos-i):(pos)]
                                c_long+=1
                            else:
                                break
                        for i in range(1,30):
                            if(str.isdigit(a[(pos+i)])):
                                b += a[(pos+i)]
                            else:
                                d = a[(pos+i):]
                                a = a[:pos-c_long]
                                a += ("("+c)
                                for j in range(int(eval(b))-1):
                                    a += ("*"+c)
                                a += (")"+d)
                                break
                    else:
                        break
                for i in range(30):
                    if "sin" in a:
                        b = ""
                        pos=a.find('sin')
                        for i in range(30):
                            if((a[pos+i+4])!=')'):
                                b += a[pos+i+4]
                            else:
                                c = a[pos+i+5:]
                                a = a[:pos]
                                b = str(math.sin((math.pi/180)*eval(b)))
                                a += b
                                a += c
                                break
                    else:
                        break
                
                for i in range(30):
                    if "cos" in a:
                        b = ""
                        pos=a.find('cos')
                        for i in range(30):
                            if((a[pos+i+4])!=')'):
                                b += a[pos+i+4]
                            else:
                                c = a[pos+i+5:]
                                a = a[:pos]
                                b = str(math.cos((math.pi/180)*eval(b)))
                                a += b
                                a += c
                                break
                    else:
                        break
                for i in range(30):
                    if "tan" in a:
                        b = ""
                        pos=a.find('tan')
                        for i in range(30):
                            if((a[pos+i+4])!=')'):
                                b += a[pos+i+4]
                            else:
                                c = a[pos+i+5:]
                                a = a[:pos]
                                b = str(math.tan((math.pi/180)*eval(b)))
                                a += b
                                a += c
                                break
                    else:
                        break
                a = eval(a[:(len(a)-1)])
                a = round(a, 5)
                await msg.channel.send(f"{e}{a}")
            except:
                await msg.channel.send("❌| 計算錯誤")
        if msg.content.startswith('addbot') and msg.author != self.bot.user:
            guild = self.bot.get_guild(871573666637426738) 
            autor = guild.get_member(561731559493861398)
            a = msg.content
            author = msg.author
            guild = msg.guild
            a = a.replace('add','')
            await msg.channel.send(f"✅| 已向 {autor} 發出請求{a} 至 {guild}")
            embed=discord.Embed(title="請求", description=f"`{author}`請求在`{guild}`邀請`{a}`", color=0xff6842)
            await autor.send(embed=embed)
        if msg.content.startswith('talkauthor') and msg.author != self.bot.user:
            guild = self.bot.get_guild(871573666637426738) 
            autor = guild.get_member(561731559493861398)
            a = msg.content
            author = msg.author
            guild = msg.guild
            a = a.replace('talkauthor','')
            await msg.channel.send(f"✅| 已轉達 {autor} `{a}`")
            embed=discord.Embed(title="轉達", description=f"{author}：`{a}`", color=0xff6842)
            await autor.send(embed=embed)
        if msg.content.startswith('getpart') and msg.author != self.bot.user:
            guild = self.bot.get_guild(871573666637426738) 
            autor = guild.get_member(561731559493861398)
            a = msg.content
            author = msg.author
            guild = msg.guild
            a = a.replace('getpart','')
            await msg.channel.send(f"✅| 已請求 `{autor}` 審核 `{author}` 加入`{a}`身分組")
            embed=discord.Embed(title="身分組請求", description=f"`{author}`：請求於 `{guild}` 更改身分組 `{a}`", color=0xff6842)
            await autor.send(embed=embed)

def setup(bot):
    bot.add_cog(React(bot))