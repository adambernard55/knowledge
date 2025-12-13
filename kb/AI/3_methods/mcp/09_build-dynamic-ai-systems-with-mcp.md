---
title: Building Dynamic AI Systems with MCP
id: 20251022100015
version: 2
Author: Adam Bernard
steward:
date: 2025-12-10
category: AI
category_id:
Excerpt: A technical reference and Python implementation guide for the Model Context Protocol (MCP), detailing the core data structures, server/client architecture, and asynchronous design patterns.
Meta Description: Technical guide for developers on implementing the Model Context Protocol (MCP) in Python, including code examples for servers, clients, resources, and tools.
Primary_Keyword: Model Context Protocol implementation
Featured_Image:
doc_type: reference
relations:
aliases:
  - MCP Implementation
  - Python MCP
last_updated: 2025-12-10
tags:
  - AI
  - MCP
  - system-design
  - python
  - agentic-ai
summary: A technical reference and Python implementation guide for the Model Context Protocol (MCP), detailing the core data structures, server/client architecture, and asynchronous design patterns.
---

# Building Dynamic AI Systems with MCP

## 1. Overview

The Model Context Protocol (MCP) is a framework for building dynamic AI systems capable of interacting with external data and tools in real-time. It provides a standardized bridge for AI models to access live resources, execute functions, and adapt to changing contexts, enabling a modular, tool-augmented approach to AI. This document provides a technical blueprint and Python implementation for the core components of an MCP system.

## 2. Core Concepts & Data Structures

MCP is built on three fundamental data structures that facilitate structured information flow between an AI system and its environment.

-   **Resource**: Represents external data or documents (e.g., a file, a database record).
-   **Tool**: Represents an executable function or capability the AI can use (e.g., an API call, a data analysis function).
-   **Message**: Represents a single unit of communication, forming a contextual history of interactions.

### Python Implementation (`dataclasses`)

```python
from dataclasses import dataclass, asdict
from typing import Dict, List, Any, Optional, Callable
from datetime import datetime

@dataclass
class Resource:
   uri: str
   name: str
   description: str
   mime_type: str
   content: Any = None

@dataclass
class Tool:
   name: str
   description: str
   parameters: Dict[str, Any]
   handler: Optional[Callable] = None

@dataclass
class Message:
   role: str
   content: str
   timestamp: str = None
   def __post_init__(self):
       if not self.timestamp:
           self.timestamp = datetime.now().isoformat()
```

## 3. System Architecture

The system consists of two primary components: a server to manage resources and tools, and a client that interacts with the server to augment the AI's capabilities.

-   **MCPServer**: Manages a collection of resources and tools. It handles requests from clients to retrieve resource content and execute tools.
-   **MCPClient**: Connects to one or more servers to query available resources, fetch data, and call tools. It maintains a local context of all interactions, enabling stateful communication.

## 4. Python Implementation

### 4.1. MCPServer Class

The server manages the registration and execution of resources and tools, supporting asynchronous operations for efficiency.

```python
import asyncio

class MCPServer:
   def __init__(self, name: str):
       self.name = name
       self.resources: Dict[str, Resource] = {}
       self.tools: Dict[str, Tool] = {}
       self.capabilities = {"resources": True, "tools": True, "prompts": True, "logging": True}

   def register_resource(self, resource: Resource) -> None:
       self.resources[resource.uri] = resource

   def register_tool(self, tool: Tool) -> None:
       self.tools[tool.name] = tool

   async def get_resource(self, uri: str) -> Optional[Resource]:
       await asyncio.sleep(0.1) # Simulate I/O
       return self.resources.get(uri)

   async def execute_tool(self, tool_name: str, arguments: Dict[str, Any]) -> Any:
       if tool_name not in self.tools:
           raise ValueError(f"Tool '{tool_name}' not found")
       tool = self.tools[tool_name]
       if tool.handler:
           return await tool.handler(**arguments)
       return {"status": "executed", "tool": tool_name, "args": arguments}

   def list_resources(self) -> List[Dict[str, str]]:
       return [{"uri": r.uri, "name": r.name, "description": r.description} for r in self.resources.values()]

   def list_tools(self) -> List[Dict[str, Any]]:
       return [{"name": t.name, "description": t.description, "parameters": t.parameters} for t in self.tools.values()]
```

### 4.2. MCPClient Class

The client connects to servers, queries them, and maintains a contextual memory of all interactions.

```python
class MCPClient:
   def __init__(self, client_id: str):
       self.client_id = client_id
       self.connected_servers: Dict[str, MCPServer] = {}
       self.context: List[Message] = []

   def connect_server(self, server: MCPServer) -> None:
       self.connected_servers[server.name] = server

   async def query_resources(self, server_name: str) -> List[Dict[str, str]]:
       if server_name not in self.connected_servers:
           raise ValueError(f"Not connected to server: {server_name}")
       return self.connected_servers[server_name].list_resources()

   async def fetch_resource(self, server_name: str, uri: str) -> Optional[Resource]:
       server = self.connected_servers[server_name]
       resource = await server.get_resource(uri)
       if resource:
           self.add_to_context(Message(role="system", content=f"Fetched resource: {resource.name}"))
       return resource

   async def call_tool(self, server_name: str, tool_name: str, **kwargs) -> Any:
       server = self.connected_servers[server_name]
       result = await server.execute_tool(tool_name, kwargs)
       self.add_to_context(Message(role="system", content=f"Tool '{tool_name}' executed"))
       return result

   def add_to_context(self, message: Message) -> None:
       self.context.append(message)

   def get_context(self) -> List[Dict[str, Any]]:
       return [asdict(msg) for msg in self.context]
```

### 4.3. Example Tool Handlers

These asynchronous functions simulate external operations that can be registered as tools.

```python
import random

async def analyze_sentiment(text: str) -> Dict[str, Any]:
   await asyncio.sleep(0.2)
   sentiments = ["positive", "negative", "neutral"]
   return {"text": text, "sentiment": random.choice(sentiments), "confidence": round(random.uniform(0.7, 0.99), 2)}

async def summarize_text(text: str, max_length: int = 100) -> Dict[str, str]:
   await asyncio.sleep(0.15)
   summary = text[:max_length] + "..." if len(text) > max_length else text
   return {"original_length": len(text), "summary": summary}

async def search_knowledge(query: str, top_k: int = 3) -> List[Dict[str, Any]]:
   await asyncio.sleep(0.25)
   mock_results = [{"title": f"Result {i+1} for '{query}'", "score": round(random.uniform(0.5, 1.0), 2)} for i in range(top_k)]
   return sorted(mock_results, key=lambda x: x["score"], reverse=True)
```

## 5. Demonstration Workflow

A typical workflow demonstrates the protocol in action:
1.  **Setup**: An `MCPServer` instance is initialized.
2.  **Registration**: Resources (e.g., documents) and tools (e.g., `analyze_sentiment`) are registered with the server.
3.  **Connection**: An `MCPClient` is initialized and connected to the server.
4.  **Interaction**: The client performs a series of actions, such as listing available resources, fetching the content of a specific resource, and calling various tools with arguments.
5.  **Context Management**: The client's context window is populated with a history of all operations performed, creating a stateful record of the interaction.

## 6. Key Architectural Principles

-   **Modularity**: MCP enables modular connections between an AI and its tools/resources, making systems easier to extend and maintain.
-   **External Context**: Resources provide a structured way to feed context from external data sources into the AI model.
-   **Dynamic Actions**: Tools empower the AI to perform dynamic operations and interact with its environment beyond simple text generation.
-   **Asynchronous Design**: The `async` architecture supports efficient I/O operations, making it suitable for scalable, real-world applications that interact with multiple APIs or data sources.