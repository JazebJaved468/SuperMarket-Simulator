
import streamlit as st 
import base64
from PIL import Image

def show():
    st.subheader("🔄 Simulation Overview")
    st.write("Customers move between sections per minute, based on a probability transition matrix.")
        
    file_ = open("assets/modern_mart_customer_simulation.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()

    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
        unsafe_allow_html=True,
    )

    # st.write("")
    # st.write("")

    # st.subheader("📊 One-Day Simulation")
    # st.write("Run a full day’s simulation of customer movements and analyze the results.")
    # # st.code("python simulation_one_day.py")
    # image = Image.open("assets/new_entrance_per_hour.png")
    # st.image(image, caption="Customer Entrance Per Hour", )



if __name__ == "__main__":
    show()