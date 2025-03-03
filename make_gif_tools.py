from customer_tools import Customer
import numpy as np
import imageio
import os
import glob
import cv2
from matplotlib import pyplot as plt


def save_each_state(Nb_customers):
    """"
    This function simulates Nb_customers, assign a random colour
    for each of them and save all states (per minute) in the supermarket
    as png pictures.
    """
    colors = [0,1,2]

    for customer_id in range (Nb_customers):
        #Create new customer
        new_customer = Customer(customer_id)
        #Assign a random colour
        new_color = np.random.choice(colors,2)
        unique_colors = np.unique(new_color)
        nb_colors_to_change = len(unique_colors)

        list(new_customer.gen)
        states = new_customer.history


        for s_nb,s in enumerate(states):

            #Read the picture to plot thge customer position at each state
            frame = cv2.imread('./simulation/modern_market.png')

            if s == 'entrance':
                for i in range(nb_colors_to_change):

                    frame[760:880, 700:820, unique_colors[i]] = 0

            elif s == 'checkout':

                for i in range(nb_colors_to_change):

                    frame[760:880, 205:325, unique_colors[i]] = 0

            elif s == 'dairy':

                for i in range(nb_colors_to_change):

                    frame[250:370, 300:420, unique_colors[i]] = 0

            elif s == 'drinks':

                for i in range(nb_colors_to_change):

                    frame[250:370, 50:170, unique_colors[i]] = 0

            elif s == 'fruit':

                for i in range(nb_colors_to_change):

                    frame[250:370, 800:920, unique_colors[i]] = 0

            elif s == 'spices':

                for i in range(nb_colors_to_change):

                    frame[250:370, 550:670, unique_colors[i]] = 0

            else:

                print('This state does not exist')

            plt.figure(figsize=(8,5))
            plt.imshow(frame)
            #Save all states to disk
            plt.savefig(f'./simulation/customer_{customer_id}_states_{s_nb}.png')
            plt.close()

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
