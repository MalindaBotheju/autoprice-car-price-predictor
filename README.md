# AutoPrice: Intelligent Used Car Valuation 🚗💰

**Live Demo:** [AutoPrice Predictor](https://autoprice-car-price-prediction.uc.r.appspot.com)

## Overview
AutoPrice is an end-to-end Machine Learning web application designed to predict the market value of used cars. By analyzing historical car details and user inputs—such as brand, purchase year, kilometers driven, and fuel type—the application provides a fast, data-driven estimated price in real-time. 

The machine learning model was trained using a custom dataset and deployed as a highly available, production-ready web service using Google Cloud Platform (GCP).

## Features
* **Predictive Accuracy:** Powered by a robust Scikit-Learn machine learning model.
* **Intuitive UI:** A clean, responsive, and dark-themed user interface for seamless data entry.
* **Dynamic Inputs:** Users can customize predictions based on Car Brand, Year, Kilometers Driven, Fuel Type, Seller Type, Transmission, and Previous Owners.
* **Cloud Deployed:** Hosted on Google App Engine for reliable, 24/7 global access.

## Tech Stack
* **Machine Learning:** Python, Scikit-Learn, Pandas, Jupyter Notebook
* **Backend Framework:** Flask, Gunicorn
* **Frontend:** HTML, CSS
* **Deployment & Hosting:** Google Cloud Platform (GCP) App Engine

## Project Structure
* `car_price.ipynb` - The Jupyter Notebook containing data exploration, feature engineering, and model training.
* `app.py` - The main Flask server application that handles API routing and interacts with the ML model.
* `car_model.pkl` & `model_columns.pkl` - The serialized, pre-trained Machine Learning model and its mapped data columns.
* `app.yaml` - The configuration file for Google Cloud App Engine deployment.
* `requirements.txt` - The list of Python dependencies required to run the project.
* `templates/` - Contains the frontend HTML interface.

## How to Run Locally
If you would like to run this application on your own local machine, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/MalindaBotheju/autoprice-car-price-predictor.git
   cd autoprice-car-price-predictor

   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate

   ```


3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt

   ```


4. **Run the Flask application:**
   ```bash
   python app.py

   ```


5. **Open your browser:** Navigate to http://127.0.0.1:5000 to view the app.

   ---

*Developed by Malinda Botheju*