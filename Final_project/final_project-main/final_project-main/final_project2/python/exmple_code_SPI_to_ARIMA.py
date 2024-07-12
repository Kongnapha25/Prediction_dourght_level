# import pandas as pd
# import numpy as np
# from statsmodels.tsa.arima.model import ARIMA
# from statsmodels.tsa.stattools import adfuller
# import matplotlib.pyplot as plt

# # Load data (assuming you have calculated SPI already)
# rain_data = pd.read_excel('path_to_your_file/merge _files_rain_data.xlsx', sheet_name='Sheet1')

# # Ensure 'SPI' column is numeric
# rain_data['SPI'] = pd.to_numeric(rain_data['SPI'], errors='coerce')

# # Drop NaN values
# rain_data = rain_data.dropna(subset=['SPI'])

# # Set 'month_year' as the index
# rain_data['month_year'] = pd.to_datetime(rain_data['month_year'], format='%m-%Y')
# rain_data.set_index('month_year', inplace=True)

# # Plot the SPI values
# rain_data['SPI'].plot()
# plt.title('SPI Time Series')
# plt.show()

# # Test for stationarity
# result = adfuller(rain_data['SPI'])
# print('ADF Statistic:', result[0])
# print('p-value:', result[1])

# # Fit ARIMA model
# model = ARIMA(rain_data['SPI'], order=(p, d, q))  # Replace p, d, q with appropriate values
# model_fit = model.fit()

# # Summary of the model
# print(model_fit.summary())

# # Forecasting
# forecast = model_fit.forecast(steps=12)  # Forecasting next 12 months
# print(forecast)
