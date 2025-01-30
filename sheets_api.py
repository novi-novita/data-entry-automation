## 2. Google Sheets Automation

### sheets_api.py
```python
import gspread
from google.oauth2.service_account import Credentials

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("credentials.json", scopes=SCOPES)
client = gspread.authorize(creds)

sheet = client.open("Data Entry Sheet").sheet1
sheet.append_row(["John Doe", "johndoe@example.com", "Completed"])
print("Data added to Google Sheets")
```
