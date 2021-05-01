import discord

client = discord.Client()


def init_bot(token):
    client.run(discord.Client())
    pass


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    pass

@client.event
async def on_emote_receive(event):
    pass