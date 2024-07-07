from crewai import Crew,Process
from agents import blood_report_analyst,researcher
from tasks import report_analyze_task, research_task
import os

# Forming the tech-focused crew with some enhanced configurations
crew = Crew(
  agents=[blood_report_analyst, researcher],
  tasks=[report_analyze_task, research_task],
  process=Process.sequential,  # Optional: Sequential task execution is default
  memory=True,
  cache=True,
  max_rpm=100,
  share_crew=True
)

## start the task execution process with enhanced feedback
current_directory = os.getcwd()
filename = 'sample_blood_report.pdf'
file_path = os.path.join(current_directory, filename)

result=crew.kickoff(inputs={'blood_report':file_path})
print(result)