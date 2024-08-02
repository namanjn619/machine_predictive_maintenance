
# Machine Predictive Maintenance

Welcome, to the Machine Predictive Maintenance project, an innovative Python-based classification initiative designed to predict machine failures and identify the specific type of failure. In an industrial setting, timely and accurate prediction of machine failures is crucial for maintaining operational efficiency and reducing downtime. This project leverages advanced machine learning techniques to achieve this goal, providing valuable insights and actionable predictions.

he Machine Predictive Maintenance project not only showcases the power of machine learning in predictive maintenance but also emphasizes the importance of data visualization and real-time analytics. By predicting machine failures and identifying their causes, this project aims to enhance operational efficiency, reduce unexpected downtime, and support proactive maintenance strategies.

Explore the project to see the detailed analysis, model comparisons, and real-time prediction capabilities. Your journey through this project will demonstrate the practical application of machine learning in industrial maintenance and the significant impact of data-driven decision-making.

## Authors

- [Naman Jain](https://www.github.com/namanjn619)

  
## 🚀 About Me
I am Naman Jain, currently pursuing my M.Tech in Data Science at Delhi Technological University, New Delhi. With a solid foundation in Computer Engineering from Arya College of Engineering and IT, Jaipur, I have developed a keen interest in machine learning, deep learning, and data analytics.

My journey in the tech world includes practical experience as a Software Engineer at APBundle Technologies, where I honed my skills in ReactJS, NodeJS, and Redux, and as a Software Engineer Intern at WisdmLabs, focusing on PHP, WordPress, and MySQL. My technical expertise spans across various programming languages like Python, C++, and JavaScript, and I am proficient in using tools such as Docker, Git, and Power BI.

In my latest project, "Machine Predictive Maintenance," I have utilized machine learning algorithms to predict machine failures and identify specific failure types. This project not only highlights my ability to develop robust machine learning models but also showcases my proficiency in data visualization and analytics using Streamlit and Power BI.

  
## Features

- Model Comparison: We have evaluated and compared the results of the aforementioned machine learning models to determine the most effective one for predicting machine failures. This comparison is based on key performance metrics such as accuracy, precision, recall, and F1-score.
- Live Prediction Page: Utilizing the best-performing model, we have created a live prediction page. This feature allows users to input new data and receive real-time predictions about the machine's maintenance status, enhancing decision-making and proactive maintenance efforts.
- Exploratory Data Analysis (EDA) and Visualizations: Comprehensive EDA has been conducted to uncover patterns and insights from the data. Various graphs and visualizations accompany the EDA, providing a deeper understanding of the factors influencing machine failures.
- Power BI Dashboard: For advanced data analytics and interactive exploration, we have developed a Power BI dashboard. This dashboard offers an intuitive interface to analyze trends, compare model performances, and monitor machine health metrics dynamically.


## Stack
- Programming Languages: Python
- Libraries: Pandas, NumPy, Scikit-learn, Streamlit
- Visualization Tools: Matplotlib, Seaborn, Power BI
- Machine Learning Algorithms: Logistic Regression, Decision Tree, Random Forest, Support Vector Machine
  
## Pages and Screenshots
### Home Page
In this project, we aim to predict whether a machine is in a state of failure and, if so, identify the specific type of failure. The types of failures considered are:
- Heat Dissipation Failure
- Power Failure
- Overstrain Failure
- Tool Wear Failure

To accomplish this, we have implemented and compared the performance of four machine learning algorithms:
- Logistic Regression
- Support Vector Machine (SVM)
- Random Forest
- Decision Tree
- 
![Home](https://github.com/namanjn619/machine_predictive_maintenance/blob/master/Images/Screenshot%20(14).png)


### Dataset Used
The dataset contains 9,973 entries with 9 columns, each representing various attributes related to machine operations and failure status.
Columns and Data Types
- Type (object): Indicates the type of machine or operation.
- Air temperature [C] (float64): The ambient air temperature in degrees Celsius.
- Process temperature [C] (float64): The temperature of the process in degrees Celsius.
- Rotational speed [rpm] (int64):The rotational speed of the machine in revolutions per minute.
- Torque [Nm] (float64):The torque applied by the machine in Newton-meters.
- Tool wear [min] (int64): The tool wear time in minutes.
- Target (int64): A binary indicator (0 or 1) of whether the machine is in a failure state.
- Failure Type (object):Specifies the type of failure if the machine is in a failure state (e.g., Heat Dissipation Failure, Power Failure, etc.).
- Temperature Difference [C] (float64):The difference in temperature between the process and the air.
![Dataset](https://github.com/namanjn619/machine_predictive_maintenance/blob/master/Images/Screenshot%20(15).png)


### Machine Learning Models

![Machine Learning Models](https://github.com/namanjn619/machine_predictive_maintenance/blob/master/Images/Screenshot%20(16).png)


### Results Comparision
![Result Comparision](https://github.com/namanjn619/machine_predictive_maintenance/blob/master/Images/Screenshot%20(17).png)
### Machine Predictive Classification
Predictive Maintenance project allows users to input various parameters to predict the maintenance status of a machine. The fields include the operational load type of the machine, which can be categorized as Low (L), Medium (M), or High (H). Users can specify the Rotational Speed of the machine's components, ranging from 1000 to 3000 rpm, and the Torque, which is the force causing rotation, with values between 0 and 100 Nm.

The Air Temperature surrounding the machine, which ranges from 0 to 100 °C, can also be input, as well as the Process Temperature, the temperature at which the machine’s process operates, also within the 0 to 100 °C range. The Tool Wear parameter measures the amount of wear the tool experiences over time, with a range from 0 to 300 minutes. Additionally, the Temperature Difference field captures the difference between the process temperature and the air temperature, with values from 0 to 20 °C.
![Machine Predictive Classification](https://github.com/namanjn619/machine_predictive_maintenance/blob/master/Images/Screenshot%20(18).png)
### Prediction Page

![Prediction Page](https://github.com/namanjn619/machine_predictive_maintenance/blob/master/Images/Screenshot%20(19).png)
### Data Visualization Page
Data visualization plays a crucial role in the Machine Predictive Maintenance project, transforming complex data into intuitive graphical representations that facilitate better understanding and decision-making. By leveraging various visualization techniques, the project presents key insights into the machine's operational parameters and their impact on maintenance needs. For instance, scatter plots, histograms, and line graphs are used to illustrate the relationships and distributions of features such as rotational speed, torque, air temperature, process temperature, tool wear, and temperature difference. These visualizations help in identifying patterns and anomalies that may indicate potential failures.
![Data Visualization Page](https://github.com/namanjn619/machine_predictive_maintenance/blob/master/Images/Screenshot%20(20).png)
### Viualization
Insights from the Visualization:
- Rotational Speed and Torque are highly co-related
- Air and Process Temprature are also Highly Co-related.
- We can see the failures are majory due to high or low values of variables.
![Viualization](https://github.com/namanjn619/machine_predictive_maintenance/blob/master/Images/Screenshot%20(21).png)
### About Page
The Machine Predictive Maintenance project aims to predict machine failures and identify the type of failure, enhancing operational efficiency and reducing downtime. This project utilizes various machine learning algorithms including Logistic Regression, Decision Tree, Random Forest, and Support Vector Machine to achieve high accuracy in predictions.
![About](https://github.com/namanjn619/machine_predictive_maintenance/blob/master/Images/Screenshot%20(22).png)


# Thank you For Visiting!!
