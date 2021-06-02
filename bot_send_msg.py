#creating a bot

import discord
client = discord.Client()

@client.event
async def on_ready():
    
    #copy ID of your general channel
    general_channel = client.get_channel(849549651400065074)
    await general_channel.send('Hello, world! This is bash!')


client.run('ODQ5NTQyNDIwMzc1MTQyNDEw.YLcsCA.73gdKpq9GDAXoJz-PZsSCxUYTdw')

 