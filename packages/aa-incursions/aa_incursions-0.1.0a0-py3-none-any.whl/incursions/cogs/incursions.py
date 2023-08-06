import logging

from discord import AutocompleteContext, Option
from discord.commands import SlashCommandGroup
from discord.embeds import Embed
from discord.ext import commands
from eveuniverse.models import EveConstellation, EveRegion, EveSolarSystem

from django.conf import settings

from incursions import __version__
from incursions.models import Incursion

logger = logging.getLogger(__name__)


class Incursions(commands.Cog):
    """
    Drifter Wormhole Mapping and Management
    From AA-incursions
    """

    def __init__(self, bot):
        self.bot = bot

    incursion_commands = SlashCommandGroup(
        "incursions", "Incursions", guild_ids=[int(settings.DISCORD_GUILD_ID)])

    async def search_solar_systems(self, ctx: AutocompleteContext):
        return list(EveSolarSystem.objects.filter(name__icontains=ctx.value).values_list('name', flat=True)[:10])

    async def search_constellations(self, ctx: AutocompleteContext):
        return list(EveConstellation.objects.filter(name__icontains=ctx.value).values_list('name', flat=True)[:10])

    async def search_regions(self, ctx: AutocompleteContext):
        return list(EveRegion.objects.filter(name__icontains=ctx.value).values_list('name', flat=True)[:10])

    async def search_incursion(self, ctx: AutocompleteContext):
        return list(Incursion.objects.filter(name__icontains=ctx.value).values_list('name', flat=True)[:10])

    @incursion_commands.command(name="about", description="About the Incursion Bot", guild_ids=[int(settings.DISCORD_GUILD_ID)])
    async def about(self, ctx):
        """
        All about the bot
        """
        embed = Embed(title="AA Incursions")
        embed.description = "https://gitlab.com/tactical-supremacy/aa-incursions"
        embed.url = "https://gitlab.com/tactical-supremacy/aa-incursions"
        embed.set_thumbnail(url="https://images.evetech.net/types/2192/render?size=128")
        embed.set_footer(
            text="Developed by Ariel Rin")
        embed.add_field(
            name="Version", value=f"{__version__}", inline=False
        )

        return await ctx.respond(embed=embed)

    @incursion_commands.command(name="focus", description="Get information on the current focus", guild_ids=[int(settings.DISCORD_GUILD_ID)])
    async def focus(
        self, ctx,
        constellation=Option(str, "Constellation", autocomplete=search_constellations),
    ):
        return await ctx.respond("Not Yet Implemented")

    @incursion_commands.command(name="set_focus", description="Set the current Focus", guild_ids=[int(settings.DISCORD_GUILD_ID)])
    async def focus_set(
        self, ctx,
        constellation=Option(str, "Constellation", autocomplete=search_constellations),
    ):
        return await ctx.respond("Not Yet Implemented")

    @incursion_commands.command(name="incursions", description="List active incursions", guild_ids=[int(settings.DISCORD_GUILD_ID)])
    async def incursions(
        self, ctx,
    ):
        return await ctx.respond("Not Yet Implemented")

    @incursion_commands.command(name="incursion_detail", description="Status of a specific incursion", guild_ids=[int(settings.DISCORD_GUILD_ID)])
    async def incursion_detail(
        self, ctx,
        incursion=Option(str, "Constellation", autocomplete=search_constellations),
    ):
        return await ctx.respond("Not Yet Implemented")


def setup(bot):
    bot.add_cog(Incursions(bot))
