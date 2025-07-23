import sys
import os
import assemblyai as aai
from utils.pocketflow import Node
from utils.transcribe_audio import check_microphone_access, on_begin, on_terminated, on_error
from assemblyai.streaming.v3 import (
    StreamingClient, StreamingClientOptions,
    StreamingParameters, StreamingEvents,
    TurnEvent
)
from typing import Type

class AudioCaptureNode(Node):
    def __init__(self, output_file="transcription.txt"):
        super().__init__()
        self.output_file = output_file
        open(self.output_file, "w").close()
        self.last_turn_order = None 

    def on_turn(self, client: StreamingClient, event: TurnEvent):
        # Only process final formatted transcripts
        if not (event.end_of_turn and event.turn_is_formatted):
            return

        self.last_turn_order = event.turn_order

        transcript = event.transcript.strip()

        if transcript.lower() == "exit":
            print("Exit detected, shutting down...")
            client.disconnect(terminate=True)
            raise SystemExit(0)

        with open(self.output_file, "a") as f:
            f.write(transcript + "\n")


    def prep(self, shared):
        check_microphone_access()
        return shared

    def exec(self, prep_res):
        api_key = os.environ['ASSEMBLY_AI_API_KEY']
        client = StreamingClient(
            StreamingClientOptions(api_key=api_key, api_host="streaming.assemblyai.com")
        )

        client.on(StreamingEvents.Begin, on_begin)
        client.on(StreamingEvents.Turn, self.on_turn)
        client.on(StreamingEvents.Termination, on_terminated)
        client.on(StreamingEvents.Error, on_error)

        try:
            client.connect(StreamingParameters(
                sample_rate=16000,
                format_turns=True,
                # Optional tuning
                end_of_turn_confidence_threshold=0.8,
                min_end_of_turn_silence_when_confident=300,
                max_turn_silence=3000
            ))
            client.stream(aai.extras.MicrophoneStream(sample_rate=16000))
        finally:
            client.disconnect(terminate=True)

    def post(self, shared, prep_res, exec_res):
        return f"Transcription completed successfully and saved to {self.output_file}"
