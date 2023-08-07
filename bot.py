# bot.py
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

description = '''An example bot to showcase the discord.ext.commands extension
module. There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

# Rest of your bot code goes here
@bot.event
async def setup_hook():
  for filename in os.listdir('./cogs'):
      if filename.endswith('.py'):
          await bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(os.getenv("TOKEN"))