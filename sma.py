import pandas as pd
import matplotlib.pyplot as plt
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators


api_key = 'RNZPXZ6Q9FEMEHM'

time_series = TimeSeries(key=api_key, output_format='pandas')
data_time_series, meta_data_time_series = time_series.get_intraday(symbol='MSFT', interval='5min', outputsize='full')


period = 300

t_indicator = TechIndicators(key=api_key, output_format='pandas')
data_t_indicator, meta_data_t_indicator = t_indicator.get_sma(symbol='MSFT', interval='5min',time_period=period, series_type='close')


data_frame_1 = data_t_indicator
data_frame_2 = data_time_series['4. close'].iloc[period-1::]

data_frame_2.index = data_frame_1.index

total_df = pd.concat([data_frame_1, data_frame_2], axis=1)
print(total_df)


total_df.plot()

plt.show()

#totally changed to san1
#changes made to san2
#add this line in remote branch directly
