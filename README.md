---

# 🏬 Walmart Weekly Sales Analytics & Demand Forecasting Pipeline

[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg?style=flat-square&logo=python)](https://www.python.org/)
[![Gradio UI](https://img.shields.io/badge/UI-Gradio-orange.svg?style=flat-square)](https://gradio.app/)
[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97-Spaces-yellow.svg?style=flat-square)](https://huggingface.co/spaces)

---

## 📌 Problem Statement & Supply Chain Context
Retail operations across sprawling nationwide networks face a systemic structural problem: **Inventory Misalignment**. Misjudging regional consumer demand results in severe capital bleeding—either via expensive warehouse holding costs for overstocked goods or direct margin loss from understocked shelf stockouts during high-velocity holiday spikes.

**The Objective:** Build an end-to-end operational pipeline that analyzes regional macroeconomic/environmental variables from Walmart store logs and uses a mathematical **ARIMA (AutoRegressive Integrated Moving Average)** engine to project a rolling 12-week forward demand curve. This enables regional logistics managers to allocate inventory dynamically.

---

## 📊 Exploratory Data Analysis (EDA) Insights

| Environmental Factor | Correlation & Strategic Business Impact |
| :--- | :--- |
| **📉 Unemployment Rate** | High negative correlation ($\approx -0.78$) specifically targeting **Store 38** and **Store 44**. Shifts in regional employment directly destroy baseline purchasing power, signaling immediate stock reduction rules. |
| **❄️ Seasonal Velocity** | Strong winter demand anomalies across Q4. Q4 seasonal spikes are heavily driven by Thanksgiving and Christmas operational volumes. |
| **🌡️ Temperature Caps** | Consumption efficiency forms a bell curve; velocity clusters strongly within temperate zones (51–75°F) but trails off sharply during extreme climate anomalies. |
| **💸 Inflation (CPI)** | Shifting Consumer Price Indexes pressure the baseline consumer wallet, decreasing overall basket volume sizes. |

### 🏆 Operational Store Extremes
* **Top Performance Engine:** Store 20 ($\approx$ **$301M** cumulative sales volume)
* **Underperforming Asset:** Store 33 ($\approx$ **$37M** cumulative sales volume)
* **The Variance Gap:** A massive **$264M divergence** in historical distribution performance across network nodes, showing why store-level isolated forecasting is necessary over blanket corporate averages.

---

## 🤖 Predictive Modeling Framework (ARIMA)

Univariate time-series demands rely on strict mathematical properties to generate robust inferences:

1. **Stationarity Transformation:** Evaluated using the **Augmented Dickey-Fuller (ADF) Test** to mathematically verify whether structural variances or means drift over time.
2. **Order Identification ($p, d, q$):** Autoregressive ($p$), Integrated ($d$), and Moving Average ($q$) parameter sets are determined by mapping correlation boundaries via Autocorrelation (**ACF**) and Partial Autocorrelation (**PACF**) decay plots.
3. **Inference Horizon:** Configured to push a rolling **12-week out-of-sample forward horizon**, providing supply chain infrastructure with a 3-month predictive cushion.

---

## 🛠️ System Architecture & Tech Stack
* **Core Modeling Mathematics:** `statsmodels.tsa.arima.model.ARIMA` (Statistical modeling and parameter selection)
* **Data Pipelines:** `pandas`, `numpy` (Time-series aggregations, resampling, and chronological indexing)
* **Dynamic Visualization Engine:** `matplotlib`, `seaborn` (Real-time generation of forecast vs. historical charts saved directly to memory buffers)
* **Microservices Application UI:** `Gradio` (Front-end form input rendering and state management)
* **MLOps Cloud Platform:** `Hugging Face Spaces` (Isolated Docker-like Linux container hosting)

---

## 🚀 Strategic Future Improvements
* **Exogenous Regression (ARIMAX):** Directly embedding the feature arrays for markdowns, promotions, temperature shocks, and macroeconomic indicators into the forecasting matrix to capture sudden shifts in demand.
* **Deep Neural Sequencers:** Evaluating deep learning time-series architectures—such as **Long Short-Term Memory (LSTM)** networks or **Prophet**—to handle non-linear seasonal interactions during extended promotional periods.

---
🔗 **Reference Links:**
* **Active Production Application Dashboard:** [Hugging Face Space Live UI Webpage](https://huggingface.co/spaces/anuragN2107/walmart-sales-forecaster)
* **Core Interactive Computation Code:** [Google Colab Research Workspace](https://colab.research.google.com/drive/17Ltg7ohU1hdYki6N7ktQug3BgnYfi92B?usp=sharing)
