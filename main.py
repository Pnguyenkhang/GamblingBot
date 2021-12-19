from dotenv import load_dotenv
import os
import discord
from discord.ext import commands
import asyncio
import random


client = commands.Bot(command_prefix='$')

@client.event
async def on_ready():
    print("I am online!, my commands are $")

@client.command(aliases = ['8ball','roll','ask']) # can avoke using any keywords
async def _8ball(ctx, *, question): # Context, question mark, asterisk allows me to take in multiple parameters
    responses = ['no',
    'yes',
    'maybe',
    'never',
    'absolutely never',
    'definite yes']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

load_dotenv()
# Environment variables
API_KEY = os.getenv("API_KEY")

client.run(API_KEY)