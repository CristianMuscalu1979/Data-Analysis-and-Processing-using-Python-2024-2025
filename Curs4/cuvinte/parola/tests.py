from django.test import TestCase

# Create your tests here.

import pandas as pd

with open("parole.csv", "w") as fwriter:
    fwriter.write("parole")

df = pd.read_csv("parole.csv")

print(df)

df.to_json("parole.json")
