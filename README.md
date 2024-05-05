# Device Price Prediction API

This repository contains the implementation of a Machine Learning model to predict the price range of mobile devices based on their specifications. The model is served through a FastAPI web application, providing a RESTful API for interacting with the prediction model.

## Overview

The project encompasses the entire workflow of a machine learning project, from exploratory data analysis (EDA) and feature engineering to model fitting and API deployment.

### Exploratory Data Analysis (EDA)

- **Balance**: The dataset is well-balanced across different price ranges.
- **Null Values**: Minimal null values, simplifying the preprocessing steps.
- **Variability**: High variability in the ranges of numerical values, suggesting diverse device specifications.
- **Correlations**: While most features show low intercorrelations, indicating they are informative, a notable exception is the high correlation between RAM and the price range.

### Feature Engineering

To enhance the model's performance, several feature engineering steps were considered:
- **Creation of New Features**: For example, combining screen height (`sc_h`) and screen width (`sc_w`) to create a new feature `screen_area`.
- **Categorization**: Transforming numerical features into categorical features, such as categorizing `ram` into four distinct categories.
- **Feature Scaling**: Normalizing data to ensure that numerical features contribute equally to model training.
- **Handling Null Values**: Dropping records with null values to maintain data quality.

For simplicity, this project implements feature scaling and null value removal.

### Model Fitting

Several machine learning models were evaluated, including:
- Random Forest
- Logistic Regression
- Support Vector Machine (SVM)
- XGBoost

The Support Vector Machine (SVM) model demonstrated superior performance, achieving an accuracy of 97% and an F1 score of 99%.

### FastAPI Implementation

The FastAPI framework is used to serve the machine learning model as a RESTful API, allowing for real-time predictions and device management. The key endpoints include:

- `POST /api/devices/`: Retrieve a list of all devices.
- `GET /api/devices/{id}`: Retrieve details of a specific device by ID.
- `POST /api/devices`: Add a new device entry.
- `POST /api/predict/{deviceId}`: Predict the price range for a specified device ID and update the device record.

## Getting Started

### Prerequisites

- FastAPI
- uvicorn

### Installation

Clone the repository and install the required packages:

```bash
git clone https://github.com/omarhassan97/DevicesProjec.git
cd DevicesProjec
pip install -r requirements.txt
```bash

### API
To run the server

```bash
uvicorn main:app --reload
```bash
This will start the server on http://127.0.0.1:8000, where you can access the API and view the automatically generated API documentation at http://127.0.0.1:8000/docs.






