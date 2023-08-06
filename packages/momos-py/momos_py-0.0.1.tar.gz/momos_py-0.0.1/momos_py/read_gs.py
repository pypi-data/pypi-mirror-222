import gspread
#from gspread.models import Cell
# import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

class read_gs:
    def __init__(self):
        # define the scope
        self.scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

    def read(self, wb_name, ws_name, json_keyfile, ws_index = 0):
        # authorize the clientsheet 
        client = gspread.authorize(ServiceAccountCredentials.from_json_keyfile_name(json_keyfile, self.scope))

        if wb_name is not None:
            # get the instance of the Spreadsheet

            sheet = client.open(wb_name)
            sheet_instance = None

            if ws_name is None:

                # get the first sheet of the Spreadsheet
                sheet_instance = sheet.get_worksheet(ws_index)
        
            else:

                sheet_instance = sheet.worksheet(ws_name)

            if sheet_instance is not None:
                return sheet_instance.get_all_records()
            else:
                return sheet_instance