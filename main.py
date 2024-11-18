# Importing required libraries
import streamlit as st  # For creating the web-based interactive dashboard
import pandas as pd  # For handling and processing the dataset
import plotly.express as px  # For creating interactive visualizations

# Setting the title of the Streamlit app
st.title("Cellphone Usage Dashboard")

# Displaying developer credits
st.markdown("### Developed by Helio Henrique (https://github.com/heliohenriquehfilho)")

# Loading the dataset from a CSV file
# The dataset contains information about user behavior, including screen time and other metrics
df = pd.read_csv("user_behavior_dataset.csv")

# Calculating the mean of the 'Screen On Time (hours/day)' column
hours_mean = df['Screen On Time (hours/day)'].mean()

# Grouping the dataset by age and calculating the mean screen time for each age
age_range = df.groupby('Age')['Screen On Time (hours/day)'].mean().reset_index()

# Creating two columns in the dashboard layout for side-by-side content
col1, col2 = st.columns(2)

# First column: Displaying a scatter plot of screen time vs. age
with col1:
    st.header("Screen Time (Hours/day) X Age")
    
    # Creating a scatter plot with a trendline using Plotly
    fig1 = px.scatter(
        age_range.set_index('Age'),  # Setting 'Age' as the index
        title="Screen Time X Age",  # Title of the plot
        trendline="ols"  # Adding an Ordinary Least Squares (OLS) trendline
    )
    
    # Customizing the plot to hide the legend
    fig1.update_layout(showlegend=False)
    
    # Displaying the plot in the Streamlit app
    st.plotly_chart(fig1)

# Second column: Displaying a dataset description
with col2:
    st.header("Data Base Description")
    st.write("""
        This dashboard is to showcase my abilities in Streamlit and Python. 
        The data is sourced from Kaggle (https://www.kaggle.com/datasets/valakhorasani/mobile-device-usage-and-user-behavior-dataset).
        
        This dataset provides a comprehensive analysis of mobile device usage patterns 
        and user behavior classification. It contains 700 samples of user data, including:
        - App usage time
        - Screen-on time
        - Battery drain
        - Data consumption

        Each entry is categorized into one of five user behavior classes, ranging from light to 
        extreme usage, allowing for insightful analysis and modeling.
    """)

# Adding a section to display the entire dataset as a table
st.header("Dataset")
st.dataframe(df)  # Displaying the dataset in an interactive table

# Adding a horizontal line as a separator
st.markdown("---")

# Reiterating developer credits at the bottom of the app
st.markdown("### Developed by Helio Henrique (https://github.com/heliohenriquehfilho)")