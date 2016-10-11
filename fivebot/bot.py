# -*- coding: utf-8 -*-

from irc.bot import SingleServerIRCBot


class FiveBot(SingleServerIRCBot):
    """ Extends the basic IRCBot

    Handles connection and receives messages from server
    """

    def __init__(self, server, port, channel, nickname):
        """ Initializes the client """
        super().__init__([(server, port)], nickname, "FiveBot")
        self.channel = channel
        print("Ready.")

    def on_nicknameinuse(self, conn, ev):
        """ Manages the case where the bot's nickname already in use. """
        print("Nickname " + conn.get_nickname() + " already in use.")
        conn.nick(conn.get_nickname() + "_")

    def on_welcome(self, conn, ev):
        """ Joins the game chan when connection OK. """
        print("Connected to server.")
        conn.join(self.channel)

    def on_pubmsg(self, conn, ev):
        """ Handles public messages on game channel """
        print(ev)
