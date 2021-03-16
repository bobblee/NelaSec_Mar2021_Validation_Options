
from pathlib import Path
import os
import great_expectations as ge 

# Ensure correct Working Directory
print(os.getcwd())
path = Path('NewThoughts')
os.chdir(path)
print(os.getcwd())

df = ge.read_csv('outputData/good_ingre.csv')
df = df[['name','measurement','amount','item','extras']]
#print(df)

check_measurement = df.expect_column_values_to_be_in_set(
    "measurement",
    ["tbsp","tsp","cup","can","small","medium","large","taste","lbs","med"])
print(check_measurement)

check_extras = df.expect_column_values_to_not_be_null(
    "extras")
print(check_extras)