import discord, os
from discord.ext import commands
from discord.ui import Button, View, Select

INTENTS = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=INTENTS)
token = os.getenv("TOKEN")

async def SendError(self, ctx:discord.ApplicationContext, message):
        embed = discord.Embed(title=f'실패 Failed # {ctx.command}', description=f'{message}', color=self.color)
        await ctx.respond(embed=embed)

@discord.slash_command(name='인증', description='서포트 서버 인증을 시도합니다.')
async def CaptchaSystem(self, ctx:discord.ApplicationContext):
    role = ctx.guild.get_role(988011044817485824)
    a = ""
    Captcha_img = ImageCaptcha()
    if role not in ctx.author.roles:
        for i in range(6):
            a += str(random.randint(0, 9))

        name = './Verifty/' + str(ctx.author. id) + ".png"
        Captcha_img.write(a, name)

        embed = discord.Embed(title=f'대기중 Waited # {ctx.command}', description=f'숫자를 채팅으로 입력해주세요.', color=self.color)
        embed.add_field(name='이용 약관', value=f'✔ㅣ이용약관 (필독)',inline=False)

        edit_msg = await ctx.respond(file=discord.File(name), embed=embed)

        def check(m: discord.Message):  # m = discord.Message.
            return m.author == ctx.author and m.channel.id == ctx.channel.id 

        try:
            msg = await self.bot.wait_for('message', check=check, timeout=15)

        except asyncio.TimeoutError:
            await self.SendError(ctx, '인증에 실패했습니다. 시간이 초과되었습니다.')
        else:
            if msg.content == a:
                embed = discord.Embed(title=f'성공 Success', description=f'{ctx.author}님의 인증에 성공했습니다.', color=self.color)
                embed.add_field(name='지급 역할', value=f'<@&{role.id}> (2초 후 자동 지급)', inline=False)
                await edit_msg.edit_original_message(embed=embed)
                await asyncio.sleep(2)
                await ctx.author.add_roles(role)
            else:
                await self.SendError(ctx, '인증에 실패했습니다. 잘못 입력하셨습니다.')
    else:
        pass
    
bot.run(token)
