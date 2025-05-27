# Strands Agents Framework Demos

A comprehensive collection of demonstrations and tutorials for building intelligent AI agents using the Amazon Strands Agents Framework.

## Overview

This repository provides hands-on examples and practical tutorials for developing AI agents with the Strands framework. From basic agent creation to advanced tool integration with external APIs, these notebooks demonstrate real-world applications and best practices for agent development.

## 📚 Notebooks

### 🚀 [Strands Demo](notebooks/strands_demo.ipynb)
**Author: Markus Bestehorn**

A comprehensive guide to building AI agents with the Strands Framework. This notebook covers:

- **Basic Agent Creation**: Setting up your first Strands agent
- **AWS Bedrock Integration**: Configuring Claude models for intelligent responses
- **Custom Tool Development**: Creating and integrating custom tools with proper type hints
- **Conversation Management**: Handling context and conversation history
- **Performance Monitoring**: Analyzing agent performance and optimization
- **Error Handling**: Implementing robust safety mechanisms

**Key Features Demonstrated:**
- Agent customization with system prompts
- Tool creation using the `@tool` decorator
- Type hints for reliable parameter conversion
- Conversation context management
- Performance analysis and monitoring

### 🔍 [Google Search Tool](notebooks/GoogleSearchTool.ipynb)
**Author: Markus Bestehorn**

Build intelligent web-enabled AI agents that can search the internet and synthesize information. This advanced tutorial includes:

- **Google Custom Search API Integration**: Complete setup and configuration
- **Intelligent Search Agent**: Web-enabled agent that knows when to search
- **Real-time Information Retrieval**: Current events, weather, and news queries
- **Comparative Research**: Complex multi-source information synthesis
- **Performance Analysis**: Optimization techniques and benchmarking
- **Production Considerations**: Error handling, security, and monitoring

**Key Features Demonstrated:**
- Google Custom Search API integration
- Intelligent decision-making for search usage
- Source citation and URL referencing
- Multi-query research capabilities
- Edge case handling and error recovery

## 🛠 Requirements

### Core Dependencies
```
google-api-python-client>=2.0.0
strands-agents
strands-agents-tools
strands-agents-builder
boto3
```

### External Services
- **AWS Account**: For Bedrock model access
- **Google Custom Search API**: For web search capabilities
  - Google API Key required
  - Custom Search Engine ID required

## 🚀 Quick Start

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd strands
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup AWS Credentials**
   Configure your AWS credentials for Bedrock access:
   ```bash
   aws configure
   ```

4. **Configure Google Search (Optional)**
   For the Google Search tool notebook:
   - Create a Google Custom Search API key
   - Set up a Custom Search Engine
   - Save credentials in the appropriate files

5. **Run the Notebooks**
   ```bash
   jupyter notebook notebooks/
   ```

## 📖 Learning Path

### Beginner: Start with Strands Demo
- Understand core Strands concepts
- Learn agent creation and customization
- Explore basic tool integration
- Practice conversation management

### Advanced: Google Search Tool
- Build complex tool integrations
- Implement web search capabilities
- Handle real-time information queries
- Optimize for production deployment

## 🔧 Setup Scripts

The repository includes setup scripts for easy environment configuration:

- **`setup.py`**: Python package setup and dependency management
- **`setup.bat`**: Windows batch setup script
- **`setup.ps1`**: PowerShell setup script

## 📁 Repository Structure

```
strands/
├── notebooks/
│   ├── strands_demo.ipynb          # Core Strands framework tutorial
│   ├── GoogleSearchTool.ipynb      # Web search integration tutorial
│   └── google-search_engine-id.txt # Google Search Engine ID
├── src/                            # Source code directory
├── docs/                           # Documentation directory
├── requirements.txt                # Python dependencies
├── setup.py                       # Package setup configuration
├── setup.bat                      # Windows setup script
├── setup.ps1                      # PowerShell setup script
├── LICENSE                         # License file
└── README.md                       # This file
```

## 🎯 Key Learning Outcomes

After working through these notebooks, you will understand:

1. **Strands Framework Fundamentals**
   - Agent creation and configuration
   - Model integration with AWS Bedrock
   - System prompt design and optimization

2. **Tool Development**
   - Custom tool creation with the `@tool` decorator
   - Type hints for parameter conversion
   - Error handling and validation

3. **Advanced Integrations**
   - External API integration patterns
   - Real-time data retrieval
   - Information synthesis and analysis

4. **Production Considerations**
   - Performance optimization
   - Error handling and recovery
   - Security best practices
   - Monitoring and analytics

## 🤝 Contributing

This repository serves as a demonstration of the Strands Agents Framework. For contributions to the core framework, please refer to the official Strands documentation.

## 📚 Additional Resources

- [Strands Agents Documentation](https://strandsagents.com/0.1.x/)
- [AWS Bedrock Documentation](https://docs.aws.amazon.com/bedrock/)
- [Google Custom Search API](https://developers.google.com/custom-search/v1/introduction)

## 👨‍💻 Author

**Markus Bestehorn** - Creator of the demonstration notebooks and tutorials

## ⚠️ Disclaimer

**IMPORTANT: This code is for personal use only and exclusively for demonstration purposes of the Strands Agents Framework. The code is explicitly not made for production workloads or any other sensitive or otherwise critical workloads. No warranties are given/provided with this code.**

This repository contains demonstration code designed to showcase the capabilities of the Strands Agents Framework. While the examples follow best practices and include error handling, they are intended for educational and experimental purposes only. Before using any concepts or code patterns in production environments, please ensure proper testing, security review, and compliance with your organization's standards.

## 📄 License

This project is licensed under the terms specified in the [LICENSE](LICENSE) file.
