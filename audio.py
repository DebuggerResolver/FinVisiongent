# Reveive input in the form of audio 
# Give the output in the form of text 

import logging
from typing import Type
import os
import signal
import sys
import assemblyai as aai
from assemblyai.streaming.v3 import (
    BeginEvent,
    StreamingClient,
    StreamingClientOptions,
    StreamingError,
    StreamingEvents,
    StreamingParameters,
    StreamingSessionParameters,
    TerminationEvent,
    TurnEvent,
)
from dotenv import load_dotenv
load_dotenv()

api_key = os.environ['ASSEMBLY_AI_API_KEY']

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
# Global variable to store the last processed transcript
last_transcript = ""

def on_terminated(self: Type[StreamingClient], event: TerminationEvent):
    """Handle the event when the transcription session is terminated."""
    print(f"Session terminated: {event.audio_duration_seconds} seconds of audio processed.")
    
def on_error(self: Type[StreamingClient], error: StreamingError):
    """Handle errors that occur during the transcription session."""
    print(f"Error occurred: {error}")
    
def on_begin(self: Type[StreamingClient], event: BeginEvent):
    """Handle the event when the transcription session begins."""
    print(f"Session started: {event.id}")

def on_turn(self: Type[StreamingClient], event: TurnEvent):
    global transcribed_text, last_transcript  # Use global variables to track transcription

    # Only process finalized transcriptions (end_of_turn == True)
    if not event.end_of_turn:
        return

    # Get the current transcript
    transcript = event.transcript.strip()

    # Avoid processing duplicate transcripts
    if transcript == last_transcript:
        return  # Skip if the transcript is the same as the last one

    # Update the last processed transcript
    last_transcript = transcript

    # Append the transcript to the global variable
    transcribed_text += transcript + " "  # Add a space between turns
    print(f"{transcript} (Finalized)")

    # Check if the user said "exit"
    if transcript.lower() == "exit":
        print("Exit command detected. Ending transcription session...")
        print("\nFinal Transcribed Text:")
        print(transcribed_text)  # Print the transcribed text before exiting the function
        self.disconnect(terminate=True)  # Gracefully disconnect the streaming client
        return  # End the function without exiting the program

def main():
    global transcribed_text, client  # Access the global variables

    client = StreamingClient(
        StreamingClientOptions(
            api_key=api_key,
            api_host="streaming.assemblyai.com",
        )
    )

    client.on(StreamingEvents.Begin, on_begin)
    client.on(StreamingEvents.Turn, on_turn)
    client.on(StreamingEvents.Termination, on_terminated)
    client.on(StreamingEvents.Error, on_error)

    client.connect(
        StreamingParameters(
            sample_rate=16000,
            format_turns=True,
        )
    )

    try:
        client.stream(
          aai.extras.MicrophoneStream(sample_rate=16000)
        )
    finally:
        client.disconnect(terminate=True)

    # Print the final transcribed text after the session ends
    print("\nFinal Transcribed Text:")
    print(transcribed_text)

def orchestrate():
    print("Hello World")

if __name__ == "__main__":
    main()
    orchestrate()