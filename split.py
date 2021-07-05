import pandas as pd
from sklearn.model_selection import train_test_split


df = pd.read_csv("train.csv",index_col=0)
train, test = train_test_split(df, test_size=0.2, random_state=42)
train.to_csv("train2.csv")
test.to_csv("test2.csv")


