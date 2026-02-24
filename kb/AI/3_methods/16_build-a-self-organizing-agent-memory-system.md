---
title: "Build a Self-Organizing Agent Memory System"
id: "kb/AI/methods/agent-memory-sqlite"
version: "1.1"
steward: "Adam Bernard"
updated: "2026-02-16"
status: "Active"
doc_type: "SOP"
summary: "A technical guide for implementing a self-organizing, long-term memory system for AI agents using SQLite and scene-based consolidation."
tags:
  - "ai-agents"
  - "memory-architecture"
  - "python"
  - "sqlite"
  - "rag"
relations:
  - "kb/CORE/core-concepts/00_anatomy"
  - "kb/AI/3_methods/mcp/12_building-a-local-mcp-client"
aliases:
  - "Agent Memory Tutorial"
  - "SQLite Memory System"
target_audience: "Developers"
security_level: "Internal"
owner_team: "Engineering"

# --- AI & RAG Enhancement ---
semantic_summary: >
  This document details a Python implementation of a self-organizing memory system for AI agents. It uses SQLite to store 'memory cells' and 'scenes', separating the reasoning logic from memory management. Key features include full-text search, salience scoring, and automated summarization of interaction scenes to enable long-term reasoning without context window bloat.
synthetic_questions:
  - "How do I build a long-term memory system for an AI agent?"
  - "What is the difference between memory cells and scenes in agent architecture?"
  - "How can SQLite be used for agent memory?"
key_concepts:
  - "Self-Organizing Memory"
  - "Scene Consolidation"
  - "Memory Cells"
  - "Salience Scoring"

# --- SEO & Publication ---
primary_keyword: "AI agent memory system"
seo_title: "Building a Self-Organizing AI Agent Memory System with SQLite"
meta_description: "Learn how to build a persistent, self-organizing memory system for AI agents using Python and SQLite to enable long-term reasoning."
excerpt: "A step-by-step guide to architecting a self-organizing memory system for AI agents. This implementation separates memory management from reasoning, using SQLite to structure interactions into 'cells' and 'scenes' for long-term context retention."
cover_image: "assets/images/agent-memory-architecture.png"
---

# How to Build a Self-Organizing Agent Memory System for Long-Term AI Reasoning

## Strategic Context
This guide provides a practical implementation for the **Memory and Relationships** layer defined in [[00_anatomy|Anatomy of a Knowledge Core]]. While the Master Hub serves as the global source of truth, individual agents require local, episodic memory to maintain context over long horizons. This system solves the "amnesia problem" by structuring interactions into persistent **Knowledge Units** rather than raw logs.

---

## Implementation Guide

In this tutorial, we build a self-organizing memory system for an agent that goes beyond storing raw conversation history and instead structures interactions into persistent, meaningful knowledge units. We design the system so that reasoning and memory management are clearly separated, allowing a dedicated component to extract, compress, and organize information. At the same time, the main agent focuses on responding to the user. We use structured storage with SQLite, scene-based grouping, and summary consolidation.

### 1. Core Runtime Setup

We set up the core runtime by importing all required libraries and securely collecting the API key at execution time. We initialize the language model client and define a single helper function that standardizes all model calls.

```python
import sqlite3
import json
import re
from datetime import datetime
from typing import List, Dict
from getpass import getpass
from openai import OpenAI


OPENAI_API_KEY = getpass("Enter your OpenAI API key: ").strip()
client = OpenAI(api_key=OPENAI_API_KEY)


def llm(prompt, temperature=0.1, max_tokens=500):
   return client.chat.completions.create(
       model="gpt-4o-mini",
       messages=[{"role": "user", "content": prompt}],
       temperature=temperature,
       max_tokens=max_tokens
   ).choices[0].message.content.strip()
````

### 2. The Memory Database Schema

We define a structured memory database that persists information across interactions. We create tables for atomic memory units (`mem_cells`), higher-level scenes (`mem_scenes`), and a full-text search index (`mem_cells_fts`) to enable symbolic retrieval.

```python
class MemoryDB:
   def __init__(self):
       self.db = sqlite3.connect(":memory:")
       self.db.row_factory = sqlite3.Row
       self._init_schema()


   def _init_schema(self):
       self.db.execute("""
       CREATE TABLE mem_cells (
           id INTEGER PRIMARY KEY,
           scene TEXT,
           cell_type TEXT,
           salience REAL,
           content TEXT,
           created_at TEXT
       )
       """)


       self.db.execute("""
       CREATE TABLE mem_scenes (
           scene TEXT PRIMARY KEY,
           summary TEXT,
           updated_at TEXT
       )
       """)


       self.db.execute("""
       CREATE VIRTUAL TABLE mem_cells_fts
       USING fts5(content, scene, cell_type)
       """)


   def insert_cell(self, cell):
       self.db.execute(
           "INSERT INTO mem_cells VALUES(NULL,?,?,?,?,?)",
           (
               cell["scene"],
               cell["cell_type"],
               cell["salience"],
               json.dumps(cell["content"]),
               datetime.utcnow().isoformat()
           )
       )
       self.db.execute(
           "INSERT INTO mem_cells_fts VALUES(?,?,?)",
           (
               json.dumps(cell["content"]),
               cell["scene"],
               cell["cell_type"]
           )
       )
       self.db.commit()
```

### 3. Retrieval and Scene Logic

We focus on memory retrieval and scene maintenance logic. We implement safe full-text search by sanitizing user queries and adding a fallback strategy when no lexical matches are found.

```python
   def get_scene(self, scene):
       return self.db.execute(
           "SELECT * FROM mem_scenes WHERE scene=?", (scene,)
       ).fetchone()


   def upsert_scene(self, scene, summary):
       self.db.execute("""
       INSERT INTO mem_scenes VALUES(?,?,?)
       ON CONFLICT(scene) DO UPDATE SET
           summary=excluded.summary,
           updated_at=excluded.updated_at
       """, (scene, summary, datetime.utcnow().isoformat()))
       self.db.commit()


   def retrieve_scene_context(self, query, limit=6):
       tokens = re.findall(r"[a-zA-Z0-9]+", query)
       if not tokens:
           return []


       fts_query = " OR ".join(tokens)


       rows = self.db.execute("""
       SELECT scene, content FROM mem_cells_fts
       WHERE mem_cells_fts MATCH ?
       LIMIT ?
       """, (fts_query, limit)).fetchall()


       if not rows:
           rows = self.db.execute("""
           SELECT scene, content FROM mem_cells
           ORDER BY salience DESC
           LIMIT ?
           """, (limit,)).fetchall()


       return rows


   def retrieve_scene_summary(self, scene):
       row = self.get_scene(scene)
       return row["summary"] if row else ""
```

### 4. The Memory Manager

We implement the dedicated memory management component responsible for structuring experience. We extract compact memory representations from interactions, store them, and periodically consolidate them into stable scene summaries.

```python
class MemoryManager:
   def __init__(self, db: MemoryDB):
       self.db = db


   def extract_cells(self, user, assistant) -> List[Dict]:
       prompt = f"""
Convert this interaction into structured memory cells.


Return JSON array with objects containing:
- scene
- cell_type (fact, plan, preference, decision, task, risk)
- salience (0-1)
- content (compressed, factual)


User: {user}
Assistant: {assistant}
"""
       raw = llm(prompt)
       raw = re.sub(r"```json|```", "", raw)


       try:
           cells = json.loads(raw)
           return cells if isinstance(cells, list) else []
       except Exception:
           return []


   def consolidate_scene(self, scene):
       rows = self.db.db.execute(
           "SELECT content FROM mem_cells WHERE scene=? ORDER BY salience DESC",
           (scene,)
       ).fetchall()


       if not rows:
           return


       cells = [json.loads(r["content"]) for r in rows]


       prompt = f"""
Summarize this memory scene in under 100 words.
Keep it stable and reusable for future reasoning.


Cells:
{cells}
"""
       summary = llm(prompt, temperature=0.05)
       self.db.upsert_scene(scene, summary)


   def update(self, user, assistant):
       cells = self.extract_cells(user, assistant)


       for cell in cells:
           self.db.insert_cell(cell)


       for scene in set(c["scene"] for c in cells):
           self.consolidate_scene(scene)
```

### 5. The Worker Agent

We define the worker agent that performs reasoning while remaining memory-aware. We retrieve relevant scenes, assemble contextual summaries, and generate responses grounded in long-term knowledge.

```python
class WorkerAgent:
   def __init__(self, db: MemoryDB, mem_manager: MemoryManager):
       self.db = db
       self.mem_manager = mem_manager


   def answer(self, user_input):
       recalled = self.db.retrieve_scene_context(user_input)
       scenes = set(r["scene"] for r in recalled)


       summaries = "\n".join(
           f"[{scene}]\n{self.db.retrieve_scene_summary(scene)}"
           for scene in scenes
       )


       prompt = f"""
You are an intelligent agent with long-term memory.


Relevant memory:
{summaries}


User: {user_input}
"""
       assistant_reply = llm(prompt)
       self.mem_manager.update(user_input, assistant_reply)
       return assistant_reply


# --- Execution ---

db = MemoryDB()
memory_manager = MemoryManager(db)
agent = WorkerAgent(db, memory_manager)


print(agent.answer("We are building an agent that remembers projects long term."))
print(agent.answer("It should organize conversations into topics automatically."))
print(agent.answer("This memory system should support future reasoning."))


for row in db.db.execute("SELECT * FROM mem_scenes"):
   print(dict(row))
```

## Summary

In this tutorial, we demonstrated how an agent can actively curate its own memory and turn past interactions into stable, reusable knowledge rather than ephemeral chat logs. We enabled memory to evolve through consolidation and selective recall, which supports more consistent and grounded reasoning across sessions.

### See Also

- [Building a Local MCP Client](app://obsidian.md/kb/AI/3_methods/mcp/12_building-a-local-mcp-client)
- [Anatomy of a Knowledge Core](app://obsidian.md/kb/CORE/core-concepts/00_anatomy)