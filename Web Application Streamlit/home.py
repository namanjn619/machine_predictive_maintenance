import streamlit as st
import pandas as pd

def load_data():
    data = pd.read_csv("df_visualization.csv")
    return data
data = load_data()

def app():
    st.markdown("""
        <h1>Machine Predictive Maintenance</h1>
    """, unsafe_allow_html=True)
    st.write("Github Repository: https://github.com/namanjn619/machine_predictive_maintenance.git")
    st.subheader("Introduction")
    st.write("Welcome, to the Machine Predictive Maintenance project, an innovative Python-based classification initiative designed to predict machine failures and identify the specific type of failure. In an industrial setting, timely and accurate prediction of machine failures is crucial for maintaining operational efficiency and reducing downtime. This project leverages advanced machine learning techniques to achieve this goal, providing valuable insights and actionable predictions.")
    st.write("he Machine Predictive Maintenance project not only showcases the power of machine learning in predictive maintenance but also emphasizes the importance of data visualization and real-time analytics. By predicting machine failures and identifying their causes, this project aims to enhance operational efficiency, reduce unexpected downtime, and support proactive maintenance strategies.")
    st.write("Explore the project to see the detailed analysis, model comparisons, and real-time prediction capabilities. Your journey through this project will demonstrate the practical application of machine learning in industrial maintenance and the significant impact of data-driven decision-making.")
    st.subheader("Project Overview")
    st.write("In this project, we aim to predict whether a machine is in a state of failure and, if so, identify the specific type of failure. The types of failures considered are:")
    st.markdown("""
        <ul>
                <li>Heat Dissipation Failure</li>
                <li>Power Failure</li>
                <li>Overstrain Failure</li>
                <li>Tool Wear Failure</li>
        </ul>
    """, unsafe_allow_html=True)
    st.write("To accomplish this, we have implemented and compared the performance of four machine learning algorithms:")
    st.markdown("""
        <ul>
                <li>Logistic Regression</li>
                <li>Support Vector Machine (SVM)</li>
                <li>Random Forest</li>
                <li>Decision Tree</li>
        </ul>
    """, unsafe_allow_html=True)
    st.subheader("Key Features of Project")
    st.markdown("""
        <ol>
                <li><spam style='font-size:20px; font-weight: bold;'>Model Comparison:</spam>  We have evaluated and compared the results of the aforementioned machine learning models to determine the most effective one for predicting machine failures. This comparison is based on key performance metrics such as accuracy, precision, recall, and F1-score.</li>
                <li><spam style='font-size:20px; font-weight: bold;'>Live Prediction Page:</spam>  Utilizing the best-performing model, we have created a live prediction page. This feature allows users to input new data and receive real-time predictions about the machine's maintenance status, enhancing decision-making and proactive maintenance efforts.</li>
                <li><spam style='font-size:20px; font-weight: bold;'>Exploratory Data Analysis (EDA) and Visualizations:</spam>  Comprehensive EDA has been conducted to uncover patterns and insights from the data. Various graphs and visualizations accompany the EDA, providing a deeper understanding of the factors influencing machine failures.</li>
                <li><spam style='font-size:20px; font-weight: bold;'>Power BI Dashboard:</spam> For advanced data analytics and interactive exploration, we have developed a Power BI dashboard. This dashboard offers an intuitive interface to analyze trends, compare model performances, and monitor machine health metrics dynamically.</li>
        </ol>
    """, unsafe_allow_html=True)
    
    st.subheader("Data Set")
    st.write("The dataset contains 9,973 entries with 9 columns, each representing various attributes related to machine operations and failure status.")
    st.write(data)
    st.write("Columns and Data Types")
    st.markdown("""
        <ol>
                <li><spam style='font-size:20px; font-weight: bold;'>Type (object):</spam> Indicates the type of machine or operation.</li>
                <li><spam style='font-size:20px; font-weight: bold;'>Air temperature [C] (float64):</spam> The ambient air temperature in degrees Celsius.</li>
                <li><spam style='font-size:20px; font-weight: bold;'>Process temperature [C] (float64): </spam> The temperature of the process in degrees Celsius.</li>
                <li><spam style='font-size:20px; font-weight: bold;'>Rotational speed [rpm] (int64):</spam>The rotational speed of the machine in revolutions per minute.</li>
                <li><spam style='font-size:20px; font-weight: bold;'>Torque [Nm] (float64):</spam>The torque applied by the machine in Newton-meters.</li>
                <li><spam style='font-size:20px; font-weight: bold;'>Tool wear [min] (int64): </spam>The tool wear time in minutes.</li>
                <li><spam style='font-size:20px; font-weight: bold;'>Target (int64): </spam>A binary indicator (0 or 1) of whether the machine is in a failure state.</li>
                <li><spam style='font-size:20px; font-weight: bold;'>Failure Type (object):</spam>Specifies the type of failure if the machine is in a failure state (e.g., Heat Dissipation Failure, Power Failure, etc.).</li>
                <li><spam style='font-size:20px; font-weight: bold;'>Temperature Difference [C] (float64):</spam>The difference in temperature between the process and the air.</li>
        </ol>
    """, unsafe_allow_html=True)
    st.subheader("Machine Learning Models")
    st.markdown("""
        <ol>
                <li><spam style='font-size:20px; font-weight: bold;'>Logistic Regression : </spam>  Logistic Regression is a statistical method used for binary classification that models the probability of a target variable being in one of two categories. It estimates the relationship between one or more independent variables and the log-odds of the dependent variable using a logistic function. The output is a probability score that is converted into a binary outcome based on a threshold, typically 0.5. 
                    </br> 
                    <div style='background-color: white; color: black; display: inline-block; width: 280px; padding: 10px 0px 10px 30px; border-radius: 10px'> 
                        Training Accuracy    : 96.71 %
                        </br> 
                        Model Accuracy Score : 96.63 %
                    </div>
                </li>
                <li><spam style='font-size:20px; font-weight: bold;'>Decision Tree : </spam> A Decision Tree is a machine learning algorithm used for classification and regression tasks. It works by splitting the data into subsets based on the most significant feature values, forming a tree-like structure of decisions. Each internal node represents a test on an attribute, each branch represents the outcome of the test, and each leaf node represents a class label (in classification) or a continuous value (in regression).
                    </br> 
                    <div style='background-color: white; color: black; display: inline-block; width: 280px; padding: 10px 0px 10px 30px; border-radius: 10px'> 
                        Training Accuracy    : 100.0 %
                        </br> 
                        Model Accuracy Score : 97.65 %
                    </div>
                </li>
                <li><spam style='font-size:20px; font-weight: bold;'>Random Forest : </spam> A Random Forest is an ensemble learning method that builds multiple decision trees during training and merges their results to improve accuracy and control over-fitting. It randomly selects subsets of features and samples to build each tree, ensuring diversity among the trees. The final prediction is made by averaging the predictions (for regression) or taking the majority vote (for classification) from all the trees in the forest.
                    </br> 
                    <div style='background-color: white; color: black; display: inline-block; width: 280px; padding: 10px 0px 10px 30px; border-radius: 10px'> 
                        Training Accuracy    : 100.0 %
                        </br> 
                        Model Accuracy Score : 98.45 %
                    </div>
                </li>
                <li><spam style='font-size:20px; font-weight: bold;'>Support Vector Machine : </spam> Support Vector Machine (SVM) is a supervised machine learning algorithm used for classification and regression tasks. It works by finding the hyperplane that best separates data points of different classes in the feature space. SVM is effective in high-dimensional spaces and is known for its robustness to overfitting, especially in cases with clear margin of separation.
                    </br> 
                    <div style='background-color: white; color: black; display: inline-block; width: 280px; padding: 10px 0px 10px 30px; border-radius: 10px'> 
                        Training Accuracy    : 96.53 %
                        </br> 
                        Model Accuracy Score : 96.95 %
                    </div>
                </li>
        </ol>
    """, unsafe_allow_html=True)
    st.subheader("Results")
    st.write("In the Machine Predictive Maintenance project, we evaluated the performance of four machine learning models: Logistic Regression, Decision Tree, Random Forest, and Support Vector Machine.")
    st.write("Among these models, the Random Forest model achieved the highest accuracy score of 98.45%, making it the best-performing model for predicting machine failure and identifying the specific type of failure. This superior performance can be attributed to Random Forest's ability to handle complex datasets and its robustness in minimizing overfitting through the aggregation of multiple decision trees. Therefore, for live predictions and maintenance status updates, the Random Forest model will be employed due to its exceptional accuracy and reliability.")
    data1 = {
        'Model': ['Logistic Regression', 'Decision Tree', 'Random Forest', 'Support Vector Machine'],
        'Accuracy Score': [96.63, 97.65, 98.45, 96.95]
    }
    df = pd.DataFrame(data1)

    # Display dataframe
    st.dataframe(df)