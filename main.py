#W I P 
#THIS IS FOR LEARNING PURPOSES

import discord
import os

intents = discord.Intents.default()
intents.members = True  # Required to see user updates

client = discord.Client(intents=intents)

@client.event


@client.event
async def on_member_update(before, after):
    # Check if the user's timeout status changed
    # 'timed_out_until' is None if they are not timed out
    if before.timed_out_until != after.timed_out_until:
        if after.timed_out_until is not None:
            print(f"{after.name} has been sealed.")
        else:
            print(f"{after.name} has been unsealed")

# Run the bot using your secure token
client.run(os.environ.get("DISCORD_BOT_TOKEN"))








