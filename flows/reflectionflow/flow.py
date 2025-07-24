from utils.pocketflow import Flow
from .historical_reflection_agent import HistoricalReflectionAgent
from .visual_reflection_agent import VisualReflectionAgent


textual_reflection=HistoricalReflectionAgent()
visual_reflection=VisualReflectionAgent()
textual_reflection>>visual_reflection
flow=Flow(start=textual_reflection)


__all__=['flow']
