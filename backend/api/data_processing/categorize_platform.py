# backend/api/data_processing/categorize_platform.py
"""
Module for categorizing party platform text into 15 predefined categories.
"""

from typing import Dict
import re

# Define the 15 categories as specified
CATEGORIES = [
    "Climate Change and Energy",
    "Cost of Living (including Taxes)",
    "Crime and Justice",
    "Defence and National Security",
    "Education and Training",
    "Foreign Policy",
    "Government Spending and Fiscal Policy",
    "Gun Control",
    "Health Care",
    "Housing",
    "Immigration",
    "Indigenous Affairs",
    "Infrastructure",
    "Jobs and Employment",
    "International Trade and Relations"
]

def categorize_text(platform_text: str) -> Dict[str, str]:
    """
    Categorize the platform text into the 15 predefined categories based on keywords.

    Args:
        platform_text (str): The full platform text.

    Returns:
        Dict[str, str]: Dictionary with category names as keys and relevant text as values.
    """
    categorized = {category: "" for category in CATEGORIES}

    # Keyword mappings based on your category descriptions
    keywords = {
        "Climate Change and Energy": ["climate", "energy", "emissions", "renewable", "hydroelectricity", "carbon tax"],
        "Cost of Living (including Taxes)": ["tax", "cost of living", "affordability", "exemption", "bracket"],
        "Crime and Justice": ["crime", "justice", "law enforcement", "rcmp", "sentencing", "three-strikes"],
        "Defence and National Security": ["defence", "military", "security", "nato", "arctic", "f-35"],
        "Education and Training": ["education", "training", "apprenticeship", "postsecondary", "grants"],
        "Foreign Policy": ["foreign", "international", "aid", "allies", "u.s.", "conflicts"],
        "Government Spending and Fiscal Policy": ["spending", "fiscal", "budget", "public service", "cbc", "foreign aid"],
        "Gun Control": ["gun", "firearm", "control", "buyback", "border", "scanners"],
        "Health Care": ["health", "care", "dental", "pharmacare", "addiction"],
        "Housing": ["housing", "affordable", "gst", "home", "housing starts"],
        "Immigration": ["immigration", "asylum", "border", "caps", "non-permanent", "levels"],
        "Indigenous Affairs": ["indigenous", "rights", "self-determination", "loan", "undrip", "trc"],
        "Infrastructure": ["infrastructure", "transportation", "energy corridor", "lng", "pipelines"],
        "Jobs and Employment": ["jobs", "employment", "labor", "trade barriers", "union", "ccaa"],
        "International Trade and Relations": ["trade", "tariff", "relations", "cusma", "bonds"]
    }

    # Split text into paragraphs for categorization
    paragraphs = re.split(r'\n+', platform_text)

    for paragraph in paragraphs:
        for category, words in keywords.items():
            if any(word.lower() in paragraph.lower() for word in words):
                categorized[category] += paragraph + "\n"

    return categorized

# Example usage:
# if __name__ == "__main__":
#     sample_text = "We will reduce taxes and invest in renewable energy."
#     categorized = categorize_text(sample_text)
#     print(categorized)