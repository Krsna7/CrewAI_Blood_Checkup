# Blood Report analysis using crewAI
This project leverages CrewAI to analyze blood reports, search the web according to the report summary, and provide recommendations to the patient along with relevant links to articles.

## Approach
The project has the following structure:

- `agents`: Contains the agents responsible for different parts of the analysis.
- `tools`: Contains the tools used for various functionalities like web scraping and data processing.
- `tasks`: Contains tasks to be performed by the agents.
- `crew`: Contains the main CrewAI configuration and setup files.
- `requirements.txt`: Lists all the dependencies required for the project.

## Setup Instructions

### 1. Create the Environment

First, create a virtual environment for the project. This helps to manage dependencies and keep the project isolated from other projects on your system.

### 2. Download all the dependencies
```pip install -r requirements.txt```

### 3. Setup the Environment variables
```OPENAI_API_KEY```,
```EXA_API_KEY```

### 4. Run the project
```python crew.py``` 
