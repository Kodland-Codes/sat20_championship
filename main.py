import discord
from discord.ext import commands
import os
import random
import requests

# Discord botunun Discord sunucusuna mesaj atmasi icin izinleri acmamiz gerekiyor.
intents = discord.Intents.default()
intents.message_content = True

#Botumu olusturuyoruz
bot = commands.Bot(command_prefix='!', intents=intents)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']



@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben bir botum!')
    
@bot.command()
async def kodland(ctx):
    await ctx.send(f'Kodlanda {bot.user}! hoşgeldiniz')

@bot.command()
async def name(ctx):
    await ctx.send(f'Merhaba, benim ismim Kuzey')
    
@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("Selim" * count_heh)
    
    
@bot.command()
async def mem(ctx):
    resimler_listesi = os.listdir('images') #['resim1.jpeg', 'resim2.jpeg', 'resim3.jpeg']
    with open(f'images/{random.choice(resimler_listesi)}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)
    
@bot.command()
async def duck(ctx): 
    '''
    Merhaba ismim Kuzey
    Bu bir yorumdur!
    '''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

bot.run("TOKENINIZI BURAYA YAPISTIRIN")

