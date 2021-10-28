import streamlit as st
import numpy as np
import pickle
import pandas as pd

model = pickle.load(open("Home_Loan.pkl","rb"))

def main():
    st.title("Home Loan Prediction")
    html_temp = """
    <div style="background-color:Aquamarine;padding:5px">
    <h2 style="color:white;text-align:center;">Enter the following details to check customer eligibility </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Gender = st.text_input("Gender","Choose 0 if Female Else 1 if Male")
    Married = st.text_input("Married","Choose 0 if No Else 1 if Yes")
    Education = st.text_input("Education","Choose 0 if Graduate Else 1 if Not Graduate")
    Self_Employed = st.text_input("Self_Employed","Choose 0 if No Else 1 if Yes")
    ApplicantIncome = st.text_input("ApplicantIncome","Enter Applicant Income in Thousands if any")
    CoapplicantIncome = st.text_input("CoapplicantIncome","Enter Co-Applicant Income in Thousands if any")
    LoanAmount = st.text_input("LoanAmount","Enter Loan Amount in thousands")
    Loan_Amount_Term = st.text_input("Loan_Amount_Term","Enter Loan term in Months")
    Credit_History = st.text_input("Credit_History","Choose 0 if No Credit History Else 1 if Yes")
    Property_Area_Rural = st.text_input("Property_Area_Rural","If Property_Area_Rural is 1 then Property_Area_Semiurban and Urban is 0")
    Property_Area_Semiurban = st.text_input("Property_Area_Semiurban","If Property_Area_Semiurban is 1 then Property_Area_Rural and Urban is 0")
    Property_Area_Urban = st.text_input("Property_Area_Urban","If Property_Area_urban is 1 then Property_Area_Rural and Semiurban is 0")
    
    inputs = [[Gender,Married,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area_Rural,Property_Area_Semiurban,Property_Area_Urban]] #our inputs
    result=""
    if st.button("Predict"): #making and printing our prediction
        result = model.predict(inputs)
    if result == 0:
        st.success('Sorry ! You are not eligible for Loan {}'.format(result))
    elif result ==1:
        st.success('Congrats ! You are eligible for Loan {}'.format(result))
        
if __name__=="__main__":
    main()
