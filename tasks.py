from crewai import Task
from tools import search_tool, PDFSearchTool
from agents import blood_report_analyst, researcher

report_analyze_task = Task(
    description=(
        "Analyze the provided {blood_report} thoroughly. Focus on all key parameters, biomarkers, and potential health issues. "
        "Create a detailed summary that explains the significance of each parameter, highlighting any abnormal findings. "
        "The summary should be accessible to non-experts, providing clear explanations of the patient's health status."
    ),
    expected_output=(
        "A comprehensive summary of the {blood_report} that includes:\n"
        "1. Explanation of all key parameters and their normal ranges\n"
        "2. Detailed description of any abnormal findings\n"
        "3. Potential health implications of these findings\n"
        "4. Any critical areas that require immediate attention\n"
        "The summary should be well-structured and written in a professional yet accessible tone."
    ),
    tools=[PDFSearchTool],
    agent=blood_report_analyst
)

research_task = Task(
    description=(
        "Based on the blood report analysis, conduct extensive research to provide health recommendations and relevant resources. "
        "1. Identify the most critical health issues from the blood report.\n"
        "2. Research and compile a list of specific, actionable health recommendations.\n"
        "3. Find credible articles and resources that support each recommendation.\n"
        "4. Provide a brief summary of each article, explaining its relevance to the blood report findings."
    ),
    expected_output=(
        "A detailed report containing:\n"
        "1. A list of critical health issues identified from the blood report\n"
        "2. Specific health recommendations for each issue, presented in bullet points\n"
        "3. For each recommendation, provide 1-3 relevant articles or resources with:\n"
        "   - A link to the article\n"
        "   - A brief summary of the article's content\n"
        "   - An explanation of how it relates to the patient's blood report findings\n"
        "4. A conclusion summarizing the key actions the patient should take"
    ),
    agent=researcher,
    tools=[PDFSearchTool, search_tool]
)