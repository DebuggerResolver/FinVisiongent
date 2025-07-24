from utils.pocketflow import AsyncFlow
from .analyst_node import TechnicalAnalysis
import numpy as np 


tech_node=TechnicalAnalysis()
flow=AsyncFlow(start=tech_node)
    

__all__=['flow']