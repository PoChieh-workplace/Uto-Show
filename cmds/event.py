import discord
from discord.ext import commands
from discord.ext.commands import errors
from core.classes import Cog_Extension
import json
from fake_useragent import UserAgent
import requests
import datetime

with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)
with open('command.json','r',encoding='utf8') as jfile:
    command = json.load(jfile)

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self,member):
        try:
            with open('welcome.json','r',encoding='utf8') as jfile:
                jwelcome = json.load(jfile)
            guild = self.bot.get_guild(member.guild.id)
            channel = self.bot.get_channel(int(jwelcome[f'{member.guild.id}.channel']))
            text = str(f"{jwelcome[f'{member.guild.id}.text']}")
            if "{member}" in text:
                pos=text.find('{member}')
                tmp = text[(pos+8):]
                text = text[:(pos)] + f'{member}' + tmp
            if "{guild}" in text:
                pos=text.find('{guild}')
                tmp = text[(pos+7):]
                text = text[:(pos)] + f'{guild}' + tmp
            embed=discord.Embed(title=text, color=0x0197f4)
            #channel = self.bot.get_channel(int(jdata['']))
            #embed=discord.Embed(title=f":tada:又有新成員 {member} :tada:拉！", description="歡迎歡迎", color=0x0197f4)
            await channel.send(embed=embed)
        except:
            pass

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        try:
            with open('welcome.json','r',encoding='utf8') as jfile:
                jwelcome = json.load(jfile)
            guild = self.bot.get_guild(member.guild.id)
            channel = self.bot.get_channel(int(jwelcome[f'{member.guild.id}.channel']))
            text = str(f"{jwelcome[f'{member.guild.id}.text2']}")
            if "{member}" in text:
                pos=text.find('{member}')
                tmp = text[(pos+8):]
                text = text[:(pos)] + f'{member}' + tmp
            if "{guild}" in text:
                pos=text.find('{guild}')
                tmp = text[(pos+7):]
                text = text[:(pos)] + f'{guild}' + tmp
            embed=discord.Embed(title=text, color=0x0197f4)
            await channel.send(embed=embed)
            #channel = self.bot.get_channel(int(jdata['212welcome']))
            #embed=discord.Embed(title=f":tada:又有新成員 @{member} :tada:離開了！", color=0x0197f4)
            #await channel.send(embed=embed)
        except:
            pass

    @commands.Cog.listener()
    async def on_message(self,msg):
        if msg.content == 'Uto' and msg.author != self.bot.user:
            embed=discord.Embed(title="已呼叫機器人", description="請問有什麼需要幫忙的呢", color=0xff6842)
            embed.add_field(name="1", value="申請更改身分組", inline=True)
            embed.add_field(name="2", value="請求邀請機器人", inline=True)
            embed.add_field(name="3", value="給予伺服器212邀請連結", inline=True)
            embed.add_field(name="4", value="檢舉", inline=True)
            embed.add_field(name="5", value="其他", inline=True)
            await msg.channel.send(embed=embed)
        if msg.content == '1' and msg.author != self.bot.user:
            embed=discord.Embed(title="回應1", description="請使用 `getpart <身分組>` 指令\nex：getpart 本班學生", color=0xff6842)
            await msg.channel.send(embed=embed)
        if msg.content == '2' and msg.author != self.bot.user:
            embed=discord.Embed(title="回應2", description="請使用 `addbot <機器人網址或名稱>` 指令並等待服主回應\nex：addbot yeecode", color=0xff6842)
            await msg.channel.send(embed=embed)
        if msg.content == '3' and msg.author != self.bot.user:
            embed=discord.Embed(title="回應3", description="https://discord.gg/c8CMDvBeEq", color=0xff6842)
            await msg.channel.send(embed=embed)
        if msg.content == '4' and msg.author != self.bot.user:
            embed=discord.Embed(title="回應4", description="請在下方留被檢舉名稱及原因，待服主查驗", color=0xff6842)
            await msg.channel.send(embed=embed)
        if msg.content == '5' and msg.author != self.bot.user:
            embed=discord.Embed(title="回應5", description="請使用 `talkauthor <想說的話>` 指令\nex：talkauthor 柏捷好帥", color=0xff6842)
            await msg.channel.send(embed=embed)


    @commands.Cog.listener()
    async def on_raw_reaction_add(self,data):
        channel = self.bot.get_channel(data.channel_id)
        message = channel.get_partial_message(data.message_id)
        if (str(data.emoji)==(str('🆗')) and (data.member)!=(self.bot.user)):
            embed=discord.Embed(title="本事件已結束 Done", description=f"已刪除此公告", color=0xa686fe, timestamp=datetime.datetime.now())
            embed.set_footer(text="discord bot name : Uto , 刪除時間:")
            msg = await message.edit(embed=embed)
            await message.clear_reactions()
        if (str(data.emoji)==(str('🤚')) and (data.member)!=(self.bot.user)):
            user = self.bot.get_user(data.user_id)
            embed=discord.Embed(title="感謝使用Uto", description=f"加入伺服器步驟", color=0xa686fe, timestamp=datetime.datetime.now())
            embed.add_field(name="說明", value=f"由於服主正在研究路由器阜口\n尚須使用hamachi輔助，\n加入帳號:_wpc.pp_\n密碼:_0_\nminecraft伺服位址_pochiehmc.ddns.net_")
            embed.set_footer(text="discord bot name : Uto , 說明時間:")
            msg = await user.send(embed=embed)
        if (str(data.emoji)==(str('⏩')) and (data.member)!=(self.bot.user)):
            #print(message.embeds.embed.title.fetch())
            #tes = message.fetch()
            #print(tes)
            text =""
            fr = int((int(command['count'])+int(command['count'])%2)/2)
            an = int(command['count'])
            for i in range(fr+1+100,an+1+100):
                text += str(f"\n{command[f'{i}']}\n")
            embed=discord.Embed(title="~ :book:指 令 總 覽 ~ command information(2/2)", description=f"{text}", color=0x00ff64, timestamp=message.created_at)
            embed.set_footer(text="discord bot name : Uto , 顯示時間:")
            msg = await message.edit(embed=embed)
            await message.clear_reactions()
            await msg.add_reaction('⏪')
        if (str(data.emoji)==(str('⏪')) and (data.member)!=(self.bot.user)):
            text =""
            an = int((int(command['count'])+int(command['count'])%2)/2)
            for i in range(101,an+1+100):
                text += str(f"\n{command[f'{i}']}\n")
            embed=discord.Embed(title="~ :book:指 令 總 覽 ~ command information(1/2)", description=f"{text}", color=0x00ff64, timestamp=message.created_at)
            embed.set_footer(text="discord bot name : Uto , 顯示時間:")
            msg = await message.edit(embed=embed)
            await message.clear_reactions()
            await msg.add_reaction('⏩')
        if (str(data.emoji)==(str('⬅️')) and (data.member)!=(self.bot.user)):
            text =""
            bn = int(command['count'])
            if(int(command['nowpage'])==1):
                command['nowpage'] = str(command['count'])
            else:
                command['nowpage'] = str(int(command['nowpage'])-1)
            with open('command.json','w') as jfile:
                    json.dump(command,jfile)
            an = int(command['nowpage'])
            text += str(f"{command[f'{an}']}")
            embed=discord.Embed(title=f"~ :book: 指 令 說 明 command information({an}/{bn}) ~", description=f":level_slider:指令 <必要函數> (非必要函數)\n{text}", color=0x00ff64, timestamp=message.created_at)
            embed.set_footer(text="discord bot name : Uto , 顯示時間:")
            msg = await message.edit(embed=embed)
            await msg.add_reaction('⬅️')
            await msg.add_reaction('➡️')
        if (str(data.emoji)==(str('➡️')) and (data.member)!=(self.bot.user)):
            text =""
            bn = int(command['count'])
            if(int(command['nowpage'])==int(command['count'])):
                command['nowpage'] = 1
            else:
                command['nowpage'] = str(int(command['nowpage'])+1)
            with open('command.json','w') as jfile:
                    json.dump(command,jfile)
            an = int(command['nowpage'])
            text += str(f"{command[f'{an}']}")
            embed=discord.Embed(title=f"~ :book: 指 令 說 明 command information({an}/{bn}) ~", description=f":level_slider:指令 <必要函數> (非必要函數)\n{text}", color=0x00ff64, timestamp=message.created_at)
            embed.set_footer(text="discord bot name : Uto , 顯示時間:")
            msg = await message.edit(embed=embed)
            await msg.add_reaction('⬅️')
            await msg.add_reaction('➡️')
        for i in range(201,212,1):
            if (str(data.emoji)==(str(command[f'{i}'])) and (data.member)!=(self.bot.user)):
                req = ""
                text = f"https://www.dcard.tw/service/api/v2/forums/{command[f'dcard{i-200}']}/posts?popular=true&limit=20"
                ua = UserAgent()
                user_agent = ua.random
                headers = {'user-agent': user_agent}
                r = requests.get(text,headers=headers)
                js = json.loads(r.text)
                req += f"**目前版類：**`{command[f'dcard{i-200}']}`\n🔹🔹🔹🔹🔹🔹🔹🔹\n"
                for j in js:
                    new = f"**{j['title']}**\n{j['excerpt']}...閱讀更多\n\n前往連結：https://www.dcard.tw/f/{command[f'dcard{i-200}']}/p/{j['id']} \n更新時間：`{j['updatedAt']}`\n🔸🔸🔸🔸🔸🔸🔸🔸\n"
                    if(len(req+new)>1930):
                        break
                    req += new
                req += f"\n\n\n變更版面請回覆表情符號\n🥺心情版\t❤️愛情版\t💬閒聊版\n👩女孩版\t🦹‍♂️追星版\t🥳有趣版\n🎀美妝版\t👚穿搭版\t🔧工作版\n😈梗圖版\t🍰美食版"
                msg = await message.edit(content=req)
                await message.clear_reactions()
                for i in range(201,212,1):
                    await msg.add_reaction(f"{command[f'{i}']}")

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self,data):
        if (str(data.emoji)==(str('⬅️')) and (data.member)!=(self.bot.user)):
            channel = self.bot.get_channel(data.channel_id)
            message = channel.get_partial_message(data.message_id)
            text =""
            bn = int(command['count'])
            if(int(command['nowpage'])==1):
                command['nowpage'] = str(command['count'])
            else:
                command['nowpage'] = str(int(command['nowpage'])-1)
            with open('command.json','w') as jfile:
                    json.dump(command,jfile)
            an = int(command['nowpage'])
            text += str(f"{command[f'{an}']}")
            embed=discord.Embed(title=f"~ :book: 指 令 說 明 command information({an}/{bn}) ~", description=f":level_slider:指令 <必要函數> (非必要函數)\n{text}", color=0x00ff64, timestamp=message.created_at)
            embed.set_footer(text="discord bot name : Uto , 顯示時間:")
            msg = await message.edit(embed=embed)
            await msg.add_reaction('⬅️')
            await msg.add_reaction('➡️')
        if (str(data.emoji)==(str('➡️')) and (data.member)!=(self.bot.user)):
            channel = self.bot.get_channel(data.channel_id)
            message = channel.get_partial_message(data.message_id)
            text =""
            bn = int(command['count'])
            if(int(command['nowpage'])==int(command['count'])):
                command['nowpage'] = 1
            else:
                command['nowpage'] = str(int(command['nowpage'])+1)
            with open('command.json','w') as jfile:
                    json.dump(command,jfile)
            an = int(command['nowpage'])
            text += str(f"{command[f'{an}']}")
            embed=discord.Embed(title=f"~ :book: 指 令 說 明 command information({an}/{bn}) ~", description=f":level_slider:指令 <必要函數> (非必要函數)\n{text}", color=0x00ff64, timestamp=message.created_at)
            embed.set_footer(text="discord bot name : Uto , 顯示時間:")
            msg = await message.edit(embed=embed)
            await msg.add_reaction('⬅️')
            await msg.add_reaction('➡️')


    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        if isinstance(error,commands.errors.MissingRequiredArgument):
            await ctx.send("❌|指令所輸入資料並不完全，可輸入*command了解更多")
        elif isinstance(error,commands.errors.CommandNotFound):
            await ctx.send("❌|查無此指令，可輸入*list了解更多")
        elif isinstance(error,commands.errors.CommandOnCooldown):
            await ctx.send("❌|指令時間限制，請稍後再試")
        else:
            guild = self.bot.get_guild(871573666637426738) 
            autor = guild.get_member(561731559493861398)
            embed=discord.Embed(title=f"❌|發生錯誤", description=f"Error：```{error}```\n已回報開發者", color=0x00e16e)
            embed.set_footer(text=f"開發者 {autor}",icon_url=autor.avatar_url)
            await ctx.send(embed=embed)
            embed=discord.Embed(title=f"❌|發生錯誤", description=f"Error：```{error}```\n發起指令者：{ctx.author}\n群組：{ctx.guild}\n頻道：{ctx.channel}", color=0x00e16e)
            embed.set_footer(text=f"開發者 {autor}",icon_url=autor.avatar_url)
            await autor.send(embed=embed)


def setup(bot):
    bot.add_cog(Event(bot))