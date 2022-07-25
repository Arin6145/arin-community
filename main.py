import discord, os
from discord import app_commands

token = os.getenv("TOKEN")

class button_view(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout=None)
    
    @discord.ui.button(label = "인증하기", style = discord.ButtonStyle.green, custom_id = "role_button")
    async def verify(self, interaction: discord.Interaction, button: discord.ui.Button):
        if type(client.role) is not discord.Role: client.role = interaction.guild.get_role(988011044817485824)
        if client.role not in interaction.user.roles:
            await interaction.user.add_roles(client.role)
            await interaction.response.send_message(f"{client.role.mention}역할이 지급되었습니다!", ephemeral = True)
        else: await interaction.response.send_message(f"이미 {client.role.mention}역할을 가지고 있습니다!", ephemeral = True)

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents = discord.Intents.default())
        self.synced = False #we use this so the bot doesn't sync commands more than once
        self.added = False
        self.role = 988011044817485824

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced: #check if slash commands have been synced 
            await tree.sync(guild = discord.Object(id=988009947684012092)) #guild specific: leave blank if global (global registration can take 1-24 hours) - sync only when you have to
            self.synced = True
        if not self.added:
            self.add_view(button_view())
            self.added = True
        print(f"We have logged in as {self.user}.")

client = aclient()
tree = app_commands.CommandTree(client)

@tree.command(guild = discord.Object(id=988009947684012092), name = 'button', description='Launches a button!') #guild specific slash command
async def launch_button(interaction: discord.Interaction): 
    await interaction.response.send_message(view = button_view())

client.run(token)
