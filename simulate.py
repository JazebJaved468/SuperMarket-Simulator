import streamlit as st
import base64
from  make_gif_simulation   import do_simulation

def show():
    st.title("🔬 Simulate Customer Movement")
    st.write("Run simulations of customer behavior in the supermarket.")
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
              st.write("SIMULATION RESULTS")
              file_ = open("simulation/customer_simulation.gif", "rb")
              contents = file_.read()
              data_url = base64.b64encode(contents).decode("utf-8")
              file_.close()

              st.markdown(
                  f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
                  unsafe_allow_html=True,
              )
                    
    

if __name__ == "__main__":
    show()
