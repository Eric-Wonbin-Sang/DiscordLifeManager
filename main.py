import discord
import datetime

from Classes import WeightRecord

from General import Constants


def weight_command(value):
    curr_record = WeightRecord.WeightRecord(
        datetime.datetime.now(),
        float(value)
    )



def main():

    client = discord.Client()

    @client.event
    async def on_message(message):

        print(message)

        if message.author != client.user:
            await message.channel.send("THIS IS A FACT")
            await message.channel.send("Bruh indeed...")

            word_list = ["trump", "election"]
            split_message = message.content.lower().split(" ")
            for word in word_list:
                if word in split_message:
                    await message.channel.send("I'm triggered")

    client.run(Constants.discord_credentials)


main()
