# Strands Framework Tutorial Series

A comprehensive tutorial series introducing the Strands AI agents framework. Each notebook is designed for a 10-minute presentation that builds on previous concepts.

## 📚 Curriculum Overview

### Tutorial 1: Getting Started with Strands
**File:** `01_getting_started.ipynb`  
**Concepts:** Framework overview, installation, basic agent creation, AWS Bedrock setup  
**Description:** Get started with Strands by creating your first AI agent and understanding the framework's core concepts. Learn about the ecosystem and set up your development environment.

### Tutorial 2: Tools and Agents
**File:** `02_tools_and_agents.ipynb`  
**Concepts:** Tool creation, @tool decorator, input validation, agent-tool integration  
**Description:** Learn how to create custom tools and integrate them with agents. Master the @tool decorator pattern and build agents that can perform specific actions.

### Tutorial 2.5: Example Tools Package (Optional)
**File:** `02_5_example_tools.ipynb`  
**Concepts:** Pre-built tools, strands-agents-tools package, file operations, utilities  
**Description:** Explore the pre-built tools available in the strands-agents-tools package. Learn to use file operations, calculators, shell commands, and more without writing custom code.  
**⚠️ Note:** Some tools have Windows compatibility issues. See notebook for workarounds.

### Tutorial 3: Web Search Agents
**File:** `03_web_search_agents.ipynb`  
**Concepts:** Web search integration, Google Search API, real-time information retrieval  
**Description:** Build agents that can search the web and retrieve real-time information. Integrate with Google Search API and create information-gathering agents.

### Tutorial 4: Local Models with Ollama
**File:** `04_local_models_ollama.ipynb`  
**Concepts:** Local LLM deployment, Ollama integration, privacy-first AI  
**Description:** Run AI models locally using Ollama. Perfect for privacy-sensitive applications or when you want to avoid cloud dependencies.

### Tutorial 4.5: Advanced Ollama Techniques
**File:** `04_5_advanced_ollama.ipynb`  
**Concepts:** Model optimization, custom models, performance tuning  
**Description:** Deep dive into advanced Ollama features including model customization, performance optimization, and specialized local model deployments.

### Tutorial 5: Agent Loop and Control Flow
**File:** `05_agent_loop.ipynb`  
**Concepts:** Agent execution loop, state management, decision making  
**Description:** Understand how agents process requests, maintain state, and make decisions. Learn to control agent behavior and implement complex logic flows.

### Tutorial 6: Streaming Responses
**File:** `06_streaming_responses.ipynb`  
**Concepts:** Real-time streaming, async operations, progress tracking  
**Description:** Create responsive AI applications with real-time streaming. Build chat interfaces with live responses and progress indicators.

### Tutorial 7: Observability and Evaluation
**File:** `07_observability_evaluation.ipynb`  
**Concepts:** Logging, metrics, tracing, evaluation frameworks  
**Description:** Build production-ready AI systems with comprehensive observability. Implement logging, track performance metrics, and evaluate agent quality.

### Tutorial 8: Multi-Agent Workflows
**File:** `08_workflows.ipynb`  
**Concepts:** Agent orchestration, parallel execution, workflow patterns  
**Description:** Orchestrate complex multi-agent systems. Learn sequential, parallel, and conditional execution patterns for enterprise applications.

### Tutorial 9: Agentic RAG Basics
**File:** `09_agentic_rag_basics.ipynb`  
**Concepts:** RAG fundamentals, vector stores, embeddings, document retrieval  
**Description:** Introduction to Retrieval-Augmented Generation. Build agents that can access and reason over custom knowledge bases.

### Tutorial 10: Advanced Agentic RAG
**File:** `10_advanced_agentic_rag.ipynb`  
**Concepts:** Multi-format documents, ChromaDB, metadata filtering, production RAG  
**Description:** Master professional document processing with advanced RAG techniques. Handle PDFs, implement intelligent chunking, and build sophisticated document analysis systems.

### Tutorial 11: MCP Fundamentals
**File:** `11_mcp_fundamentals.ipynb`  
**Concepts:** Model Context Protocol, MCP servers, tool discovery, standardized interfaces  
**Description:** Introduction to the Model Context Protocol (MCP) for building standardized AI tool servers. Learn the architecture and create your first MCP server.

### Tutorial 12: MCP Database Tools
**File:** `12_mcp_database_tools.ipynb`  
**Concepts:** Database MCP servers, SQL tools, data persistence, CRUD operations  
**Description:** Build MCP servers that provide database tools to agents. Create standardized interfaces for data operations and persistence.

### Tutorial 13: Advanced MCP Patterns
**File:** `13_advanced_mcp_patterns.ipynb`  
**Concepts:** Complex MCP servers, authentication, rate limiting, production patterns  
**Description:** Master advanced MCP server patterns including authentication, rate limiting, caching, and production deployment strategies.

### Tutorial 14: MCP Server Template & Best Practices
**File:** `14_mcp_server_template.ipynb`  
**Concepts:** Production templates, validation, error handling, deployment  
**Description:** Comprehensive guide for building production-ready MCP servers with templates, validation patterns, and deployment configurations.

### Tutorial 15: Agents as Tools
**File:** `15_agents_as_tools.ipynb`  
**Concepts:** Hierarchical agents, orchestrator pattern, specialized agents, delegation  
**Description:** Transform specialized agents into callable tools using the @tool decorator. Build hierarchical multi-agent systems with an orchestrator agent that delegates to domain-specific specialists.

### Tutorial 16: Advanced Agent Patterns
**File:** `16_advanced_agent_patterns.ipynb`  
**Concepts:** Stateful memory, agent collaboration, dynamic routing, persistent state  
**Description:** Implement advanced multi-agent patterns including stateful agents with persistent memory, inter-agent collaboration, and intelligent routing that learns from experience. Build production-ready systems with database integration.

### Tutorial 17: Swarm Intelligence Fundamentals
**File:** `17_swarm_fundamentals.ipynb`  
**Concepts:** Collective intelligence, built-in swarm tool, coordination patterns, multi-agent analysis  
**Description:** Master swarm intelligence basics using the built-in swarm tool. Learn collaborative, competitive, and hybrid coordination patterns while building market research swarms that outperform single agents.

### Tutorial 18: Custom Mesh Swarms
**File:** `18_custom_mesh_swarms.ipynb`  
**Concepts:** Mesh architecture, SharedMemory, specialized agents, multi-phase processing  
**Description:** Build sophisticated mesh swarm architectures from scratch with direct agent communication. Create specialized agent teams with research, creative, critical, and synthesizer roles for customer feedback analysis.

### Tutorial 19: Advanced Swarm Systems
**File:** `19_advanced_swarm_systems.ipynb`  
**Concepts:** RAG integration, production swarms, workflow orchestration, monitoring, enterprise deployment  
**Description:** Build enterprise-ready swarm systems that combine collective intelligence with document analysis, robust error handling, and comprehensive monitoring for business intelligence applications.

## 🎯 Learning Paths

### Beginner Track (Tutorials 1-3)
Start here if you're new to Strands or AI agent frameworks:
1. Getting Started → 2. Tools and Agents → 3. Web Search Agents

### Intermediate Track (Tutorials 4-8)
Build on the basics with more advanced features:
4. Local Models → 5. Agent Loop → 6. Streaming → 7. Observability → 8. Workflows

### Advanced Track (Tutorials 9-16)
Master production-ready techniques:
9. RAG Basics → 10. Advanced RAG → 11-14. MCP Series → 15. Agents as Tools → 16. Advanced Agent Patterns

### Swarm Intelligence Track (Tutorials 17-19)
Master collective AI and multi-agent swarms:
17. Swarm Fundamentals → 18. Custom Mesh Swarms → 19. Advanced Swarm Systems

### Optional Extensions
- Tutorial 2.5: Example Tools Package (after Tutorial 2)
- Tutorial 4.5: Advanced Ollama (after Tutorial 4)

## 🚀 Getting Started

1. **Install dependencies**:
   ```bash
   pip install strands-agents boto3 jupyter
   ```

2. **Configure AWS Bedrock**:
   - Set up AWS credentials
   - Ensure Bedrock access in your region

3. **Start learning**:
   - Open `01_getting_started.ipynb`
   - Follow the tutorials in order
   - Each notebook is self-contained with all necessary code

## 📋 Prerequisites

- Python 3.8+
- AWS Account with Bedrock access
- Basic Python programming knowledge
- Familiarity with AI/ML concepts (helpful but not required)

## 🛠️ What's Included

Each notebook contains:
- 📝 Step-by-step instructions
- 💻 Working code examples
- 🎨 Visual explanations with emojis
- ⚡ Best practices
- 🏭 Production tips
- ⏱️ 10-minute presentation format

## 🔧 Optional Components

- **Ollama**: For local model deployment (Tutorials 4 & 4.5)
- **strands-agents-tools**: Pre-built tools package (Tutorial 2.5)
- **ChromaDB**: For advanced RAG (Tutorial 10)
- **MCP Servers**: For standardized tool interfaces (Tutorials 11-14)

## 📚 Additional Resources

- [Strands Documentation](https://strandsagents.com/0.1.x/)
- [AWS Bedrock Documentation](https://docs.aws.amazon.com/bedrock/)
- [Model Context Protocol](https://github.com/anthropics/model-context-protocol)
- [Community Forum](https://community.strandsagents.com/)
- [GitHub Repository](https://github.com/strandsai/strands)

## 🤝 Contributing

We welcome contributions! Areas for improvement:
- Additional examples
- Platform-specific guides
- Integration templates
- Performance optimizations
- Bug fixes and clarifications

## 📄 License

This tutorial series is licensed under the MIT License. See LICENSE file for details.

## 🌟 Acknowledgments

Special thanks to:
- The Strands team for the amazing framework
- AWS Bedrock team for accessible AI models
- The open-source community for continuous improvements
- Tutorial contributors and reviewers

---

**Happy Learning!** 🎓🤖✨

*Last updated: June 2025 - Now with 19 complete tutorials + 2 optional extensions!*
