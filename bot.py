import discord
from discord.ext import commands
import json
import random
import os
import threading
import time
#import subprocess

intents = discord.Intents.all()

with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix='*',intents=intents)
#def fun1():
#    subprocess.call(['java', '-jar', 'JMusicBot.jar'])
@bot.event
async def on_ready():
    print("212bot已上線")
    game = discord.Game('散彈槍的炙天使 ')
    await bot.change_presence(status=discord.Status.idle, activity=game)
#    sing_thread = threading.Thread(target=fun1)
#    sing_thread.start()

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')
if __name__ == "__main__":
    bot.run(jdata['Token'])
