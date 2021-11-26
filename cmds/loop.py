import datetime,json,asyncio
import discord
from discord.ext import commands
from core.classes import Cog_Extension 
import requests
import facebook
import urllib3

with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)



class Loop(Cog_Extension):
    a = datetime.datetime.now().strftime('%Y %m %d %H')
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        async def time_task():
            await self.bot.wait_until_ready()
            now_time = datetime.datetime.now().strftime('%H')
            timer = int(now_time)-1
            while not self.bot.is_closed():
                now_time = int(datetime.datetime.now().strftime('%H'))
                if(not now_time==timer):
                    self.channel = self.bot.get_channel(901812737389244436)
                    timer = now_time
                    token = jdata['fbchixingToken']
                    took = facebook.GraphAPI(access_token=token, version = 2.12)
                    string = f"/{jdata['fbchixingid']}?fields=posts.limit(5)"
                    getdata = took.request(string)
                    for i in range(5):
                        data = getdata['posts']['data'][4-i]
                        timeid = str(data['id'])
                        if(timeid == jdata['nowchixingid']):
                            updateid = 4-i
                            break
                        else:
                            updateid = -1
                    jdata['nowchixingid'] = getdata['posts']['data'][0]['id']
                    with open('setting.json','w',encoding='utf8') as jfile:
                        json.dump(jdata,jfile,indent=4)
                    def embed(message,time,url):
                        embed=discord.Embed(title=f":tada:最新貼文", description=f"{message}\n貼文發布時間：{time}\n [閱讀更多...]({url}) ", color=0x00ff64)
                        embed.set_footer(text="discord bot name : Uto")
                        return embed
                    print("chixing："+ str(updateid))
                    if(updateid==-1):
                        for i in range(5):
                            data = getdata['posts']['data'][4-i]
                            message = data['message']
                            time = str(data['created_time'])
                            url = "https://www.facebook.com/"+ str(data['id'])
                            await self.channel.send(embed=embed(message,time,url))
                    elif(updateid==0):
                        pass
                    else:
                        for i in range(updateid):
                            data = getdata['posts']['data'][updateid-i-1]
                            message = data['message']
                            time = str(data['created_time'])
                            url = "https://www.facebook.com/"+ str(data['id'])
                            await self.channel.send(embed=embed(message,time,url))
                    

                    #for 靠北文華
                    
                    #self.channel = self.bot.get_channel(913004456029859840)
                    #token = jdata['fbwhshfuckToken']
                    #took = facebook.GraphAPI(access_token=token, version = 2.12)
                    #string = f"/{jdata['fbTHREE.KBWHSH']}?fields=posts.limit(100)"
                    #getdata = took.request(string)
                    #for i in range(100):
                    #    data = getdata['posts']['data'][100-i]
                    #    timeid = str(data['id'])
                    #    if(timeid == jdata['nowwhshfuckid']):
                    #        updateid = 100-i
                    #        break
                    #    else:
                    #        updateid = -1
                    #jdata['nowwhshfuckid'] = getdata['posts']['data'][0]['id']
                    #with open('setting.json','w',encoding='utf8') as jfile:
                    #    json.dump(jdata,jfile,indent=4)
                    #def embed(message,time,url):
                    #    embed=discord.Embed(title=f":tada:最新貼文", description=f"{message}\n貼文發布時間：{time}\n [閱讀更多...]({url}) ", color=0x00ff64)
                    #    embed.set_footer(text="discord bot name : Uto")
                    #    return embed
                    #print("whshfuck："+ str(updateid))
                    #if(updateid==-1):
                    #    for i in range(5):
                    #        data = getdata['posts']['data'][70-i]
                    #        message = data['message']
                    #        time = str(data['created_time'])
                    #        url = "https://www.facebook.com/"+ str(data['id'])
                    #        await self.channel.send(embed=embed(message,time,url))
                    #elif(updateid==0):
                    #    pass
                    #else:
                    #    for i in range(updateid):
                    #        data = getdata['posts']['data'][updateid-i-1]
                    #        message = data['message']
                    #        time = str(data['created_time'])
                    #        url = "https://www.facebook.com/"+ str(data['id'])
                    #        await self.channel.send(embed=embed(message,time,url))
                    #await asyncio.sleep(300)
                else:
                    await asyncio.sleep(300)
                    pass

        self.bg_task = self.bot.loop.create_task(time_task())
def setup(bot):
    bot.add_cog(Loop(bot))