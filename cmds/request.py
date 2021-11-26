import discord
from discord.ext import commands
from core.classes import Cog_Extension 

import requests
import facebook
import urllib3
import json

with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)


class request(Cog_Extension):
    @commands.command(aliases=['fb','fbpost'])
    async def fbupdate(self,ctx):
        token = jdata['fbchixingToken']
        took = facebook.GraphAPI(access_token=token, version = 2.12)
        getdata = took.request(f"/{jdata['fbchixingid']}?fields=posts.limit(1)")
        data = getdata['posts']['data'][0]
        time = str(data['created_time'])
        message = data['message']

        url = "https://www.facebook.com/"+ str(data['id'])
        embed=discord.Embed(title=":tada:最新貼文", description=f"{message}\n貼文發布時間：{time}\n [閱讀更多...]({url}) ", color=0x00ff64, timestamp=ctx.message.created_at)
        embed.set_footer(text="discord bot name : Uto , 現在時間:")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(request(bot))