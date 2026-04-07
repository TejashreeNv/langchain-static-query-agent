# 🚀 Agent-Orchestration Framework

**Complete LangChain Multi-Agent System with Hugging Face**

## 📋 Overview

This project implements all 4 milestones in a single Python file:

- **Milestone 1**: Basic conversational agent with memory
- **Milestone 2**: Tool integration (Calculator, Weather)
- **Milestone 3**: Multi-agent orchestration (Research → Summarize)
- **Milestone 4**: REST API + Streamlit UI + Workflow automation

## 🛠️ Installation

```bash
pip install -r requirements.txt
```

## ▶️ Usage

### Console Interface
```bash
python agent_orchestration_complete.py console
```

### Web UI
```bash
python agent_orchestration_complete.py streamlit
```

### REST API
```bash
python agent_orchestration_complete.py api
```

## 📚 Features

- ✅ Hugging Face models 
- ✅ Single file implementation
- ✅ Memory management
- ✅ Tool integration
- ✅ Multi-agent orchestration
- ✅ REST API endpoints
- ✅ Streamlit web interface
- ✅ Production-ready logging

## 🏗️ Architecture

- **LLM**: HuggingFace FLAN-T5-Base
- **Framework**: LangChain
- **Memory**: ConversationBufferMemory
- **Tools**: Calculator, Weather API
- **Agents**: Research, Summarizer, Coordinator
- **API**: FastAPI
- **UI**: Streamlit

## 📄 License

Educational project demonstrating LangChain multi-agent systems.
```

## 🚀 Features

### 🤖 Multi-Agent Capabilities
- **ResearchAgent**: Information gathering and weather queries
- **SummarizerAgent**: Text analysis and summarization
- **CalculatorAgent**: Mathematical computations
- **OrchestratorAgent**: Intelligent task coordination

### 🧠 Memory Systems
- **Individual Memory**: Per-agent conversation history
- **Shared Memory**: Cross-agent knowledge base with semantic search
- **Persistent Learning**: Memory-guided decision making

### 💬 Communication
- Agent scratchpad for real-time coordination
- Shared memory for persistent knowledge
- Orchestrated collaborative workflows

## 📋 Requirements

```bash
pip install -r requirements.txt
```

### Dependencies
- `langchain` - Core framework
- `faiss-cpu` - Vector similarity search
- `transformers` - HuggingFace models
- `python-dotenv` - Environment management

## 🎮 Usage

### Running the Multi-Agent System
```bash
python milestone3_complete.py
```

### Example Queries
```
# Single Agent Queries
"What is LangChain?"
"Calculate 25 * 4 + 10"
"Summarize: The quick brown fox jumps over the lazy dog"

# Multi-Agent Queries
"What is the weather in Mumbai and calculate 100/5?"
"Research AI and summarize the key points"
```

### Interactive Mode
```bash
python milestone3_complete.py
# Then enter queries interactively
```

## 📁 Project Structure

```
├── agent_app.py              # Main application (Milestone 2)
├── milestone3_complete.py    # Complete Milestone 3 implementation
├── test_milestone3.py        # Test suite
├── tools.py                  # Tool definitions
├── requirements.txt          # Dependencies
├── MILESTONE_2_COMPLETE.md   # Milestone 2 completion report
├── MILESTONE_3_COMPLETE.md   # Milestone 3 completion report
├── MILESTONE_2_SUMMARY.md    # Milestone 2 summary
├── MILESTONE_3_SUMMARY.md    # Milestone 3 summary
└── README.md                 # This file
```

## 🧪 Testing

Run the comprehensive test suite:
```bash
python milestone3_complete.py
```

Tests cover:
- ✅ Single agent functionality
- ✅ Multi-agent collaboration
- ✅ Memory persistence
- ✅ Communication systems
- ✅ Orchestration logic

## 📊 Milestones Completed

### Milestone 1 ✅
- Basic LangChain agent implementation

### Milestone 2 ✅
- Tool integration and API calling
- 4 integrated tools with error handling
- Intelligent query routing

### Milestone 3 ✅
- Multi-agent orchestration
- Individual and shared memory systems
- Agent communication and collaboration
- Memory-guided decision making

## 🎯 Key Achievements

1. **Scalable Architecture**: Modular agent design for easy extension
2. **Advanced Memory**: Dual memory system for context and collaboration
3. **Intelligent Orchestration**: Dynamic agent selection based on query analysis
4. **Robust Communication**: Real-time coordination between agents
5. **Semantic Search**: Vector-based knowledge retrieval
6. **Collaborative Problem Solving**: Multi-agent workflows for complex tasks

## 🔮 Future Enhancements

- **Additional Agent Types**: Domain-specific agents (e.g., Code Review, Data Analysis)
- **Advanced Memory**: Long-term memory with ChromaDB
- **Learning Capabilities**: Agent adaptation based on interaction patterns
- **Complex Workflows**: Multi-step orchestration with dependencies
- **User Interface**: Web-based interface for agent interaction

## 📝 License

This project is part of an educational milestone series demonstrating progressive agent development with LangChain.

---

**Status**: ✅ **All Milestones Complete** - Full multi-agent orchestration system with memory management implemented and tested.
