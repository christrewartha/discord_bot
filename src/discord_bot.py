import discord
import discord_responses
import sys


async def send_message(message, user_message, is_private):
    try:
        response = discord_responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
        
    except Exception as e:
        print(e)


def run_discord_bot():
    
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    
    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
        
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        
        print(f'{username} said: "{user_message}" ({channel})')
        
        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)
            
    sys.path.insert(0, '../../secret_config')
    from discord_bot_secret import DISCORD_BOT_TOKEN
    client.run(DISCORD_BOT_TOKEN)


if __name__ == "__main__":
    run_discord_bot()
