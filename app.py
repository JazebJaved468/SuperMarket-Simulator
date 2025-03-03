import streamlit as st
from utils import home, simulate, analysis
# Set page config
st.set_page_config(page_title="Markov Chain Simulation", layout="wide")
 
# Custom CSS for styling sidebar
st.markdown("""
    <style>
        /* Sidebar styles */
        [data-testid="stSidebar"] {
            background-color: #1E1E1E;  /* Dark background */
            padding:  20px;
            border-right: 2px solid #FF4B4B;
        }

        /* Sidebar title */
        [data-testid="stSidebar"] h1 {
            color: white;
            # text-align: center;
        }

        /* Adjust content width */
        .block-container {
            padding: 4rem;
        }
    </style>
""", unsafe_allow_html=True)



def add_styling():
    st.html("""
        <style>
            /* convert radio to list of buttons */
            div[role="radiogroup"] {
                flex-direction:col;
                padding: 20px 0px;
            }
            input[type="radio"] + div {
                background: #ffffff !important;
                color: #000;
                border-radius: 30px !important;
                padding: 8px 30px !important;
                margin  : 0px 20px !important;
            }
            input[type="radio"][tabindex="0"] + div {
                # background: #E6FF4D !important;
                background: #d84040 !important;
                # color: #ffffff !important;
                # color: #ffffff !important;
            }
            input[type="radio"][tabindex="0"] + div p {
                color: #fff !important; 
            # to change text color inside button
            }
            div[role="radiogroup"] label > div:first-child {
                display: none !important;
            }
            div[role="radiogroup"] label {
                margin-left: 10% !important; 
            }
            div[role="radiogroup"] {
                gap: 40px;
            }
        </style>
    """)

add_styling()   
# Sidebar Navigation
st.sidebar.title("Welcome To Market Analyzer 👋")
page = st.sidebar.radio("",["Get Started", "Simulate", "Analysis"])

# Render Selected Page
if page == "Get Started":
    home.show()
elif page == "Simulate":
    simulate.show()
elif page == "Analysis":
    analysis.show()


# import streamlit as st

# def main():
#     # st.set_page_config(page_title="Multi-Page App", layout="wide")
    
#     # Sidebar navigation
#     st.sidebar.title("Navigation")
#     page = st.sidebar.radio("Go to", ["Home", "About", "Contact"])
    
#     if page == "Home":
#         home()
#     elif page == "About":
#         about()
#     elif page == "Contact":
#         contact()

# def home():
#     st.title("Home Page")
#     st.write("Welcome to the Home Page of our Streamlit app!")

# def about():
#     st.title("About Page")
#     st.write("This is a simple Streamlit app with sidebar navigation.")

# def contact():
#     st.title("Contact Page")
#     st.write("You can reach us at: contact@example.com")

# if __name__ == "__main__":
#     main()
