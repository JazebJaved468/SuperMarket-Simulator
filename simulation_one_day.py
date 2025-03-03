from simulation_tools import arrival_time_from_hour_distribution
from simulation_tools import simulate_customers
import pandas as pd
import numpy as np

from datetime import datetime

# Get today's date in 'YYYY-MM-DD' format
today_date = datetime.today().strftime('%Y-%m-%d')
 

#Take the hour distribution estimated from a dataset
df_customer_per_hour = pd.read_csv('data/customer_per_hour.csv', index_col=0)

#Define a date
date = today_date

#Generate minute arrival time along the day and customer id
df_arrival_time = arrival_time_from_hour_distribution(df_customer_per_hour,date)

#Simulate customers behaviour for one day
df_simulation_one_day = simulate_customers(df_arrival_time)

#Save to demo folder to analyze the data
df_simulation_one_day.to_csv('./simulation/one_day_simulation.csv',index=None)
