from discord.ext import commands

class Hello(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        await ctx.send(f'Hello! I am a bot! I am here to help you! Type .help for more info! {ctx.author.mention}')

async def setup(bot):
    await bot.add_cog(Hello(bot))