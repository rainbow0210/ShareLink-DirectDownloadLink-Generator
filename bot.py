import discord
import os
from dotenv import load_dotenv
from discord.commands import Option

bot = discord.Bot()
load_dotenv()

@bot.event
async def on_ready():
    print(f'{bot.user} connect success!')


@bot.slash_command(description="Google drive link change direct download link.")
async def generate_directlink(
    ctx,
    share_url: Option(str, 'Google Drive Share link typing'),
):
    url = share_url

    # Normal mode
    if url[0:25] == 'https://drive.google.com/':
        # debug message start
        print('-Change start-')
        print('')

        print(url)
        print('')

        url = url[32:]
        print(url)
        print('')

        url = url[:-20]
        print(url)
        print('')

        url = 'https://drive.google.com/uc?export=download&id=' + url
        print(url)
        print('')

        print('-Change finish!-')
        print('')
        # debug message finish

        embed=discord.Embed(title="Success!", description=":o:Change URL!:o:", color=0x00ff2a)
        embed.add_field(name="SmartPhone and Tablet is copy url. And, your use browser paste url! PC is copy or left click!", value=url, inline=True)
        embed.set_footer(text="※Big size file is not support. (Maybe 100MB or under)")
        await ctx.respond(embed=embed)

    # Google document
    elif url[0:33] == 'https://docs.google.com/document/':
        # debug message start
        print('-Change start-')
        print('')

        print(url)
        print('')

        url = url[35:]
        print(url)
        print('')

        url = url.split('/')[0]
        print(url)
        print('')

        url = 'https://drive.google.com/uc?export=download&id=' + url
        print(url)
        print('')

        print('-Change finish!-')
        print('')
        # debug message finish

        embed=discord.Embed(title="Success!", description=":o:Change URL!:o:", color=0x00ff2a)
        embed.add_field(name="SmartPhone and Tablet is copy url. And, your use browser paste url! PC is copy or left click!", value=url, inline=True)
        embed.set_footer(text="※Big size file is not support. (Maybe 100MB or under)")
        await ctx.respond(embed=embed)

    # Google spreadsheet
    elif url[0:37] == 'https://docs.google.com/spreadsheets/':
        # debug message start
        print('-Change start-')
        print('')

        print(url)
        print('')

        url = url[39:]
        print(url)
        print('')

        url = url.split('/')[0]
        print(url)
        print('')

        url = 'https://drive.google.com/uc?export=download&id=' + url
        print(url)
        print('')

        print('-Change finish!-')
        print('')
        # debug message finish

        embed=discord.Embed(title="Success!", description=":o:Change URL!:o:", color=0x00ff2a)
        embed.add_field(name="SmartPhone and Tablet is copy url. And, your use browser paste url! PC is copy or left click!", value=url, inline=True)
        embed.set_footer(text="※Big size file is not support. (Maybe 100MB or under)")
        await ctx.respond(embed=embed)

    # Google slides
    elif url[0:37] == 'https://docs.google.com/presentation/':
        # debug message start
        print('-Change start-')
        print('')

        print(url)
        print('')

        url = url[39:]
        print(url)
        print('')

        url = url.split('/')[0]
        print(url)
        print('')

        url = 'https://drive.google.com/uc?export=download&id=' + url
        print(url)
        print('')

        print('-Change finish!-')
        print('')
        # debug message finish

        embed=discord.Embed(title="Success!", description=":o:Change URL!:o:", color=0x00ff2a)
        embed.add_field(name="SmartPhone and Tablet is copy url. And, your use browser paste url! PC is copy or left click!", value=url, inline=True)
        embed.set_footer(text="※Big size file is not support. (Maybe 100MB or under)")
        await ctx.respond(embed=embed)

    # Error message
    else:
        # debug message start
        print('-Change start!-')
        print('')

        print('Error!')
        print('')

        print('-Change finish!-')
        print('')
        # debug message finish

        embed=discord.Embed(title="Error!", description=":x:Not Support Link or No Link!:x:", color=0xff0000)
        await ctx.respond(embed=embed)

bot.run(os.environ['token'])