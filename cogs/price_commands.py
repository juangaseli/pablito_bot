import discord
from discord.ext import commands
import requests
import datetime


class PriceCommandsCog(commands.Cog, name="Cotizaciones"):

  def __init__(self, bot):
    self.bot = bot

  @staticmethod
  def obtenerCotizacion(tipo_dolar):
    try:
      urls = {
        "oficial": "https://dolarapi.com/v1/dolares/oficial",
        "blue": "https://dolarapi.com/v1/dolares/blue",
        "mep": "https://dolarapi.com/v1/dolares/bolsa",
        "liqui": "https://dolarapi.com/v1/dolares/contadoconliqui",
      }

      url = urls.get(tipo_dolar.lower())
      if not url:
        return "Tipo de dólar no válido."

      response = requests.get(url)

      if response.status_code == 200:
        data = response.json()

        # Formatear la fecha de actualización
        fecha_actualizacion = datetime.datetime.strptime(
          data['fechaActualizacion'], "%Y-%m-%dT%H:%M:%S.%fZ")
        fecha_formateada = fecha_actualizacion.strftime("%d/%m/%Y %H:%M:%S")

        # Crear un mensaje de Discord en formato embed
        embed = discord.Embed(
          title=f"Cotización Dólar {tipo_dolar.capitalize()}",
          color=discord.Color.blue())
        embed.add_field(name="Compra", value=f"${data['compra']}", inline=True)
        embed.add_field(name="Venta", value=f"${data['venta']}", inline=True)
        embed.add_field(name="Fecha de Actualización",
                        value=fecha_formateada,
                        inline=False)

        return embed

      else:
        return "Error al obtener la cotización."

    except Exception as e:
      return f"Error: {str(e)}"

  @commands.command(name="cambio")
  async def cambio(self, ctx, tipo_dolar: str):
    """Cotización del dolar, parámetros válidos: oficial, blue, mep, liqui."""
    mensaje = self.obtenerCotizacion(tipo_dolar.lower())
    # Enviar el mensaje de Discord
    if isinstance(mensaje, discord.Embed):
      await ctx.send(embed=mensaje)
    else:
      await ctx.send(mensaje)


class DolarCriptoCog(commands.Cog, name="Dólar Cripto"):

  def __init__(self, bot):
    self.bot = bot

  @staticmethod
  def obtenerCripto(fiat):
    coin = "ripio"
    volumen = 0.1  # Volumen fijo para calcular 1 dólar de fiat en ARS

    # Validar las opciones de fiat permitidas
    fiat_opciones = ["usdc", "usdt", "dai", "eth", "btc"]
    if fiat not in fiat_opciones:
      return "Tipo de cripto no válido."

    url = f"https://criptoya.com/api/{coin}/{fiat}/ars/{volumen}"

    try:
      response = requests.get(url)
      if response.status_code == 200:
        if response.text:  # Verificar que la respuesta no esté vacía
          data = response.json()

          # Obtener el timestamp de la respuesta en segundos
          timestamp_seconds = data['time']

          # Formatear la fecha de actualización
          fecha_actualizacion = datetime.datetime.fromtimestamp(
            timestamp_seconds)
          fecha_formateada = fecha_actualizacion.strftime("%d/%m/%Y %H:%M:%S")

          # Crear un mensaje de Discord en formato embed
          embed = discord.Embed(title=f"Cotización Cripto {fiat.upper()}",
                                color=discord.Color.blue())
          embed.add_field(name="Compra", value=f"${data['ask']}", inline=True)
          embed.add_field(name="Venta", value=f"${data['bid']}", inline=True)
          embed.add_field(name="Fecha de Actualización",
                          value=fecha_formateada,
                          inline=False)

          return embed
        else:
          return "La respuesta está vacía."
      else:
        return None
    except Exception as e:
      print(f"Error: {str(e)}")
      return None

  @commands.command(name="cripto")
  async def cripto(self, ctx, fiat: str):
    """Cotización de dolar cripto, parámetros válidos: USDC, USDT, DAI, ETH, BTC."""
    mensaje = self.obtenerCripto(fiat.lower())
    # Enviar el mensaje de Discord
    if isinstance(mensaje, discord.Embed):
      await ctx.send(embed=mensaje)
    else:
      await ctx.send(
        "No se pudo obtener la cotización para la cripto proporcionada.")


async def setup(bot):
  await bot.add_cog(PriceCommandsCog(bot))
  await bot.add_cog(DolarCriptoCog(bot))
