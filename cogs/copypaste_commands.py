from discord.ext import commands


class CopyPasteCommandsCog(commands.Cog, name="Copys"):

  def __init__(self, bot):
    self.bot = bot

  @commands.command(name="nashe")
  async def test(self, ctx):
    """Sos un verdadero nashe."""
    await ctx.send(
      ctx.author.display_name +
      " es un \n ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ \n ⣿⠉⠉⢻⡏⠉⢹⣿⡟⠉⠹⣿⣿⠏⠉⣉⠉⢻⡏⠉⣿⣿⠉⢹⡏⠉⠉⠉⢹⣿\n ⣿⠀⠀⠀⠃⠀⢸⣿⠁⢰⠀⢹⣿⣄⠈⠛⠻⣿⡇⠀⠛⠛⠀⢸⡇⠘⠛⠛⣿⣿ \n ⣿⠀⠀⣷⡀⠀⢸⠏⢀⣉⡀⠀⢻⠉⠹⡶⠀⠈⡇⠀⣶⣶⠀⢸⡇⠰⠶⠶⢿⣿ \n ⣿⣦⣴⣿⣷⣤⣾⣦⣼⣿⣿⣤⣼⣷⣤⣤⣤⣾⣧⣴⣿⣿⣦⣾⣧⣤⣤⣤⣾⣿ \n ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ "
    )

  @commands.command(name="dami")
  async def dami(self, ctx):
    """El motor de la historia es la lucha de clases."""
    await ctx.send(
      "'⠀⠀⠀⠀⠀⠀⢀⣤⣀⣀⣀⠀⠻⣷⣄\n⠀⠀⠀⠀⢀⣴⣿⣿⣿⡿⠋⠀⠀⠀⠹⣿⣦⡀\n⠀⠀⢀⣴⣿⣿⣿⣿⣏⠀⠀⠀⠀⠀⠀⢹⣿⣧\n⠀⠀⠙⢿⣿⡿⠋⠻⣿⣿⣦⡀⠀⠀⠀⢸⣿⣿⡆\n⠀⠀⠀⠀⠉⠀⠀⠀⠈⠻⣿⣿⣦⡀⠀⢸⣿⣿⡇\n⠀⠀⠀⠀⢀⣀⣄⡀⠀⠀⠈⠻⣿⣿⣶⣿⣿⣿⠁\n⠀⠀⠀⣠⣿⣿⢿⣿⣶⣶⣶⣶⣾⣿⣿⣿⣿⡁\n⢠⣶⣿⣿⠋⠀⠀⠉⠛⠿⠿⠿⠿⠿⠛⠻⣿⣿⣦⡀\n⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⡿'"
    )

  @commands.command(name="pepe")
  async def pepe(self, ctx):
    """El Pepe."""
    await ctx.send(
      '⣿⣿⣿⣿⣿⣿⣿⡿⠛⠉⠉⠉⠉⠛⠻⣿⣿⠿⠛⠛⠙⠛⠻⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⢀⣀⣀⡀⠀⠈⢄⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⠏⠀⠀⠀⠔⠉⠁⠀⠀⠈⠉⠓⢼⡤⠔⠒⠀⠐⠒⠢⠌⠿⢿⣿⣿⣿\n⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⢀⠤⣒⠶⠤⠭⠭⢝⡢⣄⢤⣄⣒⡶⠶⣶⣢⡝⢿⣿\n⡿⠋⠁⠀⠀⠀⠀⣀⠲⠮⢕⣽⠖⢩⠉⠙⣷⣶⣮⡍⢉⣴⠆⣭⢉⠑⣶⣮⣅⢻\n⠀⠀⠀⠀⠀⠀⠀⠉⠒⠒⠻⣿⣄⠤⠘⢃⣿⣿⡿⠫⣿⣿⣄⠤⠘⢃⣿⣿⠿⣿\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⠤⠭⣥⣀⣉⡩⡥⠴⠃⠀⠈⠉⠁⠈⠉⠁⣴⣾⣿\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⠔⠊⠀⠀⠀⠓⠲⡤⠤⠖⠐⢿⣿⣿⣿\n⠀⠀⠀⠀⠀⠀⠀⠀⣠⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿\n⠀⠀⠀⠀⠀⠀⠀⢸⣿⡻⢷⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣘⣿⣿\n⠀⠀⠀⠀⠀⠠⡀⠀⠙⢿⣷⣽⣽⣛⣟⣻⠷⠶⢶⣦⣤⣤⣤⣤⣶⠾⠟⣯⣿⣿\n⠀⠀⠀⠀⠀⠀⠉⠂⠀⠀⠀⠈⠉⠙⠛⠻⠿⠿⠿⠿⠶⠶⠶⠶⠾⣿⣟⣿⣿⣿\n⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿\n⣿⣿⣶⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣟⢿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿'
    )

  @commands.command(name="ez")
  async def ez(self, ctx):
    """Facilito."""
    await ctx.send(
      '⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⠛⢩⣴⣶⣶⣶⣌⠙⠫⠛⢋⣭⣤⣤⣤⣤⡙⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⡟⢡⣾⣿⠿⣛⣛⣛⣛⣛⡳⠆⢻⣿⣿⣿⠿⠿⠷⡌⠻⣿⣿⣿⣿\n⣿⣿⣿⣿⠏⣰⣿⣿⣴⣿⣿⣿⡿⠟⠛⠛⠒⠄⢶⣶⣶⣾⡿⠶⠒⠲⠌⢻⣿⣿\n⣿⣿⠏⣡⢨⣝⡻⠿⣿⢛⣩⡵⠞⡫⠭⠭⣭⠭⠤⠈⠭⠒⣒⠩⠭⠭⣍⠒⠈⠛\n⡿⢁⣾⣿⣸⣿⣿⣷⣬⡉⠁⠄⠁⠄⠄⠄⠄⠄⠄⠄⣶⠄⠄⠄⠄⠄⠄⠄⠄⢀\n⢡⣾⣿⣿⣿⣿⣿⣿⣿⣧⡀⠄⠄⠄⠄⠄⠄⠄⢀⣠⣿⣦⣤⣀⣀⣀⣀⠄⣤⣾\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⡶⢇⣰⣿⣿⣟⠿⠿⠿⠿⠟⠁⣾⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⡟⢛⡛⠿⠿⣿⣧⣶⣶⣿⣿⣿⣿⣿⣷⣼⣿⣿⣿⣧⠸⣿⣿\n⠘⢿⣿⣿⣿⣿⣿⡇⢿⡿⠿⠦⣤⣈⣙⡛⠿⠿⠿⣿⣿⣿⣿⠿⠿⠟⠛⡀⢻⣿\n⠄⠄⠉⠻⢿⣿⣿⣷⣬⣙⠳⠶⢶⣤⣍⣙⡛⠓⠒⠶⠶⠶⠶⠖⢒⣛⣛⠁⣾⣿\n⠄⠄⠄⠄⠄⠈⠛⠛⠿⠿⣿⣷⣤⣤⣈⣉⣛⣛⣛⡛⠛⠛⠿⠿⠿⠟⢋⣼⣿⣿\n⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠉⠉⣻⣿⣿⣿⣿⡿⠿⠛⠃⠄⠙⠛⠿⢿⣿\n⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢬⣭⣭⡶⠖⣢⣦⣀⠄⠄⠄⠄⢀⣤⣾⣿\n⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢰⣶⣶⣶⣾⣿⣿⣿⣿⣷⡄⠄⢠⣾⣿⣿⣿'
    )

  @commands.command(name="miraAtras")
  async def miraAtras(self, ctx):
    """Tené cuidado."""
    await ctx.send(
      '⣿⣿⣿⡉⢀⣾⣿⡟⣩⣭⣭⡈⠙⢿⣿⣿⣿⣿⣿⡿⣻⣿⣿⣿⣿⣿⣿⣿⡇⠄\n⣿⣿⡗⠄⣼⣿⣿⢸⡿⠉⠉⢻⡆⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢠⠄\n⣿⡻⠁⢠⣿⣿⣿⣦⡛⠢⠴⠛⠁⣸⣿⣿⣿⣿⡿⠛⢉⣉⣉⡙⢻⣿⣿⣗⠄⠄\n⠷⠁⠄⢰⣿⣿⣿⣷⣬⣭⣼⣷⣿⣿⣿⣿⣿⡏⢀⣾⠟⠛⢿⣿⣄⣿⣿⡏⠄⠄\n⠄⠄⠄⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠄⠳⢀⣀⡼⢟⣼⣿⡟⠄⠄⠄\n⠄⠄⠄⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣮⣒⣲⣶⣾⣿⣿⠏⠄⠄⠄⢠\n⠄⠄⠄⠸⣿⣽⣿⣿⣿⣿⣉⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠄⠄⠄⢠⣷\n⠄⠄⠄⠄⢻⣷⢻⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⠏⠄⠄⠄⠄⠄⢀⣾⣿\n⠄⠄⠄⠄⠄⢻⣧⡙⢿⣿⣿⣿⣿⣿⡿⣿⣿⣿⠿⠛⠁⠄⠄⠄⠄⠄⢠⣿⣿⣿\n⠄⠄⠄⡀⠄⠈⣿⣿⣶⣭⣭⣭⣿⣾⡿⠟⠋⠁⠄⠄⠄⠄⠄⠄⠄⢠⣿⣿⣿⣿\n⠄⠄⠎⠄⠄⣨⣿⣿⣿⣿⣿⣿⠋⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⣀⡲⣿⣿⣿⣿'
    )

  @commands.command(name="ganen")
  async def ganen(self, ctx):
    """Amenaza para que pongan huevo."""
    await ctx.send(
      '⠀⠀⠀⠀ ⠀⠀⣠⡶⢦⠀⠀⢰⣶⠀⠀⢰⣆⢰⡆⠀⢰⠶⠆⠀⢰⣆⢰⡆\n⠀⠀ ⠀⠀⠀⠀⡟⢠⣤⠀⠀⣾⢹⡄⠀⢸⣿⣼⡇⠀⢸⣤⠀⠀⢸⣿⣼⡇\n⠀⣰⡀⠀⠀⠀⣿⣀⣿⠀⢠⡟⠻⣇⠀⢸⡇⣿⡇⠀⢸⣀⡀⠀⢸⡇⣿⡇\n⠀⣿⡇⠀⠀⠀⠈⠉⠉⠀⠈⠁⠀⠉⠀⠈⠁⠈⠁⠀⠈⠉⠁⠀⠈⠁⠈⠁\n⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡶⠒⠒⢶⣄\n⢸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀ ⢸⣿\n⢸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀ ⠀⢸⣿\n⢸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠒⠒⠚⠛\n⢸⣿⣿⠀⢰⣶⣶⡄⠀⠀⠀⣶⡆⠀⠀⠀⣶⠀⠀⠀⠀⢰⣦⠀⠀⠀⣴⠶⡆\n⢸⣿⣿⠀⢸⣿⣸⠇⠀⠀⢠⡟⣿⠀⠀⠀⣿⠀⠀⠀⠀⣿⢿⡄⠀⠀⣿⣄\n ⠀⠀⠀⠀⢸⣿⠙⣷⠀⠀⣸⣧⣽⡆⠀⠀⣿⠀⠀⠀⢸⣧⣼⣇⠀⠀⠈⢻⣷\n ⠀⠀⠀⠀⢸⣿⣾⠟⠀⠀⡿⠀⠸⣿⠀⠀⣿⣶⡆⠀⣼⠀⠀⣿⠀⠀⣧⣼⠟⠀'
    )

  @commands.command(name="pastor")
  async def pastor(self, ctx):
    """Todo el poder del Jame invocado."""
    await ctx.send(
      '⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⢀⣠⣦⣤⣤⣀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⢠⣴⣾⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣟⠀⠀⠀⠀⠀⠸⠿⠿⣿⣿⣿⣿⣿⠿⠿⢧⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⡃⠀⠀⠀⠀⠀⠀:wipiu: ⠀ ⢸⣿ ⠀:wipiu: ⢠⡄⠀⠀⠀⠀⠹⣿⣿⣿⣿\n⣿⣿⣿⡟⠁⠀⠀⠀⠀⢰⣤⣤⣴⡿⣸⣿⣿⣷⣶⣾⣿⣧⠀⠀⠀⠀⠀⢼⣿⣿⣿\n⣿⣿⣿⡿⡇⠀⠀⠀⠀⠘⣿⣿⣿⠃⠙⠛⠛⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠻⣿⣿⣿\n⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠘⢿⠛⠀⠀⠒⠊⠏⠻⣿⠛⠁⠀⠀⠀⠀⠀⢈⣿⣿⣿\n⣿⣿⣿⣿⣡⡀⠀⠀⠀⠀⠀⠀⠐⡀⠘⠛⢛⣿⠂⠁⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣷⣦⢠⠀⠀⡀⠀⠀⠀⠈⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣄⣠⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠀⢠⣴⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠇⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⠟⠛⠁⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⣿⣿⡿⠛⠁⠉⠛⠻⣿⣿⣿⣿⣿'
    )


async def setup(bot):
  await bot.add_cog(CopyPasteCommandsCog(bot))
