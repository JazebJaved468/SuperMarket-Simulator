import streamlit as st
import home, simulate, analysis

from PIL import Image 
# Set page config
st.set_page_config(page_title="Supermarket Simulation", layout="wide")
 
# Custom CSS for styling sidebar
st.markdown("""
    <style>
        /* Sidebar styles */
        [data-testid="stSidebar"] {
            background-color: #1E1E1E;  /* Dark background */
            padding:  0 20px;
            border-right: 2px solid #FF4B4B; 
            width: 360px !important; 
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
             /* Hide scrollbar for sidebar */
        [data-testid="stSidebar"]::-webkit-scrollbar {
            display: none; 
        }
        [data-testid="stSidebar"] {
            scrollbar-width: none; /* For Firefox */
        }
    </style>
""", unsafe_allow_html=True)



def add_styling():
    st.html("""
        <style>
            /* convert radio to list of buttons */
            div[role="radiogroup"] {
                flex-direction:col;
                padding: 6px 0px;
            }
            input[type="radio"] + div {
                background: #ffffff !important;
                color: #000;
                border-radius: 30px !important;
                padding: 8px 30px !important;
                # margin  : 0px 20px !important;
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

with st.sidebar:

     
    st.markdown(
        """
        <div style="text-align: center;">
        <img src='https://res.cloudinary.com/dpe70dvug/image/upload/v1741055249/mart_track_logo_ifjdoz.png' width='100' style='display: block; margin: 0 auto;'>
                 <h2 style="margin-top: 10px;font-size:40px">MART TRACK</h2>
            <h2 style="margin-top: 0px;">Welcome to the supermarket simulation and analysis Application! 👋</h2>
        </div>
        """, 
        unsafe_allow_html=True
    )

    st.markdown("" , unsafe_allow_html=True) 


page = st.sidebar.radio("",["Get Started", "Simulate", "Analysis"])

# Render Selected Page
if page == "Get Started":
    home.show()
elif page == "Simulate":
    simulate.show()
elif page == "Analysis":
    analysis.show()


 