import os
import discord
from discord.ext import commands
import requests
from dotenv import load_dotenv
import io

from urllib.parse import quote_plus

# Load environment variables
load_dotenv()

# Configuration
API_URL = os.getenv('API_URL', "http://149.56.19.221:27004")
API_TOKEN = os.getenv('API_TOKEN')
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

# Set up intents
intents = discord.Intents.all()

# Create bot with command prefix
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    print(f'Connected to API: {API_URL}')
    print('------')

@bot.command(name='meme')
async def generate_meme(ctx, *, text=None):
    """
    Generate a meme with the given text.
    Usage: !meme Your funny text here
    """
    # Validate API token
    if not API_TOKEN:
        await ctx.send("❌ API token is not configured. Please contact the administrator.")
        return

    # Check if text is provided
    if not text:
        await ctx.send("Please provide text for the meme. Usage: !meme Your funny text here")
        return

    # Show a loading message
    loading_message = await ctx.send("Generating your meme... 🤖")

    try:
        headers = {
            'accept': 'application/json',
            'x-token': 'Test',
            'Content-Type': 'application/json'
        }
        data = {
            "user_input": text
        }

        print(f"{API_URL}/generate_meme")
        response = requests.post(f"http://149.56.19.221:27010/generate_meme", headers=headers, json=data)
        print(headers)
        print(data)
        print(response.json())
        if response.status_code == 200:
            print("SUCCESS")
            # Return the URL for the newly generated meme
            meme_url = f"{API_URL}/generated_images/" + quote_plus(response.json()["meme"])
            print(meme_url)
            embed = discord.Embed(title="Here's your image")
    
            # Set the image of the embed using the URL
            embed.set_image(url=meme_url)
            
            # Send the embed in the channel where the command was called
            await ctx.send(embed=embed)
            await loading_message.delete()
        else:
            print("Error generating meme:", response.text)
            return f"{API_URL}/home", 

    except requests.RequestException as e:
        await ctx.send(f"Error connecting to meme generation service: {str(e)}")
        await loading_message.delete()

@bot.command(name='memeguide')
async def meme_guide(ctx):
    """
    Provides instructions on how to use the meme bot
    """
    guide = """
**Meme Generator Bot Guide** 🤖🖼️

• Use `!meme` to generate a meme
• Simply type `!meme` followed by your desired text
• Example: `!meme When you finally fix that bug`

**Tips:**
• Keep your text concise and fun
• The bot will generate a meme based on your input
• Memes are generated randomly, so results may vary
    """
    await ctx.send(guide)

# Error handling for command errors
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please provide text for the meme. Use `!memeguide` for help.")
    else:
        print(f"An error occurred: {error}")

# Run the bot
def main():
    # Validate tokens
    if not DISCORD_TOKEN:
        print("ERROR: No Discord token found. Please set DISCORD_TOKEN in your .env file.")
        return
    
    if not API_TOKEN:
        print("WARNING: No API token found. API authentication may fail.")

    bot.run(DISCORD_TOKEN)

if __name__ == "__main__":
    main()