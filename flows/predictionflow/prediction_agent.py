from typing import Dict, Any
from utils.pocketflow import AsyncFlow,AsyncNode
from utils.llm import make_llm_call
from prompts.prediction_prompt import pred_prompt
import numpy as np

class PredictionAgent(AsyncNode):

    def __init__(self, max_retries=2, wait=1):
        super().__init__(max_retries=max_retries, wait=wait)

    async def prep_async(self, shared: Dict[str, Any]):
        prompt=pred_prompt(shared)
        return prompt


    async def exec_async(self, prep_res: Dict[str, Any]) -> Dict[str, Any]:
        raw_response = await make_llm_call(prep_res)
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
    async def post_async(self, shared: Dict[str, Any], prep_res: Any, exec_res: Any):
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


pred=PredictionAgent()
flow=AsyncFlow(start=pred)

__all__=['flow']