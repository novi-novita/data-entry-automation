# Data Entry Automation Repository

## 1. Data Cleaning & Formatting (Python + Excel)

### clean_data.py
```python
import pandas as pd

def clean_excel(file_path, output_path):
    df = pd.read_excel(file_path)
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    df.to_excel(output_path, index=False)
    print("Data cleaned and saved to", output_path)

# Example Usage
clean_excel("sample_data.xlsx", "cleaned_data.xlsx")
```
