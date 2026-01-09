from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from prompts import BLOG_AGENT_SYSTEM_PROMPT
from tools import save_blog, generate_blog_image

# Load environment variables
load_dotenv()

def run_blog_agent(topic: str):
    # 1. Initialize the LLM
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.7
    )

    # 2. Tools available to the agent
    tools = [save_blog, generate_blog_image]

    # 3. Create the agent with system prompt
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.OPENAI_FUNCTIONS,
        system_message=BLOG_AGENT_SYSTEM_PROMPT,
        verbose=True
    )

    # 4. Run the agent (modern API)
    agent.invoke(
        {"input": f"Write a blog on the topic: {topic}"}
    )

if __name__ == "__main__":
    topic = input("Enter the topic for the blog: ")
    run_blog_agent(topic)
