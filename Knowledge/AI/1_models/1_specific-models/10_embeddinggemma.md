---
title: EmbeddingGemma
summary: EmbeddingGemma is a state-of-the-art, open embedding model from Google, designed for on-device use and optimized for search, retrieval, and semantic similarity tasks.
category: AI Models
difficulty: Intermediate
last_updated: 2025-01-20
kb_status: published
tags:
  - ai
  - embedding-model
  - gemma
  - google
  - open-source
  - nlp
  - vector-search
related_topics:
  - ai-models
  - gemini
  - vector-databases
---

# EmbeddingGemma (Google)

EmbeddingGemma is a family of lightweight, state-of-the-art open embedding models from Google. Built with the same technology used for Gemini, these models are designed to create high-quality vector representations of text. Their small size makes them ideal for running on-device or in resource-constrained environments, powering tasks like search, retrieval, and classification without relying on large cloud-based infrastructure.

## **Key Features:**

*   **Efficient & Compact:** With a size of only 300 million parameters, EmbeddingGemma is small enough to run on laptops, desktops, and even mobile devices.
*   **High Performance:** Despite its small size, it delivers state-of-the-art performance on text retrieval benchmarks, making it highly competitive for its class.
*   **Multilingual:** Trained on a diverse dataset covering over 100 languages, making it effective for multilingual search and retrieval applications.
*   **Open Model:** Released as an open model, it is free to use and modify, democratizing access to powerful embedding technology for developers and researchers.
*   **Optimized for Retrieval:** Specifically designed to produce vector embeddings for tasks like semantic search, clustering, and Retrieval-Augmented Generation (RAG).

## **Use Cases:**

*   **Semantic Search:** Building search engines that understand the meaning of a query, not just keywords.
*   **Retrieval-Augmented Generation (RAG):** Finding relevant documents or text chunks to provide as context to a large language model, improving the accuracy of its answers.
*   **Document Clustering & Classification:** Automatically grouping similar articles, customer feedback, or other text data.
*   **Recommendation Systems:** Suggesting similar items or content based on their textual descriptions.
*   **On-Device AI:** Powering search and retrieval features in local applications where data privacy and offline capability are critical.

## **Pricing Overview:**
EmbeddingGemma is a free, open-source model. The primary costs are associated with the hardware required to run inference, which is minimal due to the model's small size. It can be easily run on consumer-grade CPUs and GPUs using tools like Ollama, Hugging Face Transformers, and others.

## **Expert Notes & Tips:**
EmbeddingGemma is not a conversational AI like [[2_gemini]] or [[1_chatgpt]]; it is a specialized tool for a specific but crucial part of the AI pipeline. Its main purpose is to convert text into numerical vectors that capture semantic meaning. This model is an excellent choice for building cost-effective and private RAG systems or for adding semantic search capabilities to any application without incurring API costs.

**Direct Link:** [Official Documentation](https://ai.google.dev/gemma/docs/embeddinggemma)

---

## EmbeddingGemma is a 300M parameter embedding model from Google.

embedding300m
## Models [View all →](https://ollama.com/library/embeddinggemma/tags)

| Name                                                                 | Size  | Context | Input |
|----------------------------------------------------------------------|-------|---------|-------|
| [embeddinggemma:latest](https://ollama.com/library/embeddinggemma:latest) | 622MB | 2K      | Text  |
| [embeddinggemma:300m](https://ollama.com/library/embeddinggemma:300m) | 622MB | 2K      | Text  |

![image.png](https://ollama.com/assets/library/embeddinggemma/9a20d963-4bf1-4177-9568-ca5d53a2d14e)

> This model requires [Ollama v0.11.10](https://github.com/ollama/ollama/releases/tag/v0.11.10) or later

**EmbeddingGemma** is a 300M parameter, state-of-the-art for its size, open embedding model from Google, built from Gemma 3 (with T5Gemma initialization) and the same research and technology used to create Gemini models. EmbeddingGemma produces vector representations of text, making it well-suited for search and retrieval tasks, including classification, clustering, and semantic similarity search. This model was trained with data in 100+ spoken languages.

The small size and on-device focus makes it possible to deploy in environments with limited resources such as mobile phones, laptops, or desktops, democratizing access to state of the art AI models and helping foster innovation for everyone.

### Benchmark

![image.png](https://ollama.com/assets/library/embeddinggemma/59a205f6-1711-4db4-8026-96d23fa2c9da)

#### Training Dataset

This model was trained on a dataset of text data that includes a wide variety of sources totaling approximately 320 billion tokens. Here are the key components:

- **Web Documents**: A diverse collection of web text ensures the model is exposed to a broad range of linguistic styles, topics, and vocabulary. The training dataset includes content in over 100 languages.
- **Code and Technical Documents**: Exposing the model to code and technical documentation helps it learn the structure and patterns of programming languages and specialized scientific content, which improves its understanding of code and technical questions.
- **Synthetic and Task-Specific Data**: Synthetically training data helps to teach the model specific skills. This includes curated data for tasks like information retrieval, classification, and sentiment analysis, which helps to fine-tune its performance for common embedding applications.

The combination of these diverse data sources is crucial for training a powerful multilingual embedding model that can handle a wide variety of different tasks and data formats.

### Reference

[Documentation](https://ai.google.dev/gemma/docs/embeddinggemma)