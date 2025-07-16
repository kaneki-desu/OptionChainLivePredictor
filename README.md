# TradeBot: End-to-End Option Chain Data Scraping, Machine Learning, and Live Market Prediction

## Project Summary

TradeBot is a comprehensive project that brings together data scraping, machine learning, and financial market analysis to predict actionable signals in the NIFTY options market. The project is designed to automate the entire pipeline: from collecting raw option chain data, processing and labeling it for machine learning, training robust models, and finally deploying them for real-time prediction using live market data.

The workflow is modular and extensible, allowing for experimentation at each stage—data collection, feature engineering, model selection, and live deployment. The primary focus is on high-frequency (1-minute tick) data, enabling the model to make timely and relevant predictions for option trading strategies.

---

## Workflow Overview

1. **Data Scraping**
    - `data_maker2.ipynb`: Scrapes historical 1-minute tick option chain data for a specific expiry date from the ABC website. This notebook is ideal for targeted data collection for a single day and expiry.
    - `runner.py`: Automates the scraping process to collect up to 20 days of past option chain data, iterating through days up to a specified expiry. This script is useful for building large datasets for model training.

2. **Data Preparation & Labeling**
    - `training_data.ipynb`: Merges and processes the raw option chain data with corresponding NIFTY spot prices. It transforms the data into supervised learning format: X (features) consists of the past 15 minutes of data, and Y (targets) consists of the next 5 minutes, enabling sequence-to-sequence modeling.
    - `trainingLabeled.ipynb`: Converts the processed data into labeled classes (e.g., BUY, NO, STRONG BUY) instead of raw price values, making it suitable for classification models. This step is crucial for framing the prediction problem in a way that aligns with trading decisions.

3. **Model Training**
    - `training.ipynb`: Trains machine learning models on the labeled data. Multiple algorithms can be tested, but XGBoost has shown the best recall in confusion matrix evaluations. The notebook supports experimentation with different model architectures and hyperparameters.

4. **Live Data Inference**
    - `main_wss2.ipynb`: Connects to a live market data websocket (endpoint discovered via scraping), receives real-time option chain and NIFTY spot data, processes it into the required feature format, and continuously calls `model.predict()` every minute for each available strike price. The notebook displays actionable predictions in real time, supporting live trading or monitoring.

---

## Key Features

- Automated scraping of both historical and live option chain data
- Flexible data preprocessing and feature engineering for ML
- Label generation for classification tasks tailored to trading actions
- Model training and evaluation with a focus on maximizing recall (minimizing missed opportunities)
- Real-time prediction and display using live market data
- Modular design: each stage can be adapted or extended for new data sources, features, or models

---

## File Descriptions

- **data_maker2.ipynb**: Scrapes 1-minute tick option chain data for a specific expiry and day from the ABC website.
- **runner.py**: Automates multi-day scraping for up to 20 days prior to a given expiry, building a comprehensive dataset.
- **training_data.ipynb**: Merges option and NIFTY data, and formats it for sequence-based ML tasks (X: past 15 timesteps, Y: next 5 timesteps).
- **trainingLabeled.ipynb**: Converts price-based targets into categorical labels for classification.
- **training.ipynb**: Trains and evaluates ML models (XGBoost recommended) for predicting option actions.
- **main_wss2.ipynb**: Handles live websocket connection, real-time data processing, and continuous prediction for all available strikes.
- **requirements.txt** / **training_requirements.txt**: List all necessary Python dependencies for running the notebooks and scripts.

---

## Requirements

- Python 3.8 or higher
- See `requirements.txt` and `training_requirements.txt` for all dependencies (e.g., pandas, numpy, xgboost, scikit-learn, socketio, etc.)

---

## Usage Guide

1. **Collect Historical Data**
    - For a single day/expiry: Run `data_maker2.ipynb`.
    - For multiple days: Run `runner.py`.

2. **Prepare and Label Data**
    - Use `training_data.ipynb` to merge and format the data.
    - Use `trainingLabeled.ipynb` to convert targets to labels.

3. **Train the Model**
    - Open `training.ipynb` and experiment with different models. Save the best model (e.g., XGBoost) for inference.

4. **Run Live Prediction**
    - Launch `main_wss2.ipynb` to connect to the live market, process incoming data, and display predictions in real time.

---

## Notes & Tips

- The project is modular—feel free to adapt data preparation, feature engineering, and modeling steps for your own research or trading strategies.
- The live prediction notebook requires access to the target websocket endpoint (see code for details and ensure you have the necessary permissions/network access).
- All data is stored in CSV format for easy inspection and further analysis.
- The code is designed for educational and research purposes; use caution and proper risk management if deploying in live trading.

---

## Author & License

**Author:** Sibajit Mazumder
**License:** 
This project is **not open source**. All rights reserved © 2025 Sibajit Mazumder.

If you'd like to collaborate or use this code, please contact me at **sibajit.mazumdar@gmail.com**.