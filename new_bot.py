import discord
import random
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



bot.run("MTQyMTIzNDI1ODY2MzU3MTY2OQ.G1-TxY.GOXMhjGS8H96m0xbAN9Uroy3LHnvT-szTNYZng")
