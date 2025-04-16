import os
import streamlit as st
import base64
from logic.simulation_with_analysis import simulation_bind_with_analysis
from  make_gif_simulation   import do_simulation, do_simulation_with_binded_data
import pandas as pd
import time

def show():
    st.title("🔬 Simulate Customer Movement")
    st.write("")
    st.warning("Run simulations of customer behavior in the supermarket.")
    st.write("")
    st.write("")
    # st.code("python simulation_one_day.py")
    # st.success("Simulation will generate movement data for one full day.")
      # Simulation input controls
    # start_time = st.time_input("Select Start Time", value=None)
    # end_time = st.time_input("Select End Time", value=None)
    # num_customers = st.number_input("Number of Customers to Simulate", min_value=1, max_value=500, value=10)

      # Add entrance data configuration section
    st.write("")
    st.subheader("📊 Customer Entrance Configuration")
    st.write("Configure the hourly entrance counts for your simulation")
    
    # # Define default values for the hourly entrance counts
    # default_hours = list(range(7, 22))  # 7 AM to 9 PM
    # # default_counts = [9, 141, 90, 79, 68 , 80, 106, 98, 80, 108, 111, 131, 148, 96,55 ]
    # default_counts = [9, 0, 0 , 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
    
    # # Initialize session state for the data if it doesn't exist
    # if 'entrance_data' not in st.session_state:
    #     st.session_state.entrance_data = pd.DataFrame({
    #         'hour': default_hours,
    #         'entrance count': default_counts
    #     })
    
    # # Create the editable dataframe
    # edited_df = st.data_editor(
    #     st.session_state.entrance_data,
    #     num_rows="fixed",
    #     column_config={
    #         "hour": st.column_config.NumberColumn(
    #             "hour",
    #             help="Hour of the day (7-21)",
    #             min_value=0,
    #             max_value=23,
    #             step=1,
    #             disabled=True,  
    #         ),
    #         "entrance count": st.column_config.NumberColumn(
    #             "Entrance Count",
    #             help="Number of customers entering per hour",
    #             min_value=0,
    #             max_value=100,
    #             step=1
    #         )
    #     },
    #     hide_index=True,
    # )
    
    # # Save button for the entrance data
    # if st.button("Save Entrance Configuration"):
    #     # Update the session state
    #     st.session_state.entrance_data = edited_df
        
    #     # Create data directory if it doesn't exist
    #     os.makedirs('data', exist_ok=True)
        
    #     # Save to CSV
    #     edited_df.to_csv('data/custom_customer_per_hour.csv', index=0)
    #     st.success("Entrance configuration saved successfully!")

    st.markdown("""
<style>
div[data-testid="stButton"] button:first-child {
    background-color: #ff4b4b;
    color:white !important; 
}

div[data-testid="stButton"] button:first-child:hover {
    background-color: #d43b3b;
    color: white !important; 
}
</style>
""", unsafe_allow_html=True)    



    if st.button("Start Simulation") :  
        print("Simulation started")
      
        with st.spinner("Preparing simulation for the latest data... Please wait."):
            # time.sleep(3)  # Simulating processing delay
            #   do_simulation(  num_customers)
            #   do_simulation_with_binded_data()
              simulation_bind_with_analysis()
              print("Simulation ended")
                    # Get the maximum customer ID from the generated file
              try:
                simulation_df = pd.read_csv('simulation/one_day_simulation.csv')
                numberOfCustomers = simulation_df['customer_id'].max()
                st.success(f"Simulation completed for {numberOfCustomers} customers")
              except FileNotFoundError:
                st.error("Error: Simulation output file not found.")
        # st.write("SIMULATION RESULTS")
              # file_ = open("simulation/customer_simulation.gif", "rb")
              # contents = file_.read()
              # data_url = base64.b64encode(contents).decode("utf-8")
              # file_.close()

              # st.markdown(
              #     f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
              #     unsafe_allow_html=True,
              # )

    st.write("")
                    
    tab1, tab2 = st.tabs(["Simulation Results", "Simulation Data Output",])  


    with tab1:
        
        try:
          st.subheader("Simulation Results")
          st.write("View the simulation of customers in the supermarket.")
          file_ = open("simulation/customer_simulation.gif", "rb")
          contents = file_.read()
          data_url = base64.b64encode(contents).decode("utf-8")
          file_.close()

          st.markdown(
              f'<img src="data:image/gif;base64,{data_url}" >',
              unsafe_allow_html=True,
          )
        except FileNotFoundError:
            st.info("Run the simulation to generate results.", icon="ℹ️")

       

    with tab2:
            # Streamlit UI
            st.write("")
            st.subheader("Customer Movement Data")
            st.write("")
            try:
                # Load data
              csv_file = "transformed_customers_journey_in_supermarket.csv"  # Change this if your file name is different
              df = pd.read_csv(csv_file)

             

              # Show raw data
              # st.subheader("Raw Data")
              st.dataframe(df)  # Displays the DataFrame in a table

              # Add a customer filter
              st.write("")
              st.write("")
              st.subheader("Search for a Specific Customer")
            
              customer_id = st.number_input("Enter Customer ID:", min_value=0, max_value=len(df)-1, step=1)
              if st.button("Show Journey"):
                  customer_data = df[df["Customer"] == customer_id]
                  if not customer_data.empty:
                      st.write(customer_data)
                  else:
                      st.warning("Customer not found!")
            except FileNotFoundError:
                st.info("Run the simulation to generate output data.", icon="ℹ️")
    


if __name__ == "__main__":
    show()
