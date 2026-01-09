from dotenv import load_dotenv
load_dotenv()

from langchain.tools import tool
from pathlib import Path
from openai import OpenAI
import base64

# Initialize OpenAI client
client = OpenAI()

# Directories
OUTPUT_DIR = Path("output")
IMAGE_DIR = OUTPUT_DIR / "images"

OUTPUT_DIR.mkdir(exist_ok=True)
IMAGE_DIR.mkdir(parents=True, exist_ok=True)

@tool
def save_blog(content: str) -> str:
    """
    Save the blog content to a markdown file.
    """
    file_path = OUTPUT_DIR / "blog.md"
    file_path.write_text(content, encoding="utf-8")
    return f"Blog saved to {file_path}"

@tool
def generate_blog_image(prompt: str) -> str:
    """
    Generate a blog header image using an AI image model and save it locally.
    """
    image_path = IMAGE_DIR / "header.png"

    result = client.images.generate(
        model="gpt-image-1",
        prompt=prompt,
        size="1024x1024"
    )

    image_base64 = result.data[0].b64_json
    image_bytes = base64.b64decode(image_base64)

    with open(image_path, "wb") as f:
        f.write(image_bytes)

    return f"Blog image generated and saved to {image_path}"
