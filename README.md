# Used Car Price Prediction System

## Project Overview

The Used Car Price Prediction System is a Machine Learning application that predicts the resale value of a used car based on its specifications. The model is trained using historical car data and provides an estimated selling price based on user inputs.

## Features

- Predicts used car selling price
- Uses Machine Learning for accurate estimation
- Interactive Streamlit web interface
- Real-time price prediction
- User-friendly input form

## Dataset

The project uses the CarDekho Used Car Dataset containing:

- Car Name
- Year
- Present Price
- Kilometers Driven
- Fuel Type
- Seller Type
- Transmission
- Owner
- Selling Price (Target Variable)

## Machine Learning Workflow

1. Data Collection
2. Data Preprocessing
3. Feature Encoding
4. Train-Test Split
5. Model Training using Random Forest Regression
6. Model Evaluation
7. Model Deployment using Streamlit

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-Learn
- Random Forest Regression
- Streamlit
- Joblib

## Project Structure

```text
UsedCarPricePrediction/
│
├── car data.csv
├── model.py
├── app.py
├── car_price_model.pkl
├── README.md
└── venv/
```

## Installation

Install required libraries:

```bash
pip install pandas numpy scikit-learn streamlit joblib
```

## Run the Project

### Train the Model

```bash
python model.py
```

### Launch the Application

```bash
python -m streamlit run app.py
```

## Sample Input

- Car Name: City
- Year: 2020
- Present Price: 8
- Kilometers Driven: 30000
- Fuel Type: Petrol
- Seller Type: Dealer
- Transmission: Manual
- Owner: 0

## Output

Predicted Selling Price: ₹6.5 Lakhs (approx.)

## Future Enhancements

- Better UI design
- Additional ML models for comparison
- Model performance dashboard
- Deployment on cloud platforms

## Author

Haripriya Reddy