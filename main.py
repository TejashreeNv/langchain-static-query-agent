from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import requests
import random

app = FastAPI()

# ✅ CORS FIX
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------- INPUT --------
class Query(BaseModel):
    query: str
    agent_type: str

# -------- BASIC AGENT --------
def basic_agent(q):
    return {
        "response": f"""
📘 Detailed Explanation:

👉 {q} is an important concept.

👉 Definition:
{q} refers to a key idea used in modern technology and real-world systems.

👉 Explanation:
It plays a major role in industries like AI, business, healthcare, and research.

👉 Example:
Used in automation, smart systems, and decision-making processes.

👉 Conclusion:
Understanding {q} helps build better real-world applications.
"""
    }

# -------- TOOL AGENT --------
def calculator(q):
    try:
        expr = q.replace("calculate", "").strip()
        return f"🧮 Result: {eval(expr)}"
    except:
        return "❌ Invalid calculation"

def weather(q):
    city = q.split("in")[-1].strip()
    return f"""
🌦️ Weather Report

📍 City: {city}
🌤️ Condition: {random.choice(['Sunny ☀️','Rainy 🌧️','Cloudy ☁️','Windy 🌬️'])}
🌡️ Temperature: {random.randint(20,35)}°C
"""

def tool_agent(q):
    if "calculate" in q.lower():
        return {"response": calculator(q)}
    elif "weather" in q.lower():
        return {"response": weather(q)}
    else:
        return {"response": "⚠️ Try: calculate 5+5 OR weather in Bangalore"}

# -------- REAL SEARCH (FIXED FINAL) --------
def search_web(query):
    try:
        # ✅ fix spaces issue
        clean_query = query.replace(" ", "_")

        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{clean_query}"
        res = requests.get(url).json()

        if "extract" in res and len(res["extract"]) > 50:
            return res["extract"]

        # fallback if not found
        return f"""
{query} is an important and rapidly growing field.

It is widely used in industries such as technology, healthcare, finance, and education.

It involves innovation, automation, and real-world applications.
"""

    except:
        return f"""
{query} is a modern topic with real-world applications.

It plays a major role in today's technology-driven world.
"""

# -------- MULTI AGENT --------
def multi_agent(q):
    research = search_web(q)

    summary = f"""
📝 Summary:
{research[:400]}...
"""

    final = f"""
✅ Final Answer:
{research}

👉 This topic has strong real-world importance and future scope.
"""

    return {
        "research": research,
        "summary": summary,
        "final_answer": final
    }

# -------- WORKFLOW + EMAIL --------
def workflow(q):
    data = multi_agent(q)

    email = f"""
📧 EMAIL GENERATED

Subject: Report on {q}

Dear Team,

Here is the detailed summary:

{data['summary']}

Conclusion:
This topic has strong future scope and industry applications.

Regards,
AI Assistant
"""

    data["email"] = email
    return data

# -------- API --------
@app.post("/run-workflow")
def run_api(data: Query):

    if data.agent_type == "basic":
        return basic_agent(data.query)

    elif data.agent_type == "tools":
        return tool_agent(data.query)

    elif data.agent_type == "multi":
        return multi_agent(data.query)

    elif data.agent_type == "workflow":
        return workflow(data.query)

    return {"error": "Invalid agent"}

# -------- RUN --------
if __name__ == "__main__":
    print("🚀 Server running at http://127.0.0.1:8000")
    uvicorn.run(app, host="127.0.0.1", port=8000)