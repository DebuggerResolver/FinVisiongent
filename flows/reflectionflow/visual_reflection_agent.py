
from typing import Dict, Any
from base64 import b64encode
from utils.pocketflow import Node
from utils.llm import make_visual_llm_call
from prompts.visual import visual_reflection

class VisualReflectionAgent(Node):
    def __init__(self, max_retries=2, wait=1):
        super().__init__(max_retries=max_retries, wait=wait)

    def prep(self, shared: Dict[str, Any]):
        s = shared["stock_symbol"]
        V_s_t_minus_1 = shared["visual_chart_path"]
        with open(V_s_t_minus_1, "rb") as image_file:
            encoded_image = b64encode(image_file.read()).decode('utf-8')

        prompt_text = visual_reflection(s)

        messages = [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt_text},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{encoded_image}"
                        }
                    }
                ]
            }
        ]
        return messages

    def exec(self, prep_res: Dict[str, Any]) -> Dict[str, Any]:
        raw_response = make_visual_llm_call(prep_res)
        return raw_response
        

    def post(self, shared: Dict[str, Any], prep_res: Any, exec_res: Any):
        ticker = shared["stock_symbol"]
        shared[f"reflection2_visual_analysis_{ticker}"] = exec_res


