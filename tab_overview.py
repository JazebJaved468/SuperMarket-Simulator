
import streamlit as st 
import base64
from PIL import Image

def show():
    st.write("")
    st.subheader("🏪 Super Market")
    # st.write("Customers move between different sections of a supermarket, based on a probability transition matrix.")

    sections = ["Entrance", "Drinks", "Dairy", "Fruit", "Spices", "Checkout"]
    st.write("")
    st.success("Customers navigate through the following sections:")
    st.write("")
    st.write("\n".join([f"- {section}" for section in sections]))
        
    file_ = open("assets/modern_mart_customer_simulation.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()

    # st.markdown(
    #     f'<img src="data:image/gif;base64,{data_url}"  >',
    #     unsafe_allow_html=True,
    # )

    image = Image.open("assets/modern_mart_customer_simulation.gif")
    st.image(image, caption="A Super Market", )


    st.write("")
    st.write("")
    st.warning("Features" ,icon="🔹" )
    
    st.write("")
    
    features = [
        "**Animated Customer Flow:** Create Simulation showcasing how customers navigate the store in real time.",
        "**Markov Chain Visualization:** Generate a transition diagram to illustrate customer movement probabilities.",
        "**One-Day Simulation:** Simulate an entire day of customer activity and analyze behaviors using pre-defined data models.",
        "**Exploratory Data Analysis (EDA):** Perform in-depth analysis of customer distribution, revenue trends, and time spent per section."
        ]
    st.write("\n".join([f"- {feature}" for feature in features]))

    
    st.write("")
    st.write("")
    st.success("Insights & Analysis" ,icon="📊" )
    st.write("")
    st.write("Once the simulation is complete, the generated data can be used to:")
    insights = [
        "Identify peak shopping hours",
        "Optimize store layout based on movement patterns",
        "Analyze customer preferences for different store sections",
        "Improve store efficiency by predicting customer flow"
        ]
    st.write("\n".join([f"- {insight}" for insight in insights]))

    



if __name__ == "__main__":
    show()