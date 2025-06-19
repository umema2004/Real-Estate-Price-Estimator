# 🏠 Real Estate Price Estimator

A machine learning project that predicts property prices in Pakistan using real estate listing data scraped from [Zameen.com](https://www.zameen.com/). The model is trained on structured property data, and the application is built using Streamlit for an interactive user experience.

## 📌 Project Overview

This project aims to estimate property prices based on features such as city, location, property type, number of bedrooms, bathrooms, and area size. It uses a regression model trained on cleaned listings data and is deployable as a lightweight web app.

---

## 📊 Features

- Predict property price in PKR using key features
- Built with `scikit-learn` and deployed via `Streamlit`
- Handles categorical and numerical preprocessing using pipelines
- Interactive UI for user input
- Trained on real-world data from Zameen.com

---

## 📁 Dataset

The dataset includes real estate listings collected from Zameen.com with the following relevant columns:

| Feature | Description |
|--------|-------------|
| `city` | City where the property is located |
| `location` | Locality or area |
| `property_type` | House, Flat, Plot, etc. |
| `bedrooms` | Number of bedrooms |
| `baths` | Number of bathrooms |
| `Area Size` | Numeric area of the property |
| `price` | Target variable (in PKR) |

---

## 🧠 Model

- **Algorithm**: Linear Regression (base model)  
- **Pipeline**: scikit-learn `Pipeline` with `ColumnTransformer`  
- **Preprocessing**: One-hot encoding for categorical variables

You can improve the model with Random Forests, XGBoost, or hyperparameter tuning for better accuracy.

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/real-estate-price-estimator.git
cd real-estate-price-estimator
