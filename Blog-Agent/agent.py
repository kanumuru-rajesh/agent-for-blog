from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from prompts import BLOG_AGENT_SYSTEM_PROMPT
from tools import save_blog, generate_blog_image
from datetime import datetime
import re

def generate_blog_id(topic: str) -> str:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", topic.lower()).strip("-")
    return f"{slug}_{timestamp}"

def run_blog_agent(topic: str):
    blog_id = generate_blog_id(topic)

    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.7
    )

    tools = [save_blog, generate_blog_image]

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.OPENAI_FUNCTIONS,
        agent_kwargs={
            "system_prompt": BLOG_AGENT_SYSTEM_PROMPT,
            },
        verbose=True
    )

    agent.invoke(
        {
            "input": f"""
Write a blog on the topic: {topic}

IMPORTANT:
- Use blog_id = "{blog_id}"
- Image path must be: images/{blog_id}_header.png
"""
        }
    )

if __name__ == "__main__":
    topic = input("Enter the topic for the blog: ")
    run_blog_agent(topic)