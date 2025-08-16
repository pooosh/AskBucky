# AskBucky 🍽️

<div align="center">
  <img src="NLWeb/static/images/bucky_logo.svg" alt="AskBucky Logo" width="200"/>
  <h3>Your UW-Madison AI Dining Companion</h3>
  <p>AskBucky is an intelligent conversational interface that helps you discover, explore, and plan your dining experience with comprehensive menu information and nutritional insights.</p>
  
  <a href="#demo">View Demo</a> •
  <a href="#report-bug">Report Bug</a> •
  <a href="#request-feature">Request Feature</a>
</div>

## 📋 Table of Contents

- [Vision](#-vision-your-uw-madison-ai-companion)
- [About The Project](#-about-the-project)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Getting Started](#-getting-started)
- [Usage](#-usage)
- [API Documentation](#-api-documentation)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)
- [Acknowledgments](#-acknowledgments)

## 🎯 Vision: Your UW-Madison AI Companion

AskBucky is just the beginning! Our ultimate vision is to create a comprehensive one-stop-shop for all things UW-Madison. While we currently focus on dining hall menus and nutrition, we're planning to expand AskBucky into a unified platform that integrates multiple university data sources:

## 🎯 About The Project

AskBucky transforms how you interact with dining hall menus through natural language conversation. Built on the powerful NLWeb framework, it provides an intuitive way to discover food options, get nutritional information, and plan balanced meals.

### Why AskBucky?

- **Natural Conversations**: Ask questions like "What's for lunch today?" or "Show me high-protein options"
- **Comprehensive Nutrition**: Get detailed macronutrient breakdowns (calories, protein, carbs, fat) for every item
- **Smart Meal Planning**: Receive personalized meal recommendations based on your preferences and dietary needs
- **Real-time Menu Access**: Stay updated with current dining hall offerings across multiple locations
- **Dietary Accommodations**: Filter by dietary restrictions and allergen information

### Key Capabilities

- **Multi-Hall Support**: Access menus from multiple dining locations (Four Lakes Market, Gordon Avenue Market, etc.)
- **Temporal Awareness**: Get menu information for specific dates and meal times
- **Section-Based Navigation**: Explore different dining sections (Fired Up, 1849, Buona Cucina, etc.)
- **Nutritional Intelligence**: Automatic display of macronutrients and calorie information
- **Conversational Memory**: Maintains context across multiple queries for seamless interactions

**Future Integrations:**
- **🏋️ RecWell Data**: Gym schedules, fitness classes, facility availability, and workout recommendations
- **📅 University Events**: Integration with today.wisc.edu for campus events, lectures, and activities
- **📚 Academic Resources**: Course information, library hours, study spaces, and academic support
- **🚌 Transportation**: Bus schedules, parking information, and campus navigation
- **🏠 Housing & Facilities**: Residence hall information, building hours, and maintenance requests
- **🎓 Student Services**: Career services, health resources, and student organization information

**The Goal**: Transform AskBucky into your personal AI assistant for everything UW-Madison, making campus life more connected, informed, and engaging through natural language conversations.

## ✨ Features

### 🍽️ Menu Discovery
- **Natural Language Queries**: "What's available for dinner?" or "Show me vegetarian options"
- **Date-Specific Menus**: "What's on the menu for tomorrow's lunch?"
- **Section Exploration**: "What's cooking at Fired Up today?"
- **Comprehensive Listings**: Get complete menu offerings with detailed descriptions

### 📊 Nutritional Intelligence
- **Automatic Macronutrient Display**: Calories, protein, carbs, and fat for every item
- **Dietary Filtering**: Vegan, gluten-free, allergen-aware options
- **Nutritional Comparisons**: Compare items side-by-side
- **Meal Planning**: Get balanced meal recommendations

### 🤖 AI-Powered Features
- **Smart Recommendations**: Personalized suggestions based on preferences
- **Contextual Understanding**: Remembers your previous queries and preferences
- **Multi-Modal Responses**: List, summarize, or generate comprehensive answers
- **Tool Integration**: Specialized tools for different query types

### 🔧 Technical Excellence
- **Scalable Architecture**: Built on NLWeb's robust framework
- **Multi-Backend Support**: Azure AI Search, Qdrant, Milvus, and more
- **LLM Flexibility**: OpenAI, DeepSeek, Gemini, Anthropic, and HuggingFace models
- **Real-time Streaming**: Instant responses with server-sent events
- **OAuth Integration**: Secure user authentication and conversation history

## 🛠️ Tech Stack

### **Backend & Core Framework**
- **Python 3.12+** - High-performance backend server and AI processing
- **AIOHTTP** - Asynchronous web framework for scalable real-time communication
- **NLWeb Framework** - Microsoft's enterprise-grade embedding and MCP framework (submodule)
- **Schema.org** - Semantic data markup for structured information

### **AI & Machine Learning**
- **Large Language Models** - OpenAI GPT-4, Claude, Gemini, DeepSeek, and HuggingFace models
- **Embedding Models** - Text-to-vector conversion for semantic search (text-embedding-3-small, etc.)
- **RAG Architecture** - Retrieval-Augmented Generation for accurate, grounded responses
- **Vector Similarity Search** - Semantic matching for relevant menu items

### **Data Storage & Search**
- **Vector Databases** - Azure AI Search, Qdrant, Milvus, Elasticsearch for semantic search
- **PostgreSQL** - Relational data storage for user data and configurations
- **JSON-LD** - Structured data format for menu information
- **Redis** - Caching layer for improved performance

### **Frontend & User Interface**
- **Modern JavaScript (ES6+)** - Responsive, interactive chat interface
- **CSS3 with Flexbox/Grid** - Beautiful, accessible, mobile-responsive styling
- **Server-Sent Events (SSE)** - Real-time streaming responses
- **WebSocket Support** - Bidirectional communication for enhanced UX

### **Development & Deployment**
- **Git Submodules** - Modular architecture with NLWeb as a submodule
- **Virtual Environments** - Isolated Python dependencies
- **Docker Support** - Containerized deployment options
- **GitHub Actions** - CI/CD pipeline for automated testing and deployment

### **Data Processing & Integration**
- **Nutrislice API** - Menu data integration from university dining services
- **Web Scraping** - Automated menu data collection and updates
- **Data Transformation** - Conversion from raw menu data to structured JSON-LD
- **Batch Processing** - Efficient loading of large datasets into vector databases

## 🚀 Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:
- **Python 3.12+** - [Download Python](https://www.python.org/downloads/)
- **Git** - [Download Git](https://git-scm.com/downloads)
- **Virtual Environment** - Python venv or conda

### Installation

1. **Clone the repository**
   ```bash
   git clone --recurse-submodules https://github.com/pooosh/AskBucky.git
   cd AskBucky
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On Windows: myenv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r NLWeb/requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   cp NLWeb/.env.template NLWeb/.env
   # Edit NLWeb/.env with your API keys and configuration
   ```

5. **Set up your API keys**
   ```bash
   # Add your LLM provider API key
   OPENAI_API_KEY=your_openai_key_here
   
   # Add your vector database configuration
   AZURE_SEARCH_ENDPOINT=your_azure_endpoint
   AZURE_SEARCH_KEY=your_azure_key
   ```

6. **Load menu data**
   ```bash
   # Fetch current menu data
   python NLWeb/pyscripts/fetch_menu.py
   
   # Transform to structured format
   python NLWeb/pyscripts/nutrislice_to_jsonld.py
   
   # Load into vector database
   python -m NLWeb.code.python.data_loading.db_load
   ```

7. **Start the server**
   ```bash
   python -m NLWeb.code.python.app-aiohttp
   ```

8. **Access AskBucky**
   - Open your browser to `http://localhost:8000`
   - Start asking questions about the menu!

## 💡 Usage

### Basic Queries

AskBucky understands natural language queries about dining hall menus:

```bash
# General menu exploration
"What's available for lunch today?"
"Show me all the options at Four Lakes Market"

# Specific dietary needs
"I need vegetarian options for dinner"
"Show me gluten-free items"

# Nutritional queries
"What are the highest protein options?"
"Find low-calorie meals under 500 calories"

# Meal planning
"Draft me a balanced lunch"
"Create a meal plan for the week"

# Date-specific queries
"What's on the menu for tomorrow's breakfast?"
"Show me Friday's dinner options"
```

### Advanced Features

#### Meal Planning
AskBucky can create comprehensive meal plans:
- "Plan a nutritious dinner with appetizer, main course, and dessert"
- "Give me a high-protein meal plan for today"

#### Nutritional Analysis
Get detailed nutritional information:
- "What are the ingredients in Chicken Alfredo?"
- "Compare the nutrition of pizza vs pasta"
- "Show me items with less than 10g of carbs"

#### Dietary Accommodations
Filter by dietary restrictions:
- "Find vegan options"
- "Show me dairy-free items"
- "What's available for someone with nut allergies?"

### API Usage

AskBucky provides a REST API for integration:

```bash
# Basic query
curl -X POST "http://localhost:8000/ask" \
  -H "Content-Type: application/json" \
  -d '{"query": "What\'s for lunch today?"}'

# With specific parameters
curl -X POST "http://localhost:8000/ask" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "Show me vegetarian options",
    "site": "four-lakes-market",
    "generate_mode": "generate",
    "streaming": true
  }'
```

## 📚 API Documentation

### Core Endpoints

#### `/ask` - Main Query Endpoint
Process natural language queries about menus and nutrition.

**Parameters:**
- `query` (string, required): Natural language question
- `site` (string/array): Target dining hall(s)
- `generate_mode` (string): "list", "summarize", or "generate"
- `streaming` (boolean): Enable real-time responses
- `model` (string): LLM model to use

#### `/sites` - Available Sites
Get list of available dining halls and sections.

#### `/api/oauth/*` - Authentication
OAuth endpoints for user authentication and conversation history.

### Response Formats

AskBucky returns structured JSON responses with:
- **Query Results**: Relevant menu items and nutritional data
- **Metadata**: Source information and confidence scores
- **Conversation Context**: For maintaining chat history

## 🗺️ Roadmap

### Upcoming Features
- [ ] **Mobile App**: Native iOS and Android applications
- [ ] **Voice Interface**: Speech-to-text and text-to-speech capabilities
- [ ] **Personalization**: User preference learning and recommendations
- [ ] **Social Features**: Share meals and recommendations with friends
- [ ] **Integration APIs**: Connect with meal tracking and fitness apps
- [ ] **RecWell Integration**: Gym schedules, fitness classes, and facility information
- [ ] **Campus Events**: Integration with today.wisc.edu for university events and activities
- [ ] **Academic Resources**: Course information, library services, and study spaces
- [ ] **Transportation**: Bus schedules, parking, and campus navigation
- [ ] **Unified UW-Madison Platform**: One-stop-shop for all campus services and information

### Planned Enhancements
- [ ] **Multi-language Support**: Spanish, Chinese, and other languages
- [ ] **Advanced Analytics**: Nutritional trend analysis and insights
- [ ] **Recipe Suggestions**: Cooking instructions and modifications
- [ ] **Allergen Alerts**: Real-time allergen warnings and substitutions
- [ ] **Sustainability Features**: Environmental impact information

### Technical Improvements
- [ ] **Performance Optimization**: Faster query processing and response times
- [ ] **Offline Support**: Local caching for offline menu access
- [ ] **Advanced Search**: Semantic search with image recognition
- [ ] **API Rate Limiting**: Improved scalability and resource management

See the [open issues](https://github.com/pooosh/AskBucky/issues) for a full list of proposed features and known issues.

## 🤝 Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

### How to Contribute

1. **Fork the Project**
2. **Create your Feature Branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit your Changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to the Branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**

### Development Setup

1. **Clone your fork**
   ```bash
   git clone --recurse-submodules https://github.com/your-username/AskBucky.git
   cd AskBucky
   ```

2. **Set up development environment**
   ```bash
   python -m venv dev_env
   source dev_env/bin/activate
   pip install -r NLWeb/requirements.txt
   pip install -r NLWeb/requirements-dev.txt
   ```

3. **Run tests**
   ```bash
   python -m pytest NLWeb/tests/
   ```

4. **Check code quality**
   ```bash
   flake8 NLWeb/code/
   black NLWeb/code/
   ```

### Contribution Guidelines

- **Code Style**: Follow PEP 8 and use Black for formatting
- **Testing**: Write tests for new features and ensure all tests pass
- **Documentation**: Update documentation for any API changes
- **Issues**: Use the issue tracker for bugs and feature requests

### Top Contributors

[![Contributors](https://contrib.rocks/image?repo=pooosh/AskBucky)](https://github.com/pooosh/AskBucky/graphs/contributors)

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

## 📞 Contact

Your Name - piyushshanbhag8@gmail.com

Project Link: [https://github.com/pooosh/AskBucky](https://github.com/pooosh/AskBucky)

## 🙏 Acknowledgments

### Open Source Libraries
- [NLWeb](https://github.com/microsoft/nlweb) - The foundational framework
- [AIOHTTP](https://aiohttp.readthedocs.io/) - Asynchronous web framework
- [Schema.org](https://schema.org/) - Structured data vocabulary
- [OpenAI](https://openai.com/) - Language model APIs

### Data Sources
- **Nutrislice** - Menu data integration
- **University Dining Services** - Menu information and nutritional data

### Community
- **Microsoft NLWeb Team** - For the amazing foundation
- **Open Source Contributors** - For continuous improvements
- **University Community** - For feedback and testing

### Resources
- [Choose an Open Source License](https://choosealicense.com/)
- [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet/)
- [Img Shields](https://shields.io/)
- [GitHub Pages](https://pages.github.com/)
- [Font Awesome](https://fontawesome.com/)
- [React Icons](https://react-icons.github.io/react-icons/)

---

<div align="center">
  <p>Made with ❤️ by the AskBucky Team</p>
  <p>Star this repository if you found it helpful!</p>
</div>

<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/pooosh/AskBucky.svg?style=for-the-badge
[contributors-url]: https://github.com/pooosh/AskBucky/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/pooosh/AskBucky.svg?style=for-the-badge
[forks-url]: https://github.com/pooosh/AskBucky/network/members
[stargazers-shield]: https://img.shields.io/github/stars/pooosh/AskBucky.svg?style=for-the-badge
[stargazers-url]: https://github.com/pooosh/AskBucky/stargazers
[issues-shield]: https://img.shields.io/github/issues/pooosh/AskBucky.svg?style=for-the-badge
[issues-url]: https://github.com/pooosh/AskBucky/issues
[license-shield]: https://img.shields.io/github/license/pooosh/AskBucky.svg?style=for-the-badge
[license-url]: https://github.com/pooosh/AskBucky/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/your-linkedin 