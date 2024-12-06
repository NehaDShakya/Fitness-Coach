# AI Fitness Coach

An intelligent fitness coaching application that provides personalized workout recommendations and exercise guidance using advanced AI technologies.

## Contributors

- Neha Devi SHAKYA
- Khushi CHITRA UDAY
- Chiara BARONE
- Abdeljalil SAYARH

## Features

- Personalized workout recommendations
- Exercise database with detailed instructions
- Visual exercise demonstrations via GIFs
- Intelligent conversation interface for workout planning
- Comprehensive exercise information including target muscles and equipment needed

## Tech Stack

- Python 3.11
- LangChain for AI conversation flow
- OpenAI's ChatGPT for natural language processing
- SQLAlchemy for database management
- Pandas for data manipulation
- Jupyter Notebook for interactive development

## Prerequisites

- Python 3.11
- OpenAI API key
- Tavily API key

## Installation

1. Create and activate a virtual environment:

```bash
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On Unix or MacOS
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.lock
```

4. Create a `.env` file with your API keys:

```
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
LANGCHAIN_API_KEY=your_langchain_api_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT=your_langchain_endpoint
LANGCHAIN_PROJECT=your_langchain_project
```

## Project Structure

```
fitness_coach/
├── data/               # Data files and database
├── src/               
│   ├── configs/       # Configuration files
│   ├── utils/         # Utility functions
│   └── Fitness_Coach.ipynb  # Main application notebook
├── requirements.lock   # Production dependencies
├── requirements-dev.lock  # Development dependencies
└── pyproject.toml     # Project configuration
```

## Usage

1. Start Jupyter Notebook:

```bash
jupyter notebook
```

2. Open `src/Fitness_Coach.ipynb`
3. Follow the notebook cells to interact with the AI Fitness Coach

## How It Works

### Code Architecture

The application is built using a modular architecture:

1. **Data Layer**
   - SQLAlchemy database for storing exercise information
   - Structured data models for exercises, including metadata like target muscles and equipment
   - API integration for fetching exercise demonstrations and GIFs

2. **AI Engine**
   - LangChain for orchestrating the conversation flow
   - Custom tools and agents for exercise recommendation
   - State management using LangGraph for maintaining conversation context

3. **Business Logic**
   - Exercise recommendation algorithms
   - Workout plan generation
   - User input processing and validation

### Generative AI Implementation

The project leverages several GenAI components:

1. **Large Language Model (ChatGPT)**
   - Natural language understanding for user queries
   - Contextual response generation
   - Exercise instruction interpretation and explanation

2. **LangChain Framework**
   - Custom agents for specialized fitness knowledge
   - Tool-augmented conversations for database queries
   - Structured output parsing for consistent responses

3. **Conversation Flow**
   - State management for maintaining context
   - Multi-step reasoning for workout planning
   - Dynamic response generation based on user needs

### MVP Features

The Minimum Viable Product (MVP) includes:

1. **Core Functionality**
   - Basic exercise database with common workouts
   - Simple conversation interface for queries
   - Exercise demonstration via GIFs
   - Basic workout plan generation

2. **User Experience**
   - Interactive Jupyter notebook interface
   - Clear exercise instructions and visual aids
   - Simple query-response workflow

3. **Technical Implementation**
   - Local database setup
   - Basic API integrations
   - Essential AI conversation capabilities

### Future Enhancements

Planned features beyond MVP:

1. **Advanced Personalization**
   - User profile and progress tracking
   - Adaptive workout recommendations
   - Goal-based program generation

2. **Enhanced AI Capabilities**
   - Multi-modal interaction (text, images, videos)
   - Real-time form correction suggestions
   - Nutrition advice integration

3. **Platform Evolution**
   - Web/mobile application interface
   - User authentication and profiles
   - Progress tracking and analytics
   - Social features and community integration
