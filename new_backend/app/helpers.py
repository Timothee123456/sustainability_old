import json
import os

import gspread
from google.oauth2.service_account import Credentials

scopes = ['https://www.googleapis.com/auth/spreadsheets']

base_path = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(base_path, 'group2.json')
creds = Credentials.from_service_account_file(config_path, scopes=scopes)
client = gspread.authorize(creds)

sheet = client.open_by_url('https://docs.google.com/spreadsheets/d/1VlOpnuUkrDvq0LD0SgQGq1X9IPv0E8xh-Oq8lrXaQ_I/')

datasheet = sheet.worksheet("Data")
cleanedsheet = sheet.worksheet("Ingredients")
imglinksheet = sheet.worksheet("Ingredients_images_links")

first_cell_value = datasheet.acell('A1').value

def find_date(date):
    cell = datasheet.find(date)
    if cell:
        return cell.row
    else:
        return None

def return_info(type, row_number, column_number):
    full_name = datasheet.cell(row_number, column_number).value
    cleaned_name = cleanedsheet.cell(row_number, column_number).value
    location_name = imglinksheet.find(cleaned_name)
    if location_name:
        img_link = imglinksheet.cell(location_name.row, location_name.col + 1).value
    else:
        img_link = False

    component_name = full_name if cleaned_name != "salad bar" else False if type == "Appetizer" else full_name
    component_name = component_name.replace('\n', '')
    component = { 
        'name': component_name,
        'type': type,
        'img_link': img_link
    }

    return component



def find_all_info(date):
    row_number = find_date(date)
    
    if row_number:
        appetizer = return_info("Appetizer", row_number, 2)
        dishA = return_info("Dish A", row_number, 3)
        dishB = return_info("Dish B", row_number, 4)
        vegetables = return_info("Vegetables", row_number, 5)
        starch = return_info("Starch", row_number, 6)
        dessert = return_info("Dessert", row_number, 8)

        return_data = [appetizer, dishA, dishB, vegetables, starch, dessert]
    else:
        return_data = False


    return json.dumps(return_data, indent=4)

#######################################################################

data_sheet = client.open_by_url('https://docs.google.com/spreadsheets/d/18PKyGEufH3nxx-YLQ1vNPgIE7TX8EQAl20VobDY6_KQ/')
def store_data(data):
    # Assumes data is a string or simple value to store in first column (A)
    # Finds the next available row by checking column A
    col_a = datasheet.col_values(1)
    next_row = len(col_a) + 1
    datasheet.update(f'A{next_row}', data)[web:2][web:6]
