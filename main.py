import discord
from discord.ext import commands

intents = discord.Intents.default()

bot = commands.Bot(command_prefix='?', description="Remember yourself!", intents=intents)

with open ("token.txt", "r") as file:
    token=file.readlines()[0]



bot.run(token)