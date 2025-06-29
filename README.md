# Strands Agents Framework - Complete Tutorial Series

A comprehensive collection of 19 tutorials and demonstrations for building intelligent AI agents using the Amazon Strands Agents Framework. From basic agent creation to advanced swarm intelligence systems.

## 🎯 Overview

This repository provides a complete learning curriculum for developing AI agents with the Strands framework. The tutorial series covers everything from basic agent creation to sophisticated multi-agent swarm systems, with hands-on examples and practical implementations for real-world applications.

**What's Included:**
- 📚 **19 Core Tutorials** + 2 Optional Extensions (21 total notebooks)
- 🛠️ **Source Code Utilities** for RAG, swarms, and MCP servers
- 📖 **Sample Documents** for RAG demonstrations
- 🔧 **MCP Server Implementations** with templates
- 🗄️ **Database Integration** examples and utilities

## 📚 Complete Tutorial Curriculum

### 🚀 Beginner Track (Tutorials 1-3)
Perfect for newcomers to AI agents and the Strands framework:

#### **Tutorial 1: Getting Started with Strands**
**File:** `01_getting_started.ipynb`  
**Duration:** 10 minutes  
**Concepts:** Framework overview, installation, basic agent creation, AWS Bedrock setup  
**Description:** Your first steps with Strands! Create a working AI agent in just 3 lines of code, understand core concepts, and set up your development environment with AWS Bedrock integration.

#### **Tutorial 2: Tools and Agents**
**File:** `02_tools_and_agents.ipynb`  
**Duration:** 10 minutes  
**Concepts:** Tool creation, @tool decorator, input validation, agent-tool integration  
**Description:** Learn to create custom tools and integrate them with agents. Master the @tool decorator pattern and build agents that can perform specific actions beyond conversation.

#### **Tutorial 3: Web Search Agents**
**File:** `03_web_search_agents.ipynb`  
**Duration:** 10 minutes  
**Concepts:** Web search integration, Google Search API, real-time information retrieval  
**Description:** Build agents that can search the web and retrieve real-time information. Integrate with Google Search API to create information-gathering agents that know current events.

### 🛠️ Intermediate Track (Tutorials 4-8)
Build on the basics with more advanced agent capabilities:

#### **Tutorial 4: Local Models with Ollama**
**File:** `04_local_models_ollama.ipynb`  
**Duration:** 10 minutes  
**Concepts:** Local LLM deployment, Ollama integration, privacy-first AI  
**Description:** Run AI models locally using Ollama. Perfect for privacy-sensitive applications or when you want to avoid cloud dependencies and costs.

#### **Tutorial 5: Agent Loop and Control Flow**
**File:** `05_agent_loop.ipynb`  
**Duration:** 10 minutes  
**Concepts:** Agent execution loop, state management, decision making  
**Description:** Understand how agents process requests, maintain state, and make decisions. Learn to control agent behavior and implement complex logic flows.

#### **Tutorial 6: Streaming Responses**
**File:** `06_streaming_responses.ipynb`  
**Duration:** 10 minutes  
**Concepts:** Real-time streaming, async operations, progress tracking  
**Description:** Create responsive AI applications with real-time streaming. Build chat interfaces with live responses and progress indicators for better user experience.

#### **Tutorial 7: Observability and Evaluation**
**File:** `07_observability_evaluation.ipynb`  
**Duration:** 10 minutes  
**Concepts:** Logging, metrics, tracing, evaluation frameworks  
**Description:** Build production-ready AI systems with comprehensive observability. Implement logging, track performance metrics, and evaluate agent quality systematically.

#### **Tutorial 8: Multi-Agent Workflows**
**File:** `08_workflows.ipynb`  
**Duration:** 10 minutes  
**Concepts:** Agent orchestration, parallel execution, workflow patterns  
**Description:** Orchestrate complex multi-agent systems. Learn sequential, parallel, and conditional execution patterns for enterprise applications.

### 🎓 Advanced Track (Tutorials 9-16)
Master production-ready techniques and sophisticated agent systems:

#### **Tutorial 9: Agentic RAG Basics**
**File:** `09_agentic_rag_basics.ipynb`  
**Duration:** 10 minutes  
**Concepts:** RAG fundamentals, vector stores, embeddings, document retrieval  
**Description:** Introduction to Retrieval-Augmented Generation. Build agents that can access and reason over custom knowledge bases with intelligent document retrieval.

#### **Tutorial 10: Advanced Agentic RAG**
**File:** `10_advanced_agentic_rag.ipynb`  
**Duration:** 10 minutes  
**Concepts:** Multi-format documents, ChromaDB, metadata filtering, production RAG  
**Description:** Master professional document processing with advanced RAG techniques. Handle PDFs, implement intelligent chunking, and build sophisticated document analysis systems.

#### **Tutorial 11: MCP Fundamentals**
**File:** `11_mcp_fundamentals.ipynb`  
**Duration:** 10 minutes  
**Concepts:** Model Context Protocol, MCP servers, tool discovery, standardized interfaces  
**Description:** Introduction to the Model Context Protocol (MCP) for building standardized AI tool servers. Learn the architecture and create your first MCP server.

#### **Tutorial 12: MCP Database Tools**
**File:** `12_mcp_database_tools.ipynb`  
**Duration:** 10 minutes  
**Concepts:** Database MCP servers, SQL tools, data persistence, CRUD operations  
**Description:** Build MCP servers that provide database tools to agents. Create standardized interfaces for data operations and persistence layers.

#### **Tutorial 13: Advanced MCP Patterns**
**File:** `13_advanced_mcp_patterns.ipynb`  
**Duration:** 10 minutes  
**Concepts:** Complex MCP servers, authentication, rate limiting, production patterns  
**Description:** Master advanced MCP server patterns including authentication, rate limiting, caching, and production deployment strategies.

#### **Tutorial 14: MCP Server Template & Best Practices**
**File:** `14_mcp_server_template.ipynb`  
**Duration:** 10 minutes  
**Concepts:** Production templates, validation, error handling, deployment  
**Description:** Comprehensive guide for building production-ready MCP servers with templates, validation patterns, and deployment configurations.

#### **Tutorial 15: Agents as Tools**
**File:** `15_agents_as_tools.ipynb`  
**Duration:** 10 minutes  
**Concepts:** Hierarchical agents, orchestrator pattern, specialized agents, delegation  
**Description:** Transform specialized agents into callable tools using the @tool decorator. Build hierarchical multi-agent systems with an orchestrator agent that delegates to domain-specific specialists.

#### **Tutorial 16: Advanced Agent Patterns**
**File:** `16_advanced_agent_patterns.ipynb`  
**Duration:** 10 minutes  
**Concepts:** Stateful memory, agent collaboration, dynamic routing, persistent state  
**Description:** Implement advanced multi-agent patterns including stateful agents with persistent memory, inter-agent collaboration, and intelligent routing that learns from experience.

### 🌐 Swarm Intelligence Track (Tutorials 17-19)
Master collective AI and sophisticated multi-agent swarm systems:

#### **Tutorial 17: Swarm Intelligence Fundamentals**
**File:** `17_swarm_fundamentals.ipynb`  
**Duration:** 10 minutes  
**Concepts:** Collective intelligence, built-in swarm tool, coordination patterns, multi-agent analysis  
**Description:** Master swarm intelligence basics using the built-in swarm tool. Learn collaborative, competitive, and hybrid coordination patterns while building market research swarms that outperform single agents.

#### **Tutorial 18: Custom Mesh Swarms**
**File:** `18_custom_mesh_swarms.ipynb`  
**Duration:** 10 minutes  
**Concepts:** Mesh architecture, SharedMemory, specialized agents, multi-phase processing  
**Description:** Build sophisticated mesh swarm architectures from scratch with direct agent communication. Create specialized agent teams with research, creative, critical, and synthesizer roles for customer feedback analysis.

#### **Tutorial 19: Advanced Swarm Systems**
**File:** `19_advanced_swarm_systems.ipynb`  
**Duration:** 10 minutes  
**Concepts:** RAG integration, production swarms, workflow orchestration, monitoring, enterprise deployment  
**Description:** Build enterprise-ready swarm systems that combine collective intelligence with document analysis, robust error handling, and comprehensive monitoring for business intelligence applications.

### 🔧 Optional Extensions
Additional specialized tutorials for specific use cases:

#### **Tutorial 2.5: Example Tools Package**
**File:** `02_5_example_tools.ipynb`  
**Concepts:** Pre-built tools, strands-agents-tools package, file operations, utilities  
**Description:** Explore the pre-built tools available in the strands-agents-tools package. Learn to use file operations, calculators, shell commands, and more without writing custom code.  
**⚠️ Note:** Some tools have Windows compatibility issues. See notebook for workarounds.

#### **Tutorial 4.5: Advanced Ollama Techniques**
**File:** `04_5_advanced_ollama.ipynb`  
**Concepts:** Model optimization, custom models, performance tuning  
**Description:** Deep dive into advanced Ollama features including model customization, performance optimization, and specialized local model deployments.

## 🛠️ Source Code & Utilities

The repository includes production-ready utilities and examples:

### **RAG Document Generator**
**File:** `src/rag_document_generator.py`  
Utility for generating sample documents and content for RAG demonstrations. Creates realistic business documents, case studies, and reference materials for testing document analysis agents.

### **Swarm Utilities**
**File:** `src/swarm_utils.py`  
Helper functions and patterns for building and managing multi-agent swarm systems. Includes coordination patterns, shared memory management, and communication protocols.

### **Customer Service Database**
**File:** `src/customer_service_db.py`  
Database utilities and examples for customer service applications, demonstrating agent integration with persistent data storage.

### **MCP Server Implementations**
**Directory:** `src/mcp_servers/`
- **`calculator_server.py`** - Basic MCP server for mathematical operations
- **`ecommerce_db_server.py`** - Database MCP server for e-commerce applications
- **`template_server.py`** - Template and starting point for custom MCP servers

### **RAG Document Collection**
**Directory:** `notebooks/rag_docs/`
- Sample PDFs, Word documents, and Markdown files
- Business case studies and API references
- Troubleshooting guides and technical documentation
- Real-world examples for RAG system testing

## 🚀 Quick Start

### **1. Install Dependencies**
```bash
# Clone the repository
git clone <repository-url>
cd strands

# Install core requirements
pip install -r requirements.txt

# Or use setup scripts
./setup.bat          # Windows
./setup.ps1          # PowerShell
python setup.py      # Cross-platform
```

### **2. Configure AWS Bedrock**
```bash
# Set up AWS credentials
aws configure

# Or use environment variables
export AWS_ACCESS_KEY_ID="your-access-key"
export AWS_SECRET_ACCESS_KEY="your-secret-key"
export AWS_DEFAULT_REGION="us-west-2"
```

### **3. Start Learning**
```bash
# Launch Jupyter
jupyter notebook notebooks/

# Begin with Tutorial 1
open notebooks/01_getting_started.ipynb
```

## 📋 Prerequisites

- **Python 3.8+**
- **AWS Account** with Bedrock access
- **Basic Python knowledge**
- **Jupyter Notebook** environment

### **Optional Requirements**
- **Ollama** - For local model deployment (Tutorials 4 & 4.5)
- **Google Search API** - For web search capabilities (Tutorial 3)
- **ChromaDB** - For advanced RAG systems (Tutorial 10)

## 🎯 Learning Paths

### **👶 Complete Beginner (New to AI Agents)**
```
01 → 02 → 03 → 05 → 06
```
Focus on core concepts, basic tools, and simple interactions.

### **🔧 Developer Track (Want to Build Tools)**
```
01 → 02 → 02.5 → 11 → 12 → 13 → 14
```
Master tool creation and MCP server development.

### **📚 RAG Specialist (Document Analysis)**
```
01 → 02 → 09 → 10 → 16 → 19
```
Focus on document processing and knowledge systems.

### **🌐 Swarm Engineer (Multi-Agent Systems)**
```
01 → 02 → 15 → 16 → 17 → 18 → 19
```
Build sophisticated collective intelligence systems.

### **🏭 Production Developer (Enterprise Ready)**
```
01 → 02 → 05 → 07 → 08 → 13 → 16 → 19
```
Focus on scalable, production-ready implementations.

## 📁 Repository Structure

```
strands/
├── 📄 README.md                    # This comprehensive guide
├── 📋 requirements.txt             # Python dependencies
├── 🔧 setup.py                     # Package configuration
├── 🖥️ setup.bat/.ps1              # Platform setup scripts
├── 📄 LICENSE                      # License information
│
├── 📚 notebooks/                   # Complete tutorial series
│   ├── 01_getting_started.ipynb   # Your first agent
│   ├── 02_tools_and_agents.ipynb  # Custom tool creation
│   ├── 03_web_search_agents.ipynb # Internet-enabled agents
│   ├── 04_local_models_ollama.ipynb # Local AI models
│   ├── 05_agent_loop.ipynb        # Control flow & state
│   ├── 06_streaming_responses.ipynb # Real-time responses
│   ├── 07_observability_evaluation.ipynb # Production monitoring
│   ├── 08_workflows.ipynb         # Multi-agent orchestration
│   ├── 09_agentic_rag_basics.ipynb # Document retrieval
│   ├── 10_advanced_agentic_rag.ipynb # Production RAG
│   ├── 11_mcp_fundamentals.ipynb  # MCP protocol basics
│   ├── 12_mcp_database_tools.ipynb # Database MCP servers
│   ├── 13_advanced_mcp_patterns.ipynb # Production MCP
│   ├── 14_mcp_server_template.ipynb # MCP best practices
│   ├── 15_agents_as_tools.ipynb   # Hierarchical agents
│   ├── 16_advanced_agent_patterns.ipynb # Stateful collaboration
│   ├── 17_swarm_fundamentals.ipynb # Swarm intelligence basics
│   ├── 18_custom_mesh_swarms.ipynb # Custom swarm architecture
│   ├── 19_advanced_swarm_systems.ipynb # Enterprise swarms
│   ├── 02_5_example_tools.ipynb   # Pre-built tools (optional)
│   ├── 04_5_advanced_ollama.ipynb # Advanced Ollama (optional)
│   │
│   ├── 🗄️ chroma_db/              # Persistent vector database
│   └── 📖 rag_docs/               # Sample documents for RAG
│       ├── 📄 *.pdf, *.docx, *.md # Various document formats
│       └── 📁 case_studies/       # Business case examples
│
├── 🔧 src/                        # Source code & utilities
│   ├── 📊 rag_document_generator.py # RAG content creation
│   ├── 🌐 swarm_utils.py          # Multi-agent coordination
│   ├── 🗄️ customer_service_db.py  # Database integration
│   └── 🔌 mcp_servers/            # MCP server implementations
│       ├── calculator_server.py   # Math operations server
│       ├── ecommerce_db_server.py # E-commerce database server
│       └── template_server.py     # MCP server template
│
├── 📖 docs/                       # Additional documentation
└── 🔨 workspace/                  # Development workspace
```

## 🎯 Key Learning Outcomes

After completing this tutorial series, you will master:

### **🤖 Core Agent Development**
- Agent creation, configuration, and customization
- Model integration with AWS Bedrock and local models
- System prompt design and conversation management
- Error handling and debugging techniques

### **🛠️ Tool Development & Integration**
- Custom tool creation with the `@tool` decorator
- Type hints and parameter validation
- External API integration patterns
- MCP server development and deployment

### **📚 Advanced Document Processing**
- RAG system implementation and optimization
- Multi-format document handling (PDF, DOCX, etc.)
- Vector stores and embedding strategies
- Intelligent chunking and metadata filtering

### **🌐 Multi-Agent Systems**
- Agent orchestration and workflow management
- Hierarchical agent architectures
- Swarm intelligence and collective decision-making
- Inter-agent communication protocols

### **🏭 Production Deployment**
- Performance optimization and monitoring
- Security best practices and authentication
- Scalable architecture patterns
- Enterprise integration strategies

## 💻 Development Environment

### **Core Dependencies**
```
strands-agents>=0.1.0
strands-agents-tools>=0.1.0
strands-agents-builder>=0.1.0
boto3>=1.35.0
jupyter>=1.0.0
chromadb>=0.4.0
```

### **Optional Extensions**
```
google-api-python-client>=2.0.0  # For web search (Tutorial 3)
ollama>=0.1.0                    # For local models (Tutorial 4)
streamlit>=1.28.0                # For web interfaces
fastapi>=0.104.0                 # For MCP server deployment
```

## 🤝 Contributing

We welcome contributions to improve the tutorial series:

### **Areas for Enhancement**
- Additional real-world examples and use cases
- Platform-specific setup guides and troubleshooting
- Integration templates for popular frameworks
- Performance optimization techniques
- Community-contributed tutorials and extensions

### **How to Contribute**
1. Fork the repository
2. Create a feature branch
3. Add your improvements
4. Submit a pull request

## 📚 Additional Resources

### **Official Documentation**
- [Strands Agents Framework Documentation](https://strandsagents.com/0.1.x/)
- [AWS Bedrock Documentation](https://docs.aws.amazon.com/bedrock/)
- [Model Context Protocol Specification](https://github.com/anthropics/model-context-protocol)

### **Community & Support**
- [Strands Community Forum](https://community.strandsagents.com/)
- [GitHub Discussions](https://github.com/strandsai/strands/discussions)
- [Tutorial Series Issues](https://github.com/strandsai/strands/issues)

### **Advanced Topics**
- [ChromaDB Documentation](https://docs.trychroma.com/)
- [Ollama Model Library](https://ollama.ai/library)
- [Google Custom Search API](https://developers.google.com/custom-search/v1/introduction)

## 👨‍💻 Author

**Markus Bestehorn** - Creator and maintainer of the tutorial series

*Passionate about making AI agent development accessible to developers at all levels, from complete beginners to enterprise architects.*

## ⚠️ Important Notice

**This code is for personal use and demonstration purposes only.** The tutorials showcase the capabilities of the Strands Agents Framework with educational examples and best practices. While the code includes error handling and follows production patterns, it is designed for learning and experimentation.

**For production deployments:**
- Conduct thorough testing and security reviews
- Implement appropriate monitoring and logging
- Follow your organization's security and compliance standards
- Consider scalability and performance requirements

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🎉 Get Started Today!

Ready to build intelligent AI agents? Start with [Tutorial 1: Getting Started](notebooks/01_getting_started.ipynb) and join the growing community of developers creating the future of AI-powered applications! 🚀

**Total Learning Time:** ~4 hours for complete mastery  
**Skill Level:** Beginner to Advanced  
**Real-World Applications:** ✅ Production Ready
