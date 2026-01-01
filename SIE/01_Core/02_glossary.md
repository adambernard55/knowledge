---
title: SIE System Glossary
id: SIE/G-E-2
version: "1.0"
steward: Adam Bernard
updated: 2025-12-14
status: Active
doc_type: glossary
summary: Canonical definitions of all Strategic Intelligence Engine terms, concepts, and system components. Single source of truth for terminology across all documentation.
tags:
  - glossary
  - terminology
  - reference
  - system
relations:
  - SIE/01_Core/index
  - SIE/01_Core/00_core-purpose
aliases:
  - System Glossary
  - Terminology Reference
  - SIE Terms
---

# SIE System Glossary

This document provides canonical definitions for all Strategic Intelligence Engine terminology. All system documents should reference these definitions to maintain consistency.

---

## Core System Terms

### Master Hub

The client-facing name for a business's living, single source of truth, structured via our proprietary methodology. Technically implemented as a [[SIE/01_Core/02_glossary#Knowledge Core|Knowledge Core]].

**See also:** [[SIE/01_Core/02_glossary#Knowledge Core]], [[SIE/01_Core/02_glossary#Strategic Intelligence Engine (SIE)]]

### Knowledge Core

The technical term for the [[SIE/01_Core/02_glossary#Master Hub|Master Hub]]—the structured markdown repository maintained in Obsidian/Git that serves as the authoritative source of business intelligence. The Knowledge Core is the "Asset" that the [[SIE/01_Core/02_glossary#Strategic Intelligence Engine (SIE)|SIE]] operates upon.

**Technical Implementation:** Markdown files with YAML frontmatter, version-controlled via Git, structured according to the system schema.

**See also:** [[SIE/01_Core/02_glossary#Master Hub]], [[SIE/01_Core/02_glossary#Document Architecture]]

### Strategic Intelligence Engine (SIE)

Our proprietary technology and methodology that builds, governs, and learns from a client's [[SIE/01_Core/02_glossary#Master Hub|Master Hub]] to automate tasks and provide strategic insights. The SIE is the "Actor" that performs operations on the [[SIE/01_Core/02_glossary#Knowledge Core|Knowledge Core]].

**Core Functions:** Ingest & Structure, Govern & Maintain, Automate & Execute, Analyze & Synthesize

**See also:** [[SIE/01_Core/00_core-purpose|Core Purpose Document]]

---

## System Components

### Knowledge Pipeline (KPL)

The operational Phase 1 system that autonomously maintains knowledge across platforms (Obsidian → GitHub → WordPress → AI Engine → Pinecone). 

**Status:** Production-ready, proven operational system  
**Achievement:** 50+ articles, 99.9% uptime, $1,160/month demonstrated value  
**Function Demonstrated:** Automate & Execute

**See also:** [[SIE/04_Engine/KPL/index|KPL Documentation]], [[SIE/01_Core/02_glossary#Agent Loop]]

### Agent Loop

The Phase 2 extension that adds autonomous AI agents for content enrichment, proactive maintenance, and strategic insight generation. Builds upon the proven [[SIE/01_Core/02_glossary#Knowledge Pipeline (KPL)|KPL]] foundation.

**Status:** Architecture complete, development Q1-Q2 2025  
**Function Demonstrated:** Analyze & Synthesize  
**Technology Stack:** CrewAI, Python agents, vector similarity analysis

**See also:** [[The Agent Loop|Agent Loop Documentation]]

### Vector Embeddings

Mathematical representations of content that enable semantic similarity search and AI query capabilities. Generated automatically by the [[SIE/01_Core/02_glossary#Knowledge Pipeline (KPL)|KPL]] via AI Engine plugin.

**Technical Details:** Stored in Pinecone vector database, enables semantic search across entire knowledge base without keyword matching.

---

## Methodologies & Processes

### Ignition Sequence

Our proprietary, structured discovery process used to gather and organize the initial data set for the [[SIE/01_Core/02_glossary#Master Hub|Master Hub]]. This process transforms scattered business knowledge into structured, schema-compliant content.

**Output:** Initial [[SIE/01_Core/02_glossary#Knowledge Core|Knowledge Core]] with complete business context, strategy, and operational intelligence.

### Document Architecture

The foundational Stage 1 of system evolution. Established schema-driven content model with structured markdown and consistent metadata.

**Function Demonstrated:** Ingest & Structure  
**Achievement:** Proved scattered knowledge could be systematically organized

**See also:** [[SIE/01_Core/00_core-purpose#7.1 Evolutionary Stages]]

### Knowledge Graph

Stage 2 of system evolution. Added semantic relationships and cross-references to create interconnected knowledge network.

**Function Demonstrated:** Govern & Maintain  
**Achievement:** Proved relationships could be systematically tracked and maintained  
**Technical Implementation:** Bidirectional links, semantic relationships, graph queries

---

## Market & Service Categories

### Strategic Intelligence as a Service (SIaaS)

The ultimate market category; providing ongoing, AI-powered business insights as a subscription. Represents the productized offering of the [[SIE/01_Core/02_glossary#Strategic Intelligence Engine (SIE)|SIE]].

**Business Model:** Subscription-based intelligence delivery powered by autonomous [[SIE/01_Core/02_glossary#Agent Loop|Agent Loop]] analyzing client [[SIE/01_Core/02_glossary#Master Hub|Master Hub]]

---

## Usage Guidelines

1. **First Use:** Link to glossary terms on first use in all core documents: `[[glossary#Term Name]]`
2. **Consistency:** Always use canonical terms as defined here
3. **Updates:** New system terms must be added within 24 hours of introduction
4. **Cross-References:** Use "See also" sections to connect related concepts

---

## Document Control

**Version History:**
- v1.0 (2025-12-14): Initial glossary with proper header structure and cross-references