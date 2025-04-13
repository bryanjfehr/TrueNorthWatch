# backend/api/data_processing/analyze_stance.py
"""
Module for analyzing the sentiment of categorized platform text to determine party stances.
"""

from typing import Dict
from transformers import pipeline

# Load a pre-trained sentiment analysis model (install transformers: pip install transformers)
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_stance(categorized_text: Dict[str, str]) -> Dict[str, str]:
    """
    Analyze the sentiment of the text in each category to determine the party's stance.

    Args:
        categorized_text (Dict[str, str]): Dictionary with categories and their corresponding text.

    Returns:
        Dict[str, str]: Dictionary with categories and their sentiment labels (e.g., 'POSITIVE', 'NEGATIVE').
    """
    stances = {}
    for category, text in categorized_text.items():
        if text.strip():
            # Limit to 512 tokens due to model constraints
            result = sentiment_pipeline(text[:512])
            stances[category] = result[0]["label"].lower()  # e.g., 'positive', 'negative', 'neutral'
        else:
            stances[category] = "neutral"  # Default if no text

    return stances

# Example usage:
# if __name__ == "__main__":
#     sample_categorized = {"Climate Change and Energy": "We support renewable energy."}
#     stances = analyze_stance(sample_categorized)
#     print(stances)