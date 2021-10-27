import streamlit as st
import numpy as np
import pickle
import pandas as pd

model = pickle.load(open("Home_Loan.pkl","rb"))

def main():
    st.title("Home Loan Prediction")
    Gender = st.text_input("Gender","Choose 0 if Female Else 1")
    Married = st.text_input("Married","Choose 0 if No Else 1")
    Education = st.text_input("Education","Choose 0 if Graduate Else 1")
    Self_Employed = st.text_input("Self_Employed","Choose 0 if No Else 1")
    ApplicantIncome = st.text_input("ApplicantIncome","Choose salary between(150-81000)")
    CoapplicantIncome = st.text_input("CoapplicantIncome","Choose salary between(0.0-41667.0)")
    LoanAmount = st.text_input("LoanAmount","Choose Loan Amount Between (0-900)")
    Loan_Amount_Term = st.text_input("Loan_Amount_Term","Choose Loan Term Between(12.0-480.0)")
    Credit_History = st.text_input("Credit_History","Choose 0 if No Else 1")
    Property_Area_Rural = st.text_input("Property_Area_Rural","If Property_Area_Rural is 1 then Property_Area_Semiurban and Urban is 0")
    Property_Area_Semiurban = st.text_input("Property_Area_Semiurban","If Property_Area_Semiurban is 1 then Property_Area_Rural and Urban is 0")
    Property_Area_Urban = st.text_input("Property_Area_Urban","If Property_Area_urban is 1 then Property_Area_Rural and Semiurban is 0")
    
    inputs = [[Gender,Married,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area_Rural,Property_Area_Semiurban,Property_Area_Urban]] #our inputs
    result=""
    if st.button("Predict"): #making and printing our prediction
        result = model.predict(inputs)
    if result == 0:
        st.success('Sorry!You are not eligible for Loan {}'.format(result))
    elif result ==1:
        st.success('Congrats!You are  eligible for Loan {}'.format(result))
        
if __name__=="__main__":
    main()
