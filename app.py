import streamlit as st
from PIL import Image

# Page Configuration
st.set_page_config(page_title="Beijing Air Quality Analysis", layout="wide")

# Sidebar Navigation
page = st.sidebar.selectbox("Select a Page", [
    "Introduction",
    "Exploratory Data Analysis",
    "Model & Evaluation",
    "Conclusion"
])

# --- Page 1: Introduction ---
if page == "Introduction":
    st.title("📘 Project Overview: Beijing Air Quality Analysis")

    st.markdown("""
    This project focuses on analyzing air quality data collected from **12 monitoring sites across Beijing** between **March 2013 and February 2017**. The primary objective is to understand the behavior and interdependence of pollutants and meteorological variables and to predict **PM2.5 concentration** using machine learning techniques.

    ### 🔍 Project Objectives:
    - Understand the structure and challenges of real-world environmental datasets
    - Perform detailed **Exploratory Data Analysis (EDA)** to extract insights
    - Handle missing values, outliers, and skewed distributions
    - Build a robust and interpretable prediction model
    - Present the workflow and results through an interactive **Streamlit application**

    ### 📦 Dataset Description:
    The dataset contains hourly records of:
    - **Air pollutants**: PM2.5, PM10, SO2, NO2, CO, O3
    - **Weather data**: Temperature, Pressure, Dew Point, Rainfall, Wind Speed, Wind Direction
    - **Time details**: Year, Month, Day, Hour
    - **Station identifiers**: Station name and location

    With **420,768 rows and 19 columns**, this dataset combines multiple sources to support a holistic analysis of Beijing’s air quality.

    ### 🧾 Scope of Analysis:
    This project showcases how raw environmental data can be refined and modeled to create useful insights and predictive solutions. It involves the complete machine learning pipeline, from preprocessing and EDA to model selection, tuning, evaluation, and visualization.

    ### 📁 Data Loading:
    The original dataset (`combined_data.csv`) was created by merging site-specific files. It is structured, time-stamped, and rich in both pollutant and meteorological indicators, making it suitable for supervised learning tasks, particularly **regression models for PM2.5 prediction**.
    """)

# --- Page 2: Exploratory Data Analysis ---
elif page == "Exploratory Data Analysis":
    st.title("📊 Exploratory Data Analysis (EDA)")

    st.markdown("""
    The EDA phase focuses on inspecting data structure, summarizing its key characteristics, and visualizing important patterns. Here are the core insights derived from the data:

    ### 📐 Dataset Structure:
    - Total Records: **420,768 rows**
    - Total Features: **19 columns** (includes both numerical and categorical data)

    ### 🔢 Column Data Types:
    - Integer: year, month, day, hour, No
    - Float: PM2.5, PM10, SO2, NO2, CO, O3, TEMP, PRES, DEWP, RAIN, WSPM
    - Object: wd (wind direction), station, Location

    ### ❗ Missing Values:
    - PM2.5: 8,739 missing
    - PM10: 6,449 missing
    - CO: 20,701 missing
    - TEMP: 398, WSPM: 318
    - Others include small gaps in SO2, NO2, O3, etc.

    ### 🧮 Summary Statistics:
    - PM2.5 has a median of **55 µg/m³**, but can spike up to **999 µg/m³**.
    - CO values range broadly, peaking at **10,000 µg/m³**.
    - RAIN shows extreme skew and kurtosis, confirming rare but intense rainfall events.
    - TEMP ranges from **-19.9°C to 41.6°C**, highlighting seasonal diversity.

    ### 📊 Distribution Insights:
    - PM2.5, CO, SO2 are all **right-skewed**, indicating heavy pollution events are uncommon but extreme.
    - RAIN has a skewness of **30+** and kurtosis over **1300**, suggesting rare, sharp rainfall bursts.
    - These findings influenced our choice of imputation, transformation, and modeling strategies.

    ### 🖼️ Visual Representations:
    Below are key visual results from the EDA (located in Task 4/img1–img5):
    """)

    for i in range(1, 6):
        st.image(f"Task 4/img{i}.png", caption=f"Visualization {i}", use_column_width=True)

    st.markdown("""
    These charts demonstrate trends, skewness, missing value patterns, and variable correlations — laying a foundation for feature selection and model design.
    """)

# --- Page 3: Model & Evaluation ---
elif page == "Model & Evaluation":
    st.title("🤖 Model Selection & Evaluation")

    st.markdown("""
    Based on EDA insights, the **Random Forest Regressor** was chosen for modeling PM2.5 values. This decision was based on its ability to handle non-linearity, mixed data types, and outliers without requiring extensive scaling or transformations.

    ### ✅ Model Selection Rationale:
    - Captures nonlinear dependencies effectively
    - Performs well on structured datasets with minimal tuning
    - Resilient to noise and missing values

    ### 📉 Initial Model Performance:
    - **RMSE (Root Mean Squared Error)**: 0.1366
    - **R² Score**: 0.999997
    These scores indicate a highly accurate model with minimal prediction error.

    ### 🔍 Hyperparameter Tuning via GridSearchCV:
    - Parameters tested:
        - `n_estimators`: [50, 100]
        - `max_depth`: [10, 20]
        - `min_samples_split`: [2, 5]
    - 3-fold cross-validation over 8 combinations (total 24 fits)
    - **Best Parameters Identified**:
        - `n_estimators = 50`
        - `max_depth = 20`
        - `min_samples_split = 2`

    ### 🧪 Tuned Model Results:
    - **Tuned RMSE**: 0.1012
    - **Tuned R² Score**: 0.999998

    These improvements validate that even with a strong baseline, thoughtful tuning can further enhance performance and reduce generalization error.
    """)

# --- Page 4: Conclusion ---
elif page == "Conclusion":
    st.title("✅ Final Conclusion")

    st.markdown("""
    This project demonstrates how real-world environmental data can be transformed into valuable insights and predictive capabilities through a structured data science workflow.

    ### 📌 Key Achievements:
    - Merged and preprocessed large-scale multi-source data
    - Identified pollution patterns and anomalies using visual/statistical analysis
    - Built and optimized a Random Forest model achieving **very low RMSE and high R²**
    - Presented results through a clear, interactive **Streamlit app**

    ### 🧠 Skills Developed:
    - Data cleaning, imputation, and visualization
    - Pipeline-based model development and evaluation
    - Hyperparameter tuning with cross-validation
    - Streamlit web app creation for real-world presentation

    ### 🚀 Real-World Relevance:
    The tools and skills demonstrated here are directly applicable in domains like:
    - Environmental monitoring and forecasting
    - Health and safety risk analysis
    - Smart city development and pollution control policy planning

    ### 💡 Final Thoughts:
    This end-to-end project reinforced the importance of structured workflows in data science — from data handling to deployment. It also proved the value of combining statistical thinking with machine learning to build scalable, interpretable, and impactful solutions.
    """)

    st.success("You're now ready to explore or deploy your own data-driven solutions!")