import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# sns.set_style('whitegrid')
# sns.set_style("dark")  # Dark theme
# ax.set_facecolor("none")  # Transparent background



fig, ax = plt.subplots(figsize=(6, 3))

sns.set_theme(style="dark", rc={"axes.facecolor": "#1e1e1e00", "figure.facecolor": "#1E1E1E00"})
plt.rcParams["text.color"] = "white"
plt.rcParams["axes.labelcolor"] = "white"
plt.rcParams["xtick.color"] = "white"
plt.rcParams["ytick.color"] = "white"

# Remove padding & spines
# plt.subplots_adjust(left=0, right=1, top=1, bottom=0)


def show():

    fig, ax = plt.subplots(figsize=(8, 5))
    for spine in ax.spines.values():
                    spine.set_visible(False)
    st.title("📊 Data Analysis - One Day Simulation")
    st.write("An in-depth analysis of customer behavior inside the supermarket. Explore different aspects of customer flow, shopping trends, revenue insights, and retention metrics using interactive visualizations.")
    st.success("Use this analysis to improve store layouts and customer experience.")

    # df_customers = pd.read_csv('simulation/one_day_simulation.csv',parse_dates=True)
    # df_customers.head(90)

    # Create tabs
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Simulations Data", "Arrival Rate",  "Revenue", "Profitable Section", "Customer Repartition",  "Customer Retainment" , "Time Distribution"])

    try:
        df_customers = pd.read_csv('simulation/one_day_simulation.csv', parse_dates=True)
        df_customers['time']= pd.to_datetime(df_customers['time'])
        df_customers['arrival_time']=df_customers.groupby('customer_id')['time'].transform(min)
        df_customers['leaving_time']=df_customers.groupby('customer_id')['time'].transform(max)
            #Hour label to plot
        df_customers['hour']=df_customers['time'].dt.hour
            #Total time spent in the supermarker

            # print(df_customers['total_time'])
        df_customers['total_time'] = df_customers['leaving_time'] - df_customers['arrival_time']
        df_customers['total_time'] = df_customers['total_time'].dt.total_seconds() // 60
                #Add a price column to map location with price of products 
        df_customers['price']=df_customers['location']
        df_customers.price = df_customers.price.map( {'entrance':0 ,'checkout':0,'fruit':4,'spices':3,'dairy':5,'drinks':6} )
        df_customers.sort_values(by=['time'],inplace=True)

    

        with tab1:
            st.write("")
            st.subheader("One Day Simulation")
            st.write("")
            st.warning("Raw simulation data of customer movements within the supermarket, tracking their journey from entrance to checkout. This dataset provides detailed insights into individual customer behavior.")
            st.write("")
            st.write("")
            try:
                st.dataframe(df_customers.head(300) , height=600 ,use_container_width=True)  # Display as an interactive table
            except FileNotFoundError:
                st.error("Some Error Occurred! while generating the customer simulation data.")


        with tab2:
            try:
                st.write("")
                st.subheader("Arrival Rate/hour")
                st.subheader("📈 Number of Customers at Entrance Per Hour")
                st.write("")
                st.warning("Analyze customer arrival patterns per hour to identify peak hours. Use this information to optimize staffing and inventory planning.")
                
                st.write("")
                st.write("")
                
                
                df_plot_entrance = df_customers.loc[df_customers['location'] == 'entrance'].copy()
                df_plot_entrance = df_plot_entrance.groupby('hour')['location'].count()
                df_plot_entrance = pd.DataFrame({'hour': df_plot_entrance.index, 'count': df_plot_entrance.values})
                
            
                fig, ax = plt.subplots(figsize=(8, 5))
                sns.barplot(x='hour', y='count', data=df_plot_entrance, ax=ax ,  width=1, palette='Reds')
               
                ax.set_ylabel('Number of New Entrances')
                st.pyplot(fig)
            
            except FileNotFoundError:
                st.error("Some Error Occurred! while analysing the arrival rate per hour.")

        with tab3:
            try:
                st.write("")
                st.subheader("💰 Revenue Per Hour")
                 
                st.write("")
                st.warning("Revenue generation trends over different hours of the day. Identify when the store is most profitable and make data-driven decisions for promotions and discounts.")
                st.write("")
                st.write("")
                
                df_revenue_hour = df_customers.groupby('hour').agg({"price": 'sum'}).reset_index()
                
                st.subheader("📈 Area Chart")
                # fig, ax = plt.subplots(figsize=(8, 5))
                fig, ax = plt.subplots(figsize=(8, 5))
                sns.lineplot(x='hour', y='price', data=df_revenue_hour, ax=ax, color="red", linewidth=2)
                ax.fill_between(df_revenue_hour["hour"], df_revenue_hour["price"], color="red", alpha=0.2)
                ax.set_ylabel('Revenue')
                ax.set_xlabel('Hour')
                st.pyplot(fig)

                st.write("")
                st.write("")
                st.write("")
                st.write("")

                    # Plot Time Distribution per Hour using a Violin Plot
              

                st.subheader("📊 Bar Chart")
               

                
                fig, ax = plt.subplots(figsize=(8, 5))
                sns.barplot(x='hour', y='price', data=df_revenue_hour, ax=ax, width=1, palette='Reds')
                ax.set_ylabel('Revenue per Hour')
                st.pyplot(fig)
            
            except FileNotFoundError:
                st.error("Some Error Occurred! while analysing the revenue per hour.")

        with tab4:
            try:
                st.write("")
                st.subheader("🛒 Revenue Per Section")
                 
                st.write("")
                st.warning("Find out which sections contribute the most to total revenue. This visualization helps in optimizing product placements and store layout for maximizing profits.")
                st.write("")
                st.write("")
                
                df_revenue_section = df_customers.loc[(df_customers['location'] != 'entrance') & (df_customers['location'] != 'checkout')].copy()
                df_revenue_section = df_revenue_section.groupby('location').agg({"price": 'sum'}).reset_index()
                
                fig, ax = plt.subplots(figsize=(6, 3))
                ax.pie(df_revenue_section['price'], labels=df_revenue_section['location'], autopct='%1.1f%%', startangle=140, colors=sns.color_palette('husl'), textprops={'fontsize': 8,})
                ax.axis('equal')
                ax.set_title("Revenue Distribution by Section" , fontsize=10, pad=20)
                st.pyplot(fig)
            
            except FileNotFoundError:
                st.error("Some Error Occurred! while analysing the revenue per section.")

        with tab5:
            try:
                st.write("")
                st.subheader("📍 Number of Customers in Each Area Over Time")
                 
                st.write("")
                st.warning("See how customers distribute across different sections of the supermarket throughout the day. Identify bottlenecks and high-traffic areas for better space management.")
                st.write("")
                st.write("")
                
                df_plot_hour = df_customers.loc[(df_customers['location'] != 'entrance') & (df_customers['location'] != 'checkout')].copy()
                df_plot_hour = df_plot_hour.groupby(['hour', 'location']).agg({"customer_id": pd.Series.nunique}).reset_index()
                
                fig, ax = plt.subplots(figsize=(8, 5))
                # for spine in ax.spines.values():
                #     spine.set_visible(False)
                    
                sns.pointplot(x='hour', y='customer_id', hue='location', data=df_plot_hour, ax=ax)
                ax.set_ylabel('Number of Customers')
                st.pyplot(fig)
            
            except FileNotFoundError:
                st.error("Some Error Occurred! while analysing the number of Customers in Each Area Over Time.")
        
        with tab6:
            try:
                # Plot Time at First State Over Time
                st.write("")
                st.subheader("⏳ Time at First State Over Time")
                 
                st.write("")
                st.warning("Analyze how long customers stay in the store, providing insights into engagement and shopping behavior. Longer stays can indicate better customer experiences and opportunities for increased sales.")
                st.write("")
                st.write("")
               
                df_plot_time = df_customers.loc[df_customers['location'] == 'entrance'].copy()
                df_plot_time = df_plot_time.groupby('hour').agg({"total_time": 'mean'}).reset_index()
                
                fig, ax = plt.subplots(figsize=(8, 5))
                # for spine in ax.spines.values():
                #     spine.set_visible(False)
                sns.pointplot(x='hour', y='total_time', data=df_plot_time, ax=ax,color="red" )
                ax.set_ylabel('Average total time (min)')
                ax.set_ylim([6, 9])
                st.pyplot(fig)
            
            except FileNotFoundError:
                st.error("Some Error Occurred! while analysing the time at first state over time.")
        
        with tab7:

            # Interactive Two-Column Layout
            # col1, empty_col, col2 = st.columns([2, 0.15, 1])

            # with col1:
                try:
                    # Plot Time Distribution per Hour
                    st.write("") 
                    st.subheader("⏳ Total Time Distribution per Hour")
                    
                    st.write("")
                    st.warning("Visualize the spread of customer time spent shopping across different hours. Identify patterns that can help improve operational efficiency and customer satisfaction..")
                    st.write("")
                    st.write("")

                    st.subheader("📊 Inter Quartile Range (IQR) Plot")
                    
                    
                    df_plot_time = df_customers.loc[df_customers['location'] == 'entrance'].copy()
                    
                    fig, ax = plt.subplots(figsize=(8, 5))
                   
                    sns.boxplot(data=df_plot_time, y="total_time", x="hour", orient="v", ax=ax , palette='Reds' , width=0.5,
                                
                                # boxprops=dict(color="cyan"),      # Box color
                                whiskerprops=dict(color="white"),  # Whisker color
                                capprops=dict(color="white"),   # Cap (end of whiskers) color
                                medianprops=dict(color="black"),   # Median line color
                                flierprops=dict(marker='o', color='white', markersize=6 , markerfacecolor='white' , markeredgecolor='#ffffff00')  # Outliers color
                                )
                    ax.set_ylabel('Total time distribution (min)')
                    st.pyplot(fig)

                    st.write("")
                    st.write("")
                    st.write("")
                    st.write("")

                    # Plot Time Distribution per Hour using a Violin Plot
                    st.subheader("🎻 Violin Plot")
                    fig, ax = plt.subplots(figsize=(8, 5))
                    sns.violinplot(data=df_plot_time, y="total_time", x="hour", ax=ax, palette='Reds' 
                                    ,inner='quartile',        # Shows quartiles inside violin
                                    linewidth=1,             # Line width
    saturation=1
                                   )
                    ax.set_ylabel('Total time distribution (min)')
                    st.pyplot(fig)

                        

                
                except FileNotFoundError:
                    st.error("Some Error Occurred! while analysing the time distribution per hour.")
                
            # with col2:
            #         st.subheader("📌 Understanding the Graph")
            #         st.markdown("""
            #         - **Each box represents the spread of customer total time per hour**
            #             - The **box (IQR - Interquartile Range)** shows the middle **50%** of customer times.
            #             - The **line inside the box** represents the **median (middle value)** of total time.
            #         - **Whiskers (Lines Extending from the Box) Indicate the Range**
            #             - They show the **minimum and maximum time values** (excluding outliers).
            #         - **Outliers (Dots Outside the Whiskers)**
            #             - If there are **dots above or below the whiskers**, it means some customers **spent significantly more or less time** than the majority.
            #         - **Comparison Across Different Hours**
            #             - If the boxes shift up/down over hours, it indicates that **customers tend to spend more/less time depending on the time of the day.**
            #             - Wider boxes suggest **greater variation** in shopping time.
            #         """)
    except FileNotFoundError:
        st.error("Data file not found! Please run the simulation first.")
        

if __name__ == "__main__":
    show()