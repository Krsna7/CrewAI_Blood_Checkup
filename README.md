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




# Blood Report Analysis using CrewAI

This project utilizes CrewAI to analyze blood reports, perform web searches based on report summaries, and provide patient recommendations along with relevant article links.

## Project Overview

Blood Report Analysis using CrewAI is designed to enhance medical diagnostics by automating the interpretation of blood test results. It leverages artificial intelligence to process and interpret data, enabling faster and more accurate insights into patient health.

## Project Structure

The project is structured as follows:

- **agents/**: Contains modules responsible for different aspects of the analysis, such as `blood_report_analyst.py` and `researcher.py`.
- **tools/**: Provides utilities and tools necessary for functionalities like web scraping (`search_tool.py`) and PDF processing (`PDFSearchTool.py`).
- **tasks/**: Defines specific tasks to be executed by the agents, facilitating modular and organized development.
- **crew/**: Includes configuration and setup files for integrating and utilizing CrewAI services.
- **requirements.txt**: Lists all Python dependencies required for the project, ensuring consistent environment setup across different machines.

## Setup Instructions

### 1. Create a Virtual Environment

Setting up a virtual environment ensures isolation and manages project dependencies efficiently. Use the following commands to set up:

'''bash
- python -m venv venv  # Create a virtual environment
- source venv/bin/activate  # Activate the virtual environment (Linux/macOS)'''

### 2. Install Dependencies
Install the required Python packages listed in requirements.txt to ensure all necessary libraries are available:

'''bash
- pip install -r requirements.txt'''


### 3. Set Environment Variables
Before running the project, configure environment variables for API keys required by external services:

OPENAI_API_KEY: API key for accessing OpenAI services.
EXA_API_KEY: API key for accessing EXA services.
These keys enable interaction with external APIs and are crucial for the project's functionality.

### 4. Run the Project
Execute the main script crew.py to initiate blood report analysis using CrewAI:

'''bash
python crew.py''' 

This command starts the analysis process, generating insights and recommendations based on the provided blood reports.

