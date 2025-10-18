import os
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='$')


def is_bot_admin():
    async def predicate(ctx):
        print("Running on channel: {}".format(ctx.channel))
        if "tsuki-admin" in [role.name.lower() for role in ctx.author.roles]:
            return True
    return commands.check(predicate)


def is_in_channel(name):
    async def predicate(ctx):
        return str(ctx.channel) == name
    return commands.check(predicate)


@bot.event
async def on_ready():
    print('Logged in as: {}'.format(bot.user.name))


@bot.command()
@is_in_channel(name="bot")
async def message(ctx, channel: discord.TextChannel, *, message):
    await channel.send(message)


@bot.command()
@is_in_channel(name="bot")
async def greet(ctx, user: discord.Member, channel: discord.TextChannel):
    await channel.send("hello {} how are you ?".format(user.mention))


@greet.error
async def greet_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        return False


@bot.command()
@is_in_channel(name="general")
async def kick(ctx, *, member: discord.Member):
    print(member)
    await ctx.send('kicking user')


@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("You forgot to mention the user...")


bot.run(os.environ['DC_BOT_KEY'])
