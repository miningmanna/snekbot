from  tweepy import OAuthHandler
import tweepy
import asyncio
import discord
from discord.ext import commands
#CONSUMER_KEY = "CarhTKVMSPh1kU5J4dNtx0SMx"
#CONSUMER_SECRET = "Dl37LqaUFW6IKQFsDMIfabg18ZGPsSpgHOz4ZmBiaVjW3aw1Gq"
#ACCESS_TOKEN = "726509762406453248-ie2V0yN6bNmYpKJWzXAQJb1pXckLmLP"
#ACCESS_TOKEN_SECRET = "tafJFVOCoPPIf3FyD6boUShpWb75XAK03ayLumrJsHlTy"

class twitterlistener(commands.Cog):
    def __init__(self,bot):
        auth = OAuthHandler("CarhTKVMSPh1kU5J4dNtx0SMx","Dl37LqaUFW6IKQFsDMIfabg18ZGPsSpgHOz4ZmBiaVjW3aw1Gq")
        auth.set_access_token("726509762406453248-ie2V0yN6bNmYpKJWzXAQJb1pXckLmLP","tafJFVOCoPPIf3FyD6boUShpWb75XAK03ayLumrJsHlTy")
        self.client = tweepy.API(auth)
        self.chanel_list = []
        self.bot = bot
        self.get_tweet()

    async def get_tweet(self):
        latest_tweet = None
        while True:
            tweet = self.client.user_timeline("726509762406453248", count=1)[0]
            if tweet.in_reply_to_status_id == None and tweet.id != latest_tweet:
                for i in self.chanel_list:
                    await i.send("https://twitter.com/"+tweet.user.name+"/status/"+str(tweet.id))
                latest_tweet = tweet.id
            await asyncio.sleep(10)

    @commands.command()
    async def add_this(self,ctx):
            self.chanel_list.append(ctx.message.channel)
            ctx.message.channel.send("Added this channel to the list!")

def setup(bot):
    bot.add_cog(twitterlistener(bot))