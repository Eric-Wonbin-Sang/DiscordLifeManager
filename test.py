import gspread
import datetime
import pyperclip
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

from Classes import WeightRecord

from General import Constants


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


def main():

    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(Constants.weight_spreadsheet_credentials, scope)

    client = gspread.authorize(creds)
    spreadsheet = client.open('Weight Tracker')
    sheet = spreadsheet.get_worksheet(0)

    weight_record_list = get_existing_weight_record_list(sheet)
    for weight_record in weight_record_list:
        print(weight_record)

    # records_data = main_sheet.get_all_records()
    # print(records_data)
    # for r in records_data:
    #     print(r)
    # records_df = pd.DataFrame.from_dict(records_data)
    # print(records_df)
    #
    # for x in records_df.values.tolist():
    #     print(x)
    #
    # main_sheet.insert_row(["test"], index=)


if __name__ == '__main__':
    main()

