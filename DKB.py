import discord

# Variabel intents menyimpan hak istimewa bot
intents = discord.Intents.default()
# Mengaktifkan hak istimewa message-reading
intents.message_content = True
# Membuat bot di variabel klien dan mentransfernya hak istimewa
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Kita telah masuk sebagai {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("ello")
    elif message.content.startswith('$bye'):
        await message.channel.send("aight goodbye")
    else:
        await message.channel.send(message.content)

client.run("MTIwNjU5MzIzNjQyMTA1NDQ5Ng.GgRho5.IWm9SDNsgIb1bCjbGJ4nHGlMWhdW3kuH-bWq4Q")
