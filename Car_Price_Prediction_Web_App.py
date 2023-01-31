# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 15:28:45 2023

@author: HP
"""

import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open('D:\Machine Learning with Python\Car Price Prediction using Lasso Regression\Trained_model.sav', 'rb'))

#creating a function for Prediction
def car_price_prediction(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    return prediction

def main():
    
    #giving a title
    st.title('Car Price Prediction Web App')
    
    #getting input from the user
    
    Year = st.text_input("Year")
    Present_price = st.text_input("Present Price")
    Kms_driven = st.text_input("Kilometers Driven")
    Fuel = st.text_input("Fuel Type : 0 -> Petrol; 1 -> Diesel; 2 -> CNG")
    Seller_type = st.text_input("Seller Type: 0 -> Dealer; 1 -> Individual")
    Transmission = st.text_input("Transmission Type: Manual -> 0; Automatic -> 1")
    Owner = st.text_input("Number of Owners till now : ")
    
    #code for prediction
    predicted_price = ''
    
    # getting the input data from the user
    if st.button('Diabetes Test Result : '):
        predicted_price = car_price_prediction([Year,Present_price,Kms_driven,Fuel,Seller_type,Transmission,Owner])
        
    st.success(predicted_price)
    

if __name__ == '__main__':
    main()