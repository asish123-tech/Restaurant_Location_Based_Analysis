import pandas as pd
import matplotlib.pyplot as plt
import os

if not os.path.exists("output"):
    os.makedirs("output")
df = pd.read_csv("dataset/Dataset.csv")

print("Dataset loaded successfully")
print("Total number of restaurants:", len(df))

