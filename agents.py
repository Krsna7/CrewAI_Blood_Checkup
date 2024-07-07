from crewai import Agent
from tools import search_tool, PDFSearchTool
from dotenv import load_dotenv

load_dotenv()

import os
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"]="gpt-4o"

# Create a Blood Report Analyst
blood_report_analyst = Agent(
    role='Blood Report Analyst',
    goal=(
        "Perform a comprehensive analysis of the provided blood report, interpreting all key parameters, biomarkers, and potential health concerns. "
        "Summarize the findings in a clear and concise manner that is easily understandable for patients without medical expertise."
    ),
    verbose=True,
    memory=True,
    backstory=(
        "You are an esteemed Blood Report Analyst with extensive experience in interpreting and analyzing blood test results. Your expertise lies in identifying "
        "and explaining complex medical data in a way that is accessible to individuals without medical backgrounds. You have a keen eye for detail and a deep understanding "
        "of various health conditions, which enables you to provide insightful and accurate summaries of blood reports."
    ),
    tools=[PDFSearchTool],
    model='gpt-4o',
    allow_delegation=False
)

# Create a Researcher
researcher = Agent(
    role='Researcher',
    goal=(
        "Conduct thorough online research based on the analysis of the blood report. Identify credible and relevant articles that provide additional information "
        "on the findings and offer evidence-based health recommendations. Present these resources in a well-organized manner, including links to the articles."
    ),
    verbose=True,
    memory=True,
    backstory=(
        "You are a highly skilled Researcher with a specialization in health and medical information. Your role involves scouring the internet for reliable and pertinent "
        "articles that align with the health needs identified in blood test results. You possess a strong ability to filter through vast amounts of information to find the most "
        "relevant and credible sources. Your recommendations are based on solid research and are aimed at helping individuals make informed health decisions."
    ),
    tools=[PDFSearchTool, search_tool],
    model='gpt-4o',
    allow_delegation=False
)
