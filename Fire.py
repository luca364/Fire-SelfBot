#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import cogs
import time
import subprocess
import sys
import csv
from discord.ext.commands import MissingRequiredArgument
import hashlib
import re
import discord, ctypes, json, os, webbrowser, requests, datetime, urllib, time, string, random, asyncio, aiohttp
from discord.ext import commands
from colorama import Fore, Back, Style
from selenium import webdriver
import threading
import subprocess, requests, time, os
import discord, ctypes, json, os, webbrowser, requests, datetime, urllib, time, string, random, asyncio, aiohttp
from discord.ext import commands
from selenium import webdriver
import threading
import os.path
from pypresence import Presence
from urllib.request import Request, urlopen
import subprocess, requests, time, os
import praw
import uuid
import random
import threading
from threading import Thread
import string
import urllib3
urllib3.disable_warnings()
import asyncio
from discord.ext.commands import CommandNotFound
import colorama
from colorama import Fore, Style, Back
import time



colorama.init(autoreset=True)
coderegex = re.compile('(discord.com/gifts/|discordapp.com/gifts/|discord.gift/)([a-zA-Z0-9]+)')

m_offets = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1)
]

m_numbers = [
    ":one:",
    ":two:", 
    ":three:", 
    ":four:", 
    ":five:",       
    ":six:"
]


def tokeninvalid():
   os.remove("config.json")
   if os.name == "posix":
       os.system("python3 Fire.py")
       os._exit(0)


isthefilethere = os.path.isfile('config.json')
if(isthefilethere == False):
    print(f""" {Fore.YELLOW}

                                                  ______________  ______
                                                 / ____/  _/ __ \/ ____/
                                                / /_   / // /_/ / __/   
                                               / __/ _/ // _, _/ /___   
                                              /_/   /___/_/ |_/_____/ 
                                                                        

    """+Fore.RESET)
    prefix = input("Enter your bot prefix >> ")
    token = input("Enter your discord account token >> ")
    pass2 = input("Enter your discord account password (optional) >> ")
    theme = input("Now give your theme file name in your themes folder without .json >> ")
    data = {}
    data = ({
    'prefix': prefix,
    'token': token,
    'dcpassword': pass2,
    'richpresence': rich,
    'THEME': THEME,
    })
    with open('config.json', 'w+') as outfile:
        json.dump(data, outfile)
with open('./config.json', 'r') as cjson:
    config = json.load(cjson)
prefix = config["prefix"]
token = config["token"]
dcpassword = config["dcpassword"]
THEME = config["theme"]
client = commands.Bot(command_prefix = prefix, self_bot=True)
client.remove_command('help')
head = {"authorization":token, "user-agent":"Mozilla/5.0"}
url = 'https://discordapp.com/api/v8/users/@me'
r5 = requests.get(url, headers=head)
username = r5.json()
if os.name == 'nt':
    try:
        ctypes.windll.kernel32.SetConsoleTitleW(f"Fire SelfBot | Logged in as {username['username']}")
    except:
        tokeninvalid()
MSGDELETE = json.load(open(f"themes/{THEME}.json"))["msg_delete"]
PUREEMBEDCOLOR = json.load(open(f"themes/{THEME}.json"))["embed_color"]
EMBEDCOLOR = int(PUREEMBEDCOLOR.replace("#", "0x"), 0)
EMBEDIMAGE = json.load(open(f"themes/{THEME}.json"))["embed_image"]
EMBEDTITLE = json.load(open(f"themes/{THEME}.json"))["embed_title"]
GLOBALEMOJI = json.load(open(f"themes/{THEME}.json"))["global_emoji"]
EMBEDFOOTER = json.load(open(f"themes/{THEME}.json"))["embed_footer"]
EMBEDURL = json.load(open(f"themes/{THEME}.json"))["embed_url"]



print(f""" {Fore.YELLOW}


                                                  ______________  ______
                                                 / ____/  _/ __ \/ ____/
                                                / /_   / // /_/ / __/   
                                               / __/ _/ // _, _/ /___   
                                              /_/   /___/_/ |_/_____/ 

                                             Fire started sucesfully
                                             Version 1.0 Release
                                             Discord User : {username['username']}
                                             Your Prefix is: {prefix}
                                             Have Fun!

    """)
        
print(f"{Fore.YELLOW}")
        
for i in range(os.get_terminal_size().columns):
    print(f'{Fore.YELLOW}─', end='')

print('\n')


def RandString():
    return "".join(random.choice(string.ascii_letters + string.digits) for i in range(random.randint(4, 4)))

def Nitro():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f'https://discord.gift/{code}'    

client = commands.Bot(
    command_prefix=prefix,
    self_bot=True
)
#Here you can change the prefix for the commands (@Fire.command)
Fire = client
client.remove_command('help')


@Fire.command()
async def help(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title=EMBEDTITLE, color=EMBEDCOLOR)
    embed.set_thumbnail(url=EMBEDIMAGE)
    embed.add_field(name="", value="_ _", inline=True)
    embed.add_field(name=f"`{prefix}`**fun** » shows fun commands", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}` **mod** » shows moderation commands", value="_ _", inline=True)
    embed.add_field(name="Your Prefix is : ", value=f"{prefix}", inline=True)
    embed.set_footer(text=EMBEDFOOTER)
    await ctx.send(embed=embed, delete_after= 15)
    print(Fore.YELLOW + 'Command Used | help')


@Fire.command()
async def fun(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title=EMBEDTITLE, color=EMBEDCOLOR)
    embed.set_thumbnail(url=EMBEDIMAGE)
    embed.add_field(name="", value="_ _", inline=True)
    embed.add_field(name=f"`{prefix}`**fakenitro** » generates fakenitro (just troll)", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}` **rickroll** » rickroll @user", value="_ _", inline=True)
    embed.add_field(name=f"`{prefix}` **gp** » gp/ghostping @user", value="_ _", inline=True)
    embed.add_field(name=f"`{prefix}` **catbox** » do you love cats?", value="_ _", inline=True)
    embed.add_field(name=f"`{prefix}` **_ball** » 8ball", value="_ _", inline=True)
    embed.add_field(name=f"`{prefix}` **ascii** » Create a ascii text", value="_ _", inline=True)
    embed.add_field(name=f"`{prefix}` **nitroemojispoofer** » Use nitro emojis without nitro", value="_ _", inline=True)
    embed.add_field(name=f"`{prefix}` **cloneprofilepic** » cloneprofilepic @user", value="_ _", inline=True)
    embed.add_field(name=f"`{prefix}` **bait** » generates a rondom nitro code to span nitro snipers", value="_ _", inline=True)
    embed.add_field(name=f"`{prefix}` **fakedata** » generates a fake data", value="_ _", inline=True)
    embed.add_field(name="Your Prefix is : ", value=f"{prefix}", inline=True)
    embed.set_footer(text=EMBEDFOOTER)
    await ctx.send(embed=embed, delete_after= 15)
    print(Fore.YELLOW + 'Command Used | Fun')



@Fire.command()
async def Mod(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title=EMBEDTITLE, color=EMBEDCOLOR)
    embed.set_thumbnail(url=EMBEDIMAGE)
    embed.add_field(name="", value="_ _", inline=True)
    embed.add_field(name=f"`{prefix}`**nitrosniper** » nitro sniper on / off ( snipe nitro lol )", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}` **restart** » restarts the selfbot", value="_ _", inline=True)
    embed.add_field(name=f"`{prefix}` **discordfucker** » ducks a user token if you have them", value="_ _", inline=True)
    embed.add_field(name=f"`{prefix}` **botlogin** » login into a bot account", value="_ _", inline=True)
    embed.add_field(name="Your Prefix is : ", value=f"{prefix}", inline=True)
    embed.set_footer(text=EMBEDFOOTER)
    await ctx.send(embed=embed, delete_after= 15)
    print(Fore.YELLOW + 'Command Used | Moderation')  

@Fire.command()
async def fakenitro(ctx, server):
    await ctx.message.delete()
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    nitro= f'https://discord.gift/{code}'
    embed = discord.Embed(description="        ")
    embed.add_field(name="GG poor boy aou won Nitro", value=f"[{nitro}]({server})")
    embed.set_image(url="https://cdn.discordapp.com/attachments/827008716263522314/830714076480798780/a9ng95vvs8c41.png")
    await ctx.send(embed=embed)

@Fire.command(aliases=["rick"])
async def rickroll(ctx):
  await ctx.message.delete()
  message = await ctx.send(f'Were no stangers to love')
  time.sleep(1.5)
  await message.edit(content='You know the rules and so do I') 
  time.sleep(1.5)
  await message.edit(content='A full commitments what Im thinking of') 
  time.sleep(1.5)
  await message.edit(content='You wouldnt get this from any other guy') 
  time.sleep(1.5)
  await message.edit(content='I just wanna tell you how Im feeling') 
  time.sleep(1.5)
  await message.edit(content='Gotta make you understand') 
  time.sleep(1.5)
  await message.edit(content='Never gonna give you up') 
  time.sleep(1.5)
  await message.edit(content='Never gonna let you down') 
  time.sleep(1.5)
  await message.edit(content='Never gonna run around and desert you') 
  time.sleep(1.5)
  await message.edit(content='Never gonna make you cry')
  time.sleep(1.5)
  await message.edit(content='Never gonna say goodbye') 
  time.sleep(1.5)
  await message.edit(content='Never gonna tell a lie and hurt you') 
  time.sleep(1.5)
  await message.edit(content='We known each other for so long') 
  time.sleep(1.5)
  await message.edit(content='Your hearts been aching but your too shy to say it')
  time.sleep(1.5)
  await message.edit(content='Inside we both know whats been going on') 
  time.sleep(1.5)
  await message.edit(content='We know the game and were gonna play it')
  time.sleep(1.5)
  await message.edit(content='And if you ask me how Im feeling') 
  time.sleep(1.5)
  await message.edit(content='Dont tell me your too blind to see') 
  time.sleep(1.5)
  await message.edit(content='Never gonna give you up') 
  time.sleep(1.5)
  await message.edit(content='Never gonna let you down')
  time.sleep(1.5)
  await message.edit(content='Never gonna run around and desert you') 
  time.sleep(1.5)
  await message.edit(content='Never gonna make you cry')
  time.sleep(1.5)
  await message.edit(content='Never gonna say goodbye')
  time.sleep(1.5)
  await message.edit(content='Never gonna tell a lie and hurt you') 
  time.sleep(1.5)
  await message.edit(content='Never gonna give you up') 
  time.sleep(1.5)
  await message.edit(content='Never gonna let you down') 
  time.sleep(1.5)
  await message.edit(content='Never gonna run around and desert you') 
  time.sleep(1.5)
  await message.edit(content='Never gonna make you cry')
  time.sleep(1.5)
  await message.edit(content='Never gonna say goodbye') 
  time.sleep(1.5)
  await message.edit(content='Never gonna tell a lie and hurt you') 
  time.sleep(1.5)
  await message.edit(content='Never gonna give, never gonna give')
  time.sleep(1.5)
  await message.edit(content='(Give you up)') 
  time.sleep(1.5)
  await message.edit(content='(Ooh) Never gonna give, never gonna give') 
  time.sleep(1.5)
  await message.edit(content='(Give you up)')
  time.sleep(1.5)
  await message.edit(content='We known each other for so long') 
  time.sleep(1.5)
  await message.edit(content='Your hearts been aching but your too shy to say it')
  time.sleep(1.5)
  await message.edit(content='Inside we both know whats been going on') 
  time.sleep(1.5)
  await message.edit(content='We know the game and we gonna play it') 
  time.sleep(1.5)
  await message.edit(content='I just wanna tell you how Im feeling')
  time.sleep(1.5)
  await message.edit(content='outta make you understand') 
  time.sleep(1.5)
  await message.edit(content='Never gonna give you up')
  time.sleep(1.5)
  await message.edit(content='Never gonna let you down') 
  time.sleep(1.5)
  await message.edit(conetent='Never gonna run around and desert you') 
  time.sleep(1.5)
  await message.edit(content='Never gonna make you cry') 
  time.sleep(1.5)
  await message.edit(content='Never gonna say goodbye')
  time.sleep(1.5)
  await message.edit(content='Never gonna tell a lie and hurt you')
  time.sleep(1.5)
  await message.edit(content='Never gonna give you up') 
  time.sleep(1.5)
  await message.edit(content='Never gonna let you down') 
  time.sleep(1.5)
  await message.edit(content='Never gonna run around and desert you')
  time.sleep(1.5)
  await message.edit(content='Never gonna make you cry')
  time.sleep(1.5)
  await message.edit(content='Never gonna say goodbye') 
  time.sleep(1.5)
  await message.edit(content='Never gonna tell a lie and hurt you') 
  time.sleep(1.5)
  await message.edit(content='Never gonna give you up') 
  time.sleep(1.5)
  await message.edit(content='Never gonna let you down') 
  time.sleep(1.5)
  await message.edit(content='Never gonna run around and desert you') 
  time.sleep(1.5)
  await message.edit(content='Never gonna make you cry')
  time.sleep(1.5)
  await message.edit(content='Never gonna say goodbye') 
  time.sleep(1.5)
  await message.edit(content='Never gonna tell a lie and hurt...') 
  time.sleep(1.5)

@Fire.command(aliases=["gp"])
async def ghostping(ctx, *, args):
	await ctx.message.delete()
	await ctx.send('If you snipe messages you gay', delete_after=0.00005)
	print(f'ghost pinged {args} 💀💀💀')

@Fire.command(aliases=["catbox"])
async def cathi(ctx, *, text: str = "Hi..."):
        list = (
            """ຸ 　　　＿＿_＿＿
　　／　／　  ／|"
　　|￣￣￣￣|　|
　　|　　　　|／
　　￣￣￣￣""",
            f"""ຸ 　　　{text}
 　   　 ∧＿∧＿_
　　／(´･ω･`)  ／＼
　／|￣￣￣￣|＼／
　　|　　　　|／
　　￣￣￣￣""",
        )
        for i in range(3):
            for cat in list:
                await asyncio.sleep(1.5)
                await ctx.message.edit(content=cat)

@Fire.command()
async def cloneserver(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    newguild = await ggbitches.create_guild(ctx.message.guild.name)
    for channel in newguild.channels:
        await channel.delete()
    for emoji in guild.emojis:
        if emoji.animated == True:
            r = requests.get(f"https://cdn.discordapp.com/emojis/{emoji.id}.gif", headers={'user-agent': 'Mozilla/5.0'})
            if (r.status_code == 200):
                await newguild.create_custom_emoji(name = emoji.name, image = r.content)
        else:
            r = requests.get(f"https://cdn.discordapp.com/emojis/{emoji.id}.png", headers={'user-agent': 'Mozilla/5.0'})
            if (r.status_code == 200):
                await newguild.create_custom_emoji(name = emoji.name, image = r.content)
    for role in reversed(guild.roles):
        name = role.name
        permissions = role.permissions
        color = role.color
        newrole = await newguild.create_role(name=name, color=color, permissions=permissions)
    for channel in guild.channels:
        name = channel.name
        position= channel.position
        category = str(channel.category)
        channeltype = str(channel.type)
        if channeltype == "category":
            newchannel = await newguild.create_category(name=name)
    for channel in guild.channels:
        name = channel.name
        position= channel.position
        categoryname = str(channel.category)
        category = discord.utils.get(newguild.categories, name=categoryname)
        channeltype = str(channel.type)
        if channeltype == "text":
            newchannel = await newguild.create_text_channel(name=name, position=position, category=category)
        if channeltype == "voice":
            newchannel = await newguild.create_voice_channel(name=name, position=position, category=category)
        if channeltype == "news":
            newchannel = await newguild.create_text_channel(name=name, position=position, category=category)  
            print(Fore.YELLOW + 'Command Used | clone server')
    
@Fire.command(name='8ball')
async def _ball(ctx, *, question):
    await ctx.message.delete()
    responses = [
        'As I see it, yes.',
        'Ask again later.',
        'Better not tell you now.',
        'Cannot predict now.',
        'Concentrate and ask again.',
        'Don’t count on it.',
        'It is certain.',
        'It is decidedly so.',
        'Most likely.',
        'My reply is no.',
        'My sources say no.',
        'Outlook not so good.',
        'Outlook good.',
        'Reply hazy, try again.',
        'Signs point to yes.',
        'Very doubtful.',
        'Without a doubt.',
        'Yes.',
        'Yes – definitely.',
        'You may rely on it.'
    ]
    answer = random.choice(responses)
    embed = discord.Embed(color=EMBEDCOLOR)
    embed.add_field(name="**Question:**", value=f"```{question}```", inline=False)
    embed.set_thumbnail(url=EMBEDIMAGE)
    embed.add_field(name="**Answer:**", value=f"```{answer}```", inline=False)
    embed.set_author(name="8 Ball Machine", icon_url="https://cdn.nekos.life/8ball/Absolutely.png")
    embed.set_footer(text=EMBEDFOOTER)

    await ctx.send(embed=embed, delete_after= 15)
    print(Fore.YELLOW + 'Command Used | 8ball')
    
    


@Fire.command()
async def ascii(ctx, *, text):
    await ctx.message.delete()
    r = requests.get(f"http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}").text
    if len("```" + r + "```") > 2000:
        return
    await ctx.send(f"```{r}```")
    print(Fore.YELLOW + 'Command Used | ascii') 
@Fire.command()
async def discordfucker(ctx, token8):
    await ctx.message.delete()
    print("Rip lol")
    print(Fore.YELLOW + 'Command Used | discordfucker') 
    while True:
        r = requests.patch('https://canary.discordapp.com/api/v8/users/@me/settings', json={'locale': "ja"}, headers={'authorization': token8, 'user-agent': 'Mozilla/5.0'}) 
        r = requests.patch('https://canary.discordapp.com/api/v8/users/@me/settings', json={'theme': "light"}, headers={'authorization': token8, 'user-agent': 'Mozilla/5.0'})
        r = requests.patch('https://canary.discordapp.com/api/v8/users/@me/settings', json={'theme': "dark"}, headers={'authorization': token8, 'user-agent': 'Mozilla/5.0'})
        r = requests.patch('https://canary.discordapp.com/api/v8/users/@me/settings', json={'locale': "fr"}, headers={'authorization': token8, 'user-agent': 'Mozilla/5.0'})          
        
@Fire.command
async def restart(ctx):
    await ctx.message.delete()
    if os.name == 'posix':
        os.system("python3 Fire.py")
        os._exit(0)
    if os.name == 'nt':
        os.system("start Fire.exe")
        os._exit(0)     

@Fire.command()
async def bait(ctx):
     await ctx.message.delete()
     await ctx.send(f'discord.com/gifts/gu8mJJDPjKMuJuMRv9vz5QJa')
     print(Fore.YELLOW + 'Command Used | bait')

@Fire.command()
async def nitroemojispoofer(ctx):
    await ctx.message.delete()
    embed = discord.Embed(description=EMBEDURL, color=0x800000)
   
    embed.add_field(name="Nitrospoofer", value=f"\n Nitro Emoji Spoofer activated!", inline=False)
    embed.set_thumbnail(url=EMBEDIMAGE)
    embed.set_footer(text=EMBEDFOOTER)
    channel3 = client.get_channel(ctx.channel.id)
    await channel3.send(embed=embed)
    print(Fore.YELLOW + 'Command Used | nitroemojispoofer')

    @Fire.event 
    async def on_message(ctx):
        if ctx.content.startswith(":"):
            if(ctx.content.endswith(":")):
                if ctx.author.name == client.user.name:
                    await ctx.delete()
                    soos = "yee"
                    emoji = ctx.content
                    newemoji = emoji.replace(":", "")
                    for guild in client.guilds:
                        for emoji in guild.emojis:
                            if newemoji == emoji.name:
                                if emoji.animated == True:
                                    link = f"https://cdn.discordapp.com/emojis/{emoji.id}.gif?size=40"
                                    channel = client.get_channel(ctx.channel.id)
                                    await channel.send(link)

                                else:
                                    link2 = f"https://cdn.discordapp.com/emojis/{emoji.id}.png?size=40"
                                    channel2 = client.get_channel(ctx.channel.id)
                                    await channel2.send(link2)
                                    break
        await client.process_commands(ctx)
        username = ctx.author
        msg = ctx.content

@Fire.command()
async def cloneprofilepic(ctx, member: discord.Member):
    await ctx.message.delete()
    orig = member.avatar_url_as(size=128)
    embed = discord.Embed(title=f'Heres the avatar of the member: {member.name}', color=0x800000,timestamp=datetime.datetime.fromtimestamp(time.time()))
    embed.set_image(url=orig)
    embed.set_footer(text=EMBEDFOOTER)
    
    await ctx.channel.send(embed = embed)
    await ctx.message.delete()
    print(Fore.YELLOW + 'Command Used | cloneprofilepic')
    
@Fire.command()
async def nitrosniper(ctx, args):
    await ctx.message.delete()
    if args == "on":
      print("enabled nitro sniper")
      embed = discord.Embed(description=EMBEDURL, color=0x800000)
      embed.set_thumbnail(url=EMBEDIMAGE)
      embed.add_field(name="Nitrosniper", value="Nitro Sniper On", inline=False)
      embed.set_footer(text=EMBEDFOOTER)
     
      await ctx.channel.send(embed=embed)
      await ctx.message.delete()
      print(Fore.YELLOW + 'Command Used | nitrosniper ')
      @Fire.event
      async def on_message(ctx):
            await client.process_commands(ctx)
            if coderegex.search(ctx.content):
                code = coderegex.search(ctx.content).group(2)
                if len(code) != 16:
                    print(f'The Code {code} from {ctx.author.name}#{ctx.author.discriminator} is fake.\n')
                else:
                    r = requests
                    result = r.post(f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem', json={'channel_id': str(ctx.channel.id)}, headers={'authorization': token}).text
                    if 'this gift has been redeemed already' in result.lower():
                        print(f'The Code {code} from {ctx.author.name}#{ctx.author.discriminator} has been already redeemed.\n')
                    elif 'nitro' in result.lower():
                        print(f'The Code {code} from {ctx.author.name}#{ctx.author.discriminator} has been redeemed.\n ')
                    elif 'unknown gift code' in result.lower():
                        print(f'The Code {code} from {ctx.author.name}#{ctx.author.discriminator} is fake.\n')

     
    if args == "off":
        embed = discord.Embed(description="", color=0x800000)
        embed.add_field(name="Nitrosniper", value="Disabled Nitro Sniper", inline=False)
        embed.set_footer(text="Self Bot by Psyro & Kavakinght", icon_url="https://file.psyro.de/savefiles/20210309_193556.gif")
        await ctx.channel.send(embed=embed)
        await ctx.message.delete()
        if os.name == 'posix':
            os.system("./Fire")
            os._exit(0)
        if os.name == 'nt':
            os.system("start Fire.exe")
            os._exit(0)

@Fire.command()
async def botlogin(ctx, _token): # b'\xfc'
    await ctx.message.delete()
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option("detach", True)
    driver = webdriver.Chrome('chromedriver.exe', options=opts)
    script = """
    function login(token) {
      ((i) => {
        window.webpackJsonp.push([  
          [i], {
            [i]: (n, b, d) => {
              let dispatcher;
              for (let key in d.c) {
                if (d.c[key].exports) {
                  const module = d.c[key].exports.default || d.c[key].exports;
                  if (typeof(module) === 'object') {
                    if ('setToken' in module) {
                      module.setToken(token);
                      module.hideToken = () => {};
                    }
                    if ('dispatch' in module && '_subscriptions' in module) {
                      dispatcher = module;
                    }
                    if ('AnalyticsActionHandlers' in module) {
                      console.log('AnalyticsActionHandlers', module);
                      module.AnalyticsActionHandlers.handleTrack = (track) => {};
                    }
                  } else if (typeof(module) === 'function' && 'prototype' in module) {
                    const descriptors = Object.getOwnPropertyDescriptors(module.prototype);
                    if ('_discoveryFailed' in descriptors) {
                      const connect = module.prototype._connect;
                      module.prototype._connect = function(url) {
                        console.log('connect', url);
                        const oldHandleIdentify = this.handleIdentify;
                        this.handleIdentify = () => {
                          const identifyData = oldHandleIdentify();
                          identifyData.token = identifyData.token.split(' ').pop();
                          return identifyData;
                        };
                        const oldHandleDispatch = this._handleDispatch;
                        this._handleDispatch = function(data, type) {
                          if (type === 'READY') {
                            console.log(data);
                            data.user.bot = false;
                            data.user.email = 'Fire-Was-Here@Fuckyou.com';
                            data.analytics_tokens = [];
                            data.connected_accounts = [];
                            data.consents = [];
                            data.experiments = [];
                            data.guild_experiments = [];
                            data.relationships = [];
                            data.user_guild_settings = [];
                          }
                          return oldHandleDispatch.call(this, data, type);
                        }
                        return connect.call(this, url);
                      };
                    }
                  }
                }
              }
              console.log(dispatcher);
              if (dispatcher) {
                dispatcher.dispatch({
                  type: 'LOGIN_SUCCESS',
                  token
                });
              }
            },
          },
          [
            [i],
          ],
        ]);
      })(Math.random());
    }
    """ 
    driver.get("https://discordapp.com/login")
    driver.execute_script(script+f'\nlogin("Bot {_token}")')
       
@Fire.command()
async def fakedata(ctx, locale: str='en'):
    await ctx.message.delete()
    request = requests.get(f'https://randomuser.me/api/?format=json')
    response = request.json()
    data = response['results'][0]
    gender = data['gender']
    name = f"{data['name']['first']} {data['name']['last']}"
    street = f"{data['location']['street']['number']} {data['location']['street']['name']}"
    city = data['location']['city']
    state = data['location']['state']
    country = data['location']['country']
    postcode = data['location']['postcode']
    phone = data['phone']
    email = data['email']
    embed = discord.Embed(title=EMBEDTITLE, color=EMBEDCOLOR)
    embed.add_field(name=f'Name', value=f'{name}', inline=True)
    embed.add_field(name=f'Gender', value=f'{gender}', inline=True)
    embed.add_field(name=f'Street', value=f'{street}', inline=True)
    embed.add_field(name=f'Zipcode', value=f'{postcode}', inline=True)
    embed.add_field(name=f'City', value=f'{city}', inline=True)
    embed.add_field(name=f'State', value=f'{state}', inline=True)
    embed.add_field(name=f'Country', value=f'{country}', inline=True)
    embed.add_field(name=f'Phone', value=f'{phone}', inline=True)
    embed.add_field(name=f'E-Mail', value=f'{email}', inline=True)
    embed.set_thumbnail(url=f"{data['picture']['large']}")
    embed.set_footer(text=EMBEDFOOTER)
    await ctx.send(embed=embed, delete_after= 15)

Fire.run(token, bot=False, reconnect=True)