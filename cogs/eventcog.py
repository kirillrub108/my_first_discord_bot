import discord
from discord.ext import commands
from discord.utils import find

intents = discord.Intents.all()  # or .all() if you ticked all, that is easier
intents.members = True  # If you ticked the SERVER MEMBERS INTENT
intents.message_content = True

bot = commands.Bot(command_prefix=["rb!", "Rb!"], intents=intents)


class EventCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send(
                embed=discord.Embed(description=f'** {ctx.author.name}, данной команды не существует.**', color=0x0c0c0c))


    @commands.Cog.listener()
    async def on_member_join(self, member):
        role_1 = member.guild.get_role(558372660346880020)  # Роль
        emb = discord.Embed(title='Добро пожаловать в ПИДОРСКИЙ ОМУТ', color=0xff0000)  # Приветствие
        emb.add_field(name="Команды бота", value='Чтоб узнать команды пропиши rb!help в чат сервера',
                      inline=False)  # Приветствие
        emb.set_author(name=f'{member.name}#{member.discriminator}')  # Приветствие
        await member.add_roles(role_1)  # Выдача роли
        await member.send(embed=emb)  # Отправка приветсия
        if welcome_channel := member.guild.get_channel(558392271884648467):  # Приветствие в чате
            await welcome_channel.send(f"{member.mention}, добро пожаловать в {member.guild.name}")  # Приветствие в чате


    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        general = find(lambda x: x.name == '☺плотная-зига-всем-нашим', guild.text_channels)
        if general and general.permissions_for(guild.me).send_messages:
            await general.send('Подстилка админа зашла в {}!'.format(guild.name))
            await bot.process_commands(guild)


    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        if 'пидор' in message.content:
            await message.channel.send('Сам ты пидор епта!')

        if 'нахуй' in message.content:
            await message.channel.send('Пошёл в пизду')


def setup(bot):
    bot.add_cog(EventCog(bot))