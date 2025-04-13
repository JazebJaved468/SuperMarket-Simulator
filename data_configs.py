import os
import streamlit as st
import base64
from logic.simulation_with_analysis import simulation_bind_with_analysis
from  make_gif_simulation   import do_simulation, do_simulation_with_binded_data
import pandas as pd
import time


def show():
        st.title("🔬 Customer Data Configuration")
        st.write("")
        st.warning("Configure customer entrance patterns and behavior parameters for simulation.")
        st.write("")
        st.write("")
    # st.code("python simulation_one_day.py")
    # st.success("Simulation will generate movement data for one full day.")
      # Simulation input controls
    # start_time = st.time_input("Select Start Time", value=None)
    # end_time = st.time_input("Select End Time", value=None)
 
        st.subheader("Hourly Customer Entrance Configuration")
        st.write("Set the number of customers entering the supermarket each hour")
        
        # Define default values for the hourly entrance counts
        default_hours = list(range(7, 22))  # 7 AM to 9 PM
        # default_counts = [9, 20, 35, 45, 65, 80, 70, 55, 60, 75, 85, 80, 65, 40, 15]
        # default_counts = [5, 12, 18, 15, 10, 14, 25, 30, 24, 16, 10, 8, 5, 3, 2]
        default_counts = [5, 0, 0 , 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # Initialize session state for the data if it doesn't exist
        if 'entrance_data' not in st.session_state:
            st.session_state.entrance_data = pd.DataFrame({
                'hour': default_hours,
                'entrance count': default_counts
            })

      
         
        st.write("")
        # Create the editable dataframe
        edited_df = st.data_editor(
            st.session_state.entrance_data,
            num_rows="fixed",
            height=563,
            column_config={
                "hour": st.column_config.NumberColumn(
                    "Hour",
                    help="Hour of the day (7-21)",
                    min_value=0,
                    max_value=23,
                    step=1,
                    disabled=True,
                    format="%d : 00",  # Format to show as "7:00", "8:00", etc.
                   required=True,
               

                ),
                "entrance count": st.column_config.NumberColumn(
                    "Entrance Count",
                    help="Number of customers entering per hour",
                    min_value=0,
                    max_value=200,
                    step=1
                )
            },
            hide_index=True,
            use_container_width=True,
             
        )

        st.write("")
        st.write("")

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

      
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            # Save button for the entrance data
          
            if st.button("Save Configuration", use_container_width=True):
                # Update the session state
                st.session_state.entrance_data = edited_df
                
                # Create data directory if it doesn't exist
                os.makedirs('data', exist_ok=True)
                
                # Save to CSV
                edited_df.to_csv('data/custom_customer_per_hour.csv', index=False)
                st.success("Entrance configuration saved successfully!")
        
        with col2:
            # Reset button
            if st.button("Reset to Default", use_container_width=True):
                st.session_state.entrance_data = pd.DataFrame({
                    'hour': default_hours,
                    'entrance count': default_counts
                })
                # st.experimental_rerun()
        
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        # Display chart of current data
        st.subheader("Hourly Distribution Visualization")
        chart_data = edited_df.set_index('hour')
        st.bar_chart(chart_data)