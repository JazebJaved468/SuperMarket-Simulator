from make_gif_tools import make_gif_from_states_with_binded_data, save_each_state, make_gif_from_states, save_each_state_with_binded_data
import pandas as pd



# print(f"Total number of customers: {total_customers}")

def do_simulation( nb_customers: int = 1):
    #Number of customers to simulate
   
    Nb_customers = nb_customers

    #Simulate Nb_customers, assign a random colour for each customer and save the states
    save_each_state(Nb_customers)
    #Make a gif of all the states for all customers in the order of occurence
    make_gif_from_states(Nb_customers)


def do_simulation_with_binded_data():
     # Read the CSV file
    df = pd.read_csv('transformed_customers_journey_in_supermarket.csv')

    # Get the total number of customers (number of rows)
    total_customers = len(df)
    print(f"Total number of customers: {total_customers}")

    save_each_state_with_binded_data()

    #Make a gif of all the states for all customers in the order of occurence
    make_gif_from_states_with_binded_data()


# #Number of customers to simulate
# Nb_customers = 1

# #Simulate Nb_customers, assign a random colour for each customer and save the states
# save_each_state(Nb_customers)
# #Make a gif of all the states for all customers in the order of occurence
# make_gif_from_states(Nb_customers)

if __name__ == '__main__':
    do_simulation()