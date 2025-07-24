# Integration of the subflows to flow 
import asyncio
from utils.pocketflow import AsyncFlow
from flows.chatflow.chat import chat_flow
from flows.summarizeflow.summarize_flow import flow as summarize_flow
from flows.technical_analyst_flow.flow import flow as analysis_flow
from flows.reflectionflow.flow import flow as reflection_flow
from flows.predictionflow.prediction_agent import flow as prefiction_flow
from utils.llm import make_llm_call
async def main():
    shared={}
    chat_flow >> summarize_flow >> analysis_flow >> reflection_flow >> prefiction_flow
    flow=AsyncFlow(start=chat_flow)
    await flow.run_async(shared=shared)
    prompt=f"""{shared['decision']}. Explain this breafly. Dont write anything extra"""
    response=await make_llm_call(prompt)
    print(response)

if __name__=="__main__":
    asyncio.run(main())




