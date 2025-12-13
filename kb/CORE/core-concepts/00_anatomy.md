---
title: "Fueling the SIE: Anatomy of an Agent Knowledge Base"
id: kb/CORE/00_anatomy
version: "1.0"
steward: Adam Bernard
updated: 2025-11-27
status: Active
doc_type: reference_document
summary: Defines the architecture and components of the knowledge base (the Master Hub) that powers the Strategic Intelligence Engine's (SIE) agents, enabling them to perform complex reasoning and automated tasks with high accuracy and context.
tags:
  - knowledge-base
  - ai-agents
  - sie-engine
  - master-hub
  - rag
  - graphrag
  - data-governance
relations:
  - SIE/E/index
aliases:
  - Agent Knowledge Base
  - SIE Knowledge Architecture
  - Master Hub Anatomy
---

# Fueling the SIE: Anatomy of an Agent Knowledge Base

For the **Strategic Intelligence Engine (SIE)**, the knowledge base—referred to as the **Master Hub**—is the central nervous system. It is the curated repository of truth that fuels fast, accurate responses from the engine's specialized agents and enables them to perform complex, automated tasks. This document outlines the anatomy of that Master Hub.

The SIE framework relies on multiple specialized agents working in concert. A shared, coherent Master Hub is the essential component that allows them to share context, retain memory, and act as a collective intelligence, transforming a client's scattered knowledge into a living, intelligent asset.

A well-designed Master Hub ensures that all SIE agents have access to up-to-date and comprehensive institutional knowledge. This directly improves the consistency, accuracy, and governance of all engine-driven actions, from content generation to strategic analysis.

## What the Master Hub Contains

The Master Hub is designed to hold the full spectrum of a company’s operational reality, combining structured, semi-structured, and unstructured data. All data must conform to the SIE's master schema to be ingested.

-   **Procedures and Policies:** These are the operational rules for SIE agents. This includes style guides for content generation, coding conventions for automation scripts, compliance rules, and escalation paths for tasks requiring human approval, directly enforcing the principles in the [[lol/01_Core/01_governance-rules]].

-   **Structured Data:** Formatted in JSON, YAML, or CSV, this includes databases, API documentation, product catalogs, and service-level agreements. This machine-readable data is critical for tasks requiring precise, factual information.

-   **Semi-Structured Data:** This includes internal wikis, workflow guides, and detailed runbooks. Custom field mappings are used to define relationships between data points, allowing agents to interpret context beyond the raw data.

-   **Unstructured Data:** This includes text from documents, meeting notes, and PDFs, as well as media like images or diagrams. The Master Hub also includes "negative examples"—what not to say or do—and contextual decision trees to help agents navigate edge cases.

-   **Memory and Relationships:** The Master Hub maintains persistent memory of past interactions, such as prompts and support tickets, to ensure continuity. Crucially, it emphasizes explicit connections between data points, creating a rich knowledge graph rather than a simple collection of documents.

## Implementing the Master Hub

At its core, the Master Hub is built on two main components: an object store for scalable storage and a vector database for semantic search. This architecture is designed to be layered on top of a client's existing systems, using APIs and connectors to make data accessible to SIE agents without requiring a complete infrastructure overhaul.

The greatest challenge is not creation, but maintenance. To solve this, SIE agents are designed to participate in the upkeep, capturing new information and flagging stale data to keep the Master Hub fresh and accurate.

## Connecting Agents to the Master Hub

SIE agents connect to the Master Hub using a multi-modal retrieval strategy to ensure the best possible context is found for any given task.

-   **Retrieval-Augmented Generation (RAG):** This is the primary method. Agents use vector search to find semantically similar concepts and inject them as context into their operational prompts.
-   **GraphRAG:** For more complex reasoning, agents leverage GraphRAG. This technique represents the Master Hub as a knowledge graph, allowing agents to understand the relationships *between* nodes of information, not just the information itself. This provides "multi-node" knowledge, enabling a deeper level of analysis.
-   **Keyword Search:** For finding exact matches, such as a specific product SKU or rule ID, traditional keyword search is also employed.

## No ‘One-Size-Fits-All’

While the SIE provides a standardized infrastructure (vector databases, embedding models, retrieval strategies), each client's Master Hub is unique. The ontologies, schemas, and business logic are highly customized to reflect the client's specific domain and operational reality. This customization is a fundamental requirement for achieving a positive return on investment.

The "how" of the engine is standardized, but the "what"—the client's unique data moat—remains wildly different and is the source of their competitive advantage.

## The Mandate: Keep the Knowledge Fresh

The core purpose of the SIE is to be a *living* asset. Therefore, its knowledge must be current. **Freshness, or a lack thereof, is the silent killer of any AI knowledge system.** Since institutional knowledge is constantly evolving, the primary ongoing task is to update the Master Hub to keep its data fresh, without duplicating information or breaking agentic behavior. This is the most significant challenge and the highest-priority maintenance task.