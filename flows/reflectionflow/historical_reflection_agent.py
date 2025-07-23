
from typing import Dict, Any
from utils.pocketflow import Node
from utils.llm import make_llm_call
from prompts.historical_reflection_prompt import historical_prompt

class HistoricalReflectionAgent(Node):
    def __init__(self, max_retries=2, wait=1):
        super().__init__(max_retries=max_retries, wait=wait)

    def prep(self, shared: Dict[str, Any]):        
        prompt = historical_prompt(shared)
        return prompt

    def exec(self, prep_res: Dict[str, Any]) -> Dict[str, Any]:
        raw_response = make_llm_call(prep_res)
        return raw_response

    def post(self, shared: Dict[str, Any], prep_res: Any, exec_res: Any):
        ticker=shared['stock_symbol']
        shared[f"reflection1_text_analysis_{ticker}"] = exec_res



