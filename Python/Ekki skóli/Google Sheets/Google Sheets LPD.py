from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import datetime

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

#Input

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = '14gUMjBigeCdfySGGzjnQvbgUDG0N9HimafP3ZJIOueE'
RANGE_NAME = 'LPD!A2:C'

def main():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Breytur
    value_input_option = "RAW"

    # Call the Sheets API
    values = [
        [
            # Cell values ...
            "Rod 1",
            "Rod 2",
            "Rod 3"
        ],
        # Additional rows ...
    ]
    body = {
        'values': values
    }
    result = service.spreadsheets().values().append(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME, valueInputOption=value_input_option, body=body).execute()

if __name__ == '__main__':
    main()