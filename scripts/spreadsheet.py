import gspread
from oauth2client.service_account import ServiceAccountCredentials as ServiceA
import pprint

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceA.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("Contact Information (Responses)").sheet1

# Extract and print all of the values
list_of_hashes = sheet.get_all_records()
pp = pprint.PrettyPrinter()
print(pp.pprint(list_of_hashes))
