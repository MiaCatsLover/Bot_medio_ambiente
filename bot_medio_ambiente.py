import discord
from discord.ext import commands
import os
import random
import requests

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Ha iniciado sesión como {bot.user}')

def dato():
    datos_curiosos = [
        "Reciclar una lata de aluminio ahorra suficiente energía como para hacer funcionar una televisión durante tres horas.",
        "Reciclar una sola botella de vidrio ahorra suficiente energía para encender una bombilla de 100 vatios durante cuatro horas.",
        "En promedio, una persona produce aproximadamente 1.5 kg de basura al día.",
        "Reciclar una tonelada de papel puede salvar 17 árboles, 26,500 litros de agua, y 3 metros cúbicos de espacio en el vertedero."
    ]
    return random.choice(datos_curiosos)

@bot.command()
async def medio_ambiente(ctx):
    await ctx.send("Bienvenido al bot del medio ambiente, con este bot aprenderemos sobre el medio ambiente y como cuidarlo!")
    await ctx.send("_______________________")
    await ctx.send("Para empezar, escribe $como_funciona para poder ver los comandos del bot!")
    await ctx.send("_______________________")
    await ctx.send("Toma un pequeño dato curioso sobre el medio ambiente antes de seguir:")
    await ctx.send("_______________________")
    await ctx.send(dato())

@bot.command()
async def como_funciona(ctx):
    await ctx.send("-$el_medio_ambiente para poder aprender sobre el medio ambiente.")
    await ctx.send("_______________________")
    await ctx.send("-$reciclaje para poder aprender sobre el reciclaje")
    await ctx.send("_______________________")
    await ctx.send("-$manualidad_1 para aprender como hacer una alcancía de cerdito con materiales reciclables")
    await ctx.send("_______________________")
    await ctx.send("-$manualidad_2 para aprender como hacer un carrito de juguete con materiales reciclables")
    await ctx.send("_______________________")
    await ctx.send("-$manualidad_3 para aprender como hacer una maceta de animales con materiales reciclables")
    await ctx.send("_______________________")
    await ctx.send("-$RRR para aprender sobre las 3 R")
    await ctx.send("_______________________")
    await ctx.send("-$prueba_final cuando ya hayas terminado con todo lo anterior, ponte aprueba con esta prueba final corta!")

@bot.command()
async def el_medio_ambiente(ctx):
    await ctx.send("Vamos a empezar con un video explicando qué es.")
    video_url = "https://youtu.be/8yo99_T4QZI?si=yhOaBdXKyNij7s7z"
    await ctx.send(video_url)
    await ctx.send("_______________________")
    await ctx.send("Muy bien! hay que tener en cuenta algo muy importante acerca del medio ambiente y es como lo afectamos?")
    await ctx.send("Con este video podras aprender como afectamos al medio ambiente")
    video_url = "https://youtu.be/TV-YEQOIFuQ?si=jVpLZCRzL7LQCcRs"
    await ctx.send(video_url)
    await ctx.send("_______________________")
    await ctx.send("puedes utilizar el comando -$como_funciona para poder seguir adelante!")

@bot.command()
async def reciclaje(ctx):
    await ctx.send("Vamos a empezar con un video explicando qué es.")
    video_url = "https://youtu.be/G3Vlm8abEfc?si=DBSgD1iWzVy-l8f4"
    await ctx.send(video_url)
    await ctx.send("_______________________")
    await ctx.send("Genial verdad? si quieres poner en practica el reciclaje recuerda esto!")
    video_url = "https://youtu.be/WVrxkF6TcQU?si=LBybDILVb_IAtVV3"
    await ctx.send(video_url)
    await ctx.send("utiliza $como_funciona para ver las otras opciones!")
@bot.command()
async def manualidad_1(ctx):
    await ctx.send("Primera manualidad: alcancía de cerdito.")
    with open('6 clase/imagenes/descargar (1).jpeg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    await ctx.send("Sigue los siguientes pasos para realizar tu alcancía.")
    video_url = "https://youtu.be/75B8pGCk4Y4?si=QGzrCSRw4VwM9VJI"
    await ctx.send(video_url)

@bot.command()
async def manualidad_2(ctx):
    await ctx.send("Segunda manualidad: carrito de juguete.")
    with open('6 clase/imagenes/descargar (2).jpeg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    await ctx.send("Sigue los siguientes pasos para realizar tu carrito.")
    video_url = "https://youtu.be/KwjI0iDT4dw?si=5zcRrMwUF8jXAo3f"
    await ctx.send(video_url)

@bot.command()
async def manualidad_3(ctx):
    await ctx.send("Tercera manualidad: maceta de animales.")
    with open('6 clase/imagenes/descargar.jpeg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    await ctx.send("Sigue los siguientes pasos para realizar tu maceta.")
    video_url = "https://youtu.be/yc_HsLrl6lY?si=oCHojDtr5oZImV0Y"
    await ctx.send(video_url)

@bot.command()
async def RRR(ctx):
    await ctx.send("Ahora aprenderemos un poco sobre las 3 R!")
    await ctx.send("_______________________")
    await ctx.send("Vamos a empezar con un video explicando qué es.")
    await ctx.send("_______________________")
    video_url = "https://youtu.be/cvakvfXj0KE?si=mdT66tc31jJBIBl1"
    await ctx.send(video_url)
    await ctx.send("_______________________")
    await ctx.send("Como podemos ver, las 3 R son muy importantes para el medio ambiente, así que las vamos a poner en práctica!")

@bot.command()
async def prueba_final(ctx):
    await ctx.send("Bienvenido a la prueba final! recuerda seguir instrucciones!")
    await ctx.send("Responde las siguientes preguntas colocando el numero de la pregunta y su respuesta.")
    await ctx.send("Por ejemplo: $1.A $2.B $3.C $4.D. USA MAYUSCULAS")
    await ctx.send("_______________________")
    await ctx.send("1. ¿Qué significan las 3 R?")
    await ctx.send("A- Reciclar, Reutilizar, Reducir.")
    await ctx.send("B- Reciclar, Rapidez, Reembolso.")
    await ctx.send("C- Riqueza, Reutilizar, Romper")
    await ctx.send("_______________________")
    await ctx.send("2. ¿Qué es el medio ambiente?")
    await ctx.send("A- Un lugar donde se gaurdan los animales.")
    await ctx.send("B- El conjunto de elementos naturales y humanos que rodean a los seres vivos.")
    await ctx.send("C- Un tipo de comida saludable.")
    await ctx.send("_______________________")
    await ctx.send("3. ¿Qué es la contaminación?")
    await ctx.send("A- El proceso de limpiar el agua.")
    await ctx.send("B- La presencia de sustancias sucias en el medio ambiente.")
    await ctx.send("C- La creacion de nuevos productos.")
    await ctx.send("_______________________")
    await ctx.send("4. ¿Qué es el reciclaje?")
    await ctx.send("A- El reciclaje es mezclar desechos para compactarlos.")
    await ctx.send("B- El reciclaje es eliminar basura sin darle un nuevo proposito")
    await ctx.send("C- El reciclaje es convertir desechos en nuevos productos.")


@bot.event
async def on_message(message):
    if message.content.startswith('1.A') or message.content.startswith('2.B') or message.content.startswith('3.B') or message.content.startswith('4.C'):
        opciones = {'1.A 2.B 3.B 4.C': 'Reciclar, Reutilizar, Reducir., El conjunto de elementos naturales y humanos que rodean a los seres vivos., La presencia de sustancias sucias en el medio ambiente.'}
        jugada_usuario = message.content
        resultado = ''
        if jugada_usuario == '1.A 2.B 3.B 4.C':
            resultado = '¡Todas tus respuestas son correctas!'
        else:
            resultado = '¡Incorrecto! La opción correcta era:'
            resultado += ' 1.A Reciclar, Reutilizar, Reducir., 2.B El conjunto de elementos naturales y humanos que rodean a los seres vivos., 3.B La presencia de sustancias sucias en el medio ambiente., 4.C El reciclaje es convertir desechos en nuevos productos.'
        await message.channel.send(resultado)
        await message.channel.send("Escribe -$terminar para acabar con la prueba")
    await bot.process_commands(message)

@bot.command()
async def terminar(ctx):
    await ctx.send("Felicidades, has acabado con la prueba final! gracias por usar nuestro bot.")
    await ctx.send("Recuerda que siempre hay que cuidar al planeta!")

bot.run("")