"""
Day 3 - Session 4  |  Azure AI Language demo

Uses a model Microsoft already trained. No compute instance, no training.

HOW TO RUN (in Azure Cloud Shell)
    pip install azure-ai-textanalytics

    export AZURE_LANGUAGE_KEY="paste-your-key-here"
    export AZURE_LANGUAGE_ENDPOINT="paste-your-endpoint-here"

    python language_demo.py

Get the key and endpoint from:
    Azure portal -> your Language resource -> Keys and Endpoint

NEVER paste your key into a file you push to GitHub. Use the environment
variables above, or a .env file that stays on your own machine.
"""

import os
import sys

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError


# ---------------------------------------------------------------
# Read the key and endpoint from the environment
# ---------------------------------------------------------------
KEY = os.environ.get("AZURE_LANGUAGE_KEY")
ENDPOINT = os.environ.get("AZURE_LANGUAGE_ENDPOINT")

if not KEY or not ENDPOINT:
    print("ERROR: key or endpoint not set.\n")
    print("Run these two lines first, with your own values:\n")
    print('  export AZURE_LANGUAGE_KEY="your-key-1"')
    print('  export AZURE_LANGUAGE_ENDPOINT="https://lang-yourname.cognitiveservices.azure.com/"')
    sys.exit(1)


def line(title):
    print("\n" + "=" * 62)
    print("  " + title)
    print("=" * 62)


# ---------------------------------------------------------------
# 1. Sentiment - is this positive or negative?
# ---------------------------------------------------------------
def sentiment(client):
    line("1. SENTIMENT  -  is this positive or negative?")

    sentences = [
        "The training today was excellent and very clear.",
        "I am tired and the room is too hot.",
        "The mission was completed, but we lost equipment.",
    ]

    for result in client.analyze_sentiment(sentences):
        if result.is_error:
            print("  error:", result.error.message)
            continue
        scores = result.confidence_scores
        print(f"  {result.sentiment.upper():9} "
              f"(pos {scores.positive:.2f} / neu {scores.neutral:.2f} / neg {scores.negative:.2f})")
        print(f"            {result.text}")


# ---------------------------------------------------------------
# 2. Key phrases - what is this text about?
# ---------------------------------------------------------------
def key_phrases(client):
    line("2. KEY PHRASES  -  what is this text about?")

    documents = [
        "The drone flew over the training field at dawn and recorded video of the exercise.",
        "Students at Ethiopian Defense University learned cloud computing and machine learning.",
    ]

    for result in client.extract_key_phrases(documents):
        if result.is_error:
            print("  error:", result.error.message)
            continue
        print("  ", result.key_phrases)


# ---------------------------------------------------------------
# 3. Language detection - what language is this?
# ---------------------------------------------------------------
def detect_language(client):
    line("3. LANGUAGE DETECTION  -  what language is this?")

    documents = [
        "The training today was excellent.",
        "አገልግሎቱ በጣም ጥሩ ነበር።",          # Amharic
        "Bonjour tout le monde",
        "Hola, como estas?",
    ]

    for result in client.detect_language(documents):
        if result.is_error:
            print("  error:", result.error.message)
            continue
        lang = result.primary_language
        print(f"  {lang.name:12} (confidence {lang.confidence_score:.2f})  {result.id}")

    print("\n  Note: on Day 1 the English-only Hugging Face model could not handle")
    print("  Amharic at all. This service detects it. That difference is what a")
    print("  hosted, maintained, multilingual service buys you.")


# ---------------------------------------------------------------
# 4. Entities - who and what is mentioned?
# ---------------------------------------------------------------
def entities(client):
    line("4. NAMED ENTITIES  -  who and what is mentioned?")

    documents = [
        "Abebe travelled from Gondar to Addis Ababa in January 2026 for the AI training.",
    ]

    for result in client.recognize_entities(documents):
        if result.is_error:
            print("  error:", result.error.message)
            continue
        for entity in result.entities:
            print(f"  {entity.text:20} -> {entity.category:14} ({entity.confidence_score:.2f})")


# ---------------------------------------------------------------
# 5. Your turn
# ---------------------------------------------------------------
def your_turn(client):
    line("5. YOUR TURN  -  edit these sentences and run again")

    my_sentences = [
        "Write your own sentence here.",
        "And another one, in any language you like.",
    ]

    for result in client.analyze_sentiment(my_sentences):
        if result.is_error:
            print("  error:", result.error.message)
            continue
        print(f"  {result.sentiment.upper():9} {result.text}")


def main():
    print("Connecting to", ENDPOINT)
    client = TextAnalyticsClient(
        endpoint=ENDPOINT,
        credential=AzureKeyCredential(KEY),
    )

    try:
        sentiment(client)
        key_phrases(client)
        detect_language(client)
        entities(client)
        your_turn(client)
    except ClientAuthenticationError:
        print("\nERROR: the key was rejected.")
        print("Copy KEY 1 again from the portal - no extra spaces.")
        sys.exit(1)
    except HttpResponseError as error:
        print(f"\nERROR from Azure: {error.message}")
        print("Check that the endpoint URL is correct and ends with a /")
        sys.exit(1)

    print("\n" + "=" * 62)
    print("  Done. No compute instance was used - nothing to switch off here.")
    print("  But DO go and stop your compute instance from Session 3.")
    print("=" * 62)


if __name__ == "__main__":
    main()
