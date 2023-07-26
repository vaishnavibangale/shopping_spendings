import pickle
import json
import numpy as np
import pandas as pd
import config

class Shopping:
    def __init__(self, CustomerID, Gender, Age, Annual_Income):
        print("*****INIT Function*****")
        self.CustomerID = CustomerID
        self.Gender = Gender
        self.Age = Age
        self.Annual_Income = Annual_Income

    def __load_saved_data(self):
        with open(config.MODEL_FILE_PATH, 'rb') as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH, 'r') as f:
            self.json_data = json.load(f)

    def predict_spendings(self):
        self.__load_saved_data()

        Gender = self.json_data['Gender'][self.Gender]
        test_data = {
            'CustomerID': [self.CustomerID],
            'Gender': [Gender],
            'Age': [self.Age],
            'Annual_Income ($)': [self.Annual_Income]  # Use the correct column name from the training data
        }

        test_df = pd.DataFrame(test_data)

        predict_spendings = np.around(self.model.predict(test_df)[0], 3)
        return predict_spendings
