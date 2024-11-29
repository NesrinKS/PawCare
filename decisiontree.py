def predictsss(pet,pc,pcc,ba,bgr,bu,sc,sod):
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import LabelEncoder
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.metrics import accuracy_score, classification_report

    # Step 1: Load the CSV file
    df = pd.read_csv('pet.csv')

    # Step 2: Preprocess the data
    # Create a dictionary of LabelEncoders
    encoders = {column: LabelEncoder().fit(df[column]) for column in df.columns}

    # Transform the data using the encoders
    for column in df.columns:
        df[column] = encoders[column].transform(df[column])

    # Step 3: Split the dataset into features and target variable
    X = df.drop('PredictedHealthConditionsLevel', axis=1)
    y = df['PredictedHealthConditionsLevel']

    # Step 4: Train the Decision Tree Classifier
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    clf = DecisionTreeClassifier()
    clf.fit(X_train, y_train)

    # Step 5: Evaluate the model
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    # Print results
    print(f'Accuracy: {accuracy}')
    print('Classification Report:')
    print(report)

    # Step 6: Predict for the new input data
    input_data = {
        'Pet': pet,
        'SleepingPatterns': pc,
        'ActivityPatterns': pcc,
        'Exercise': ba,
        'Diet': bgr,
        'CommonHealthIssues': bu,
        'BehavioralPattern': sc,
        'ObedienceLevel': sod
    }

    # Convert the input data to DataFrame
    input_df = pd.DataFrame([input_data])

    # Encode the input data using the same encoders
    for column in input_df.columns:
        input_df[column] = encoders[column].transform(input_df[column])

    # Predict the output
    prediction = clf.predict(input_df)

    # Decode the prediction
    predicted_health_conditions_level = encoders['PredictedHealthConditionsLevel'].inverse_transform(prediction)
    print(f'Predicted Health Conditions Level: {predicted_health_conditions_level[0]}')

    return predicted_health_conditions_level
