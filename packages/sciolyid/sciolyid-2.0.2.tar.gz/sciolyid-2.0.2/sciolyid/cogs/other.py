# other.py | misc. commands
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

import itertools
import random
from difflib import get_close_matches

import wikipedia
from discord import app_commands
from discord.ext import commands

import sciolyid.config as config
from sciolyid.core import send_image
from sciolyid.data import (
    aliases,
    all_categories,
    arg_autocomplete,
    dealias_group,
    groups,
    logger,
    master_id_list,
    meme_list,
    states,
)
from sciolyid.functions import CustomCooldown, build_id_list

# Discord max message length is 2000 characters, leave some room just in case
MAX_MESSAGE = 1950


class Other(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @staticmethod
    def broken_join(input_list, max_size: int = MAX_MESSAGE):
        out = []
        temp = ""
        for item in input_list:
            temp += f"{item}\n"
            if len(temp) > max_size:
                out.append(temp)
                temp = ""
        if temp:
            out.append(temp)
        return out

    # Info - Gives image
    @commands.hybrid_command(
        help=f"- Gives images of specific {config.options['id_type']}", aliases=["i"]
    )
    @commands.check(CustomCooldown(5.0, bucket=commands.BucketType.user))
    @app_commands.rename(arg=f"{config.options['id_type']}_and_filters")
    @app_commands.describe(
        arg=f"The {config.options['id_type']} must come before any options."
    )
    async def info(self, ctx: commands.Context, *, arg):
        logger.info("command: info")

        matches = get_close_matches(
            arg.lower(),
            itertools.chain(master_id_list, *aliases.values()),
            n=1,
            cutoff=0.8,
        )
        if matches:
            item = matches[0]

            if item in itertools.chain.from_iterable(aliases.values()):
                logger.info("matched alias! getting item name.")
                item = next(key for key, value in aliases.items() if item in value)

            if ctx.interaction is None:
                delete = await ctx.send("Please wait a moment.")
            else:
                await ctx.typing()

            an = "an" if item.lower()[0] in ("a", "e", "i", "o", "u") else "a"
            await send_image(
                ctx, str(item), message=f"Here's {an} *{item.lower()}* image!"
            )
            if ctx.interaction is None:
                await delete.delete()

        else:
            await ctx.send(
                f"{config.options['id_type'][:-1].title()} not found. Are you sure it's on the list?",
                ephemeral=True,
            )

    # List command
    @commands.hybrid_command(
        help="- DMs the user with the appropriate list.", name="list"
    )
    @commands.check(CustomCooldown(5.0, bucket=commands.BucketType.user))
    @app_commands.describe(state_or_group="list or group options")
    @app_commands.autocomplete(state_or_group=arg_autocomplete)
    async def list_of_items(self, ctx: commands.Context, state_or_group=""):
        logger.info("command: list")

        if ctx.interaction is not None:
            await ctx.typing()

        group_args = set(
            map(
                dealias_group,
                all_categories.intersection(set(state_or_group.lower().split(" "))),
            )
        )
        state_args = set(states.keys()).intersection(
            set(state_or_group.upper().split(" "))
        )
        if not state_args:
            state_args = {config.options["default_state_list"]}

        build = build_id_list(group_args, state_args)
        group_list = sorted(build)
        item_lists = self.broken_join(group_list)

        display_group = list(group_args)
        if not display_group:
            display_group.append(config.options["id_type"])
        elif len(display_group) > 1:
            display_group[-1] = "and " + display_group[-1]

        display_state = list(state_args)
        if len(display_state) > 1:
            display_state[-1] = "and " + display_state[-1]

        if ctx.author.dm_channel is None:
            await ctx.author.create_dm()

        await ctx.author.dm_channel.send(
            f"**{','.join(display_group).capitalize()} in the {','.join(display_state)} list{'s' if len(display_state) > 1 else ''}:**"
        )
        for page in item_lists:
            await ctx.author.dm_channel.send(f"```\n{page}```")

        await ctx.send(
            f"The {','.join(display_state)} list{'s' if len(display_state) > 1 else ''} has **{len(group_list)}** {','.join(display_group)}.\n"
            + "*A full list has been sent to you via DMs.*"
        )

    # Group command - lists groups
    if config.options["id_groups"]:

        @commands.hybrid_command(
            help="- Prints a list of all available groups.",
            aliases=[
                config.options["category_name"].lower(),
                config.options["category_name"].lower() + "s",
                "group",
                "category",
                "categories",
            ],
        )
        @commands.check(CustomCooldown(8.0, bucket=commands.BucketType.user))
        async def groups(self, ctx: commands.Context):
            logger.info("command: list")

            await ctx.send(f"**Valid Groups**: `{', '.join(map(str, groups.keys()))}`")

    # Wiki command - argument is the wiki page
    @commands.hybrid_command(help="- Fetch the wikipedia page for any given argument")
    @commands.check(CustomCooldown(5.0, bucket=commands.BucketType.user))
    @app_commands.rename(arg="query")
    @app_commands.describe(arg="A Wikipedia query")
    async def wiki(self, ctx: commands.Context, *, arg):
        logger.info("command: wiki")

        arg = arg.capitalize()

        try:
            page = wikipedia.page(arg, auto_suggest=False)
        except (
            wikipedia.exceptions.DisambiguationError,
            wikipedia.exceptions.PageError,
        ):
            # fall back to suggestion
            try:
                page = wikipedia.page(arg)
            except wikipedia.exceptions.DisambiguationError:
                await ctx.send(
                    "Sorry, that page was not found. Try being more specific.",
                    ephemeral=True,
                )
                return
            except wikipedia.exceptions.PageError:
                await ctx.send("Sorry, that page was not found.", ephemeral=True)
                return

        await ctx.send(page.url)

    if config.options["meme_file"]:
        # meme command - sends a random item video/gif
        @commands.hybrid_command(
            help=f"- Sends a funny {config.options['id_type'][:-1]} video/image!"
        )
        @commands.check(
            CustomCooldown(180.0, disable=True, bucket=commands.BucketType.user)
        )
        async def meme(self, ctx: commands.Context):
            logger.info("command: meme")

            if meme_list:
                await ctx.send(random.choice(meme_list))
            else:
                await ctx.send("No memes available :(")

    if config.options["sendas"]:
        # Send command - for testing purposes only
        @commands.command(help="- send command", hidden=True, aliases=["sendas"])
        @commands.is_owner()
        async def send_as_bot(self, ctx: commands.Context, *, args_str):
            logger.info("command: send")

            logger.info(f"args: {args_str}")
            args = args_str.split(" ")

            channel_id = int(args[0])
            try:
                message = args[1:]
            except IndexError:
                await ctx.send("No message provided!")
            channel = self.bot.get_channel(channel_id)
            await channel.send(" ".join(message))
            await ctx.send("Ok, sent!")

    # # Test command - for testing purposes only
    # @commands.command(help="- test command", hidden=True)
    # async def test(self, ctx, *, item):
    #     logger.info("command: test")
    #     await ctx.send(await get_aliases(item))

    # # Test command - for testing purposes only
    # @commands.command(help="- test command", hidden=True)
    # async def error(self, ctx):
    #     logger.info("command: error")
    #     await ctx.send(1 / 0)


async def setup(bot):
    await bot.add_cog(Other(bot))
