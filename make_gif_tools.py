from customer_tools import Customer
import numpy as np
import imageio
import os
import glob
import cv2
from matplotlib import pyplot as plt
import pandas as pd


def save_each_state(Nb_customers):
    """
    Simulates Nb_customers, assigns a random color to each of them, 
    and saves all states (per minute) in the supermarket as PNG pictures.
    Also saves the simulation history to a CSV file.
    """
    colors = [0,1,2]
    customer_histories = []  # Store all customers' journey history

    for customer_id in range(Nb_customers):
        # Create new customer
        new_customer = Customer(customer_id)

        # Assign a random color
        new_color = np.random.choice(colors, 2)
        unique_colors = np.unique(new_color)
        nb_colors_to_change = len(unique_colors)

        # Simulate the customer's journey
        list(new_customer.gen)
        states = new_customer.history
        customer_histories.append([customer_id] + states)  # Store customer path

        print(f"Customer {customer_id} colors: {new_color}")
        print(f"Customer {customer_id} journey: {new_customer.history}")

        for s_nb, s in enumerate(states):
            # Read the background supermarket map
            frame = cv2.imread('./simulation/modern_market.png')

            # Define state positions
            state_positions = {
                'entrance': (760, 880, 700, 820),
                'checkout': (760, 880, 205, 325),
                'dairy': (250, 370, 300, 420),
                'drinks': (250, 370, 50, 170),
                'fruit': (250, 370, 800, 920),
                'spices': (250, 370, 550, 670)
            }

            if s in state_positions:
                x1, x2, y1, y2 = state_positions[s]
                for i in range(nb_colors_to_change):
                    frame[x1:x2, y1:y2, unique_colors[i]] = 0  # Change color

                # Save image for each state
                plt.figure(figsize=(8,5))
                plt.imshow(frame)
                plt.savefig(f'./simulation/customer_{customer_id}_states_{s_nb}.png')
                plt.close()
            else:
                print(f"Warning: State '{s}' does not exist!")

    # Convert customer histories into a DataFrame
    max_length = max(len(h) for h in customer_histories)  # Find longest journey
    df_output = pd.DataFrame(customer_histories, columns=["Customer"] + [f"Step_{i}" for i in range(max_length - 1)])

    # Save to CSV
    df_output.to_csv('customers_journey_in_supermarket.csv', index=False) 

def make_gif_from_states(Nb_customers):
    """
    This function reads all customers states in the order of occurence
    and make a gif of all states (and delete the png pictures from disk).
    """
    image_directory = './simulation'

    list_of_images=[]

    for customer_id in range (Nb_customers):
        path_to_read = os.path.join(image_directory,f'customer_{customer_id}_*.png')
        files = glob.glob(path_to_read)
        files.sort(key=os.path.getmtime)
        for f in files:
            im = imageio.imread(f)
            list_of_images.append(im)
            os.remove(f)

    imageio.mimsave(f'./simulation/customer_simulation.gif', list_of_images, duration = 500)
