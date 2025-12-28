from pynetqoe import preprocess_qoe_data, QoEPredictor
import pandas as pd

df = pd.read_csv('pokemon.csv') # use your dataset
clean_df = preprocess_qoe_data(df)
print(clean_df.head())