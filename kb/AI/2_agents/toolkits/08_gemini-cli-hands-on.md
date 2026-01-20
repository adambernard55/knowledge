---
title: Hands-on Guide to Gemini CLI
id: kb/AI/toolkits/gemini-cli
version: "1.0"
steward: Adam Bernard
updated: 2026-01-20
status: Active
doc_type: Reference
summary: Comprehensive guide to installing, configuring, and using Gemini CLI - Google's open-source AI agent that brings Gemini's power directly into your terminal with built-in tools, MCP server support, and autonomous workflow capabilities.
tags:
  - gemini
  - cli
  - ai-agents
  - toolkits
  - mcp
  - google
  - terminal
  - automation
  - workflows
relations:
  - kb/AI/2_agents/00_introduction-to-ai-agents
  - kb/AI/2_agents/01_ai-agents-running-workflows
  - kb/AI/3_methods/mcp/1_mcp-foundations-and-architecture
  - kb/AI/3_methods/mcp/2_mcp-connectors-and-integrations
  - kb/AI/2_agents/toolkits/index
aliases:
  - Gemini CLI
  - Gemini Command Line Interface
  - Google Gemini CLI
  - Gemini Terminal Agent
target_audience: Developer
security_level: Public
owner_team: Knowledge
semantic_summary: Gemini CLI is an open-source AI agent from Google that operates directly in your terminal, featuring built-in tools for file operations, web search, code execution, and extensibility through MCP servers. This guide covers installation, configuration, tool usage, MCP server setup (GitHub, Cloud Run), and practical use cases from code generation to database operations and automation.
synthetic_questions:
  - How do I install and configure Gemini CLI?
  - What built-in tools does Gemini CLI provide?
  - How do I set up MCP servers with Gemini CLI?
  - Can Gemini CLI execute shell commands and automate workflows?
  - What are the differences between Gemini CLI's interactive and non-interactive modes?
  - How does Gemini CLI handle file operations and code generation?
key_concepts:
  - Gemini CLI
  - AI terminal agent
  - MCP servers
  - GitHub MCP integration
  - Cloud Run deployment
  - Built-in tools
  - Shell mode
  - Extensions system
  - Autonomous workflows
  - Tool permissions
primary_keyword: Gemini CLI
seo_title: "Gemini CLI: Complete Hands-On Guide to Google's AI Terminal Agent"
meta_description: "Master Gemini CLI with this comprehensive guide covering installation, MCP servers, built-in tools, and practical workflows."
excerpt: "Learn how to harness the power of Google's Gemini CLI - an open-source AI agent that brings autonomous intelligence directly to your terminal with built-in tools, MCP server support, and extensibility for real-world automation workflows."
---

# Hands-on Guide to Gemini CLI

## Introduction

Gemini CLI is Google's open-source AI agent that brings the power of Gemini directly into your terminal. Unlike traditional chatbots, Gemini CLI acts as an autonomous agent capable of executing tools, managing files, searching the web, and orchestrating complex workflows through the Model Context Protocol (MCP).

### What You'll Learn

1. Installing and configuring Gemini CLI
2. Working with built-in tools and commands
3. Configuring and using MCP servers (GitHub, Cloud Run)
4. Customizing Gemini CLI via configuration files
5. Practical use cases: code generation, file organization, database operations, and automation

### Prerequisites

This guide can be completed entirely within Google Cloud Shell (which comes with Gemini CLI pre-installed) or on your local machine with:

- Node.js 20+
- Chrome web browser
- A Google account
- Basic command-line familiarity

## Installation

### Option 1: Google Cloud Shell (Recommended for Getting Started)

Gemini CLI comes pre-installed in Google Cloud Shell. Simply activate Cloud Shell from the Google Cloud Console and run:

```bash
gemini --version
```

## Initial Configuration

### Theme Selection

On first launch, Gemini CLI prompts you to select a visual theme. Choose the one that matches your preferences:

![Theme selection interface](https://codelabs.developers.google.com/static/gemini-cli-hands-on/img/35a98edaf7f22e8e.png)

### Authentication

Gemini CLI supports three authentication methods:

1. **OAuth (Personal Account)** - Recommended for individual use
    - Free tier: 60 requests/min, 1,000 requests/day
    - Access to Gemini 2.5 Pro with 1 million token context window
2. **API Key** - For programmatic access
3. **Google Cloud Vertex AI** - For enterprise deployments

**For this guide, use OAuth with your personal Google Account.**

The authentication flow will open a browser window. After granting permissions, Gemini CLI is ready to use.

## Configuration Files

Gemini CLI stores settings in `settings.json` with the following precedence:

1. **System**: `/etc/gemini-cli/settings.json` (all users, highest priority)
2. **Workspace**: `.gemini/settings.json` (project-specific)
3. **User**: `~/.gemini/settings.json` (personal settings)

### Platform-Specific Paths

**Linux/Cloud Shell:**

- User: `~/.gemini/settings.json`
- System: `/etc/gemini-cli/settings.json`

**Windows:**

- User: `%USERPROFILE%\.gemini\settings.json`
- System: `%ProgramData%\gemini-cli\settings.json`

**macOS:**

- User: `~/.gemini/settings.json`
- System: `/etc/gemini-cli/settings.json`

### Example settings.json

```json
{
  "theme": "Default",
  "selectedAuthType": "oauth-personal"
}
```

## First Interaction

Launch Gemini CLI:

```bash
gemini
```

Try your first query:

```
Give me a famous quote on Artificial Intelligence and who said that?
```

**Expected Response:**

```
GoogleSearch Searching the web for: "famous quote on Artificial Intelligence and who said it"
...
✦ "The development of full artificial intelligence could spell the end of the human race." - Stephen Hawking.
```

Notice that Gemini CLI automatically invoked the **GoogleSearch** tool to ground its response with web data.

## Command-Line Parameters

View all available options:

```bash
gemini --help
```

### Model Selection

Gemini CLI supports two models:

- **gemini-2.5-pro** (default) - Highest capability
- **gemini-2.5-flash** - Faster, lower cost

Switch models at launch:

```bash
gemini -m "gemini-2.5-flash"
```

Or use the `/model` command within an active session to change models interactively.

### Non-Interactive Mode

Execute a single prompt without entering the interactive terminal:

```bash
gemini "What is the gcloud command to deploy to Cloud Run"
```

**Important:** Non-interactive mode does not:

- Allow follow-up questions
- Support tool authorization prompts
- Execute WriteFile or shell commands

## Built-in Tools

View available tools:

```
/tools
```

**Available Tools:**

- **Codebase Investigator Agent** - Analyze repository structure
- **Edit (replace)** - Modify file contents
- **FindFiles (glob)** - Search for files by pattern
- **GoogleSearch** - Web search with grounding
- **ReadFile** - Read file contents
- **ReadFolder (list_directory)** - List directory contents
- **SaveMemory** - Persist information across sessions
- **SearchText** - Search within file contents
- **Shell (run_shell_command)** - Execute shell commands
- **WebFetch** - Fetch web page content
- **WriteFile** - Create or update files
- **WriteTodos** - Manage task lists

### Tool Permissions

Gemini CLI requires explicit permission for sensitive operations (file writes, network access, shell execution). You can:

- **Allow once** - Execute the tool for this single request
- **Allow always** - Grant blanket permission for this session
- **Deny** - Block the tool execution

**Best Practice:** Use "Allow once" until you're confident in the tool's behavior. The `--yolo` flag bypasses all permission checks but is not recommended.

### Practical Example: Web Search + File Writing

**Prompt:**

```
Search for the latest headlines today in the world of finance and save them in a file named finance-news-today.txt
```

**What Happens:**

1. **GoogleSearch** tool executes to fetch financial news
2. **WriteFile** tool requests permission to create the file
3. After approval, the file is created with the search results

**Verify the file:**

```
read the contents of @finance-news-today.txt
```

The `@` symbol allows you to reference files in your current directory.

## Shell Mode

Press `!` to toggle shell mode, allowing you to execute system commands directly:

```bash
! pwd
! ls -la
! cat finance-news-today.txt
```

Press `!` again or hit `ESC` to return to AI interaction mode.

**Note:** Shell command outputs are included in the model's context window, so Gemini CLI can reason about the results.

## Gemini CLI Extensions

Extensions package prompts, MCP servers, and custom commands into reusable, shareable modules. They expand Gemini CLI's capabilities beyond built-in tools.

### Extensions Gallery

Browse all official and third-party extensions at:  
**[https://geminicli.com/extensions/](https://geminicli.com/extensions/)**

### Extension Management Commands

```bash
# List installed extensions
gemini extensions list

# Install an extension from a git repository
gemini extensions install <source> [--auto-update]

# Uninstall extensions
gemini extensions uninstall <names..>

# Update all extensions
gemini extensions update --all

# Enable/disable extensions
gemini extensions enable <name>
gemini extensions disable <name>

# Link a local extension for development
gemini extensions link <path>

# Create a new extension from a template
gemini extensions new <path> [template]

# Validate an extension
gemini extensions validate <path>
```

## Configuring MCP Servers

MCP servers extend Gemini CLI's capabilities by connecting to external systems and APIs through the Model Context Protocol.

### GitHub MCP Server

**Step 1: Install the Extension**

```bash
gemini extensions install https://github.com/github/github-mcp-server
```

**Step 2: Set Up GitHub Personal Access Token (PAT)**

1. Generate a PAT at: [https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)
2. Create a `.env` file or export an environment variable:

```bash
export GITHUB_MCP_PAT=<your_token_here>
```

**Step 3: Verify Installation**

Launch Gemini CLI and check available MCP servers:

```
/mcp list
```

**Expected Output:**

```
🟢 github (from github) - Ready (40+ tools)
  Tools:
  - add_comment_to_pending_review
  - create_branch
  - create_pull_request
  - get_file_contents
  - issue_read
  ...
```

**Step 4: Test the Integration**

```
Who am I on GitHub?
```

Gemini CLI will use the GitHub MCP Server's `get_me` tool to retrieve your profile information.

### Cloud Run MCP Server

**Step 1: Install the Extension**

```bash
gemini extensions install https://github.com/GoogleCloudPlatform/cloud-run-mcp
```

**Step 2: Verify Installation**

```
/mcp list
```

**Expected Output:**

```
🟢 cloud-run (from cloud-run) - Ready (8 tools, 2 prompts)
  Tools:
  - create_project
  - deploy_container_image
  - deploy_file_contents
  - deploy_local_folder
  - get_service
  - get_service_log
  - list_projects
  - list_services
  
  Prompts:
  - deploy
  - logs
```

**Step 3: Deploy to Cloud Run**

```
Deploy the current folder to Cloud Run as a new service named "my-app"
```

Gemini CLI will orchestrate the deployment using the Cloud Run MCP Server tools.

## Practical Use Cases

### 1. Vibe Coding: Generate and Deploy an Application

**Scenario:** Create a web application for a one-day technical event with 6 talks.

**Prompt:**

```
Generate a website for a 1-day event filled with technical talks. There are going to be 6 talks in a single track of 1 hour each. Each talk has the following information: title, 1 or maximum of 2 speakers, category (1 or maximum of 3 keywords), duration and a description. The website has a single page where users can see the schedule for the entire day with the timings. There will be one lunch break of an hour and the event starts at 10:00 AM. Keep a 10 minute transition between talks. I would like to use Node.js on the server side and standard HTML, JavaScript and CSS on the front-end. The users should be able to search the talks based on category.

I would like you to proceed in the following way:
1. Plan out how you would design and code this application.
2. Ask me for any clarifications along the way.
3. Once I am fine with it, do generate the code and provide me instructions to run and test locally.
```

**What Gemini CLI Does:**

1. Presents an architecture plan
2. Asks clarifying questions (lunch break timing, styling preferences)
3. Generates server-side (`server.js`) and client-side (`index.html`, `style.css`, `script.js`) code
4. Creates a `.gitignore` file
5. Provides instructions to run the application locally

**Follow-up: Push to GitHub**

```
Great! I would now like to push all of this to a new repository in my Github account. I would like to name this repository event-talks-app
```

Gemini CLI uses the GitHub MCP Server to:

1. Create the repository
2. Initialize Git (`git init`, `git add`, `git commit`)
3. Set up the remote and push the code

### 2. Working with an Existing GitHub Repository

**Scenario:** Understand a codebase, generate documentation, implement features, and manage issues.

**Understanding the Code:**

```
I would like to understand this project in detail. Help me understand the main features and then break it down into Server and Client side. Take a sample flow and show me how the request and response works.
```

**Generating Documentation:**

```
Generate a README file for this project.
```

**Implementing a New Feature:**

```
I would like to implement a new feature where the user is allowed to search by a specific Speaker too. First show me a plan of how you would implement this change and then we can generate the code.
```

**Creating GitHub Issues:**

```
I would like you to assess the application from a user experience point of view. Ease of use, responsiveness, helpful messages and more. Please come up with a list of improvements and I would like you to then create them as Issues in the Github repository.
```

**Working on an Issue:**

```
Please go through the Issue: <ISSUE_URL> and understand what changes need to be made. First discuss the plan and then show the proposed changes in code.
```

### 3. Organizing Files and Folders

**Navigate to a folder with various file types** (e.g., Desktop, Downloads):

```bash
cd ~/Downloads
gemini
```

**Create folders:**

```
Create the following folders "Images","Documents","Videos"
```

**Organize files by type:**

```
Go through all the files in this folder and then organize them by moving all the files ending with .jpg, .jpeg, .gif into the "Images" folder. Move all ".txt" files into the "Documents" folder. Move all the ".mp4" files in the "Videos" folder.
```

**Advanced: Summarize documents:**

```
For each document in the 'Documents' folder, create a txt file in the same folder named 'summary_ORIGINAL_FILENAME.txt' that contains a 3-sentence summary of the document's main points.
```

### 4. Processing Images (Multimodal AI)

**Scenario:** Extract invoice data from image files.

**Setup:**

1. Create a folder and download sample invoice images
2. Launch Gemini CLI from that folder

**Extract invoice information:**

```
The current folder contains a list of invoice files in Image format. Go through all the files in this folder and extract the following invoice information in the form of a table: Invoice No, Invoice Date, Invoice Sent By, Due Date, Due Amount.
```

**Add derived columns:**

```
List all files with .png extension in this folder. Extract the invoice information from it by reading them locally and display it in a table format containing the following column headers: Invoice No, Invoice Date, Invoice Sent By, Due Date, Due Amount. Add a column at the end of the table that shows a red cross emoji in case the due date is in the past.
```

### 5. Working with Databases

**Scenario:** Query a SQLite database using natural language.

**Setup:**

1. Install SQLite3 (pre-installed on most systems)
2. Download the [Chinook sample database](https://www.sqlitetutorial.net/wp-content/uploads/2018/03/chinook.zip)
3. Launch Gemini CLI from the database folder

**List tables:**

```
What tables are present in the file: chinook.db
```

**Query data:**

```
How many employees are there?
What is the schema of the invoices table?
Which are the top 3 invoices by total and which customers have placed those invoices?
```

Gemini CLI generates the correct SQL statements and executes them using the `sqlite3` command-line tool.

### 6. Generating Mock Data

**JSON array of customer reviews:**

```
Generate a JSON array of 3 synthetic customer reviews for a new smartphone. Each review should have 'reviewId' (string, UUID-like), 'productId' (string, e.g., 'SMARTPHONE_X'), 'rating' (integer, 1-5), 'reviewText' (string, 20-50 words), and 'reviewDate' (string, YYYY-MM-DD format).
```

**Mock API response:**

```
Generate a JSON array representing 7 daily sales records for a mock API endpoint. Each record should include 'date' (YYYY-MM-DD, chronologically increasing), 'revenue' (float, between 5000.00 and 20000.00), 'unitsSold' (integer, between 100 and 500), and 'region' (string, either 'North', 'South', 'East', 'West').
```

**SQL INSERT statements:**

```
Generate 5 SQL INSERT statements for a table named 'users' with columns: 'id' (INTEGER, primary key), 'username' (VARCHAR(50), unique), 'email' (VARCHAR(100)), 'password_hash' (VARCHAR(255)), 'created_at' (DATETIME, current timestamp). Ensure the password_hash is a placeholder string like 'hashed_password_X'.
```

## Best Practices

1. **Start with a clean working directory** to avoid unintended file operations
2. **Use "Allow once" permissions** until you're confident in tool behavior
3. **Review shell commands** before granting execution permission
4. **Leverage the `@` symbol** to reference files in your prompts
5. **Use non-interactive mode** for scripting and automation
6. **Organize extensions** by enabling/disabling based on current task
7. **Monitor the context window** - extensive shell output consumes tokens

## Advanced Configuration

### Custom GEMINI.md Files

Create a `GEMINI.md` file in your workspace to provide persistent context and instructions:

```markdown
# Project Context

This is a Node.js event management application built with Express.

## Coding Standards
- Use ES6 syntax
- Follow Airbnb style guide
- Include JSDoc comments for all functions

## Testing
- Use Jest for unit tests
- Aim for 80% code coverage
```

Gemini CLI automatically loads this context for all interactions in that directory.

### Creating Custom Extensions

```bash
# Create a new extension from a template
gemini extensions new my-extension

# Link for local development
gemini extensions link ./my-extension
```

## Troubleshooting

### Common Issues

**Tool permissions repeatedly required:**

- Use "Allow always" for trusted operations