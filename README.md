# Laptop price analysis and price prediction
This project builds a machine learning model to predict TCS close price. It involves data preprocessing, save piple line data, and save clean data for model training, evaluation, create a pipeline and Streamlit deployment.

---
## Project Structure

```
├── Data/                  
├── notebook/
|    ├── cleaning.ipynb          
│    └── Model_Train.ipynb       
├── Model Deploy/
│   ├── app.py              
│   └── model.pkl           
├── requirements.txt          
├── README.md      
├── .gitignore 
└── Report file
```

## Objective

To predict TCS stock close price.
---

## Features Used

- Open
- Close 
- Volume		 
- Year		 
- Month		 
- Day    
---

##  Technologies Used

- Python (Pandas, NumPy, seaborn, matplotlib, Scikit-learn, Imbalanced-learn)
- Streamlit (for deployment)
- Joblib (for model saving/loading)

---

## Model & Evaluation

- **Model Used:** e.g., RandomForestRegressor / XGBoostRegressor /StackingRegressor
- **Evaluation Metrics:**
  - R2 score 
  - Adjusted r2, Mean absolute error, mean squared error, Cross val score

- **Issue Solved:** Fix Over fitting and analyse Tcs close price.

---

## How to Run the App

1. Clone the repository:
   ```bash
   git clone https://github.com/Priyanshu-techp/TCS-stck-close-proce-prediction.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:
   ```bash
   streamlit run "Model_deploying/app.py"
   ```
---

## Deploy link
[Streamlit app link](https://tcs-close-price-prediction.streamlit.app/)

## Results

- **Best r2-score:** ~0.99  
- **Overall Accuracy:** ~0.99
- **R2 gap:** ~0.003  
- **Fix over fitting**

---

## Author

**Priyanshu Pandey**  
Diploma in Automation & Robotics  
Aspiring Data Scientist  
[LinkedIn Profile](https://www.linkedin.com/in/priyanshu-pandey-672767320)

