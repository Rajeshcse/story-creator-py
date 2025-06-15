# utils/story_parser.py

import re
from typing import List, Dict

def parse_chapters(story_text: str) -> List[Dict[str, str]]:
    """
    Splits a generated story into chapters.

    Expects the story text to contain lines like:
        Chapter 1: Title of Chapter
        Once upon a time...
        Chapter 2: Next Title
        And so on...

    Returns a list of dicts:
        [
          {"title": "Chapter 1: Title of Chapter", "text": "Once upon a time..."},
          {"title": "Chapter 2: Next Title",   "text": "And so on..."},
          …
        ]
    """
    # Pattern matches lines starting with "Chapter <number>:"
    # The regex group captures the chapter header itself.
    pattern = r"(Chapter\s+\d+:\s+.+)"
    
    # Split on each header, keeping the header in the result list
    parts = re.split(pattern, story_text)
    
    chapters = []
    # parts will look like:
    #   ["", "Chapter 1: …", "text…", "Chapter 2: …", "text…", …]
    for idx in range(1, len(parts), 2):
        title = parts[idx].strip()
        body = parts[idx + 1].strip() if idx + 1 < len(parts) else ""
        chapters.append({"title": title, "text": body})
    
    return chapters
