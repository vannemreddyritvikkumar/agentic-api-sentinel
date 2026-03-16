# agentic-api-sentinel
Instead of a static scan that just looks for basic bugs, this is an Autonomous Agent built with LangGraph.

# 🛡️ Agentic API Sentinel

An autonomous AI Security Agent designed to perform **intelligent penetration testing** on REST APIs. 

### 🎯 The Problem
Standard security scanners (Dast/Sast) miss **Business Logic Flaws**. They can't "reason" that a user shouldn't be able to access another user's private data via a URL parameter.

### 🧠 The AI Solution
This project uses **LangGraph** to build a multi-step security agent that:
1. Parses OpenAPI documentation to map the attack surface.
2. Generates context-aware payloads for **OWASP Top 10** vulnerabilities (BOLA, Mass Assignment, Injection).
3. Evaluates system responses to distinguish between a blocked attempt (403) and a successful breach (200).

### 🛠 Tech Stack
- **Python / LangGraph** (Agentic Workflow)
- **OpenAI GPT-4o** (Attack Reasoning)
- **Requests** (Payload Execution)
