from utils.pocketflow import Flow
from .analyst_node import TechnicalAnalysis
import numpy as np 


tech_node=TechnicalAnalysis()
flow=Flow(start=tech_node)
    

__all__=['flow']