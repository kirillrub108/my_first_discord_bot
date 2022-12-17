import asyncio
import discord
import youtube_dl
from discord.ext import commands
from dotenv import load_dotenv
from pretty_help import PrettyHelp

from cogs.roflcog import RoflCog
from cogs.eventcog import EventCog
from config import settings

load_dotenv()
intents = discord.Intents.all()  # or .all() if you ticked all, that is easier
intents.members = True  # If you ticked the SERVER MEMBERS INTENT
intents.message_content = True

bot = commands.Bot(command_prefix=["rb!", "Rb!"], intents=intents)

song_queue = []


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------
@bot.event
async def on_ready():
    print('RUBA is ready!')
    game = discord.Game("DOTA 2")
    # activity = discord.Activity(type=discord.ActivityType.watching, name="как пацаны в доту играют")
    await bot.change_presence(status=discord.Status.online, activity=game)

    await bot.add_cog(RoflCog(bot))

    await bot.add_cog(EventCog(bot))


# ----------------------------------------------------------------music----------------------------------------------------------------------------------------------------


youtube_dl.utils.bug_reports_message = lambda: ''
ytdl_format_options = {
    'format': 'bestaudio/best',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'  # bind to ipv4 since ipv6 addresses cause issues sometimes
}
ffmpeg_options = {
    'options': '-vn'
}
ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = ""

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]
        filename = data['title'] if stream else ytdl.prepare_filename(data)
        return filename


@bot.command(name='play', help='To play song')
async def play(ctx, url):
    if not ctx.message.author.voice:
        await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
        return
    else:
        channel = ctx.message.author.voice.channel
        await channel.connect()
    if 'shayba_snusa' in url:
        server = ctx.message.guild
        voice_channel = server.voice_client
        filename = await YTDLSource.from_url('https://youtu.be/_qHn43p0iZ0', loop=bot.loop)
        voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=filename))
        await ctx.send('https://youtu.be/_qHn43p0iZ0')
    if 'chika' in url:
        server = ctx.message.guild
        voice_channel = server.voice_client
        filename = await YTDLSource.from_url('https://youtu.be/OW-tSm6HnOA', loop=bot.loop)
        voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=filename))
        await ctx.send('https://youtu.be/OW-tSm6HnOA')
    if 'zlodya' in url:
        server = ctx.message.guild
        voice_channel = server.voice_client
        filename = await YTDLSource.from_url('https://youtu.be/-UFkpgwtJF0', loop=bot.loop)
        voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=filename))
        await ctx.send('https://youtu.be/-UFkpgwtJF0')
    if 'dota_twinky' in url:
        server = ctx.message.guild
        voice_channel = server.voice_client
        filename = await YTDLSource.from_url('https://youtu.be/DUuQj0JTM4o', loop=bot.loop)
        voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=filename))
        await ctx.send('https://youtu.be/DUuQj0JTM4o')
    else:
        server = ctx.message.guild
        voice_channel = server.voice_client
        filename = await YTDLSource.from_url(url, loop=bot.loop)
        voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=filename))
        # async with ctx.typing():
        # await ctx.send('**Now playing:** {}'.format(filename))


@bot.command(name='pause', help='This command pauses the song')
async def pause(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        await ctx.send('Music playback has been paused.')
        await voice_client.pause()
    else:
        await ctx.send("The bot is not playing anything at the moment.")


@bot.command(name='resume', help='Resumes the song')
async def resume(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_paused():
        await ctx.send('Music playback has been resumed.')
        await voice_client.resume()
    else:
        await ctx.send("The bot was not playing anything before this. Use play command")


@bot.command(name='stop', help='Stops the song')
async def stop(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_connected():
        await voice_client.disconnect()
        await ctx.send('Stopped music playback and left the voice channel.')
    else:
        await ctx.send("The bot is not connected to a voice channel.")


# @bot.command(name='skip', help='Skips the song')
# async def skip(ctx):
# voice_client = ctx.message.guild.voice_client
# if voice_client.is_playing():
# links.pop(0)
# queue.pop(0)
# await voice_client.stop()
# try:
# server = ctx.message.guild
# voice_channel = server.voice_client
# voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source='{0}'.format(queue[0])))
# except:
# pass

# else:
# await ctx.send("The bot is not playing anything at the moment.")


bot.help_command = PrettyHelp()

bot.run(settings['token'])  # Обращаемся к словарю settings с ключом token, для получения токена
