from datetime import datetime 
import json

def pred_prompt(shared:dict):
    ticker = shared["stock_symbol"]
    current_shares =int(shared["current_number_of_shares"])
    current_price = float(shared["current_price"])
    avg_purchase_price = float(shared["avg_purchase_price"])
    cash_reserve = float(shared["cash_reserve"])
    
    historical_data = shared["short_medium_term_data"]
    current_shares = int(shared["current_number_of_shares"])
    current_price = float(shared["current_price"])
    avg_purchase_price = float(shared["avg_purchase_price"])
    historical_data = shared["short_medium_term_data"]
    total_value = current_shares * current_price + cash_reserve
    cash_percentage = (cash_reserve / total_value * 100) if total_value > 0 else 100
       
    unrealized_pnl = (current_price - avg_purchase_price) * current_shares
    unrealized_profit_percentage = (
        (current_price - avg_purchase_price) / avg_purchase_price * 100
        if avg_purchase_price > 0 else 0
    )
    current_date =  datetime.today().date()
    chart_analysis = shared["technical_analysis"]
    news_summary = shared["stock_news"]
    reflection1_insights = shared.get(f"reflection1_text_analysis_{ticker}", "No short-term insight")
    reflection2_insights = shared.get(f"reflection2_visual_analysis_{ticker}", "No market intelligence")
    short_term_reflection = reflection1_insights 
    medium_term_reflection = reflection1_insights 
    market_intelligence = reflection2_insights 
    json_data = json.dumps(historical_data.to_dict(orient="records"), indent=2)

    prompt = f"""# The main prompt for the LLM, providing context and instructions for trading decisions.
    As an advanced trading strategy agent for {ticker} stock, analyze the following data to formulate an opportunistic trading decision:

    # Current Date information.
    Current Date: {current_date}

    # Current Portfolio details.
    Current Portfolio:

    # Number of shares held.
    - Shares: {current_shares}
    # Current share price.
    - Share Price: ${current_price:.2f}
    # Average price at which shares were purchased.
    - Average Purchase Price: ${avg_purchase_price:.2f}
    # Total value of the portfolio.
    - Total Value: ${total_value:.2f}
    # Amount of cash held in reserve.
    - Cash Reserve: ${cash_reserve:.2f}
    # Percentage of total portfolio held in cash.
    - Cash Percentage: {cash_percentage:.2f}%
    # Unrealized Profit/Loss.
    - Unrealized P/L: ${unrealized_pnl:.2f}
    # Unrealized Profit Percentage.
    - Unrealized Profit Percentage: {unrealized_profit_percentage:.2f}%

    # Technical analysis insights.
    Technical Analysis: {chart_analysis}

    # Summary of recent news.
    News Summary: {news_summary}

    # Reflection insights from analysis agents.
    Reflections:

    # Short-term reflection insights.
    - Short-term: {short_term_reflection}

    # Medium-term reflection insights.
    - Medium-term: {medium_term_reflection}

    # Market intelligence based on past trading decisions.
    Effectiveness of past trading decisions: {market_intelligence}

    # Historical trading data for the last N days.
    Historical Trading Data (Last {len(historical_data)} days): {json_data}

    # Instructions for the LLM to formulate a trading strategy.
    Based on this data, provide an opportunistic trading strategy. Consider:

    # Rule 1: Identify and prioritize holding during strong upward trends.
    1. Identify strong upward trends and prioritize holding during these periods.

    # Rule 2: Look for buying opportunities during price dips within upward trends.
    2. Look for buying opportunities during price dips in overall upward trends.

    # Rule 3: Consider partial selling to lock in profits.
    3. Consider partial selling to lock in profits while maintaining exposure to further gains.

    # Rule 4: Evaluate past trading decisions.
    4. Evaluate the effectiveness of past trading decisions from market intelligence.

    # Rule 5: Factor in market sentiment, news, and technical indicators.
    5. Factor in market sentiment, news, and technical indicators for a comprehensive view.

    # Rule 6: Balance short-term opportunities with long-term growth.
    6. Balance short-term opportunities with long-term growth potential.

    # Specific trading rules and conditions.
    Rules:

    # Rule: Maintain at least 10% cash reserve.
    - Maintain at least 10% of the portfolio in cash for opportunistic buying.

    # Conditions for recommending a BUY.
    - Recommend BUY if:

    # Condition a) for BUY: Strong upward trend and sufficient cash.
    a) Strong upward trend and sufficient cash (>10% of portfolio)

    # Condition b) for BUY: Price dip in upward trend and higher cash reserve.
    b) Price dip in overall upward trend and cash reserve above 20%

    # Conditions for recommending a SELL.
    - Recommend SELL if:

    # Condition a) for SELL: Signs of significant trend reversal.
    a) Signs of significant trend reversal, OR

    # Condition b) for SELL: Exceptional gains for partial sell.
    b) Exceptional gains (>5% from avg purchase price) for partial sell, OR

    # Condition c) for SELL: Consistent gains over multiple days.
    c) Consistent gains for 3 or more consecutive days

    # Conditions for recommending a HOLD.
    - Recommend HOLD if:

    # Condition a) for HOLD: Upward trend continues without reversal.
    a) Upward trend continuing without significant reversal signs

    # Condition b) for HOLD: Market uncertainty but current positions are profitable.
    b) Market uncertainty and current positions are profitable

    # Recommended position size for BUY actions.
    - For BUY: 5-10% in strong upward trends, 1-5% for dip opportunities

    # Recommended position size for SELL actions.
    - For SELL: Consider partial sells (3-5%) to lock in profits

    # Aggressiveness for SELL during strong upward trends.
    - Be more aggressive with SELL during strong upward trends

    # Required output format for the trading strategy.
    Provide your trading strategy in the following format:

    # Recommendation field.
    Recommendation: [BUY/SELL/HOLD]

    # Position Size field.
    Position Size: [1-10] (0 if HOLD)

    # Explanation field.
    Explanation: [Detailed rationale for the decision]

    # Instruction to ensure detailed explanation.
    Ensure your explanation is detailed and covers all aspects of your analysis and decision-making process, with a focus on capturing opportunistic gains.
"""
    return prompt
