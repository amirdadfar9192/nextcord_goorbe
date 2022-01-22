
import nextcord
from nextcord.ext import commands
from nextcord import Member
import os


intents = nextcord.Intents.default()
intents.members = True
dash = '!------------------------!'
client = commands.Bot(command_prefix = '%', intents = intents)


@client.event
async def on_ready():
    print("bot is now ready to use")
    print(dash)
    await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.listening, name='Prefix == "%" Enjoy:)'))



initial_extensions = []

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        initial_extensions.append("cogs." + filename[:-3])



if __name__ == '__main__':
    for extension in initial_extensions:
        client.load_extension(extension)          

token = os.getenv("DISCORD_TOKEN")
client.run(token)    