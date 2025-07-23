from typing import Dict, Any
from utils.pocketflow import Node,Flow
from utils.llm import make_llm_call
from prompts.prediction_prompt import pred_prompt
import numpy as np

class PredictionAgent(Node):

    def __init__(self, max_retries=2, wait=1):
        super().__init__(max_retries=max_retries, wait=wait)

    def prep(self, shared: Dict[str, Any]):
        prompt=pred_prompt(shared)
        return prompt


    def exec(self, prep_res: Dict[str, Any]) -> Dict[str, Any]:
        raw_response = make_llm_call(prep_res)
        try:
            recommendation = self._extract_field(raw_response, "Recommendation:")
            position_size_str = self._extract_field(raw_response, "Position Size:")
            explanation = self._extract_field(raw_response, "Explanation:", end_markers=["Recommendation:", None])
            position_size = 0
            if recommendation.strip().upper() == "HOLD":
                position_size = 0
            else:
                try:
                    position_size = int(position_size_str.strip())
                    position_size = max(1, min(10, position_size))  
                except ValueError:
                    position_size = 5  
            return {
                "recommendation": recommendation.strip().upper(),
                "position_size": position_size,
                "explanation": explanation.strip(),
                "raw_response": raw_response
            }
        except Exception as e:
            raise ValueError(f"Failed to parse LLM response: {str(e)}Raw response:{raw_response}")

    # Helper method to extract a field from the LLM response.
    def _extract_field(self, text: str, key: str, end_markers=None):
        # Finds the starting index of the key in the text.
        start = text.find(key)
        # If the key is not found, return "Unknown".
        if start == -1:
            return "Unknown"
        # Adjusts the start index to be after the key.
        start += len(key)
        # Initializes end index to None.
        end = None
        # If end markers are provided, iterate through them.
        if end_markers:
            for marker in end_markers:
                # If a marker exists and is found in the text after the start index.
                if marker and (pos := text.find(marker, start)) != -1:
                    # Set the end index to the position of the marker.
                    end = pos
                    # Break the loop once a marker is found.
                    break
        # If no end marker is found, set the end index to the length of the text.
        if not end:
            end = len(text)
        # Returns the extracted text, stripped of leading/trailing whitespace.
        return text[start:end].strip()

    # Post-processing method to store the decision in the shared dictionary.
    def post(self, shared: Dict[str, Any], prep_res: Any, exec_res: Any):
        # Retrieves the ticker from the prepared response.
        ticker = shared["stock_symbol"]
        # Constructs the decision key using the ticker.
        decision_key = f"decision_{ticker}"
        # Stores the execution results (decision) in the shared dictionary under the decision key.
        shared[decision_key] = exec_res
        # Also store flat fields for easy access
        # Stores the recommendation as "action" in the shared dictionary.
        shared["action"] = exec_res["recommendation"]
        # Stores the position size in the shared dictionary.
        shared["position_size"] = exec_res["position_size"]
        # Stores the explanation as "decision_explanation" in the shared dictionary.
        shared["decision_explanation"] = exec_res["explanation"]

if __name__=="__main__":
    pred=PredictionAgent()
    shared={'input_type': 'text', 'stock_name': 'reliance', 'number_of_shares_to_be_bought_or_sold': '10', 'cash_reserve': '50000', 'current_number_of_shares': '10', 'avg_purchase_price': '1600', 'stock_symbol': 'RELIANCE', 'current_price': np.float64(1425.0), 'stock_news': "Here is a concise summary of the news and its potential trading implications for RELIANCE.NS:\n\nThe stock price of RELIANCE.NS may be impacted by the company's recent earnings report, which showed a 78% surge in first-quarter profit driven by strong growth in key businesses and gains from the sale of its stake in Asian Paints. However, earnings before interest, taxes, depreciation, and amortization in its key oil-to-chemicals and retail segments came in below analyst expectations, leading to a 3.6% intraday drop in the stock price. The company's reliance on Russian crude oil may also be affected by the latest European Union sanctions, which could force refiners to find new markets for their products. Additionally, the uncertainty over a trade deal between India and the US may lead to stock-specific action based on earnings.\n\nThe positive factors mentioned in the news include the company's strong earnings growth, driven by improved refining margins and petrochemical demand, as well as the launch of a new virtual desktop service by Jio Platforms. The negative factors include the company's reliance on Russian crude oil, which may be affected by sanctions, and the uncertainty over a trade deal between India and the US.\n\nBased on this news, the overall sentiment towards RELIANCE.NS stock is likely to be neutral, as the company's strong earnings growth is offset by concerns over its reliance on Russian crude oil and the uncertainty over a trade deal between India and the US. The stock price may be subject to stock-specific action based on earnings, and investors may need to wait for further clarity on these issues before making any trading decisions.", 'short_medium_term_data': '  Open    High     Low   Close    Volume  Dividends  Stock Splits\nDate                                                                                        \n2025-06-23 00:00:00+05:30  1453.0  1463.8  1442.0  1456.8   5989078        0.0           0.0\n2025-06-24 00:00:00+05:30  1465.0  1475.0  1443.1  1450.8  16402744        0.0           0.0\n2025-06-25 00:00:00+05:30  1464.0  1472.4  1460.5  1467.3   7525851        0.0           0.0\n2025-06-26 00:00:00+05:30  1469.1  1498.8  1465.1  1495.3  14657893        0.0           0.0\n2025-06-27 00:00:00+05:30  1499.4  1522.0  1496.9  1515.4  11117052        0.0           0.0\n2025-06-30 00:00:00+05:30  1513.8  1524.8  1496.0  1500.6   8409527        0.0           0.0\n2025-07-01 00:00:00+05:30  1500.6  1531.4  1500.1  1528.4  10368523        0.0           0.0\n2025-07-02 00:00:00+05:30  1528.4  1530.0  1508.7  1518.8   6361002        0.0           0.0\n2025-07-03 00:00:00+05:30  1520.8  1531.9  1513.0  1517.8  11283291        0.0           0.0\n2025-07-04 00:00:00+05:30  1524.0  1530.0  1517.2  1527.3   6603501        0.0           0.0\n2025-07-07 00:00:00+05:30  1526.6  1544.8  1525.0  1541.5   7251074        0.0           0.0\n2025-07-08 00:00:00+05:30  1536.0  1544.9  1530.2  1537.6   7171261        0.0           0.0\n2025-07-09 00:00:00+05:30  1536.7  1551.0  1510.1  1519.0   8870660        0.0           0.0\n2025-07-10 00:00:00+05:30  1519.7  1524.7  1507.5  1517.2  10047129        0.0           0.0\n2025-07-11 00:00:00+05:30  1512.0  1515.0  1490.3  1495.2   7234991        0.0           0.0\n2025-07-14 00:00:00+05:30  1492.2  1500.0  1479.1  1483.7  10311846        0.0           0.0\n2025-07-15 00:00:00+05:30  1486.2  1496.5  1482.4  1485.4   8132454        0.0           0.0\n2025-07-16 00:00:00+05:30  1473.0  1491.0  1471.5  1485.6  10409983        0.0           0.0\n2025-07-17 00:00:00+05:30  1487.4  1489.6  1473.9  1476.4  11854613        0.0           0.0\n2025-07-18 00:00:00+05:30  1484.8  1484.8  1469.1  1476.0  10296318        0.0           0.0\n2025-07-21 00:00:00+05:30  1465.0  1476.0  1423.1  1428.6  22442744        0.0           0.0\n2025-07-22 00:00:00+05:30  1427.4  1431.9  1410.7  1412.8  20396320        0.0           0.0', 'technical_analysis': ('## Analysis of RELIANCE Candlestick Chart\n\n### Strategy 1: MACD Crossover Strategy\n- **Key Market Trend Observation**: Price shows downtrend.\n- **Potential Trading Signal**: Bearish crossover.\n\n### Strategy 2: KDJ with RSI Filter Strategy\n- **Key Market Trend Observation**: Oversold conditions.\n- **Potential Trading Signal**: Buy at support.\n\n## Formatted Response\nStrategy1: Downtrend | Bearish Crossover\nStrategy2: Oversold | Buy Signal',)}
    flow=Flow(start=pred)
    flow.run(shared=shared)
    print("SHARE")
    print(shared)