# Lahore Real Estate Price Prediction 🏠

A **Flask-based** web application that predicts real estate (house) prices in **Lahore**, Pakistan. This project uses **machine learning** (Linear Regression) along with extensive **data cleaning**, **feature engineering**, and **outlier removal** to provide more accurate predictions.

---

## Overview ✨

- **Predict House Prices** based on **location**, **area** (Marla/Kanal), **number of baths**, **beds**, and **property type**.  
- **Data Preprocessing** includes converting area units to square feet, removing outliers, grouping rare locations into `"other"`, etc.  
- **Model Score**: Achieved an **R² ≈ 0.83** on the test set.  
- **Web Interface**: A simple **HTML** form (using **Flask**) to collect user input and display predicted prices.

---

## Table of Contents 📚

1. [Project Structure](#project-structure-)
2. [Installation](#installation-)
3. [Usage](#usage-)
4. [Model Training Details](#model-training-details-)
5. [How It Works](#how-it-works-)
6. [Screenshots](#screenshots-)
7. [License](#license-)
8. [Contact & Contributing](#contact--contributing-)

---

## Project Structure 📂

    .
    ├── model
    │   ├── Lahore_Real_Estate_Price_Prediction_model.pickle
    │   ├── columns.json
    │   └── ...
    ├── templates
    │   └── index.html
    ├── server.py
    ├── requirements.txt
    ├── README.md
    └── ...

- **`server.py`**: Main Flask application (backend).  
- **`templates/index.html`**: Front-end form to collect user inputs.  
- **`model/Lahore_Real_Estate_Price_Prediction_model.pickle`**: Pre-trained model (Linear Regression).  
- **`model/columns.json`**: JSON file containing column names used by the model.  
- **`requirements.txt`**: Python dependencies needed for this project.  

---

## Installation ⚙️

1. **Clone the Repository**  
    ```
    git clone https://github.com/tehseen-h/lahore-house-price-prediction.git
   
    ```

2. **Create a Virtual Environment** (optional but recommended)  
    ```
    python -m venv venv
    ```
    - **Windows**:  
      ```
      venv\Scripts\activate
      ```
    - **Linux/Mac**:  
      ```
      source venv/bin/activate
      ```

3. **Install Dependencies**  
    ```
    pip install -r requirements.txt
    ```

---

## Usage 🚀

1. **Run the Flask App**  
    ```
    python server.py
    ```
   By default, the app will run on **http://127.0.0.1:5000/** (local environment).

2. **Open in Your Browser**  
   - Go to [http://127.0.0.1:5000](http://127.0.0.1:5000).  
   - Enter the **area** (with unit), **location**, **baths**, **beds**, and **type** (House/Flat).  
   - Click **"Predict"** to get the estimated price.

3. **Deploy on Replit** (optional)  
   - Update `.replit` to `run = "python server.py"` (or your correct file path).  
   - Make sure `app.run(host="0.0.0.0", port=8080)` in `server.py` if you want a public URL on Replit.

---

## Model Training Details 🏗️

> **Note**: These steps are **not** strictly necessary to run the web app. They are for those who want to **retrain** or **understand** the model-building process.

1. **Data Source**  
   - The dataset comes from a CSV file containing Lahore housing prices (`lahore_housing_prices.csv`).

2. **Data Cleaning & Preprocessing**  
   - Dropped missing values.  
   - Removed **inconsistent rows** (e.g., properties with fewer beds/baths having higher prices than properties with more).  
   - Converted **Marla/Kanal** to **square feet**.  
   - Grouped rare **location** values as `"other"`.  
   - Calculated `Price_per_sqft` and removed outliers using **z-score** thresholds.

3. **Feature Engineering**  
   - One-hot encoding for **location**.  
   - Split area into numeric value + unit, then combined them to **square feet**.

4. **Model Building**  
   - **Linear Regression** (`sklearn.linear_model`) was used.  
   - Achieved **R² ≈ 0.83** on the test set.

5. **Saving Artifacts**  
   - The trained model is saved in `Lahore_Real_Estate_Price_Prediction_model.pickle`.  
   - The columns (features) are saved in `columns.json`.

---

## How It Works ⚡

1. **User Input**  
   - User fills out a form with property details (area, location, baths, beds, type).

2. **Data Transformation**  
   - Flask converts Marla/Kanal to square feet.  
   - One-hot encoding is applied for the chosen location.

3. **Model Inference**  
   - The processed input is fed into the **Linear Regression** model (`lr_clf`).  
   - A price is predicted based on the learned coefficients.

4. **Result Display**  
   - The predicted price is shown on the web page.  
   - If invalid inputs (e.g., negative area) are detected, a warning message is displayed.

---

## License ⚖️

This project is licensed under the **MIT License**. For more details, see the [LICENSE](LICENSE) file in this repository.

---

## Contact & Contributing 🤝

- **Author**:((https://github.com/tehseen-h/))  
- **Contributions**: Feel free to **open an issue** or **submit a pull request**.  

> **Thank you for checking out the Lahore Real Estate Price Prediction project!**  
>  
> ⭐ **Star** this repo if you found it useful, and happy coding!
