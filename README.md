#  Children's Storybook Generator

## Description

Py-Storybook Generator is a lightweight Python toolkit and web app that automatically turns your story ideas into fully illustrated storybooks. At its core, it:

Takes your text prompts (scene descriptions, character sketches, setting details)

Generates high-quality images on-the-fly using community or commercial AI backends (Stable Horde’s free API, Hugging Face Inference, or Replicate)

Encodes and displays each generated illustration in a Gradio-powered interface, so you can preview, tweak, and download your story pages in real time

Under the hood, it’s organized into:

app.py – a Gradio UI that collects prompts and shows results

utils/image_gen.py – interchangeable backends for queuing jobs, polling for completion, and returning Base64 PNGs

Environment-driven configuration (e.g. HF_TOKEN, STABLE_HORDE_KEY, REPLICATE_API_TOKEN) so you can switch providers without touching code

Whether you’re an author who wants instant visuals or a developer prototyping an AI-powered children’s book, Py-Storybook Generator gives you a ready-to-use pipeline for text-to-illustration.


## Installation

To install this project, follow these steps:

```bash
# Example installation command
# pip install -r requirements.txt
```

## Usage

Here's how to use my project:

```python
# Example usage code
# print("Hello from my project!")
```

## License

This project is licensed under the [Your License Name] - see the [LICENSE.md](LICENSE.md) file for details.
