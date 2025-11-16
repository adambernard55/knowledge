---
title: oLLM
summary: oLLM is an open-source Python library designed to run large language models with extensive context on consumer-grade NVIDIA GPUs by offloading model weights and the KV cache to fast SSD storage.
category: AI Tools
difficulty: Advanced
last_updated: 2025-01-20
kb_status: published
tags:
  - ai
  - llm
  - open-source
  - self-hosting
  - inference
  - gpu
  - kv-cache
related_topics:
  - ai-models
  - llama
  - model-deployment
---

# oLLM

oLLM is a lightweight, open-source Python library built on PyTorch and Hugging Face Transformers. It enables users to run large language models (LLMs) with very long contexts (up to 100K tokens) on single, consumer-grade NVIDIA GPUs. It achieves this by aggressively offloading model weights and the attention KV cache to a fast local SSD, keeping VRAM usage exceptionally low.

## **Key Features:**

*   **SSD Offloading:** Streams layer weights and offloads the KV cache directly from an SSD to the GPU, making it possible to run models that would otherwise require significantly more VRAM.
*   **Low VRAM Footprint:** Designed to keep VRAM usage within 8–10 GB, making it compatible with popular consumer GPUs like the RTX 30xx and 40xx series.
*   **High-Precision Inference:** Explicitly avoids quantization, running models in their native FP16 or BF16 precision for maximum accuracy.
*   **Large Context Handling:** Capable of managing contexts of up to ~100,000 tokens by writing the large KV cache to disk instead of holding it in VRAM.
*   **Optimized for Speed:** Utilizes technologies like FlashAttention-2 and GPUDirect Storage (via KvikIO/cuFile) to maximize throughput from fast NVMe SSDs.
*   **Broad Model Support:** Supports various large models, including MoEs like Qwen3-Next-80B and standard models like Llama 3 and GPT-OSS-20B.

## **Use Cases:**

*   **Offline Data Analysis:** Analyzing or summarizing massive documents, codebases, or logs on a local machine without high-end hardware.
*   **Research & Experimentation:** Running and studying very large models (e.g., 80B+ parameters) without access to expensive multi-GPU servers.
*   **Compliance & Privacy:** Processing sensitive data in-house on consumer hardware, ensuring information never leaves the local environment.
*   **Batch Processing:** Ideal for non-interactive, high-volume tasks where inference speed is not the primary concern.

## **Pricing Overview:**
oLLM is free and open-source under the MIT license. The primary costs are associated with the required hardware:
*   A compatible NVIDIA GPU (Ampere, Ada, or Hopper series) with at least 8 GB of VRAM.
*   A very fast NVMe SSD to handle the constant offloading of weights and cache.
*   Sufficient host RAM and electricity.

## **Expert Notes & Tips:**
The core trade-off with oLLM is sacrificing throughput for accessibility. Inference speeds are low (e.g., ~0.5 tokens/second for an 80B model on an RTX 3060 Ti), making it unsuitable for real-time chat applications. The performance bottleneck shifts from VRAM to storage I/O, so using a high-quality NVMe SSD is critical for the best possible experience. Treat oLLM as a powerful tool for large-context, offline workloads, not as a replacement for production-grade serving stacks like vLLM.

**Direct Link:** [GitHub Repository](https://github.com/OpenNMT/oLLM) 