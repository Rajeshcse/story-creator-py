# app.py

import gradio as gr
from utils.story_gen        import generate_story
from utils.story_parser     import parse_chapters
from utils.image_prompt     import generate_image_prompts
from utils.image_gen  import generate_images

def story_pipeline(prompt: str, age_group: str, pages: int, style: str):
    # 1️⃣ Generate the raw story text via Gemini
    raw_story = generate_story(prompt, age_group, pages)
    
    # 2️⃣ Parse into chapters
    chapters = parse_chapters(raw_story)
    
    # 3️⃣ Create one image prompt per chapter
    image_prompts = generate_image_prompts(chapters, style)
    
    # 4️⃣ Generate images from the image prompts (commented out as per user request)
    # image_urls = generate_images(image_prompts)
    
    # 5️⃣ Build Markdown for the story
    md = "## ✨ Generated Story\n\n"
    for chap in chapters:
        md += f"### {chap['title']}\n\n{chap['text']}\n\n"

    # Prepare image prompts for display
    image_prompts_md = "## 🖼️ Generated Image Prompts\n\n"
    for i, img_prompt in enumerate(image_prompts):
        image_prompts_md += f"**Chapter {i+1}**: {img_prompt}\n\n"
    
    return md, image_prompts_md

with gr.Blocks(title="Children's Storybook Generator") as demo:
    gr.Markdown("# ✨ Children's Storybook Generator")
    gr.Markdown("Enter a fun idea, and watch it become a magical illustrated story!")

    with gr.Row():
        prompt    = gr.Textbox(label="Story Prompt", placeholder="e.g., A panda who wants to be a chef")
        age_group = gr.Radio(["3-5", "6-8", "9-12"], label="Age Group", value="3-5")
    with gr.Row():
        pages = gr.Slider(3, 10, value=5, step=1, label="Number of Pages")
        style = gr.Dropdown(["Watercolor", "Cartoon", "Paper Cutout"], value="Watercolor", label="Image Style")

    generate_button = gr.Button("Generate Story")
    story_output    = gr.Markdown()
    image_prompt_output = gr.Markdown(label="Generated Image Prompts")

    generate_button.click(
        fn=story_pipeline,
        inputs=[prompt, age_group, pages, style],
        outputs=[story_output, image_prompt_output]
    )

if __name__ == "__main__":
    demo.launch()
