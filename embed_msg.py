#creating a bot

import discord
from discord.ext import commands

from discord import colour
# client = discord.Client()

# creating a command
client = commands.Bot(command_prefix='--')


@client.command(name='version')
async def version(context):

    myEmbed = discord.Embed(
        title="Current version", description="The bot is version 1.0", color=0xff00)
    myEmbed.add_field(name="Version code: ", value="v1.0.0", inline=False)
    myEmbed.add_field(name="Date Released ",
                      value="July 18th, 2021", inline=False)
    myEmbed.set_footer(text="This is a sample footer!")
    myEmbed.set_author(name="Spunkey")

    # Here we are not specifying any particular channel id so these commands can run on any channel
    await context.message.channel.send(embed=myEmbed)


@client.event
async def on_ready():

    general_channel = client.get_channel(849549651400065074)
    await general_channel.send('Hello, world! This is bash!')


@client.event
# on_message func takes an parameter message and this function runs when somebody sends a message
async def on_message(message):
    if message.content == 'what is the version':
        general_channel = client.get_channel(849549651400065074)

        myEmbed = discord.Embed(
            title="Current version", description="The bot is version 1.0", color=0xff00)
        myEmbed.add_field(name="Version code: ", value="v1.0.0", inline=False)
        myEmbed.add_field(name="Date Released ",
                          value="July 18th, 2021", inline=False)
        myEmbed.set_footer(text="This is a sample footer!")
        myEmbed.set_author(name="Spunkey")

        await general_channel.send(embed=myEmbed)

    # we have to specify this bc we are using this content for commands
    await client.process_commands(message)

    if message.content == '/who':
        general_channel = client.get_channel(849549651400065074)
        await general_channel.send('I\'m bash')


client.run('ODQ5NTQyNDIwMzc1MTQyNDEw.YLcsCA.73gdKpq9GDAXoJz-PZsSCxUYTdw')
