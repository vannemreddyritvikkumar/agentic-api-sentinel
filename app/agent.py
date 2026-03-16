import os
from langchain_openai import ChatOpenAI
from langgraph.graph import Graph
import requests

# This agent "thinks" before it attacks
def security_planner(state):
    prompt = f"Analyze this API spec: {state['spec']}. Identify the top 3 endpoints vulnerable to Broken Object Level Authorization (BOLA)."
    # AI logic to pick targets...
    return {"targets": ["/api/v1/user/123/profile"]}

def attacker(state):
    target = state['targets'][0]
    # AI generates a payload to try and access user 124 while logged in as 123
    payload = {"user_id": "124"} 
    response = requests.get(f"https://api.example.com{target}", params=payload)
    return {"result": response.status_code}

# Graph setup
workflow = Graph()
workflow.add_node("plan", security_planner)
workflow.add_node("attack", attacker)
workflow.set_entry_point("plan")
workflow.add_edge("plan", "attack")
app = workflow.compile()
