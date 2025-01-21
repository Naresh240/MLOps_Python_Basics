import pandas as pd

dct = {"empId": [101, 102, 103, 104], "empName": ["Naresh", "Suresh", "Anusha", "Srinu"], "empCity": ["Ongole", "Bangalore", "Hyderabad", "Chennai"]}
df = pd.DataFrame(dct)
print(df)