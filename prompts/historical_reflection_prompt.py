import json

def historical_prompt(shared):
    s=shared['stock_symbol']
    H_s_t_minus_L_to_t_minus_1 = shared["short_medium_term_data"]
    json_historical_data = json.dumps(H_s_t_minus_L_to_t_minus_1.to_dict(orient='records'), indent=2)
    len_data = len(H_s_t_minus_L_to_t_minus_1)
    return f"""Reflection Agent Prompt (Short/Medium-Term).Analyze this {len_data}-day {s} stock trading data:{json_historical_data}
    Focus on:
    1. Recent recommendations and their outcomes (reward)
    2. Key factors influencing decisions
    3. Cumulative return trend

    Provide three insights:
    1. Decision effectiveness (based on recommendations and rewards)
    2. Most impactful key factors
    3. Short/medium-term return trend

    Format: [Effectiveness] | [Key Factors] | [Return Trend]
    Keep each insight under 15 words.
    """