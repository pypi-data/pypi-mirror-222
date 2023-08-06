# skip.py | commands for skipping images
# Copyright (C) 2019-2021  EraserBird, person_v1.32, hmmm

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from discord.ext import commands

from sciolyid.data import database, format_wiki_url, logger
from sciolyid.data_functions import streak_increment
from sciolyid.functions import CustomCooldown


class Skip(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Skip command - no args
    @commands.hybrid_command(help="- Skip the current image to get a new one", aliases=["sk"])
    @commands.check(CustomCooldown(5.0, bucket=commands.BucketType.channel))
    async def skip(self, ctx: commands.Context):
        logger.info("command: skip")

        current_item = database.hget(f"channel:{ctx.channel.id}", "item").decode(
            "utf-8"
        )
        database.hset(f"channel:{ctx.channel.id}", "item", "")
        database.hset(f"channel:{ctx.channel.id}", "answered", "1")
        if current_item:  # check if there is image
            url = format_wiki_url(ctx, current_item)
            await ctx.send(f"Ok, skipping {current_item.lower()}")
            await ctx.send(url)  # sends wiki page
            streak_increment(ctx, None)  # reset streak
            if database.exists(f"race.data:{ctx.channel.id}"):
                logger.info("auto sending next image")
                group, state, bw = database.hmget(
                    f"race.data:{ctx.channel.id}", ["group", "state", "bw"]
                )
                media = self.bot.get_cog("Media")
                await media.send_pic(ctx, group.decode("utf-8"), state.decode("utf-8"), bw.decode("utf-8"))
        else:
            await ctx.send("You need to ask for an image first!")


async def setup(bot):
    await bot.add_cog(Skip(bot))
