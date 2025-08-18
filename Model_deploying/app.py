import pandas as pd 
import joblib
import streamlit as st

# load the model 
model = joblib.load('Model_deploying/model.pkl')


#  Set title
st.title('TCS stock  close price predict')


# create input feild
# numerical input
open = st.slider('Open', 0.0, 3000.00, 100.00)
# high = st.slider('High', 0.0, 3000.0, 100.0)
# low = st.slider('Low', 0.0, 3000.0, 100.0)
volume = st.slider('Volume', 0, 10000000, 10000)
year = st.slider('Year', 2000, 2030, 2014)
month = st.slider('Month', 1, 12, 5)
day = st.slider('Day', 1, 31, 15)

# Categorical input


input_dict = {
    'Open' : [open],
    'Volume' : [volume],
    'Year' : [year],
    'Month' : [month],
    'Day' : [day]
}

input_df = pd.DataFrame(input_dict)

if st.button('predict'):
    # Make prediction
    prediction = model.predict(input_df)
    # Display result
    st.success(f"Predicted Close Price: ₹ {prediction[0]:.2f}")

# how to run
# Streamlit run "Model_deploying/app.py"












