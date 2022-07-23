import discord, os
from discord.ext import commands
from discord.ui import Button, View, Select

INTENTS = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=INTENTS)
token = os.getenv("TOKEN")

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.dnd ,activity=discord.Activity(name="문의는 DM"))
    print(f"-------------------------------\n"
    f"[ + ] Bot connected to Discord\n"
    f"> User: {bot.user.name}#{bot.user.discriminator}\n"
    f"> ID: {bot.user.id}\n"
    f"> Server: {len(bot.guilds)}\n"
    f"----------- ⮟ Log ⮟ ----------")

@bot.command(name="나이버튼")
async def ageroles(ctx):
    button4 = Button(
        label="나이비공개",
        style=discord.ButtonStyle.gray,
        emoji="💙"
    )
    button1 = Button(
        label="10대",
        style=discord.ButtonStyle.gray,
        emoji="🧡"
    )
    button2 = Button(
        label="20대",
        style=discord.ButtonStyle.gray,
        emoji="💛"
    )
    button3 = Button(
        label="30대",
        style=discord.ButtonStyle.gray,
        emoji="💚"
    )

    embed = discord.Embed(
        title="당신의 나이를 알려주세요!",
        description="아래의 버튼에서 당신의 나이대에 맞는 버튼을 눌러주시면 역할이 들어옵니다!",
        color=discord.Color.nitro_pink()
    )

    view = View(timeout=None)
    view.add_item(button1)
    view.add_item(button2)
    view.add_item(button3)
    view.add_item(button4)

    await ctx.send(embed=embed, view=view)
    async def button4callback(interaction: discord.Interaction):
        member = interaction.user
        role = interaction.guild.get_role(874283897796558878)
        await member.add_roles(role)
        await interaction.response.send_message("나이비공개 역할을 받았습니다!", ephemeral=True)
    async def button1callback(interaction: discord.Interaction):
        member = interaction.user
        role = interaction.guild.get_role(874283861784297542)
        await member.add_roles(role)
        await interaction.response.send_message("10대 역할을 받았습니다!", ephemeral=True)
    async def button2callback(interaction: discord.Interaction):
        member = interaction.user
        role = interaction.guild.get_role(874283862568615958)
        await member.add_roles(role)
        await interaction.response.send_message("20대 역할을 받았습니다!", ephemeral=True)
    async def button3callback(interaction: discord.Interaction):
        member = interaction.user
        role = interaction.guild.get_role(874283897385537546)
        await member.add_roles(role)
        await interaction.response.send_message("30대 역할을 받았습니다!", ephemeral=True)

    button1.callback = button1callback
    button2.callback = button2callback
    button3.callback = button3callback
    button4.callback = button4callback


@bot.command(name="성별버튼")
async def genderroles(ctx):
    button1 = Button(
        label="남자",
        style=discord.ButtonStyle.gray,
        emoji="👦"
    )
    button2 = Button(
        label="여자",
        style=discord.ButtonStyle.gray,
        emoji="👩"
    )
    button3 = Button(
        label="성별비공개",
        style=discord.ButtonStyle.gray,
        emoji="👨‍🦲"
    )

    embed = discord.Embed(
        title="당신의 성별를 알려주세요!",
        description="아래의 버튼에서 당신의 성별에 맞는 버튼을 눌러주시면 역할이 들어옵니다!",
        color=discord.Color.nitro_pink()
    )

    view = View()
    view.add_item(button1)
    view.add_item(button2)
    view.add_item(button3)

    await ctx.send(embed=embed, view=view)

    async def button1callback(interaction: discord.Interaction):
        member = interaction.user
        role = interaction.guild.get_role(874283666807877673)
        await member.add_roles(role)
        await interaction.response.send_message("남자 역할을 받았습니다!", ephemeral=True)
    async def button2callback(interaction: discord.Interaction):
        member = interaction.user
        role = interaction.guild.get_role(874283657207099413)
        await member.add_roles(role)
        await interaction.response.send_message("여자 역할을 받았습니다!", ephemeral=True)
    async def button3callback(interaction: discord.Interaction):
        member = interaction.user
        role = interaction.guild.get_role(874289033453387836)
        await member.add_roles(role)
        await interaction.response.send_message("성별비공개 역할을 받았습니다!", ephemeral=True)

    button1.callback = button1callback
    button2.callback = button2callback
    button3.callback = button3callback

bot.run(token)