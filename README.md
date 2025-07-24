# FinVision Agent

FinVision Agent is a comprehensive financial analysis tool that provides stock predictions, news summaries, and technical analysis. It leverages the power of large language models to provide a conversational interface for financial data analysis.

## Features

- **Stock Analysis**: Get detailed stock analysis, including historical data and technical indicators.
- **News Summarization**: Summarizes the latest financial news to keep you updated.
- **Stock Prediction**: Predicts future stock prices using advanced algorithms.
- **Interactive Chat**: A conversational interface to interact with the agent.
- **Audio Transcription**: Transcribe audio to text for seamless interaction.

## How to Use

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/finvision.git
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the application:**
   ```bash
   python main.py
   ```

## Project Structure

```
.
├── flows
│   ├── chatflow
│   ├── predictionflow
│   ├── reflectionflow
│   ├── summarizeflow
│   └── technical_analyst_flow
├── prompts
├── tests
├── utils
├── main.py
├── requirements.txt
└── README.md
```

- **`main.py`**: The main entry point of the application.
- **`flows/`**: Contains the core logic for different agent functionalities.
- **`prompts/`**: Contains the prompts for the language model.
- **`utils/`**: Contains utility functions for stock data, LLM interaction, etc.
- **`tests/`**: Contains the tests for the project.

## Dependencies

The project uses the following major dependencies:

- `requests`
- `python-dotenv`
- `yfinance`
- `assemblyai`
- `pyaudio`
- `finnhub-python`
- `polygon-api-client`
- `groq`
- `openchart`
- `pandas`
- `mplfinance`
- `matplotlib`
- `seaborn`
- `assemblyai[extras]`
- `aiohttp`

For a full list of dependencies, please see `requirements.txt`.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.
