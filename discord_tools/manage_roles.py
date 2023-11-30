import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!', description='Role management bot')

@bot.command()
@commands.has_permissions(manage_roles=True)
async def role(ctx, action, member: discord.Member, role: discord.Role):
    if action == 'assign':
        await member.add_roles(role)
        await ctx.send(f'Assigned {role.name} to {member.display_name}')
    elif action == 'remove':
        await member.remove_roles(role)
        await ctx.send(f'Removed {role.name} from {member.display_name}')
    else:
        await ctx.send('Invalid action. Use assign or remove.')

def manage_roles(action, user_id, role_name):
    # This function would be integrated with the bot commands for role management
    bot.run()