#creating a bot

import discord
client = discord.Client()


@client.event
async def on_ready():

    general_channel = client.get_channel(849549651400065074)
    await general_channel.send('Hello, world! This is bash!')


@client.event
# on_message func takes an parameter message and this function runs when somebody sends a message
async def on_message(message):
    if message.content == 'what is the version':
        general_channel = client.get_channel(849549651400065074)
        await general_channel.send('The version is bash 1.0!')


client.run('ODQ5NTQyNDIwMzc1MTQyNDEw.YLcsCA.73gdKpq9GDAXoJz-PZsSCxUYTdw')
