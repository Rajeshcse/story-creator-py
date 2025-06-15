# utils/image_prompt.py
from typing import List, Dict

def generate_image_prompts(
    chapters: List[Dict[str, str]],
    style: str
) -> List[str]:
    """
    Given parsed chapters and an image style, create a list of
    image prompts for each chapter.

    Example output:
      "Watercolor painting of a shy dragon hiding behind a rock,The scene should be warm vibrant and colorful."
    """
    prompts = []
    for chap in chapters:
        title = chap["title"]
        # Take the first sentence or 20 words from the body
        snippet = " ".join(chap["text"].split()[:20]).rstrip(".") + "..."
        # Build prompt
        prompt = (
            f"{style} illustration of {title.replace('Chapter ', '')}, "
            f"showing {snippet}"
        )
        prompts.append(prompt)
    return prompts
