#!/usr/bin/env python

import discord
from discord.ext import commands
import random
import asyncio
import re
import sys

from fivebot.dice import DiceBag, DiceError

description = """ FiveBot est un lanceur de dés pour le système Roll n' Keep.
Entre autres choses. """

bot = commands.Bot(command_prefix='@', description=description)


@bot.event
@asyncio.coroutine
def on_ready():
    print("Connecté en tant que:")
    print(bot.user.name)
    print(bot.user.id)
    print("------------")

@bot.command(pass_context=True, description="Kills the bot")
@asyncio.coroutine
def kill(ctx):
    print("Kill command received")
    
    if (ctx.message.author.name=="Calmacil"):
        yield from bot.logout()
    yield from bot.send_message(ctx.message.channel, "Bien essayé, petit coquin, mais c’est raté! *Fait une croix*")

@bot.event
@asyncio.coroutine
def on_message(msg):
    """ Parses incoming messages """
    response = None
    comment = ""
    
    if not isinstance(msg, discord.Message):
        raise TypeError("Message expected")
    
    chan = msg.channel
    user_nick = msg.author.name
    content = ' '.join(msg.content.replace('+', ' + ').replace('-', ' - ').split())
    if hasattr(msg.author, 'nick'):
        user_nick = msg.author.nick
    
    # get comment
    comment_pos = content.find('#')     # no excetpion raised if not found
    if comment_pos > 0:
        comment = content[comment_pos+1:]
        content = content[:comment_pos]
        
    # splits the string
    content = content.split(' ')
    
    # check for dice roll
    dice_pattern = re.compile('\d+k[euml]{,4}\d+')
    
    if dice_pattern.match(content[0]):
        print("Roll detected")
        bag = DiceBag(content)
        try:
            resp = "%s a lancé %s et a obtenu %s\n%s" % (user_nick,
                                                         " ".join(content),
                                                         bag.roll(),
                                                         comment)
        except DiceError as e:
            resp = e.args[0]
        
        del bag
        yield from bot.send_message(chan, resp)
    
    yield from bot.process_commands(msg)


bot.run('shiba.kusabana@gmail.com', 'T3r03k@r')