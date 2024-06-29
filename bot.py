import discord
import subprocess

# Discord bot token and channel ID
TOKEN = "MTI1NjQzOTUwMDM4OTg3NTc2Mw.GXigMy.HMRdE6x2IW_oW6rqFQra5zzGs6KEehMatOd_RU"
CHANNEL_ID = 1254225272018960468  # Replace with your channel ID

# Discord webhook URL for logging
DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/1256332185250693170/gJYC8ICYlDSaboCy-3sSluywg2RY1VrUGuSI4fGPPk_USJx8JMmfKrO_wasZmK81UEqo'

# Start task_script.py subprocess
subprocess.Popen(["python", "main.py", DISCORD_WEBHOOK_URL])

# Initialize Discord client
intents = discord.Intents.default()
intents.typing = False
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    # Forward message content to specified channel
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        await channel.send(message.content)  # Sending only the message content without prefix

# Run the bot with your token
client.run(TOKEN)
