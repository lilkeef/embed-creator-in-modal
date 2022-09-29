from nextcord.ext import commands
import nextcord

bot = commands.Bot(command_prefix='!', intents = nextcord.Intents.all())

@bot.event
async def on_ready():
    print("Logged in")

class EmbedModal(nextcord.ui.Modal):
    def __init__(self):
        super().__init__(
            "Embed Maker",
        )

        self.emTitle = nextcord.ui.TextInput(label="Embed Title", min_length=2, max_length=124, required=True, placeholder="Enter the embed title here!")
        self.add_item(self.emTitle)

        self.emDesc = nextcord.ui.TextInput(label="Embed Description", min_length=5, max_length=3000, required=True, placeholder="Enter the Embed Description here!", style=nextcord.TextInputStyle.paragraph)
        self.add_item(self.emDesc)

    async def callback(self, interaction: nextcord.Interaction):
        title = self.emTitle.value
        desc = self.emDesc.value
        em = nextcord.Embed(title=title, description=desc)
        return await interaction.response.send_message(embed=em)

@bot.slash_command(name="embed", description="Create a custom Embed!", guild_ids=[])#guild id
async def embed(interaction: nextcord.Interaction):
    await interaction.response.send_modal(EmbedModal())

bot.run("")#bot token