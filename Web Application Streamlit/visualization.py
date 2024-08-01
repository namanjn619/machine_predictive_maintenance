import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_data():
    data = pd.read_csv("df_visualization.csv")
    return data

data = load_data()

def show_visualization_page():
    st.title("Data Visualization")
    st.markdown("""
    Data visualization plays a crucial role in the Machine Predictive Maintenance project, transforming complex data into intuitive graphical representations that facilitate better understanding and decision-making. By leveraging various visualization techniques, the project presents key insights into the machine's operational parameters and their impact on maintenance needs. For instance, scatter plots, histograms, and line graphs are used to illustrate the relationships and distributions of features such as rotational speed, torque, air temperature, process temperature, tool wear, and temperature difference. These visualizations help in identifying patterns and anomalies that may indicate potential failures.

    Moreover, advanced visualization tools like Power BI are employed to create interactive dashboards, allowing users to explore the data dynamically. These dashboards offer a comprehensive view of the machine's performance metrics and failure predictions, making it easier to monitor trends and pinpoint critical factors contributing to machine failures. The integration of exploratory data analysis (EDA) techniques further enhances the visualizations, providing deeper insights into the data through detailed statistical summaries and correlations. Overall, the data visualization component of this project not only aids in the accurate prediction of machine maintenance status but also empowers users with actionable insights for optimizing machine performance and minimizing downtime.
    """)
    # st.subheader("Dataset")
    # st.write(data)

    main_chart_type = st.sidebar.selectbox(
        "Select Main Chart Type",
        ["Matplotlib/Seaborn Charts"]
    )

    if main_chart_type == "Matplotlib/Seaborn Charts":
        
        chart_type = st.sidebar.selectbox(
            "Select Chart Type",
            ["Pair Plot", "Violen Plot", "Percentage of Failure", "Corelation Heatmap", "Features on Basis of Type of Failure", "Skewness", ]
        )

        if chart_type == "Corelation Heatmap":
            st.title("Corelation Heatmap")
            st.subheader("Insights from the Visualization: ")
            st.write("As mentioned before, there is high correlation between process temperature and air temperature, and between rotational speed and torque.")
            numeric_dataset = data.select_dtypes(include=['number'])
            correlation_matrix = numeric_dataset.corr()
            plt.figure(figsize=(8, 8))
            fig = sns.heatmap(correlation_matrix.corr(), annot=True)
            st.pyplot(plt.gcf())

        elif chart_type == "Pair Plot":
            st.title("Pair Plot")
            st.subheader("Insights from the Visualization: ")
            st.write("1) Rotational Speed and Torque are highly co-related")
            st.write("2) Air and Process Temprature are also Highly Co-related.")
            st.write("3) We can see the failures are majory due to high or low values of variables.")

            x_column = st.sidebar.selectbox("X_Column", data.columns[1:-1])
            y_column = st.sidebar.selectbox("Y_Column", data.columns[1:-1])
            
            fig = sns.pairplot(data, x_vars=x_column, y_vars=y_column, hue="Target", height=3, aspect=3, palette='husl',)
            
            st.pyplot(fig)

        elif chart_type == "Features on Basis of Type of Failure":
            st.title("Features on Basis of Type of Failure")
            st.subheader("Insights from the Visualization: ")
            st.write("1) Rotational Speed and Torque are highly co-related")
            fig, ax = plt.subplots(1,2, figsize=[22,8])
            plt.title('Rot. Speed vs Torque wrt Failure Type')
            sns.scatterplot(data=data, x='Rotational speed [rpm]', y='Torque [Nm]', hue='Failure Type', palette=['#E9C0CB', '#39A692', '#976EBD', '#ACBF5C', '#DF8B4E'], ax=ax[0])
            sns.scatterplot(data=data[data['Target'] == 1], x='Rotational speed [rpm]', y='Torque [Nm]', hue='Failure Type', palette=['#39A692', '#976EBD', '#ACBF5C', '#DF8B4E'], ax=ax[1])

            ax[0].set_title('Including class no failure')
            ax[1].set_title('Excluding class no failure')
            st.pyplot(fig)

        elif chart_type == "Skewness":
            st.title("Skewness")
            st.subheader("Insights from the Visualization: ")
            st.write("Rotational speed is positively skewed. From the boxplots we can see that 'Rotational speed' and 'Torque' have outliers.")
            fig, axes = plt.subplots(2, 5, figsize=[25,10])
            j = 0
            colors = ['#E1728F', '#409E7D']

            for i in ['Air temperature [C]', 'Process temperature [C]', 'Rotational speed [rpm]', 'Torque [Nm]', 'Tool wear [min]']:
                sns.histplot(data=data, x=i, kde=True, ax=axes[0,j], hue='Target', palette=colors)
                sns.boxplot(data=data, x=i, ax=axes[1,j], palette=['#976EBD'])
                j+=1

            st.pyplot(fig)
        
        elif chart_type == "Violen Plot":
            st.title("Violen Plot")
            st.subheader("Insights from the Visualization: ")
            st.write("It can be seen that most failures are triggered for much lower or much higher values than the Mean ")

            fig, axes = plt.subplots(1, 2, figsize=(14, 6))
            sns.violinplot(x="Target", y="Rotational speed [rpm]", data=data, palette='husl', ax=axes[0])
            axes[0].set_title(f'Violin Plot of {"Rotational speed [rpm]"} vs {"Target"}')

            sns.violinplot(x="Target", y="Torque [Nm]", data=data, palette='husl', ax=axes[1])
            axes[1].set_title(f'Violin Plot of {"Torque [Nm]"} vs {"Target"}')
            
            st.pyplot(plt)
            plt.close()

        elif chart_type == "Percentage of Failure":
            st.title("Percentage of Failure and Non Failure")
            st.subheader("Insights from the Visualization: ")
            st.write("The dataset is highly Unbalanced ")

            labels = 'No Failure', 'Failure'
            counts = data['Target'].value_counts()
            explode = (0, 0.1)
            fig1, ax1 = plt.subplots()
            ax1.pie(counts, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
            ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

            st.pyplot(fig1)

            
            


    
    