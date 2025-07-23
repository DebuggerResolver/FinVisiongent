from openchart import NSEData
import datetime
import mplfinance as mpf
import os 
from pathlib import Path

def plot_chart(stock_symbol:str)->Path:
    # Fetch data
    nse = NSEData()
    nse.download()

    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=1)
    start = yesterday.replace(hour=9, minute=15, second=0, microsecond=0)
    end = yesterday.replace(hour=15, minute=30, second=0, microsecond=0)

    df = nse.historical(
        symbol=stock_symbol,
        exchange='NSE',
        start=start,
        end=end,
        interval='5m'
    )

    # Plot and save
    fig, axes = mpf.plot(
        df,
        type='candle',
        style='yahoo',
        title=f'{stock_symbol} – 5‑Min Intraday – {start.date()}',
        volume=True,
        mav=(3, 6),
        figsize=(12, 8),
        returnfig=True
    )

    # Enable grid (optional)
    axes[0].grid(True)

    # Save to PNG with high resolution
    fig.savefig(f'{stock_symbol}.png', dpi=300)

    absolute_path = os.path.abspath(f'{stock_symbol}.png')
    return absolute_path

    