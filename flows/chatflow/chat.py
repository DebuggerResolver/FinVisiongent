from utils.pocketflow import Flow
from .audio_capture_node import AudioCaptureNode
from .handle_input import InputMode
from .text_capture_node import TextCaptureNode

input_node=InputMode()
audio_node=AudioCaptureNode()
text_node=TextCaptureNode()


input_node -"capture_audio">>audio_node
input_node-"capture_text">>text_node
chat_flow=Flow(start=input_node)


__all__=["chat_flow"]
