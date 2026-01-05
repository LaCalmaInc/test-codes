import matplotlib as plt
import numpy as np
import seaborn as sns
import pandas as pd

path = "VD/2023 Car Dataset.csv"
df = pd.read_csv(path)
df.head()