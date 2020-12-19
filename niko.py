from  tweepy import OAuthHandler
import tweepy
import asyncio
import discord
from discord.ext import commands
#CONSUMER_KEY = "CarhTKVMSPh1kU5J4dNtx0SMx"
#CONSUMER_SECRET = "Dl37LqaUFW6IKQFsDMIfabg18ZGPsSpgHOz4ZmBiaVjW3aw1Gq"
#ACCESS_TOKEN = "726509762406453248-mwzLPJescuCAzlQ0jGXlKUt3mXr8qS0"
#ACCESS_TOKEN_SECRET = "4gdabNFwautslbM2mevnLw1kutkQkPnlNnNufMvIWDsGa"

class twitterlistener(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        auth = OAuthHandler("CarhTKVMSPh1kU5J4dNtx0SMx","Dl37LqaUFW6IKQFsDMIfabg18ZGPsSpgHOz4ZmBiaVjW3aw1Gq")
        auth.set_access_token("726509762406453248-mwzLPJescuCAzlQ0jGXlKUt3mXr8qS0","4gdabNFwautslbM2mevnLw1kutkQkPnlNnNufMvIWDsGa")
        self.client = tweepy.API(auth)
        self.chanel_list = []
        bot.loop.create_task(self.get_tweet())

    async def get_tweet(self):
        latest_tweet = None
        while True:
            tweet = self.client.user_timeline("3096462845", count=1)[0]
            if tweet.in_reply_to_status_id == None and tweet.id != latest_tweet:
                for i in self.chanel_list:
                    await i.send("https://twitter.com/"+tweet.user.name+"/status/"+str(tweet.id))
                    await i.send("https://tenor.com/view/niko-gif-18543948")
                latest_tweet = tweet.id
            await asyncio.sleep(30)

    @commands.command()
    async def add_this(self,ctx):
            if (ctx.message.channel not in self.chanel_list):
                self.chanel_list.append(ctx.message.channel)
                await ctx.message.channel.send("Added this channel to the list!")
                tweet = self.client.user_timeline("3096462845", count=1)[0]
                await ctx.message.channel.send("The latest tweet is: https://twitter.com/" + tweet.user.name + "/status/" + str(tweet.id))
                await ctx.message.channel.send("https://tenor.com/view/niko-gif-18543948")
            else:
                await ctx.message.channel.send("This channel is already in the list!")

    @commands.command()
    async def niko_moment(self,ctx):
        tweet = self.client.user_timeline("3096462845", count=1)[0]
        await ctx.message.channel.send("The latest niko tweet is: https://twitter.com/" + tweet.user.name + "/status/" + str(tweet.id))
        await ctx.message.channel.send("https://tenor.com/view/niko-gif-18543948")



def setup(bot):
    bot.add_cog(twitterlistener(bot))