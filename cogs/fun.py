import random
from discord.ext import commands

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roll(ctx, sides: int = 6):
      if sides <= 1:
        await ctx.send("Invalid number of sides. The dice must have at least 2 sides.")
      else:
        result = random.randint(1, sides)
        await ctx.send(f"Rolled a {sides}-sided dice: {result}")

async def setup(bot):
    await bot.add_cog(Fun(bot))