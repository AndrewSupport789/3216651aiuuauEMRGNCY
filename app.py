# Work with Py xxx
import discord
from discord.ext import commands, tasks
import os
import asyncio
from discord import Activity, ActivityType
import random
import time
from itertools import cycle
from discord.utils import get
from discord import Game
import os

reminder = 'Do not forget try all links for all accounts!'

owo = "**__We are sorry but bot will be offline for other servers for few days due low account stock!__**"

msgg = '```Check your DMs man!```'

client = commands.Bot(command_prefix='!')
#client = discord.Client()
Clientdiscord = discord.Client()

#create an arraylist containing phrases you want your bot to switch through.
status = cycle(['web: www.rabbits-gen.cf', 'With BlackRabbit', 'discord.gg/cZ8GcPF', '!cmds for commands', '!cmds'])

client.remove_command('help')

@client.command()
async def clr(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.command()
async def ban(ctx):
    check_role = get(ctx.message.guild.roles, name='BAN-SQUAD')
    if check_role in ctx.author.roles:
        await ctx.send("https://gifimage.net/wp-content/uploads/2017/07/ban-hammer-gif-14.gif")
    else:
        await ctx.send("You can't use this!")




@client.event
async def on_message(message):
 message.content = message.content.lower().replace(' ', '')
 await client.wait_until_ready()
 print(message.author.name)
 twitter = ' ;) '
 if message.content.startswith("!hello"):
        print(message.author.name)
        embed = discord.Embed(color=0xFF09D7)

        await message.author.send(embed=embed)
        
        
 if message.content.startswith("!p_up"):
    print(message.author.name)
    print('****=======Update presence=========****')
    await client.wait_until_ready()
    await message.channel.send('Done, updated!')
    await client.change_presence(activity=Activity(name=f"{len(client.guilds)}guilds|!𝙘𝙢𝙙𝙨|rabbits-gen.cf ", 
                                                type=ActivityType.watching))
                                                
                                                        
 if message.content.startswith("!"):
    print(message.author.name)
    print('****=======Update presence=========****')
    await client.wait_until_ready()
    await client.change_presence(activity=Activity(name=f"{len(client.guilds)}guilds|!𝙘𝙢𝙙𝙨|rabbits-gen.cf ", 
                                                type=ActivityType.watching))                                               
                                                                                                        
 if message.content.startswith("?"):
    print(message.author.name)
    print('****=======Update presence=========****')
    await client.wait_until_ready()
    await client.change_presence(activity=Activity(name=f"{len(client.guilds)}guilds|!𝙘𝙢𝙙𝙨|rabbits-gen.cf ", 
                                                type=ActivityType.watching))
                                                
                                                                                                        
 if message.content.startswith("hello"):
    print(message.author.name)
    print('****=======Update presence=========****')
    await client.wait_until_ready()
    await client.change_presence(activity=Activity(name=f"{len(client.guilds)}guilds|!𝙘𝙢𝙙𝙨|rabbits-gen.cf ", 
                                                type=ActivityType.watching))
                                                
                                                
 if message.content.startswith("hi"):
    print(message.author.name)
    print('****=======Update presence=========****')
    await client.wait_until_ready()
    await client.change_presence(activity=Activity(name=f"{len(client.guilds)}guilds|!𝙘𝙢𝙙𝙨|rabbits-gen.cf ", 
                                                type=ActivityType.watching))
 
 if message.content.startswith("!invite"):
        print(message.author.name)
        msg = 'I sent invite link into your DMs man!'
        embed = discord.Embed(color=0xFF09D7)
        await message.channel.send('Check your DMs!')

        await message.author.send(embed=embed) 

 if message.content.startswith("!help"):
        print(message.author.name)
        embed = discord.Embed(color=0xFF09D7)
        embed.add_field(name="**__Supporter__**", value="You can buy **__Supporter__** role here on my server: https://discord.gg/2ZnMK4m", inline=False)
        embed.add_field(name="Why?", value="With **__Supporter__** role you don't have to watch ads and you will get accounts almost instantly!", inline=False)
        await message.channel.send('Check your DMs!')
        await message.author.send(embed=embed)
        
 if message.content.startswith("!supporter"):
        print(message.author.name)
        embed = discord.Embed(color=0xFF09D7)
        embed.add_field(name="**__Supporter__**", value="You can buy **__Supporter__** role here on my server: https://discord.gg/2ZnMK4m", inline=False)
        embed.add_field(name="Why?", value="With **__Supporter__** role you don't have to watch ads and you will get accounts almost instantly!", inline=False)
        await message.channel.send('Check your DMs!')
        await message.author.send(embed=embed)
             
        
 if message.content.startswith("!stock"):
        print(message.author.name)
        msg = 'Check DMs!'
        embed = discord.Embed(color=0xFF09D7)
        embed.add_field(name="I can't display stock but you can check my #gen-announcmenets channel on my server, if you aren't on my server here is invite link tho", value="https://discord.gg/2ZnMK4m", inline=False)
        await message.author.send(embed=embed) 
        await message.channel.send('Check your DMs!')
        
 if message.content.startswith("!scribd"):
        print(message.author.name)
        msg = '```Check your DMs man!```'
        embed = discord.Embed(title="`Scrib acc`", color=0x840055)
        embed.add_field(name="Your link:", value="/27527/Scribd", inline=False)
        embed.add_field(name="Invite this bot on your server!", value="https://discordapfp.com/oauth2/authorize?client_id=60496724186339f7376&permissions=8&scope=bot", inline=False)
        await message.author.send(embed=embed)
        await message.channel.send('Check your DMs!')
        
        
 if message.content.startswith("!cmds"):
        print(message.author.name)
        embed = discord.Embed(title="**COMMANDS**", color=0xFF09D7)
        embed.add_field(name="Visit my website for list of commands:", value="http://bit.ly/gen_commands", inline=False)
        embed.add_field(name="**__**__Supporter__**__**", value="You can buy **__Supporter__** role for save your time on my server! https://discord.gg/2ZnMK4m", inline=False)
        await message.author.send(embed=embed)
        await message.channel.send('Check your DMs!')
		
        
 if message.content.startswith("!commands"):
        print(message.author.name)
        embed = discord.Embed(title="**COMMANDS**", color=0xFF09D7)
        embed.add_field(name="Visit my website for list of commands:", value="http://bit.ly/gen_commands", inline=False)
        await message.author.send(embed=embed)
        await message.channel.send('Check your DMs!')
	        
 if message.content.startswith("!grammarly"):
        print(message.author.name)
        msg = '```Check your DMs man!```'
        embed = discord.Embed(title="`Grammarly acc`", color=0x840055)
        embed.add_field(name="Your link:", value="OUT OF STOCK, BE PATIENT", inline=False)
        embed.add_field(name="Invite this bot on your server!", value="https://discordapfp.com/oauth2/authorize?client_id=60496724186339f7376&permissions=8&scope=bot", inline=False)
        await message.author.send(embed=embed)
        await message.channel.send('Check your DMs!')
        
		        
 if message.content.startswith("!eset"):
        print(message.author.name)
        embed = discord.Embed(title="`Eset keys`", color=0x400cc1)
        embed.add_field(name="Your link:", value="OUT OF STOCK, BE PATIENT", inline=False)
        embed.add_field(name="Link #2:", value="OUT OF STOCK, BE PATIENT", inline=False)
        embed.add_field(name="__**Tutorial:**__", value="https://youtu.be/kJbWiPKP_gg", inline=False)
        embed.add_field(name="Twitter:", value="https://twitter.com/RGen001?s=09", inline=False)
        await message.author.send(embed=embed)
        await message.channel.send('Check your DMs!')
        
			        
 if message.content.startswith("!crunchyroll"):
        print(message.author.name)
        embed = discord.Embed(title="Crunchyroll accs`", color=0x400cc1)
        embed.add_field(name="Your link:", value="OUT OF STOCK, BE PATIENT", inline=False)
        embed.add_field(name="Link #2:", value="OUT OF STOCK, BE PATIENT", inline=False)
        embed.add_field(name="__**Tutorial:**__", value="https://youtu.be/kJbWiPKP_gg", inline=False)
        embed.add_field(name="Twitter:", value="https://twitter.com/RGen001?s=09", inline=False)
        await message.author.send(embed=embed)
        await message.channel.send('Check your DMs!')
        
        
 if message.content.startswith("!minecraft"):
        print(message.author.name)
        embed = discord.Embed(title="`Minecraft acc`", color=0x400cc1)
        embed.add_field(name="Your link:", value="OUT OF STOCK, BE PATIENT", inline=False)
        embed.add_field(name="Link #2:", value="OUT OF STOCK, BE PATIENT", inline=False)
        embed.add_field(name="Link #3:", value="OUT OF STOCK, BE PATIENT", inline=False)
        embed.add_field(name="__**Tutorial:**__", value="https://youtu.be/kJbWiPKP_gg", inline=False)
        embed.add_field(name="Twitter:", value="https://twitter.com/RGen001?s=09", inline=False)
        await message.author.send(embed=embed)
        await message.channel.send('Check your DMs!')
        
		
		        
 if message.content.startswith("!hulu"):
        print(message.author.name)
        embed = discord.Embed(title="`Hulu acc`", color=0x400cc1)
        embed.add_field(name="Your link:", value="OUT OF STOCK, BE PATIENT", inline=False)
        embed.add_field(name="Link #2:", value="OUT OF STOCK, BE PATIENT", inline=False)
        embed.add_field(name="Link #3:", value="OUT OF STOCK, BE PATIENT", inline=False)
        embed.add_field(name="__**Tutorial:**__", value="https://youtu.be/kJbWiPKP_gg", inline=False)
        embed.add_field(name="Twitter:", value="https://twitter.com/RGen001?s=09", inline=False)
        await message.author.send(embed=embed) 
        await message.channel.send('Check your DMs!')
        
			        
 if message.content.startswith("!dominos"):
        print(message.author.name)
        embed = discord.Embed(title="`Dominos acc`", color=0x400cc1)
        embed.add_field(name="Your link:", value="OUT OF STOCK, BE PATIENT", inline=False)
        embed.add_field(name="__**Tutorial:**__", value="https://youtu.be/kJbWiPKP_gg", inline=False)
        embed.add_field(name="Twitter:", value="https://twitter.com/RGen001?s=09", inline=False)
        await message.author.send(embed=embed) 
        await message.channel.send('Check your DMs!')
        
				        
 if message.content.startswith("!origin"):
        print(message.author.name)
        embed = discord.Embed(title="`Origin acc`", color=0x400cc1)
        embed.add_field(name="Your link:", value="OUT OF STOCK, BE PATIENT", inline=False)
        embed.add_field(name="Link #2:", value="OUT OF STOCK, BE PATIENT", inline=False)
        embed.add_field(name="__**Tutorial:**__", value="https://youtu.be/kJbWiPKP_gg", inline=False)
        embed.add_field(name="Twitter:", value="https://twitter.com/RGen001?s=09", inline=False)
        await message.author.send(embed=embed)
        await message.channel.send('Check your DMs!')
        
		
						        
 if message.content.startswith("!uplay"):
        print(message.author.name)
        embed = discord.Embed(title="`Uplay acc`", color=0x400cc1)
        embed.add_field(name="Your link:", value="OUT OF STOCK, BE PATIENT", inline=False)
        embed.add_field(name="Link #2:", value="OUT OF STOCK, BE PATIENT", inline=False)
        embed.add_field(name="Link #3:", value="OUT OF STOCK, BE PATIENT", inline=False)
        embed.add_field(name="__**Tutorial:**__", value="https://youtu.be/kJbWiPKP_gg", inline=False)
        embed.add_field(name="Twitter:", value="https://twitter.com/RGen001?s=09", inline=False)
        await message.author.send(embed=embed)
        await message.channel.send('Check your DMs!')
        
								        
 if message.content.startswith("!steam"):
        print(message.author.name)
        embed = discord.Embed(title="`Steam acc`", color=0x400cc1)
        embed.add_field(name="Your link:", value="OUT OF STOCK, BE PATIENT", inline=False)
        embed.add_field(name="Link #2:", value="OUT OF STOCK, BE PATIENT", inline=False)
        embed.add_field(name="__**Tutorial:**__", value="https://youtu.be/kJbWiPKP_gg", inline=False)
        embed.add_field(name="Twitter:", value="https://twitter.com/RGen001?s=09", inline=False)
        await message.author.send(embed=embed)
        await message.channel.send('Check your DMs!')
        
							        
				        
 if message.content.startswith("!fortnite"):
        print(message.author.name)
        embed = discord.Embed(title="`Fortnite acc`", color=0x400cc1)
        embed.add_field(name="Your link:", value="OUT OF STOCK, BE PATIENT", inline=False)
        embed.add_field(name="Link #2:", value="OUT OF STOCK, BE PATIENT", inline=False)
        embed.add_field(name="__**Tutorial:**__", value="https://youtu.be/kJbWiPKP_gg", inline=False)
        embed.add_field(name="Twitter:", value="https://twitter.com/RGen001?s=09", inline=False)
        await message.author.send(embed=embed)
        await message.channel.send('Check your DMs!')
        
		
				        
 if message.content.startswith("!spotify"):
        print(message.author.name)
        embed = discord.Embed(title="`Spotify acc`", color=0x400cc1)
        embed.add_field(name="Your link:", value="OUT OF STOCK, BE PATIENT", inline=False)
        embed.add_field(name="Link #2:", value="OUT OF STOCK, BE PATIENT", inline=False)
        embed.add_field(name="__**Tutorial:**__", value="https://youtu.be/kJbWiPKP_gg", inline=False)
        embed.add_field(name="Twitter:", value="https://twitter.com/RGen001?s=09", inline=False)
        await message.author.send(embed=embed)
        await message.channel.send('Check your DMs!')
        
						        
 if message.content.startswith("!nord"):
        print(message.author.name)
        embed = discord.Embed(title="`NordVPN acc`", color=0x400cc1)
        embed.add_field(name="Your link:", value="OUT OF STOCK, BE PATIENT", inline=False)
        embed.add_field(name="Link #2:", value="OUT OF STOCK, BE PATIENT", inline=False)
        embed.add_field(name="Link #3:", value="OUT OF STOCK, BE PATIENT", inline=False)
        embed.add_field(name="__**Tutorial:**__", value="https://youtu.be/kJbWiPKP_gg", inline=False)
        embed.add_field(name="Twitter:", value="https://twitter.com/RGen001?s=09", inline=False)
        await message.author.send(embed=embed)
        await message.channel.send('Check your DMs!')
        
        
   						        
 if message.content.startswith("!pinterest"):
        print(message.author.name)
        embed = discord.Embed(title="`Pinterest acc`", color=0x400cc1)
        embed.add_field(name="Your link:", value="OUT OF STOCK, BE PATIENT", inline=False)
        embed.add_field(name="Twitter:", value="https://twitter.com/RGen001?s=09", inline=False)
        await message.author.send(embed=embed)
        await message.channel.send('Check your DMs!')  
        	


#embed.add_field(name="link #2:", value="OUT OF STOCK, BE PATIENT", inline=False)
		


@client.event
async def on_ready():
    await client.wait_until_ready()
    await client.change_presence(activity=Activity(name="your mum", type=ActivityType.watching))
	
client.run(os.getenv('BOT_TOKEN'))
