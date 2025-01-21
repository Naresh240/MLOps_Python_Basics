import os
import pandas as pd

print("List of file in this directory: ", os.listdir())
df = pd.read_excel('SampleWork.xlsx', sheet_name=None)

print(df)