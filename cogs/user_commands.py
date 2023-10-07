import random
from discord.ext import commands


class UserCommandsCog(commands.Cog, name="Comandos generales"):

  def __init__(self, bot):
    self.bot = bot

  @staticmethod
  def getUsers(guild):
    # Obtener la lista de miembros del servidor (sin incluir bots)
    members = [member for member in guild.members if not member.bot]
    # Obtener los nombres de los usuarios
    usersList = [member.display_name for member in members]
    return usersList

  @commands.command(name="meMide")
  async def meMide(self, ctx):
    """Te digo el tamaño de tu cosa."""
    value = str(random.randint(3, 23))
    if random.randint(1, 30) == 22:
      await ctx.send('A ' + ctx.author.display_name + ' le mide ' + value +
                     'cm de profundo.')
    else:
      await ctx.send('A ' + ctx.author.display_name + ' le mide ' + value +
                     'cm.')

  @commands.command(name="sex")
  async def sex(self, ctx):
    """Te digo hace cuanto no tenes relaciones."""
    value = str(random.randint(2, 300))
    await ctx.send(ctx.author.display_name + ' no la pone hace ' + value +
                   ' días.')

  @commands.command(name="facha")
  async def facha(self, ctx):
    """Te digo tu nivel de facha hoy."""
    value = str(random.randint(1, 100))
    await ctx.send(ctx.author.display_name + ' tiene un ' + value +
                   '% de facha.')

  @commands.command(name="cancelade")
  async def cancelade(self, ctx):
    """Te digo las probabilidades de ser cancelade."""
    value = str(random.randint(1, 100))
    await ctx.send(ctx.author.display_name + ' tiene un ' + value +
                   '% de probabilidades de ser cancelade.')

  @commands.command(name="pelea")
  async def pelea(self, ctx):
    """Vas a pelear contra alguien del discord."""

    # Recupero lista de usuarios
    users = self.getUsers(ctx.guild)
    autor = ctx.message.author.display_name
    user = autor
    # Mientras el usuario aleatorio sea igual al autor, elige uno nuevo
    while user == autor:
      user = random.choice(users)

    value = random.randint(40, 50)
    if value > 45:
      await ctx.send(autor + ' peleo con ' + user + ' y le cagó a piñas.')
    elif value == 45:
      await ctx.send(
        autor + ' peleo con ' + user +
        ' y termino en un encuentro sexual donde ambos se rompieron el orto.')
    elif value < 45:
      await ctx.send(autor + ' peleo con ' + user + ' y le cagaron a piñas.')


#  @commands.command(name="lista")
#  async def lista(self, ctx):
#    """Lista de usuarios"""
#    users = self.getUsers(ctx.guild)
#    # Enviar la lista de nombres de usuarios
#    await ctx.send(f'Lista de usuarios en el servidor:\n{", ".join(users)}')


async def setup(bot):
  await bot.add_cog(UserCommandsCog(bot))
