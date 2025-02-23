# 


import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    st.set_page_config(page_title="Streamlit Web App", layout="wide")
    
    st.markdown(
    """
    <h1 style='text-align: left; 
               font-family: cursive; 
               font-size: 55px; 
               font-weight: bold; 
               color: #b366ff;'>
    💨 SweepIt Easy
    </h1>
    """, 
    unsafe_allow_html=True
    )
    
    st.write("Quickly refine, reshape, visualize, and convert your datasets with ease.")
    
    # Sidebar customization
    with st.sidebar:
        st.markdown(
            """
            <style>
                .sidebar .sidebar-content {
                    background-color: #f0f0f5;
                    padding: 20px;
                    border-radius: 10px;
                    transition: all 0.3s ease;
                }
                .sidebar .sidebar-content:hover {
                    background-color: #e0e0eb;
                }
                .sidebar select:hover, .sidebar button:hover {
                    cursor: pointer;
                }
            </style>
            """, unsafe_allow_html=True
        )
        st.title("Customize View")
    
    # File uploader
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("### Dataset Preview")
        st.dataframe(df.head())
        
        # Select column for visualization
        numerical_cols = df.select_dtypes(include=['number']).columns
        categorical_cols = df.select_dtypes(include=['object']).columns
        
        chart_type = st.sidebar.selectbox("Select Chart Type", ["Scatter Plot", "Bar Chart", "Line Chart", "Histogram", "Box Plot"], key='chart_type')
        
        if chart_type == "Scatter Plot":
            x_axis = st.sidebar.selectbox("Select X-axis", numerical_cols, key='x_axis_scatter')
            y_axis = st.sidebar.selectbox("Select Y-axis", numerical_cols, key='y_axis_scatter')
            fig = px.scatter(df, x=x_axis, y=y_axis, title=f"{chart_type} of {x_axis} vs {y_axis}")
            st.plotly_chart(fig)
        
        elif chart_type == "Bar Chart":
            x_axis = st.sidebar.selectbox("Select X-axis (Categorical)", categorical_cols, key='x_axis_bar')
            y_axis = st.sidebar.selectbox("Select Y-axis (Numerical)", numerical_cols, key='y_axis_bar')
            fig = px.bar(df, x=x_axis, y=y_axis, title=f"{chart_type} of {x_axis} vs {y_axis}")
            st.plotly_chart(fig)
        
        elif chart_type == "Line Chart":
            x_axis = st.sidebar.selectbox("Select X-axis (Numerical)", numerical_cols, key='x_axis_line')
            y_axis = st.sidebar.selectbox("Select Y-axis (Numerical)", numerical_cols, key='y_axis_line')
            fig = px.line(df, x=x_axis, y=y_axis, title=f"{chart_type} of {x_axis} vs {y_axis}")
            st.plotly_chart(fig)
        
        elif chart_type == "Histogram":
            column = st.sidebar.selectbox("Select Column", numerical_cols, key='hist_column')
            fig = px.histogram(df, x=column, title=f"{chart_type} of {column}")
            st.plotly_chart(fig)
        
        elif chart_type == "Box Plot":
            column = st.sidebar.selectbox("Select Column", numerical_cols, key='box_column')
            fig = px.box(df, y=column, title=f"{chart_type} of {column}")
            st.plotly_chart(fig)
    
    else:
        st.write("Upload a CSV file to get started!")
        
if __name__ == "__main__":
    main()
