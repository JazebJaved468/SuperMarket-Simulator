from customer_tools import Customer
import numpy as np
import imageio
import os
import glob
import cv2
from matplotlib import pyplot as plt
import pandas as pd

import pandas as pd

def create_customer_journey_dicts():
    # Read the CSV file
    df = pd.read_csv('transformed_customers_journey_in_supermarket.csv')
    
    # List to hold customer journey dictionaries
    customer_journeys = []
    
    # Process each row (customer)
    for _, row in df.iterrows():
        customer_id = row['Customer']
        
        # Extract all states (skipping Customer column and NaN values)
        customer_states = [state for state in row.values[1:] if isinstance(state, str)]
        
        # Create a dictionary and add to list
        customer_journey = {
            'customer_id': customer_id,
            'customer_states': customer_states
        }
        customer_journeys.append(customer_journey)
    
    return customer_journeys

# Create the customer journey dictionaries
customer_journey_dicts = create_customer_journey_dicts()

# Print the result
for journey in customer_journey_dicts:
    print(journey)







def save_each_state_with_binded_data():
    """
    Uses the pre-loaded customer journey data,
    assigns a random color to each customer, 
    and saves all states in the supermarket as PNG pictures.
    """
    colors = [0, 1, 2,]
    
    # Get customer journeys from our existing dictionary
    customer_journeys = create_customer_journey_dicts()
    
    for journey in customer_journeys:
        customer_id = journey['customer_id']
        states = journey['customer_states']
        
        # Assign a random color
        new_color = np.random.choice(colors, 2)
        unique_colors = np.unique(new_color)
        nb_colors_to_change = len(unique_colors)
        
        print(f"Customer {customer_id} colors: {new_color}")
        print(f"Customer {customer_id} journey: {states}")
        
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
                
                 # Convert to RGB for matplotlib
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                
                # Create figure with proper size
                fig, ax = plt.subplots(figsize=(8, 5))
                ax.imshow(frame_rgb)
                
                # Add customer ID text to the frame
                ax.text(35, 65, f"Customer: {customer_id}", fontsize=14, 
                        color='white', bbox=dict(facecolor='black', alpha=0.7))
                
                # Add the current state
                ax.text(545, 65, f"Location: {s}", fontsize=14, 
                        color='white', bbox=dict(facecolor='black', alpha=0.7 ))
                
                # Add step number
                ax.text(35, 140, f"Step: {s_nb}", fontsize=12,
                        color='white', bbox=dict(facecolor='black', alpha=0.7, ))
                
                # Remove axes
                ax.axis('off')
                
                # Save image for each state
                plt.savefig(f'./runtime/customer_{customer_id}_states_{s_nb}.png')
                plt.close(fig)
            else:
                print(f"Warning: State '{s}' does not exist!")

    print(f"Generated visualization for {len(customer_journeys)} customers")


def make_gif_from_states_with_binded_data():
    """
    This function reads all customers states in the order of occurrence
    and makes a gif of all states (and deletes the png pictures from disk).
    """
    image_directory = './runtime'
    
    # Get the customer IDs from the journey dictionaries
    customer_journeys = create_customer_journey_dicts()
    customer_ids = [journey['customer_id'] for journey in customer_journeys]
    
    list_of_images = []
    
    for customer_id in customer_ids:
        path_to_read = os.path.join(image_directory, f'customer_{customer_id}_*.png')
        files = glob.glob(path_to_read)
        files.sort(key=os.path.getmtime)
        for f in files:
            im = imageio.imread(f)
            list_of_images.append(im)
            os.remove(f)
    
    imageio.mimsave(f'./simulation/customer_simulation.gif', list_of_images, duration=500)
    print(f"Created GIF with {len(list_of_images)} frames")




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
        print(states)
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
