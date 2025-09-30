# assignment.py
# Data Structures & File Handling

import json
import csv
import yaml
import xml.etree.ElementTree as ET
from typing import TypedDict, NamedTuple
from dataclasses import dataclass
from pydantic import BaseModel
import numpy as np
import pandas as pd
import time

# -------------------------------
# 1. Create example JSON, CSV, YAML, XML files
# -------------------------------
user_data = {
    "name": "Alice",
    "age": 25,
    "email": "alice@example.com"
}

# JSON
with open("user.json", "w") as f:
    json.dump(user_data, f, indent=4)

# CSV
with open("user.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=user_data.keys())
    writer.writeheader()
    writer.writerow(user_data)

# YAML
with open("user.yaml", "w") as f:
    yaml.dump(user_data, f)

# XML
user_xml = ET.Element("User")
for k, v in user_data.items():
    child = ET.SubElement(user_xml, k)
    child.text = str(v)

tree = ET.ElementTree(user_xml)
tree.write("user.xml")

print("✅ Files created: user.json, user.csv, user.yaml, user.xml")

# -------------------------------
# 2. Define User structures
# -------------------------------
class UserDict(TypedDict):
    name: str
    age: int
    email: str

class UserNT(NamedTuple):
    name: str
    age: int
    email: str

@dataclass
class UserDC:
    name: str
    age: int
    email: str

class UserModel(BaseModel):
    name: str
    age: int
    email: str

print("✅ User structures defined")

# -------------------------------
# 3. NumPy array vs Python list
# -------------------------------
py_list = [1, 2, 3, 4, 5]
np_array = np.array([1, 2, 3, 4, 5])

print("Python List:", py_list)
print("NumPy Array:", np_array)

# -------------------------------
# 4. Execution time decorator
# -------------------------------
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.6f} seconds")
        return result
    return wrapper

# -------------------------------
# 5. Compare execution time (List vs NumPy)
# -------------------------------
@timer
def multiply_list(lst, scalar):
    return [x * scalar for x in lst]

@timer
def multiply_array(arr, scalar):
    return arr * scalar

lst = list(range(1000000))
arr = np.array(range(1000000))

print("Multiplying Python list...")
multiply_list(lst, 10)

print("Multiplying NumPy array...")
multiply_array(arr, 10)

# -------------------------------
# 6. Load CSV into Pandas DataFrame
# -------------------------------
df = pd.read_csv("user.csv")
print("\nDataFrame from CSV:")
print(df)
