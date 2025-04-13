from simulation_tools import arrival_time_from_hour_distribution
from simulation_tools import simulate_customers
import pandas as pd
import numpy as np

from datetime import datetime

def one_day_simulation():

    # Get today's date in 'YYYY-MM-DD' format
    today_date = datetime.today().strftime('%Y-%m-%d')
    

    #Take the hour distribution estimated from a dataset
    df_customer_per_hour = pd.read_csv('data/custom_customer_per_hour.csv', index_col=0)
    print(df_customer_per_hour.columns)

    #Define a date
    date = today_date

    #Generate minute arrival time along the day and customer id
    # It takes the average number of customer entering the shop per hour and return a randomly sampled
    # arrival time per minute to simulate arrival time of customers in the shop for one day
    df_arrival_time = arrival_time_from_hour_distribution(df_customer_per_hour,date)

    # print(df_arrival_time)

    #Simulate customers behaviour for one day
    df_simulation_one_day = simulate_customers(df_arrival_time)

    # print(df_simulation_one_day)

    #Save to demo folder to analyze the data
    df_simulation_one_day.to_csv('./simulation/one_day_simulation.csv',index=None)


if __name__ == '__main__':
    one_day_simulation()
    
