from crewai import Agent
from tools import search_tool, PDFSearchTool
from dotenv import load_dotenv

load_dotenv()

import os
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = "gpt-4"  # Changed from "gpt-4o" to "gpt-4"

blood_report_analyst = Agent(
    role='Blood Report Analyst',
    goal=(
        "Perform a comprehensive analysis of the provided blood report, interpreting all key parameters, biomarkers, and potential health concerns. "
        "Provide a detailed summary that is both thorough and accessible to non-experts."
    ),
    backstory=(
        "You are an experienced Blood Report Analyst with a keen eye for detail and a talent for explaining complex medical data in layman's terms. "
        "Your analyses are known for their thoroughness and clarity, helping patients understand their health status comprehensively."
    ),
    tools=[PDFSearchTool],
    verbose=True
)

researcher = Agent(
    role='Health Researcher',
    goal=(
        "Based on the blood report analysis, provide specific health recommendations and find relevant, credible resources to support these recommendations. "
        "Ensure that the information is tailored to the patient's specific health situation as indicated by their blood report."
    ),
    backstory=(
        "You are a meticulous Health Researcher with a background in both medical science and scientific communication. "
        "You excel at finding the most relevant and up-to-date health information and presenting it in a way that's both informative and actionable for patients."
    ),
    tools=[PDFSearchTool, search_tool],
    verbose=True
)