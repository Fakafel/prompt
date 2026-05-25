#W I P 
#THIS IS FOR LEARNING PURPOSES

import discord
import os

intents = discord.Intents.default()
intents.members = True  # Matches the toggle you switched in the portal

client = discord.Client(intents=intents)

# Replace this with the actual ID of the Discord channel where you want messages to post
# (Right-click a channel in Discord and select "Copy Channel ID")
LOG_CHANNEL_ID = 1487218761013661918 

@client.event
async def on_member_update(before, after):
    # Check if their timeout status changed
    if before.timed_out_until != after.timed_out_until:
        channel = client.get_channel(LOG_CHANNEL_ID)
        if not channel:
            print("Error: Could not find the specified channel ID.")
            return

        if after.timed_out_until is not None:
            message = f"{after.mention} has been sealed."
            print(message)  # Prints to GitHub terminal
            await channel.send(message)  # Sends directly into your Discord server
        else:
            message = f"{after.mention} has been unsealed."
            print(message)
            await channel.send(message)

# Run the bot
client.run(os.environ.get("DISCORD_BOT_TOKEN"))

