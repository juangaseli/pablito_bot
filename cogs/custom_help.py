import discord
from discord.ext import commands


class CustomHelpCommand(commands.HelpCommand):

  async def send_bot_help(self, mapping):
    embed = discord.Embed(title="Comandos disponibles",
                          description="Lista de comandos y sus descripciones:")

    for cog, commands in mapping.items():
      if cog is None:
        continue

      command_list = []
      for command in commands:
        command_list.append(f'`{command.name}`: {command.short_doc}')

      if command_list:
        embed.add_field(name=cog.qualified_name,
                        value='\n'.join(command_list),
                        inline=False)

    await self.get_destination().send(embed=embed)
