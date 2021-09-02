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
            'https://66.media.tumblr.com/f1449d030ffb2a856b2ec8fe6ece0798/tumblr_pw6x3nggXd1ue1d0so1_500.gif', # noqa
            'https://www.icegif.com/wp-content/uploads/icegif-3463.gif',
            'https://mkwishes.com/wp-content/uploads/2021/01/Good-Morning-Tuesday1.gif',
            'https://mkwishes.com/wp-content/uploads/2021/04/Good-Morning-Tuesday19.gif',
            'https://c.tenor.com/4GPy7EP_4i8AAAAd/happy-taco-tuesday-cat.gif',
            'https://c.tenor.com/yXU2_012aB4AAAAC/taco-tuesday.gif',
            'https://c.tenor.com/5oHfBsoa6EcAAAAC/taco-tuesday-time.gif'
        ]
        self.send_card(
            in_reply_to=msg,
            color='white',
            image=secrets.choice(urls))
