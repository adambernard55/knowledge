---
title: "Implementation Outline: Building the Research Agent"
id: 20260101074800
version: 1
Author: Adam Bernard
steward:
date: 2026-01-01
category:
category_id:
Excerpt:
Meta Description:
Primary_Keyword:
Featured_Image:
doc_type:
relations:
aliases:
last_updated: 2026-01-01
tags:
---

### Implementation Outline: Building the Research Agent

This guide will walk you through setting up the environment, creating the necessary tools, defining the agent, and providing a simple interface to run it.

#### Phase 0: Environment Setup & Prerequisites

First, let's set up the project structure and install the required libraries as outlined in your document.

1. **Create the Project Directory:**  
    Based on your plan, create the following folder structure:
    
    ```
    sie-agent-loop/
    ├── .env
    ├── requirements.txt
    ├── agents/
    │   ├── __init__.py
    │   └── research_agent.py
    └── tools/
        ├── __init__.py
        ├── pinecone_tool.py
        ├── web_search_tool.py
        └── content_scraping_tool.py
    ```
    
2. **Set up Python Environment:**
    
    ```bash
    cd sie-agent-loop
    python3 -m venv venv
    source venv/bin/activate
    ```
    
3. **Install Dependencies:**  
    Create a `requirements.txt` file with the initial dependencies for this agent:
    
    ```
    crewai
    langchain-openai
    python-dotenv
    fastapi
    uvicorn
    tavily-python
    firecrawl-py
    pinecone-client
    ```
    
    Then, install them:
    
    ```bash
    pip install -r requirements.txt
    ```
    
4. **Configure Environment Variables (`.env` file):**  
    Create a `.env` file in the root of `sie-agent-loop/`. You will need API keys for the services Agent A will use.
    
    ```
    OPENAI_API_KEY="sk-..."
    TAVILY_API_KEY="tvly-..."
    FIRECRAWL_API_KEY="fc-..."
    PINECONE_API_KEY="..."
    PINECONE_ENVIRONMENT="..."
    PINECONE_INDEX_NAME="..."
    ```
    

---

#### Phase 1: Implementing the Agent's Core Tools

An agent is only as good as its tools. Let's create the Python functions for its primary capabilities.

1. **Web Search Tool (`tools/web_search_tool.py`):**  
    This tool will use Tavily for LLM-optimized web searches.
    
    ```python
    # tools/web_search_tool.py
    from crewai_tools import tool
    from tavily import TavilyClient
    import os
    
    @tool("Web Search Tool")
    def web_search(query: str) -> str:
        """
        Performs a web search using Tavily to find recent and relevant information.
        Use this for any external research needs.
        
        Args:
            query: The search query.
        
        Returns:
            A formatted string of search results.
        """
        tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
        results = tavily.search(query=query, search_depth="advanced", max_results=5)
        return "\n---\n".join([f"URL: {res['url']}\nContent: {res['content']}" for res in results['results']])
    ```
    
2. **Content Scraping Tool (`tools/content_scraping_tool.py`):**  
    This tool will use Firecrawl to get clean, structured content from a URL.
    
    ```python
    # tools/content_scraping_tool.py
    from crewai_tools import tool
    from firecrawl import FirecrawlApp
    import os
    
    @tool("Content Scraper Tool")
    def scrape_url(url: str) -> str:
        """
        Scrapes a URL to extract its main content in a clean, readable format.
        Use this to read the content of a specific webpage found during a search.
        
        Args:
            url: The URL to scrape.
            
        Returns:
            The cleaned markdown content of the page.
        """
        firecrawl = FirecrawlApp(api_key=os.getenv("FIRECRAWL_API_KEY"))
        scraped_data = firecrawl.scrape_url(url)
        return scraped_data.get('markdown', 'Error: Could not retrieve markdown content.')
    ```
    
3. **Knowledge Core Tool (`tools/pinecone_tool.py`):**  
    You already have an excellent implementation in your document. Copy that code into this file. It allows the agent to query your internal knowledge base first.
    

---

#### Phase 2: Defining the Research Agent and a Test Task

Now, let's define the agent itself using CrewAI and give it a task to perform.

1. **Create the Agent Definition (`agents/research_agent.py`):**  
    This file will define the agent's persona and capabilities by assigning it the tools we just built.
    
    ```python
    # agents/research_agent.py
    from crewai import Agent
    from tools.web_search_tool import web_search
    from tools.content_scraping_tool import scrape_url
    from tools.pinecone_tool import query_knowledge_core
    
    research_agent = Agent(
        role="External Intelligence Gatherer",
        goal="To conduct thorough, fact-based research on any given topic by leveraging both internal knowledge and external web sources.",
        backstory="""You are a world-class research analyst, skilled in sifting through noise to find the most relevant and up-to-date information. You are meticulous about fact-checking and always prioritize authoritative sources. You start by checking the internal Knowledge Core before searching the web to supplement and validate findings.""",
        tools=[query_knowledge_core, web_search, scrape_url],
        verbose=True,
        allow_delegation=False
    )
    ```
    
2. **Create a Test Runner Script (`run_test.py`):**  
    Create this file in the root directory to test the agent.
    
    ```python
    # run_test.py
    from crewai import Task, Crew
    from agents.research_agent import research_agent
    from dotenv import load_dotenv
    
    load_dotenv()
    
    # Define the research task based on the example in your document
    research_task = Task(
        description="""
        Research the latest developments in 'semantic depth' from authoritative SEO sources published in the last 6 months. 
        
        Your final answer must be a comprehensive report that includes:
        1. A summary of what 'semantic depth' means in 2026.
        2. The top 3-5 key findings or new strategies.
        3. Citations for each finding with URLs.
        4. A check against our internal Knowledge Core to see what we've already written on the topic.
        """,
        agent=research_agent,
        expected_output="A detailed research report in markdown format."
    )
    
    # Form the crew and kick it off
    crew = Crew(
        agents=[research_agent],
        tasks=[research_task],
        verbose=2
    )
    
    result = crew.kickoff()
    
    print("\n\n########################")
    print("## Research Report")
    print("########################\n")
    print(result)
    ```
    

---

#### Phase 3: Running and Validating the Agent

Now you can run your first agent task from the command line.

1. **Activate your environment:**
    
    ```bash
    source venv/bin/activate
    ```
    
2. **Run the test script:**
    
    ```bash
    python run_test.py
    ```
    

You will see the agent's thought process in the terminal as it decides which tools to use (first `query_knowledge_core`, then `web_search`, then potentially `scrape_url`) to complete the task. The final, formatted report will be printed at the end.

---

#### Next Steps: Moving Towards Phase 2A Completion

This outline gets you a functional, command-line-driven Research Agent. To fully realize the Phase 2A vision from [The Agent Loop](obsidian://open?file=SIE%2F04_Engine%2FLOOP%2FThe%20Agent%20Loop.md), your next steps would be:

1. **Build the FastAPI Server:** Create a `server/main.py` file to wrap the agent logic in an API endpoint. This will allow you to trigger the agent via a web request (and eventually, a WordPress webhook).
2. **Integrate Logging:** Implement the logging strategy to write agent actions to `SIE/09_Logs/agent-actions.md`.
3. **Add the WordPress Tool:** Implement the `update_wordpress_post` tool from your document and add it to the agent's toolset, allowing it to save its findings as a draft.
4. **Connect to Webhooks:** Once the FastAPI server is running, configure WordPress to send a webhook to your server's endpoint whenever a post is saved, officially connecting the Agent Loop to your Knowledge Pipeline.

