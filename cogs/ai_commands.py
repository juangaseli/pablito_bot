import discord
from discord.ext import commands
import requests


class AICommandsCog(commands.Cog, name="AI"):

  def __init__(self, bot):
    self.bot = bot

  @staticmethod
  def obtenerRespuesta(consulta):
    try:
      #IMPORTANTE: tener instalado y corriendo Ollama AI localmente
      url = "http://localhost:11434/api/generate"
      response = requests.post(
        url, 
        json={
          "prompt": f"{consulta}\nRespondé en una sola oración.",
          "model": "mistral:latest",
          "stream": False,
          "options": {
            "num_predict": 50  # Limita a 50 tokens generados (~30-40 palabras)
        }}) # stream false es para recibir toda la respuesta de una vez, para saber el model que se usa ir a /api/tags

      if response.status_code == 200:
        respuesta = response.json().get("response", "").strip()
        return respuesta

      else:
        return "Error al obtener la respuesta."

    except Exception as e:
      return f"Error: {str(e)}"

  @commands.command(name="pregunta")
  async def pregunta(self, ctx):
    """Consulta lo que quieras a Ollama AI."""
    consulta = ctx.message.content[9:]
    respuesta = self.obtenerRespuesta(consulta) 
    await ctx.send(respuesta)

async def setup(bot):
  await bot.add_cog(AICommandsCog(bot))
