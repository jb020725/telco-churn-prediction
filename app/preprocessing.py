import pandas as pd

MODEL_COLUMNS = [
    'SeniorCitizen', 'tenure', 'MonthlyCharges', 'TotalCharges', 
    'gender_Male', 'Partner_Yes', 'Dependents_Yes', 'PhoneService_Yes',
    'MultipleLines_No phone service', 'MultipleLines_Yes', 
    'InternetService_Fiber optic', 'InternetService_No',
    'OnlineSecurity_No internet service', 'OnlineSecurity_Yes',
    'OnlineBackup_No internet service', 'OnlineBackup_Yes',
    'DeviceProtection_No internet service', 'DeviceProtection_Yes',
    'TechSupport_No internet service', 'TechSupport_Yes',
    'StreamingTV_No internet service', 'StreamingTV_Yes',
    'StreamingMovies_No internet service', 'StreamingMovies_Yes',
    'Contract_One year', 'Contract_Two year', 'PaperlessBilling_Yes',
    'PaymentMethod_Credit card (automatic)', 'PaymentMethod_Electronic check',
    'PaymentMethod_Mailed check'
]

def preprocess_input(input_dict):
    data = {col: 0 for col in MODEL_COLUMNS}
    
    data['SeniorCitizen'] = int(input_dict.get('SeniorCitizen', 0))
    data['tenure'] = float(input_dict.get('tenure', 0))
    data['MonthlyCharges'] = float(input_dict.get('MonthlyCharges', 0))
    data['TotalCharges'] = float(input_dict.get('TotalCharges', 0))

    gender = input_dict.get('gender', 'Female')
    data['gender_Male'] = 1 if gender.lower() == 'male' else 0

    for feat in ['Partner', 'Dependents', 'PhoneService', 'PaperlessBilling']:
        key = f"{feat}"
        col = f"{feat}_Yes"
        data[col] = 1 if input_dict.get(key, False) else 0

    ml_value = input_dict.get('MultipleLines', 'No')
    data['MultipleLines_Yes'] = 1 if ml_value == 'Yes' else 0
    data['MultipleLines_No phone service'] = 1 if ml_value == 'No phone service' else 0

    internet = input_dict.get('InternetService', 'DSL').lower()
    data['InternetService_Fiber optic'] = 1 if internet == 'fiber optic' else 0
    data['InternetService_No'] = 1 if internet == 'no' else 0

    os_val = input_dict.get('OnlineSecurity', False)
    if os_val is True:
        data['OnlineSecurity_Yes'] = 1
    elif os_val is None or os_val == 'No internet service':
        data['OnlineSecurity_No internet service'] = 1

    ob_val = input_dict.get('OnlineBackup', False)
    if ob_val is True:
        data['OnlineBackup_Yes'] = 1
    elif ob_val is None or ob_val == 'No internet service':
        data['OnlineBackup_No internet service'] = 1

    dp_val = input_dict.get('DeviceProtection', False)
    if dp_val is True:
        data['DeviceProtection_Yes'] = 1
    elif dp_val is None or dp_val == 'No internet service':
        data['DeviceProtection_No internet service'] = 1

    ts_val = input_dict.get('TechSupport', False)
    if ts_val is True:
        data['TechSupport_Yes'] = 1
    elif ts_val is None or ts_val == 'No internet service':
        data['TechSupport_No internet service'] = 1

    stv_val = input_dict.get('StreamingTV', False)
    if stv_val is True:
        data['StreamingTV_Yes'] = 1
    elif stv_val is None or stv_val == 'No internet service':
        data['StreamingTV_No internet service'] = 1

    stm_val = input_dict.get('StreamingMovies', False)
    if stm_val is True:
        data['StreamingMovies_Yes'] = 1
    elif stm_val is None or stm_val == 'No internet service':
        data['StreamingMovies_No internet service'] = 1

    contract = input_dict.get('Contract', 'month-to-month').lower()
    data['Contract_One year'] = 1 if contract == 'one year' else 0
    data['Contract_Two year'] = 1 if contract == 'two year' else 0

    pay = input_dict.get('PaymentMethod', 'electronic check').lower()
    data['PaymentMethod_Credit card (automatic)'] = 1 if pay == 'credit card (automatic)' else 0
    data['PaymentMethod_Electronic check'] = 1 if pay == 'electronic check' else 0
    data['PaymentMethod_Mailed check'] = 1 if pay == 'mailed check' else 0

    df = pd.DataFrame([data], columns=MODEL_COLUMNS)
    return df
