import discord
from discord.ext import commands

intents = discord. Intents.default()
 # type: ignoreintents.members = True

client = commands.Bot(command_prefix = '!', intents=intents)

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name='noob')
    await member.add_roles(role)

client.run('MTA2MDAwNTk5NTgwOTYwNzc4MQ.GSMJyR.GyCBwVXZ2pA7YfwxONHzOGFDRayhKhxJ9phO5E')