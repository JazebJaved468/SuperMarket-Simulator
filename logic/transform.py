import pandas as pd


# function to convert the one_day_simulation dataframe to a customer journey dataframe
# and save it to a csv file
def simulation_adapter():

    # Read the simulation data
    df_simulation = pd.read_csv('simulation/one_day_simulation.csv')

    # Sort by customer_id and time to ensure proper sequence
    df_simulation = df_simulation.sort_values(['customer_id', 'time'])

    # Initialize a dictionary to store customer journeys
    customer_journeys = {}

    # Process each row to build customer journeys
    for _, row in df_simulation.iterrows():
        customer_id = row['customer_id']
        location = row['location']
        
        # Initialize customer journey if not exists
        if customer_id not in customer_journeys:
            customer_journeys[customer_id] = []
        
        # Add every location entry (including repeated ones)
        customer_journeys[customer_id].append(location)

    # # Process each row to build customer journeys
    # for _, row in df_simulation.iterrows():
    #     customer_id = row['customer_id']
    #     location = row['location']
        
    #     # Initialize customer journey if not exists
    #     if customer_id not in customer_journeys:
    #         customer_journeys[customer_id] = ['entrance']  # Step_0 is always entrance
    #     else:
    #         # Add location only if it's different from the previous one
    #         # This handles cases where a customer stays in the same location for multiple time steps
    #         if location != customer_journeys[customer_id][-1]:
    #             customer_journeys[customer_id].append(location)



    # Find the maximum journey length
    max_steps = max(len(journey) for journey in customer_journeys.values())

    # Create a DataFrame for the journeys
    journey_columns = ['Customer'] + [f'Step_{i}' for i in range(max_steps)]
    journey_df = pd.DataFrame(columns=journey_columns)

    # Fill the DataFrame
    for customer_id, journey in customer_journeys.items():
        # Create a row with appropriate length
        row_data = {'Customer': customer_id}
        
        # Fill steps with journey data
        for i, location in enumerate(journey):
            row_data[f'Step_{i}'] = location
        
        # Add the row to the DataFrame
        journey_df = pd.concat([journey_df, pd.DataFrame([row_data])], ignore_index=True)

    # Sort by customer ID
    journey_df = journey_df.sort_values('Customer').reset_index(drop=True)

    # Save to CSV
    journey_df.to_csv('transformed_customers_journey_in_supermarket.csv', index=False)

    print(f"Converted {len(customer_journeys)} customer journeys with maximum {max_steps} steps.")