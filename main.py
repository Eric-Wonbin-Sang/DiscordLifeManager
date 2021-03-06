import gspread
import discord
import datetime
from oauth2client.service_account import ServiceAccountCredentials

from Classes import WeightRecord

from General import Constants


def get_weight_tracker_sheet():
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(Constants.weight_spreadsheet_credentials, scope)

    client = gspread.authorize(creds)
    spreadsheet = client.open('Weight Tracker')
    return spreadsheet.get_worksheet(0)


def get_existing_weight_record_list(sheet):
    weight_record_list = []
    for data_dict in sheet.get_all_records():

        last_weight_record = weight_record_list[-1] if len(weight_record_list) != 0 else None

        weight_record_list.append(
            WeightRecord.WeightRecord(
                datetime.datetime.strptime(data_dict["Datetime"], "%Y/%m/%d %H:%M %p"),
                float(data_dict["Weight (lb)"]),
                last_weight_record=last_weight_record
            )
        )
    return weight_record_list


def weight_command(value):

    weight_tracker_sheet = get_weight_tracker_sheet()
    weight_record_list = get_existing_weight_record_list(weight_tracker_sheet)

    curr_record = WeightRecord.WeightRecord(
        datetime.datetime.now(),
        float(value),
        last_weight_record=weight_record_list[-1] if len(weight_record_list) != 0 else None
    )
    curr_record.add_to_google_sheet(weight_tracker_sheet)

    emote, gained_or_lost = ("Yikes!", "gained") if curr_record.weight_lb_delta >= 0 else ("Congrats!", "lost")

    day_delta = curr_record.dt.day - curr_record.last_weight_record.dt.day
    time_since = "{} days ago".format(day_delta) if day_delta > 1 else "yesterday"

    ret_str = "Weight record added! "
    ret_str += "{} You've {} {} since {}.".format(
        emote,
        gained_or_lost,
        curr_record.weight_lb_delta,
        time_since
    )
    return ret_str


def main():

    client = discord.Client()

    @client.event
    async def on_ready():
        for guild in client.guilds:
            print(guild.name)

    @client.event
    async def on_message(message):

        print("--------------------------------------")

        if message.author == client.user:
            print("DiscordLifeBot")
            print(message.content)

        elif message.author != client.user:

            print(message.author)
            print(message.content)

            command_key, *split_message = message.content.lower().split(" ")
            if command_key in ["weight", "w"]:
                if split_message:
                    await message.channel.send(weight_command(split_message[0]))
                else:
                    await message.channel.send("WeightCommand: no weight given")
            else:
                # await message.channel.send("I don't know that command...")
                print(message.author)

    client.run(Constants.discord_credentials)


main()
