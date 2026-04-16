import gspread
from google.oauth2.service_account import Credentials

scopes = ['https://www.googleapis.com/auth/spreadsheets']

creds = Credentials.from_service_account_file('group2.json', scopes=scopes)
client = gspread.authorize(creds)

# Open the first available spreadsheet (replace 'Your Spreadsheet Name' with actual name if known)
sheet = client.open_by_url('https://docs.google.com/spreadsheets/d/18PKyGEufH3nxx-YLQ1vNPgIE7TX8EQAl20VobDY6_KQ/edit?gid=0#gid=0')
worksheet = sheet.sheet1  # First worksheet [web:7]

data = {
    "startTime": 1774483407343,
    "elapsedTime": 7146,
    "selectedIngredients": {
        "Chicken Basquaise": "green",
        "Cauliflowers & Peas Gratin": False,
        "Roasted Bell Peppers": "red",
        "Couscous": False,
        "Apple/Strawberry Compote": "gold"
    }
}

start_time = data.get('startTime', '')
elapsed_time = data.get('elapsedTime', '')

selected = data.get('selectedIngredients', {})
ingredient_values = list(selected.values())

# Ensure we always have 5 columns for ingredients to keep the Icon in column 8
# If there are fewer than 5, pad with empty strings. 
# If there are more, it will shift the icon column.
while len(ingredient_values) < 5:
    ingredient_values.append('')

# 3. Extract Icon Value
icon_value = data.get('iconValue', '')

# Construct the row: 
# [StartTime, ElapsedTime, Ing1, Ing2, Ing3, Ing4, Ing5, IconValue]
row = [start_time, elapsed_time] + ingredient_values[:5] + [icon_value]
