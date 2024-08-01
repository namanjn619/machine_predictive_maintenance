import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder, MinMaxScaler, RobustScaler

# Loading Model -----------------------------------
def load_target_model():
    with open('target_model.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

def load_failure_type_model():
    with open('failure_type_model.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

target_model = load_target_model()
failure_type_model = load_failure_type_model()

# Loading Scalers -----------------------------------

with open('scaler1.pkl', 'rb') as f:
    scaler1 = pickle.load(f)

with open('scaler2.pkl', 'rb') as f:
    scaler2 = pickle.load(f)

# ------------------------------------------------
feature_columns = ['Temperature Difference [C]', 'Type', 'Rotational speed [rpm]', 
                   'Torque [Nm]', 'Air temperature [C]', 'Process temperature [C]', 
                   'Tool wear [min]']

# Main Function -----------------------------------
def show_prediction_page():
    st.title("Machine Predictive Maintenance Classification")
    st.markdown("""
         Predictive Maintenance project allows users to input various parameters to predict the maintenance status of a machine. The fields include the operational load type of the machine, which can be categorized as Low (L), Medium (M), or High (H). Users can specify the **Rotational Speed** of the machine's components, ranging from 1000 to 3000 rpm, and the **Torque**, which is the force causing rotation, with values between 0 and 100 Nm. 

        The **Air Temperature** surrounding the machine, which ranges from 0 to 100 °C, can also be input, as well as the **Process Temperature**, the temperature at which the machine’s process operates, also within the 0 to 100 °C range. The **Tool Wear** parameter measures the amount of wear the tool experiences over time, with a range from 0 to 300 minutes. Additionally, the **Temperature Difference** field captures the difference between the process temperature and the air temperature, with values from 0 to 20 °C.

        By inputting these parameters, users can predict whether the machine is likely to fail and identify the type of failure, such as Heat Dissipation Failure, Power Failure, Overstrain Failure, or Tool Wear Failure. This functionality helps in proactive maintenance, ensuring operational efficiency and reducing downtime.
    """)
    st.header("Input Features")
    # Taking Inputs ------------------------------------------------
    type_input = st.selectbox("Type | Values - [L, M, H]", options=['L','M','H'], index=0) # Ordinal Encoded

    rot_speed = st.number_input("Rotational speed [rpm] | Range - [1000-3000]", min_value=1000.0, max_value=3000.0, value=1000.0, step=50.0) # Scaling Type-1
    torque = st.number_input("Torque [Nm] [0-100]", min_value=0.0, max_value=100.0, value=0.0, step=1.0) # Scaling Type-1

    air_temp = st.number_input("Air temperature [C] | Range - [0-100]", min_value=0.0, max_value=100.0, value=0.0, step=1.0) # Scaling Type-2
    proc_temp = st.number_input("Process temperature [C] | Range - [0-100]", min_value=0.0, max_value=100.0, value=0.0, step=1.0) # Scaling Type-2
    tool_wear = st.number_input("Tool wear [min] | Range - [0-300]", min_value=0.0, max_value=300.0, value=0.0, step=5.0) # Scaling Type-2

    temp_diff = st.number_input("Temperature Difference [C] | Range - [0-20]", min_value=0.0, max_value=20.0, value=0.0, step=1.0) # No preprocessing Required
    
    

    # Preprocessing ------------------------------------------------
     # 1) Ordinal Encoding
    if type_input == 'L':
        type_input = 0
    elif type_input == 'M':
        type_input = 1
    elif type_input == 'H':
        type_input = 2

    # Array Converstion------------------------------------------------
    input_data = np.array([[temp_diff, type_input, rot_speed, torque, air_temp, proc_temp, tool_wear]])
    input_df = pd.DataFrame(input_data, columns=feature_columns)

     # 2) Scaling Type - 1
    columns1 = ['Rotational speed [rpm]', 'Torque [Nm]']
    scaling1 = scaler1.transform(input_df[columns1])
    scaling1 = pd.DataFrame(scaling1, columns=columns1)
    input_df.drop(columns1, axis=1, inplace=True)
    input_df = pd.concat([input_df, scaling1], axis=1)
    
    # 3) Scaling Type - 2
    columns2 = ['Air temperature [C]', 'Process temperature [C]', 'Tool wear [min]']
    scaling2 = scaler2.transform(input_df[columns2])
    scaling2 = pd.DataFrame(scaling2, columns=columns2)
    input_df.drop(columns2, axis=1, inplace=True)
    input_df = pd.concat([input_df, scaling2], axis=1)


    # When Predict Button Clicked------------------------------------------------
    if st.button("Predict"):
        # Model Prediction------------------------------------------------
        target_prediction = target_model.predict(input_df)
        failure_type_prediction = failure_type_model.predict(input_df)
    
        st.subheader("Prediction")

        # Printing Target(Failure/No Failure) ------------------------------------------------
        name_of_target = ""
        if(int(target_prediction)) == 0:
            name_of_target = "No Failure"
        else:
            name_of_target = "Failure"
        
        st.write(f"Predicted Target: {name_of_target}")

        # Printing Failure Type------------------------------------------------
        name_of_failure_type = ""
        if(int(failure_type_prediction)) == 1:
            name_of_failure_type = "Power Failure"
        elif(int(failure_type_prediction)) == 2:
            name_of_failure_type = "Tool Wear Failure"
        elif(int(failure_type_prediction)) == 3:
            name_of_failure_type = "Overstrain Failure"
        elif(int(failure_type_prediction)) == 4:
            name_of_failure_type = "Heat Dissipation Failure"
        else:
            name_of_failure_type = "No Problem Exists"

        st.write(f"Predicted Failure Type: {name_of_failure_type}")

    # Running Streamlit ------------------------------------------------
    if __name__ == "__main__":
        st.run()

