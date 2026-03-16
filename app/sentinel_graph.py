import os
from dotenv import load_dotenv
from typing import TypedDict, Annotated, List, Union
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, END
from app.security_tools import analyze_iso_8583_message, execute_bola_test

load_dotenv()

# Define the Agent's State
class AgentState(TypedDict):
    input: str
    chat_history: list
    next_step: str
    final_report: str

# Initialize LLM and Tools
llm = ChatOpenAI(model="gpt-4o", temperature=0)
tools = {
    "analyze_iso": analyze_iso_8583_message,
    "test_bola": execute_bola_test
}

def security_agent(state: AgentState):
    """The node that decides which security tool to use."""
    prompt = f"Target Task: {state['input']}. Decisions must prioritize ISO 8583 compliance and BOLA checks."
    response = llm.invoke(prompt)
    # Simplified logic: The LLM would normally call the tool here
    return {"next_step": "analyze_result", "final_report": response.content}

# Build the Graph
workflow = StateGraph(AgentState)
workflow.add_node("agent", security_agent)
workflow.set_entry_point("agent")
workflow.add_edge("agent", END)

app = workflow.compile()

if __name__ == "__main__":
    inputs = {"input": "Audit this hex message for PII: 02004220000000800000... and check BOLA on account 999"}
    for output in app.stream(inputs):
        print(output)
