# Blog Agent

This is a blog writing assistant powered by LangChain and OpenAI. The agent takes a topic as input and generates a well-structured technical blog post in markdown format.

## Prerequisites

- Python 3.9 or higher

## Setup

Follow these steps to set up the environment and run the agent.

### 1. Create a Virtual Environment

It is recommended to use a virtual environment to manage dependencies.

```bash
python3 -m venv venv
```

### 2. Activate the Virtual Environment

**macOS / Linux:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
.\venv\Scripts\activate
```

### 3. Install Dependencies

Install the required Python packages using pip:

```bash
pip install -r Blog-Agent/requirements.txt
```

### 4. Configuration

Create a `.env` file in the root directory of the project (if it doesn't already exist) and add your OpenAI API key:

```bash
OPENAI_API_KEY=your_openai_api_key_here
```

## Running the Agent

Once the environment is set up and activated, you can run the agent using the following command from the root directory:

```bash
python Blog-Agent/agent.py
```

Follow the on-screen prompts to enter a topic for your blog post. The generated blog will be saved automatically.
