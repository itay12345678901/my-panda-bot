import os
import discord
from discord.ext import commands

intents = discord.Intents.all()

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

WELCOME_CHANNEL_ID = 1502710155005919443
GOODBYE_CHANNEL_ID = 1502710219648532602


@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

    print(f"🎉 SUCCESS! Panda is online as: {bot.user}")


@bot.tree.command(
    name="ping",
    description="בדיקה שהבוט עובד - הודעה פרטית"
)
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(
        "pong! 🐼",
        ephemeral=True
    )


@bot.event
async def on_member_join(member):
    print(f"👤 משתמש חדש זוהה: {member.name}")

    channel = bot.get_channel(WELCOME_CHANNEL_ID)

    if channel:
        avatar_url = member.display_avatar.url

        encoded_username = member.name.replace(" ", "%20")
        encoded_guild = member.guild.name.replace(" ", "%20")

        member_count = member.guild.member_count

        image_url = (
            f"https://api.popcat.xyz/welcomecard?"
            f"background=https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe"
            f"&avatar={avatar_url}"
            f"&text1={encoded_username}"
            f"&text2=Welcome%20To%20{encoded_guild}"
            f"&text3=Member%20%23{member_count}"
        )

        await channel.send(
            f"ברוכים הבאים לשרת {member.mention}! 👋"
        )

        await channel.send(image_url)

    else:
        print("❌ שגיאה: לא מצאתי את חדר הברוכים הבאים.")


@bot.event
async def on_member_remove(member):
    print(f"🏃 משתמש עזב: {member.name}")

    channel = bot.get_channel(GOODBYE_CHANNEL_ID)

    if channel:
        await channel.send(
            f"להתראות {member.name} 👋"
        )


if __name__ == "__main__":
    bot.run(os.getenv("TOKEN"))
