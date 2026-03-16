# 🛡️ Agentic API Security Sentinel

An autonomous security researcher built with **LangGraph** to identify business logic flaws and compliance failures in financial APIs.

### 🚀 Key Capabilities
- **ISO 8583 Auditing:** Deep-packet inspection of raw financial hex messages to ensure PII (Field 2) masking.
- **BOLA/IDOR Hunting:** Agentic reasoning to simulate multi-step account-takeover scenarios.
- **Stateful Analysis:** Uses a directed acyclic graph (DAG) to maintain context during complex penetration tests.

### 🛠️ Usage
1. `pip install -r requirements.txt`
2. Run `python app/sentinel_graph.py`
