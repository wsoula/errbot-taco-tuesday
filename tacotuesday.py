"""Random Facts"""
import re
import secrets
from errbot import BotPlugin, re_botcmd


class Tacotuesday(BotPlugin):
    """Random Taco Tuesday Gif"""
    @re_botcmd(pattern=r"Taco Tuesday", prefixed=False, flags=re.IGNORECASE)
    def taco_tuesday(self, msg, args):
        """Send gif"""
        urls = [
            'https://wifflegif.com/gifs/682069-taco-tuesday-lebron-james-gif',
            'https://wifflegif.com/gifs/10653-taco-tuesday-taco-spam-gif'
        ]
        self.send_card(
            in_reply_to=msg,
            color='white',
            image=secrets.choice(urls))
