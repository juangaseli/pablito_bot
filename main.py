import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from cogs.custom_help import CustomHelpCommand

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix='.',
                   intents=intents,
                   help_command=CustomHelpCommand())

#aca añado los archivos con comandos que quiera inicializar en el bot
initial_extensions = [
  'cogs.user_commands', 'cogs.copypaste_commands', 'cogs.nsfw_commands',
  'cogs.price_commands', 'cogs.ai_commands'
]


async def load_extensions():
  for extension in initial_extensions:
    await bot.load_extension(extension)


@bot.event
async def on_ready():
  await load_extensions()
  print(f'Logged in as {bot.user.name}')


load_dotenv()
bot.run(os.getenv('TOKEN2'))
