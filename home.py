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
    st.title("Supermarket Simulation Using Markov Chains 🏪")
    st.markdown(
        """
        <h4>This app visualizes customer behavior in a supermarket using <b>Markov Chain simulation</b>.</h4>
        <p style="font-size:20px;margin-top:10px;">
        Customers transition between different sections based on predefined probabilities in Transition Probability Matrix.
        </p>
        """, 
        unsafe_allow_html=True
    )

    

    # Create tabs
    tab1, tab2, tab3 = st.tabs(["Overview", "TPM",  "Markov Diagram"])  

    # Tab 1: Overview
    with tab1:
        tab_overview.show()

    with tab2:
        st.write("")
        st.subheader("📊 Transition Probability Matrix")
        st.write("")
        st.success("A visual representation of the Transition Probability Matrix used in the simulation.")
        st.write("")
        st.write("")
        # st.code("python make_markov_diagram.py")
        image = Image.open("assets/probability_transition_matrix.png")
        st.image(image, caption="Transition Probability Matrix")
        

   
  

    # Tab 3: Markov Diagram
    with tab3:
        st.write("")
        st.subheader("🔗 Markov Chain Diagram")
        st.write("")
        st.success("A visual representation of the transition probabilities between different supermarket sections.")
        st.write("")
        st.write("")
        image = Image.open("assets/markov.png")
        st.image(image, caption="Markov Chain Diagram")
 
        



    
   
 

if __name__ == "__main__":
        show()