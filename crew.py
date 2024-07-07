from crewai import Crew, Process
from agents import blood_report_analyst, researcher
from tasks import report_analyze_task, research_task
import os

crew = Crew(
    agents=[blood_report_analyst, researcher],
    tasks=[report_analyze_task, research_task],
    process=Process.sequential,
    verbose=2  # Increased verbosity for more detailed output
)

current_directory = os.getcwd()
filename = 'sample_blood_report.pdf'  # Make sure this matches your actual file name
file_path = os.path.join(current_directory, filename)

result = crew.kickoff(inputs={'blood_report': file_path})
print(result)