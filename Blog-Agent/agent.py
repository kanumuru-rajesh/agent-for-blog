import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from langchain.prompts import SystemMessagePromptTemplate
from tools import save_Blog

# Load environment variables
load_dotenv()

def run_blog_agent(topic : str):
    # 1. Initialize the LLM
    llm = ChatOpenAI(
        model_name="gpt-3.5-turbo",
        temperature=0.7
    )

    # 2. System prompt
    system_prompt = """
    You are a blog writing assistant.
    Your goal is to write a clear, well-structured technical blog
    in markdown format.

    After writing the blog, you MUST save it using the save_blog tool.
    """

    # 3. Tools available to the agent
    tools = [save_Blog]

    # 4. Create the agent 
    agent = initialize_agent(
        agent=AgentType.OPENAI_FUNCTIONS,
        tools=tools,
        llm=llm,
        verbose=True
    )

    # 5. Run the agent
    agent.run(f"Write a blog on the topic: {topic}")

if __name__ == "__main__":
    topic = input("Enter the topic for the blog: ")
    run_blog_agent(topic)