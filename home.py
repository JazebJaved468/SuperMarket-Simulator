# import streamlit as st

# st.title("Markov Chain Simulator 🚀")
# st.write("This app will help visualize customer arrival and interaction in a shop, their statistics and simulations.")
# st.write("Please select the code snippet you want to visualize from the dropdown menu.")

import streamlit as st
from PIL import Image 
import tab_overview

# Load and Display Images
def display_image(image_path, caption):
    image = Image.open(image_path)
    st.image(image, caption=caption, use_container_width=True)


def show():

    # Title & Description
    st.title("Markov Chain Supermarket Simulation 🏪")
    st.write("""
    This app visualizes customer behavior in a supermarket using **Markov Chain simulation**.
    Customers transition between different sections based on predefined probabilities.
    """)

    

    # Create tabs
    tab1, tab2, tab3, tab4 = st.tabs(["Overview", "TPM",  "Markov Diagram",  "Usage Guide"])

    # Tab 1: Overview
    with tab1:
        tab_overview.show()

    with tab2:
        st.subheader("📊 Transition Probability Matrix")
        st.write("A visual representation of the transition probability Matrix")
        # st.code("python make_markov_diagram.py")
        image = Image.open("assets/probability_transition_matrix.png")
        st.image(image, caption="Markov Chain Diagram")
        

   
  

    # Tab 3: Markov Diagram
    with tab3:
        st.subheader("🔗 Markov Chain Diagram")
        st.write("A visual representation of the transition probabilities between different supermarket sections.")
        # st.code("python make_markov_diagram.py")
        image = Image.open("assets/markov.png")
        st.image(image, caption="Markov Chain Diagram")

    # Tab 4: Usage Guide
    with tab4:
        st.subheader("🚀 How to Use?")
        st.write("""
        1. Clone the repository.
        2. Install dependencies: `pip install -r requirements.txt`
        3. Run this app: `streamlit run app.py`
        """)
        st.success("You're all set! Use the sidebar to navigate.")



    
   

    # How to Use
    # st.subheader("🚀 How to Use?")
    # st.write("""
    # 1. Clone the repository.
    # 2. Install dependencies: `pip install -r requirements.txt`
    # 3. Run this app: `streamlit run app.py`
    # """)

    # st.success("Ready to explore customer movements? Use the sidebar to navigate!")

if __name__ == "__main__":
    show()