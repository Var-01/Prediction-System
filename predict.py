import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

df = pd.read_csv('C:\\Users\\anok1\\Documents\\Predict Git\\Prediction-System\\inventory_dataset.csv')
# print(df)

cookies_data = df[df['Sub Category'] == 'Cookies']
df = cookies_data
print(df)