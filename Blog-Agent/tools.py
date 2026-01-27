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
def save_blog(content: str, blog_id: str) -> str:
    """
    Save the blog content to a unique named markdown file.
    """
    file_path = OUTPUT_DIR / f"{blog_id}.md"
    file_path.write_text(content, encoding="utf-8")
    return f"Blog saved to {file_path}"

@tool
def generate_blog_image(prompt: str, blog_id: str) -> str:
    """
    Generate a blog header image and save it locally.
    """
    image_path = IMAGE_DIR / f"{blog_id}_header.png"

    result = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        response_format="b64_json"
    )

    image_bytes = base64.b64decode(result.data[0].b64_json)

    with open(image_path, "wb") as f:
        f.write(image_bytes)

    return f"Blog image generated and saved to {image_path}"
d