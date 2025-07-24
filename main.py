# Integration of the subflows to flow 
from utils.pocketflow import Flow
from flows.chatflow.chat import chat_flow
from flows.summarizeflow.summarize_flow import flow as summarize_flow
from flows.technical_analyst_flow.flow import flow as analysis_flow
from flows.reflectionflow.flow import flow as reflection_flow
from flows.predictionflow.prediction_agent import flow as prefiction_flow

shared={}
chat_flow >> summarize_flow >> analysis_flow >> reflection_flow >> prefiction_flow
flow=Flow(start=chat_flow)
flow.run(shared=shared)
print("SHARED ")
print(shared)





