import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = "/calc ", intents = intents)

@bot.event  
async def on_ready():
    print(f"se inicio el bot {bot.user}")

@bot.command()
async def hola(ctx):
    await ctx.send("Hola, cono estas ¿que operacion basica quieres que haga?")

@bot.command()
async def suma (ctx,num1:int,num2:int):
    suma = num1 + num2
    await  ctx.send(f"el resultado de {num1} mas {num2} es {suma}")

@bot.command()
async def resta (ctx,num1:int,num2:int):
    resta = num1 - num2
    await  ctx.send(f"el resultado de {num1} menos {num2} es {resta}")

@bot.command()
async def divide (ctx,num1:int,num2:int):
    division = num1 / num2
    await  ctx.send(f"el resultado de {num1} entre {num2} es {division}")

@bot.command()
async def multiplica(ctx, num1: int, num2: int):
    multiplicacion = num1 * num2
    await ctx.send(f"El resultado de {num1} por {num2} es {multiplicacion}")

@bot.command()
async def potencia(ctx, num1: int, num2: int):
    potencia = num1 ** num2
    await ctx.send(f"El resultado de {num1} evelado a la {num2} es {potencia}")

@bot.command()
async def compara(ctx, num1: int, num2: int):
    if num1 < num2:
        await ctx.send(f"El numero {num1} es menor a {num2}")
    elif num1 > num2:
        await ctx.send(f"El numero {num1} es mayor a {num2}")
    else:
        await ctx.send(f"El numero {num1} es igual a {num2}")

@bot.command()
async def raiz (ctx, num: int):
    resultado = num ** 0.5
    await ctx.send(f"La raíz cuadrada de {num} es {resultado}")

@bot.command()
async def porcentaje (ctx, num1: int, num2: int):
    resultado1 = num2 / 100
    resultado = resultado1 * num1
    await ctx.send(f"El {num1}% de {num2} es {resultado}")

@bot.command()
async def numero (ctx, ran1: int, ran2:int):
    num1 = random.randint(ran1,ran2)
    await ctx.send(f"Eligo el numero {num1}")

#traductor

bot.run("MTMwMDU3OTA4NTc3MjM5MDQ1MA.GW3TXQ.5-grxyVHx4Pc2SqUusgFZw8mUDOMNC1GZp2lFU")