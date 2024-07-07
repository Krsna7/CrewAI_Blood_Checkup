from crewai import Task
from tools import search_tool, PDFSearchTool
from agents import blood_report_analyst, researcher

# Research Task
report_analyze_task = Task(
    description=(
        "Conduct a thorough analysis of the provided {blood_report}. The analysis should cover all key parameters, biomarkers, and potential health issues "
        "identified in the report. The goal is to create an easy-to-understand summary that explains the significance of each parameter and highlights any "
        "abnormal findings. This summary should be accessible to non-experts, providing clear and concise explanations that help the patient understand "
        "their health status."
    ),
    expected_output=(
        "A detailed and comprehensive summary of the {blood_report} that covers all important aspects of the analysis. The summary should include explanations "
        "of key parameters, descriptions of any abnormal findings, and their potential health implications. The document should be well-structured, clear, "
        "and written in a professional tone."
    ),
    tools=[PDFSearchTool],
    agent=blood_report_analyst,
    model='gpt-4o'
)

# Writing Task with Language Model Configuration
research_task = Task(
    description=(
        "Conduct extensive online research based on the summary of the {blood_report}. Identify credible articles and resources that provide further information "
        "on the biomarkers and conditions mentioned in the report. Additionally, develop health recommendations tailored to the patient's needs, based on the "
        "findings from the blood report and the research. Provide a list of relevant links to articles and resources that support the health recommendations."
    ),
    expected_output=(
        "A comprehensive list of health recommendations based on the analysis of the {blood_report}, presented in bullet points. Each recommendation should be "
        "supported by relevant articles and resources, with links provided. The document should include brief summaries of each article, explaining its relevance "
        "to the blood report findings."
    ),
    agent=researcher,
    async_execution=False,
    tools=[PDFSearchTool, search_tool],
    model='gpt-4o',
    output_file='readable-blood-report.md'
)
