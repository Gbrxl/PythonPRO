import discord
import random
import os
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello, I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.group()
async def cool(ctx):
    """Says if a user is cool.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool.')

@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')


@bot.command()
async def song(ctx):
    """Recommends a random song"""
    songs = [
        "'Blinding Lights' - The Weeknd",
        "'Shape of You' - Ed Sheeran",
        "'Levitating' - Dua Lipa",
        "'As It Was' - Harry Styles",
        "'Flowers' - Miley Cyrus",
    ]
    choice = random.choice(songs)
    await ctx.send(f"I recommend listening to: {choice}")

@bot.command()
async def meme(ctx):
    imagenes = os.listdir('imagenes')
    with open(f'imagenes/{random.choice(imagenes)}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)
    #Obtener imagenes aleatorias de patos
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

    #Obtener aleatoriamente una imagen de perro desde una API
def get_dog_image_url():
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']
@bot.command('dog')
async def dog(ctx):
    image_url = get_dog_image_url()
    embed = discord.Embed(title="🐶 ¡Un perrito para ti!")
    embed.set_image(url=image_url)
    await ctx.send(embed=embed)

#Obtener aleatoriamente una imagen de zorro desde una API
def get_fox_image_url():
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    data = res.json()
    return data['image']

@bot.command('fox')
async def fox(ctx):
    image_url = get_fox_image_url()
    embed = discord.Embed(title="🦊 ¡Un zorro salvaje aparece!")
    embed.set_image(url=image_url)
    await ctx.send(embed=embed)

#Obtener aleatoriamente un Pokémon desde una API
def get_pokemon():
    pokemon_id = random.randint(1, 151)  # primeros 151 (generación 1)
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}'
    res = requests.get(url)
    data = res.json()
    nombre = data['name'].capitalize()
    imagen = data['sprites']['front_default']
    return nombre, imagen
@bot.command('pokemon')
async def pokemon(ctx):
    nombre, imagen = get_pokemon()
    embed = discord.Embed(title=f"🎮 ¡Has encontrado a {nombre}!")
    embed.set_image(url=imagen)
    await ctx.send(embed=embed)

#Buscar información de un anime usando la API de Kitsu
def buscar_anime(texto):
    url = f'https://kitsu.io/api/edge/anime?filter[text]={texto}'
    res = requests.get(url)
    data = res.json()
    if not data['data']:
        return None
    anime = data['data'][0]['attributes']
    titulo = anime['canonicalTitle']
    sinopsis = anime['synopsis'][:400] + "..."
    imagen = anime['posterImage']['original']
    return titulo, sinopsis, imagen
@bot.command('anime')
async def anime(ctx, *, nombre_anime):
    resultado = buscar_anime(nombre_anime)
    if resultado:
        titulo, sinopsis, imagen = resultado
        embed = discord.Embed(title=f"🎌 {titulo}", description=sinopsis)
        embed.set_image(url=imagen)
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ No encontré ningún anime con ese nombre.")

@bot.command('eco')
async def eco(ctx):
    consejos = {
        "♻️ Usa botellas reutilizables en lugar de botellas plásticas.": "https://images.unsplash.com/photo-1600181953229-3a2ce3cdb5b4?auto=format&fit=crop&w=800&q=80",  
        "🛍️ Lleva tus propias bolsas cuando vayas de compras.": "https://images.unsplash.com/photo-1593032465171-8fda6a22e8b0?auto=format&fit=crop&w=800&q=80",  # 
        "🍽️ Evita los utensilios de un solo uso. Usa platos y cubiertos reutilizables.": "https://images.unsplash.com/photo-1615485290345-8ff2a34b0b2f?auto=format&fit=crop&w=800&q=80",  
        "👕 Dona o reutiliza ropa en lugar de tirarla.": "https://images.unsplash.com/photo-1593032465171-8fda6a22e8b0?auto=format&fit=crop&w=800&q=80",  
        "🌱 Crea un pequeño huerto con restos de frutas o verduras.": "https://images.unsplash.com/photo-1501004318641-b39e6451bec6?auto=format&fit=crop&w=800&q=80",  
        "🔌 Apaga luces y dispositivos que no estés usando.": "https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&w=800&q=80",  
        "💧 Cierra el grifo mientras te cepillas los dientes para ahorrar agua.": "https://images.unsplash.com/photo-1603561590928-1c9adf5f1d4b?auto=format&fit=crop&w=800&q=80",  
        "📦 Reutiliza cajas y frascos para guardar tus cosas.": "https://images.unsplash.com/photo-1616628188463-1f7c0e4a91cf?auto=format&fit=crop&w=800&q=80",  
        "🚴 Usa la bici o camina cuando puedas, en lugar de usar auto.": "https://www.google.com/imgres?q=Imagenes%20de%20bici%20en%20el%20parque&imgurl=https%3A%2F%2Fmedia.tacdn.com%2Fmedia%2Fattractions-splice-spp-674x446%2F13%2F63%2F41%2F1e.jpg&imgrefurl=https%3A%2F%2Fwww.viator.com%2Fes-ES%2Ftours%2FSan-Francisco%2FGolden-Gate-Park-Bike-Rentals%2Fd651-5557P40&docid=0RiRhntqoBma7M&tbnid=UI5MC725YTTBCM&vet=12ahUKEwiIurrokayQAxVmRDABHYyYNe4QM3oECBwQAA..i&w=670&h=446&hcb=2&ved=2ahUKEwiIurrokayQAxVmRDABHYyYNe4QM3oECBwQAA"  
    }

    consejo, imagen_url = random.choice(list(consejos.items()))

    embed = discord.Embed(
        title="🌿 Consejo ecológico del día",
        description=consejo,
        color=0x2ECC71
    )
    embed.set_image(url=imagen_url)
    await ctx.send(embed=embed)


bot.run()
