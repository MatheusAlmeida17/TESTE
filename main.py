import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup

TOKEN = 'SEU_TOKEN_DO_DISCORD'

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def complete(ctx):
    await ctx.send('pesquisar')
  
@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

@bot.command(name='pesquisar')
async def search(ctx, *, query):
    """
    Pesquisa no site BC.
    Uso: !pesquisar <termo de pesquisa>
    """
    search_url = f'https://bc.demaria.com.br/?s={query}'

    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = soup.find_all('h2', class_='entry-title')

    found_results = []
    for result in results:
        link = result.a['href']
        if query.lower() in link.lower():
            found_results.append(link)

    if found_results:
        await ctx.send('Resultados encontrados:')
        for link in found_results:
            await ctx.send(link)
    else:
        await ctx.send('Nenhum resultado encontrado.')
      
@bot.event
async def on_message(message):
    if message.content.lower() == '!requisitos':
        link = 'https://demaria.com.br/contratos/DOCWindows-Requisitos-vs6-vs2017.pdf?_gl=1*166ubup*_ga*OTY2ODUxMzE2LjE2ODQyNDUwMTU.*_ga_4H3B9QN4Y1*MTY4NTY0MzY4Ni41LjEuMTY4NTY0MzY5My41My4wLjA.&_ga=2.132789894.943848404.1685643687-966851316.1684245015'
        await message.channel.send(link)

    await bot.process_commands(message)
bot.run('MTExMzU1NTgwMDY5NTI1NTEzMA.G4sKvE.855QYFaz6MdW40sdOQbRAwDZb11XMyOmQoj20E')