from utils.pocketflow import Flow
from .summarise_node import SummarizeNode
import numpy as np


summarizer=SummarizeNode()
flow=Flow(start=summarizer)

__all__=['flow']
    

