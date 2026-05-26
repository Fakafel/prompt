#W I P 
#THIS IS FOR LEARNING PURPOSES

import discord
import os

# 1. SETUP INTENTS
intents = discord.Intents.default()
intents.members = True 

# 2. CREATE THE CLIENT VARIABLE (Make sure this line is exactly here!)
client = discord.Client(intents=intents)

LOG_CHANNEL_ID = 1487218761013661918

# 3. YOUR EVENT LISTENER
@client.event
async def on_member_update(before, after):
    if before.timed_out_until != after.timed_out_until:
        channel = client.get_channel(LOG_CHANNEL_ID)
        if not channel:
            return

        if after.timed_out_until is not None:
            await channel.send(f"{after.mention} has been sealed, decisions have consequences young one.")
        else:
            await channel.send(f"{after.mention} has been unsealed. Behave yourself.")

# 4. RUN THE CLIENT (This looks for the variable created in step 2)
client.run(os.environ.get("DISCORD_BOT_TOKEN"))
