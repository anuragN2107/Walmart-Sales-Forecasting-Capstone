# 🛒 Walmart Weekly Sales Analysis & Forecasting 📈

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![Google Colab](https://img.shields.io/badge/Google%20Colab-Focused-orange?style=for-the-badge&logo=googlecolab)
![Data Science](https://img.shields.io/badge/Domain-Data%20Science-green?style=for-the-badge&logo=datascience)

> **Executive PG Certification in Data Science and AI** > *Associated with iHub Divyasampark, IIT Roorkee & Intellipaat* > **Prepared by:** Anurag Srivastva

---

## 📌 Problem Statement
A retail store with multiple outlets countrywide faces major inventory management issues—specifically, matching demand with supply. This project analyzes historical weekly sales data to uncover key economic/environmental drivers and forecasts sales for the next 12 weeks.

## 📊 Key Insights from EDA

| Factor | Business Impact & Observations |
| :--- | :--- |
| **Unemployment** | High negative impact on **Store 38** and **Store 44** ($\approx -0.78$). As unemployment rises, sales drop drastically. |
| **Seasonality** | Strong winter spikes driven by holiday seasons and festive shopping. |
| **Temperature** | Sales peak at moderate-to-high temperatures (51–75°F) but decline sharply during extreme weather. |
| **Inflation (CPI)** | High inflation drastically reduces consumer purchasing power, triggering sales drops. |

### 🏆 Store Performance Highlights
* **Top Performer:** Store 20 ($\approx$ $301M total sales)
* **Worst Performer:** Store 33 ($\approx$ $37M total sales)
* **The Gap:** A massive **$264M difference** between the best and worst outlets!

---

## 🤖 Predictive Modeling (ARIMA)
We utilized the **ARIMA (AutoRegressive Integrated Moving Average)** model to handle univariate time-series forecasting. 
* **Stationarity:** Verified via the **ADF (Augmented Dickey-Fuller) Test**.
* **Parameters ($p, d, q$):** Identified using **ACF and PACF** plots.
* **Horizon:** Generates robust, short-term **12-week sales forecasts** for data-driven demand planning.

---

## 🛠️ Tech Stack & Tools
* **Language:** Python
* **Environment:** Google Colab
* **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Statsmodels (ARIMA)

🔗 **[Click Here to View the Interactive Google Colab Notebook](https://colab.research.google.com/drive/17Ltg7ohU1hdYki6N7ktQug3BgnYfi92B?usp=sharing))**
