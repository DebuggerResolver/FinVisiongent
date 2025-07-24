from utils.pocketflow import AsyncNode
from utils.save_chart import plot_chart
from prompts.analysis import analysis_prompt
from utils.llm import make_visual_llm_call
import base64


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

class TechnicalAnalysis(AsyncNode):
    async def prep_async(self,shared):
        return shared["stock_symbol"]
    
    async def exec_async(self, prep_res):
        img_path = plot_chart(prep_res)              
        prompt = analysis_prompt(prep_res)
        base64_image = encode_image(img_path)
        messages = [{
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": prompt
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/png;base64,{base64_image}"
                    }
                }
            ]
        }]

        response = await make_visual_llm_call(messages)
        return response,img_path

    async def post_async(self,shared,prep_res,exec_res):
        response,img_path=exec_res
        shared['visual_chart_path']=img_path
        shared['technical_analysis']=response

