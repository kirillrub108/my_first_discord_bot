import discord
from discord.ext import commands
import json
import requests


#-------------------------------------------------------------------------------------------------------------------------------------------------------------


class RoflCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='hello', help='Бот поздоровается с тобой')  # Не передаём аргумент pass_context, так как он был нужен в старых версиях.
    async def hello(self, ctx):  # Создаём функцию и передаём аргумент ctx.
        author = ctx.message.author  # Объявляем переменную author и записываем туда информацию об авторе.
        await ctx.send(
            f'Привет, {author.mention}!')  # Выводим сообщение с упоминанием автора, обращаясь к переменной author.


    @commands.command(name='fox', help='Рандомная лиса')
    async def fox(self, ctx):
        response = requests.get('https://some-random-api.ml/img/fox')  # Get-запрос
        json_data = json.loads(response.text)  # Извлекаем JSON

        embed = discord.Embed(color=0xff9900, title='Random FOX')  # Создание Embed'a
        embed.set_image(url=json_data['link'])  # Устанавливаем картинку Embed'a
        await ctx.send(embed=embed)  # Отправляем Embed


    @commands.command(name='pudge', help='Ебало пуджа')
    async def pudge(self, ctx):
        emb = discord.Embed(title="ПАДЖЕРО", colour=discord.Colour.dark_green())
        emb.set_image(
            url="https://avatars.mds.yandex.net/i?id=21c0955a458266d09d41c2fd85b7d4fb-4275191-images-thumbs&n=13")
        await ctx.send(embed=emb)


    @commands.command(name='pudge_secret', help='Пудж кайфует')
    async def pudge_secret(self, ctx):
        emb = discord.Embed(title="ПИДЖАК КАЙФУЕТ", colour=discord.Colour.dark_green())
        emb.set_image(url="https://s5o.ru/storage/simple/cyber/edt/99/32/7c/fb/cybere8a692adabb.jpg")
        await ctx.send(embed=emb)


    @commands.command(name='invoker', help='Ебало инвокера представили?')
    async def invoker(self, ctx):
        emb = discord.Embed(title="величайший маг Карл", colour=discord.Colour.dark_green())
        emb.set_image(
            url="https://sun1-91.userapi.com/s/v1/ig2/_uBQ00BPFw7lXkVJx7p0QhIrB7fXnkol8G78Lx0390KqbqLZIsVsH6iMybYEvZ_Tpjg1LbVctWFElcy6iuxH6_nd.jpg?size=200x0&quality=96&crop=85,0,346,346&ava=1")
        await ctx.send(embed=emb)


    @commands.command(name='pudge_gif', help='Пудж флексит')
    async def pudge_gif(self, ctx):
        await ctx.send("https://ibb.co/YTwz1hh")


    @commands.command(name='wiki', help='Даёт ссылку на вики персонажа')
    async def wiki(self, ctx, *, arg):
        await ctx.send('https://dota2.fandom.com/wiki/{0}'.format(arg))


    @commands.command(name='doteri', help='Профили всех дотеров в ВК')
    async def doteri(self, ctx):
        await ctx.send('https://vk.com/kirillrubets')
        await ctx.send('https://vk.com/fmtvwarezhka')
        await ctx.send('https://vk.com/sambukalover')
        await ctx.send('https://vk.com/nikita.ochen.sasniy')
        await ctx.send('https://vk.com/daddy54356')
        await ctx.send('https://vk.com/tirvn2003')


    @commands.command(name='radi_kala', help='Ютуб канал RadiKaifa')
    async def radi_kala(self, ctx):
        await ctx.send('https://www.youtube.com/@radikaifa7238')


    @commands.command(name='rk_tw', help='Твич RadiKaifa')
    async def rk_tw(self, ctx):
        await ctx.send('https://www.twitch.tv/radika1fa')


    @commands.command(name='perfect', help="Ютуб канал perfct'a")
    async def perfect(self, ctx):
        await ctx.send('https://www.youtube.com/@ggwplanaya4488')


    @commands.command(name='sh', help='Асуждаю')
    async def sh(self, ctx):
        await ctx.send('https://ibb.co/47MmvNM')


    @commands.command(name='sh_1', help='Асуждаю/2')
    async def sh_1(self, ctx):
        await ctx.send('https://ibb.co/wCcQVBt')


def setup(bot):
    bot.add_cog(RoflCog(bot))
