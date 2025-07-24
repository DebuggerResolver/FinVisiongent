from utils.pocketflow import AsyncFlow
from .historical_reflection_agent import HistoricalReflectionAgent
from .visual_reflection_agent import VisualReflectionAgent


textual_reflection=HistoricalReflectionAgent()
visual_reflection=VisualReflectionAgent()
textual_reflection>>visual_reflection
flow=AsyncFlow(start=textual_reflection)


__all__=['flow']
