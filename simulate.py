import streamlit as st
import base64
from  make_gif_simulation   import do_simulation
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
    num_customers = st.number_input("Number of Customers to Simulate", min_value=1, max_value=500, value=10)
    if st.button("Start Simulation") and num_customers > 0 and num_customers <= 50:  
        print("Simulation started")
      
        with st.spinner("Preparing simulation... Please wait."):
            # time.sleep(3)  # Simulating processing delay
              do_simulation(  num_customers)
              print("Simulation ended")
              st.success(f"Simulation completed for {num_customers} customers")
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
              csv_file = "customers_journey_in_supermarket.csv"  # Change this if your file name is different
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
