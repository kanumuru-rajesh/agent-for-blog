from langchain.tools import tool
from pathlib import Path

OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)

@tool
def save_Blog(content : str ) -> str:
    """
    Save the blog content to a markdown file
    """
    file_path = OUTPUT_DIR / "blog.md"
    file_path.write_text(content, encoding="utf-8")
    return f"Blog saved to {file_path}"