#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This file is the launcher file of FiveBot
'And Five rings for the holy Samurai, beyond the mountains'
Copyright © Calmacil 2016
"""

from fivebot.bot import FiveBot

config = {
    "server": "irc.quakenet.org",
    "port": 6667,
    "channel": "#Iaijutsu",
    "nickname": "Yamaneko",
    "gmnick": ["Calmacil","MJ-Sama", "MJ", "Meujeu", "Calmaster", "Calmacil_"],
    "datadir": "characters"
}

if __name__ == '__main__':
    bot = FiveBot(config['server'], config['port'], config['channel'], config['nickname'])
    bot.start()
