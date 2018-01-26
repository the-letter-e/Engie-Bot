import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix="#")

@bot.event
async def on_ready():
    print("Ready when you are!")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: Pong!")
    
@bot.command(pass_context=True)
async def Bam(ctx):
    await bot.say("Pow!")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    await bot.say("The users name is: {}".format(user.name))
    await bot.say("The users ID is: {}".format(user.id))
    await bot.say("The users status is: {}".format(user.status))
    await bot.say("The users highest role is: {}".format(user.top_role))
    await bot.say("The user joined at: {}".format(user.joined_at))

@bot.command(pass_context=True)
async def pootis(ctx):
    await bot.say("Pow!")

@bot.command(pass_context=True)
async def commands(ctx):
    await bot.say("A list of commands are:")
    await bot.say("#Ping")
    await bot.say("#Bam")
    await bot.say("#Pootis")
    await bot.say("#info -@user-")

bot.run ("NDA1MTc4NzIyMDg2Mjg5NDM4.DUwJYQ.R4mzxZ4j42OIc6ztCUt_d7yQ7uM")
client.close
