# AskBucky 🍽️

<div align="center">
  <img src="static/images/bucky_logo.svg" alt="AskBucky Logo" width="200"/>
  <h3>Your UW-Madison AI Dining Companion</h3>
  <p>AskBucky is an intelligent conversational interface that helps you discover, explore, and plan your dining experience with comprehensive menu information and nutritional insights.</p>
  
  <a href="#www.askbucky.com">View Demo</a> •
  <a href="#https://forms.gle/eZrJ5zyoJzoeGNSN7">Report Bug</a> •
  <a href="#https://forms.gle/hEvYrQEgcgFP376j8">Request Feature</a>
</div>

## 🔧 Technical Implementation

**📖 For detailed technical information, architecture, and implementation details, see the [NLWeb-AskBucky README](https://github.com/pooosh/NLWeb-AskBucky#readme).**

This includes:
- Complete data pipeline workflow
- Automation scripts and processes
- Configuration and setup instructions
- Architecture diagrams
- Development guidelines

## 📋 Table of Contents

- [Vision](#-vision-your-uw-madison-ai-companion)
- [About The Project](#-about-the-project)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Getting Started](#-getting-started)
- [Usage](#-usage)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

## 🎯 Vision: Your UW-Madison AI Companion

AskBucky is just the beginning! Our ultimate vision is to create a comprehensive one-stop-shop for all things UW-Madison. While we currently focus on dining hall menus and nutrition, we're planning to expand AskBucky into a unified platform that integrates multiple university data sources:

**Future Integrations:**
- **🏋️ RecWell Data**: Gym schedules, fitness classes, facility availability
- **📅 University Events**: Integration with today.wisc.edu for campus events
- **📚 Academic Resources**: Course information, library hours, study spaces
- **🚌 Transportation**: Bus schedules, parking information, campus navigation
- **🏠 Housing & Facilities**: Residence hall information, building hours
- **🎓 Student Services**: Career services, health resources, student organizations

**The Goal**: Transform AskBucky into your personal AI assistant for everything UW-Madison, making campus life more connected, informed, and engaging through natural language conversations.

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

## 🛠️ Tech Stack

**Core Technologies:**
- **Python 3.12+** - Backend server and AI processing
- **AIOHTTP** - Asynchronous web framework
- **NLWeb Framework** - Microsoft's enterprise-grade embedding and MCP framework
- **Large Language Models** - OpenAI GPT-4, Claude, Gemini, and more
- **Vector Databases** - Azure AI Search, Qdrant, Milvus, Elasticsearch
- **Schema.org** - Structured data markup

**For detailed technical implementation, see the [NLWeb-AskBucky README](https://github.com/pooosh/NLWeb-AskBucky#readme).**

## 🚀 Getting Started

### Prerequisites

- **Python 3.12+** - [Download Python](https://www.python.org/downloads/)
- **Git** - [Download Git](https://git-scm.com/downloads)

### Quick Setup

1. **Clone the repository**
   ```bash
   git clone --recurse-submodules https://github.com/pooosh/AskBucky.git
   cd AskBucky
   ```

2. **Set up environment**
   ```bash
   cd NLWeb
   python -m venv myenv
   source myenv/bin/activate  # On Windows: myenv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure and run**
   ```bash
   cp .env.template .env
   # Edit .env with your API keys
   python -m code.python.app-aiohttp
   ```

4. **Access AskBucky**
   - Open your browser to `http://localhost:8000`
   - Start asking questions about the menu!

**For detailed setup instructions, automation workflows, and configuration options, see the [NLWeb-AskBucky README](https://github.com/pooosh/NLWeb-AskBucky#readme).**

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

- **Meal Planning**: "Plan a nutritious dinner with appetizer, main course, and dessert"
- **Nutritional Analysis**: "Compare the nutrition of pizza vs pasta"
- **Dietary Accommodations**: "Find vegan options" or "Show me dairy-free items"

## 🗺️ Roadmap

### Upcoming Features
- [ ] **Mobile App**: Native iOS and Android applications
- [ ] **Voice Interface**: Speech-to-text and text-to-speech capabilities
- [ ] **Personalization**: User preference learning and recommendations
- [ ] **Social Features**: Share meals and recommendations with friends
- [ ] **RecWell Integration**: Gym schedules, fitness classes, and facility information
- [ ] **Campus Events**: Integration with today.wisc.edu for university events
- [ ] **Academic Resources**: Course information, library services, and study spaces
- [ ] **Transportation**: Bus schedules, parking, and campus navigation
- [ ] **Unified UW-Madison Platform**: One-stop-shop for all campus services

### Planned Enhancements
- [ ] **Multi-language Support**: Spanish, Chinese, and other languages
- [ ] **Advanced Analytics**: Nutritional trend analysis and insights
- [ ] **Recipe Suggestions**: Cooking instructions and modifications
- [ ] **Allergen Alerts**: Real-time allergen warnings and substitutions

## 🤝 Contributing

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
   cd NLWeb
   python -m venv dev_env
   source dev_env/bin/activate
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```

3. **Run tests**
   ```bash
   python -m pytest tests/
   ```

**For detailed development guidelines, contribution areas, and technical documentation, see the [NLWeb-AskBucky README](https://github.com/pooosh/NLWeb-AskBucky#readme).**

### Top Contributors

[![Contributors](https://contrib.rocks/image?repo=pooosh/AskBucky)](https://github.com/pooosh/AskBucky/graphs/contributors)

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

## 📞 Contact

Your Name - piyushshanbhag8@gmail.com

Project Link: [https://github.com/pooosh/AskBucky](https://github.com/pooosh/AskBucky)

## 🙏 Acknowledgments

### Open Source Libraries
- [NLWeb](https://github.com/nlweb-ai/NLWeb) - The foundational framework
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

---

<div align="center">
  <p>Made with ❤️ by the AskBucky Team</p>
  <p>Star this repository if you found it helpful!</p>
</div> 