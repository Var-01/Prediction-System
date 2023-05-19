import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller
from pandas.plotting import autocorrelation_plot
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import statsmodels.api as sm
from pandas.tseries.offsets import DateOffset


class SalesPrediction:
    def __init__(self, data_file):
        self.df = pd.read_csv(data_file)
        self.filtered_dataset = None