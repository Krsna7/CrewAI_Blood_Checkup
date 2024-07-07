
from crewai_tools import EXASearchTool, tool
import os
from PyPDF2 import PdfReader
# Initialize the tool for internet searching capabilities
search_tool = EXASearchTool()


pdf_path = os.path.join(os.getcwd(), 'sample-blood-report.pdf')

@tool("PDFSearchTool")
def PDFSearchTool(pdf_path:str) -> str:
    """Reads a PDF file and returns the text format"""
    reader = PdfReader(pdf_path)
    text = ""
    
    for page in reader.pages:
        text += page.extract_text()
    return text




