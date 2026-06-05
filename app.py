import gradio as gr
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import io
from PIL import Image

# 1. Load data assets and model files safely
df = pd.read_csv("historical_summary.csv")
df['Date'] = pd.to_datetime(df['Date'])

with open("arima_model.pkl", "rb") as f:
    model_fit = pickle.load(f)

def generate_forecast_dashboard(store_id, steps_to_forecast):
    store_id = int(store_id)
    steps_to_forecast = int(steps_to_forecast)
    
    # Filter historical metrics for the selected store outlet
    store_data = df[df['Store'] == store_id].sort_values('Date')
    
    # Generate future forecasts from the out-of-sample statistical model
    forecast = model_fit.forecast(steps=steps_to_forecast)
    
    # Map future forecast timeline index dates
    last_date = store_data['Date'].max()
    forecast_dates = pd.date_range(start=last_date + pd.Timedelta(weeks=1), periods=steps_to_forecast, freq='W')
    
    # 2. Build the output visualization plot
    plt.figure(figsize=(10, 5))
    plt.plot(store_data['Date'][-52:], store_data['Weekly_Sales'][-52:], label="Historical Weekly Sales (Last 52 Weeks)", color="blue")
    plt.plot(forecast_dates, forecast, label=f"ARIMA Forecast (Next {steps_to_forecast} Weeks)", color="orange", linestyle="--", marker='o')
    
    plt.title(f"Walmart Store #{store_id} Demand Forecast Pipeline")
    plt.xlabel("Timeline Date")
    plt.ylabel("Weekly Sales ($)")
    plt.legend(loc="upper left")
    plt.grid(True, linestyle=":")
    plt.tight_layout()
    
    # Save chart to a memory byte buffer stream
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=150)
    buf.seek(0)
    plot_img = Image.open(buf)
    plt.close()
    
    # Calculate key aggregate metrics for text displays
    avg_predicted_sales = forecast.mean()
    total_forecasted_demand = forecast.sum()
    
    insights_text = (
        f"### 📈 Forecast Insights for Store #{store_id}:\n"
        f"* **Total Expected Inventory Demand (Next {steps_to_forecast} Weeks):** ${total_forecasted_demand:,.2f}\n"
        f"* **Estimated Average Weekly Volume:** ${avg_predicted_sales:,.2f}\n\n"
        f"💡 *Supply Chain Recommendation:* Align regional stock logistics to support these projected peaks to minimize stockouts and avoid overstocking."
    )
    
    return plot_img, insights_text

# 3. Build the Gradio App Layout Interface
with gr.Blocks(theme=gr.themes.Default()) as demo:
    gr.Markdown("# 🏬 Walmart Inventory Demand Forecasting Service")
    gr.Markdown("An automated demand management app using historical time-series forecasting to map future supply requirements.")
    
    with gr.Row():
        with gr.Column(scale=1):
            store_selector = gr.Dropdown(choices=[str(i) for i in sorted(df['Store'].unique())], value="1", label="Select Retail Outlet ID")
            horizon_slider = gr.Slider(minimum=4, maximum=12, step=1, value=12, label="Forecast Horizon Window (Weeks)")
            run_btn = gr.Button("Generate Demand Forecast", variant="primary")
            
        with gr.Column(scale=2):
            output_plot = gr.Image(type="pil", label="Demand Timeline Visualization")
            output_text = gr.Markdown(label="Operational Projections")
            
    run_btn.click(
        fn=generate_forecast_dashboard,
        inputs=[store_selector, horizon_slider],
        outputs=[output_plot, output_text]
    )

if __name__ == "__main__":
    demo.launch()