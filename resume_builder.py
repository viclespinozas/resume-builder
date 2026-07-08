#!/usr/bin/env python3
"""
Resume Builder for Senior IT Professionals
This script generates a professional resume in PDF format based on provided information.
"""

import os
import sys
from datetime import datetime

# Check if we have the required dependencies
try:
    from fpdf import FPDF
    import markdown
except ImportError as e:
    print("Missing required dependencies. Please install them with:")
    print("pip install fpdf markdown")
    sys.exit(1)

class ResumePDF(FPDF):
    def header(self):
        # Add a header with name and contact info
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'VICTOR LUIS ESPINOZA SOTO', 0, 1, 'C')
        self.set_font('Arial', '', 12)
        self.cell(0, 8, 'Senior Software Engineer | Backend Engineer | Distributed Systems Specialist', 0, 1, 'C')
        self.cell(0, 8, 'Davenport, FL | Open to Remote / EU Relocation | +1 (863) 221-8050 | vespinoza.software.engineer@gmail.com', 0, 1, 'C')
        self.ln(10)

    def chapter_title(self, title):
        # Add a chapter title
        self.set_font('Arial', 'B', 14)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 10, title, 0, 1, 'L', 1)
        self.ln(5)

    def chapter_body(self, body):
        # Add body text
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 6, body)
        self.ln(5)

    def add_section(self, title, content):
        # Add a section with title and content
        self.chapter_title(title)
        if isinstance(content, list):
            for item in content:
                self.chapter_body(f"- {item}")
        else:
            self.chapter_body(content)

def create_resume_pdf():
    """Create a PDF resume from the template data"""
    
    # Create PDF instance
    pdf = ResumePDF()
    pdf.add_page()
    
    # Professional Summary
    summary = [
        "Results-driven Senior Software Engineer with over 10 years of experience in designing, developing, and maintaining scalable backend systems and distributed applications.",
        "Expertise in Python, Golang, microservices architecture, and backend engineering principles.",
        "Proven track record of delivering high-performance, reliable software solutions in fast-paced environments.",
        "Strong problem-solving abilities and passion for creating efficient, maintainable code."
    ]
    pdf.add_section("PROFESSIONAL SUMMARY", summary)
    
    # Technical Skills
    skills = [
        "Languages: Python, Golang, JavaScript, SQL, Shell Scripting",
        "Backend Technologies: RESTful APIs, Microservices, GraphQL, Docker, Kubernetes",
        "Databases: PostgreSQL, MySQL, MongoDB, Redis",
        "Cloud & DevOps: AWS, Azure, CI/CD pipelines, Terraform, Jenkins",
        "Systems: Distributed Systems, Load Balancing, Caching Strategies, API Design",
        "Tools: Git, Jira, Confluence, Linux, PostgreSQL, Docker, Kubernetes"
    ]
    pdf.add_section("TECHNICAL SKILLS", skills)
    
    # Professional Experience
    experience = [
        "Senior Backend Engineer | Company Name | Location | Dates",
        "- Led development of scalable backend services using Python and Golang",
        "- Designed and implemented microservices architecture for high-traffic applications",
        "- Collaborated with cross-functional teams to deliver robust distributed systems",
        "- Optimized database performance and implemented caching strategies",
        "- Mentored junior developers and conducted code reviews",
        "- Participated in system design discussions and architecture planning",
        "",
        "Software Engineer | Company Name | Location | Dates",
        "- Developed and maintained backend services and APIs",
        "- Implemented automated testing and CI/CD pipelines",
        "- Worked with agile development methodologies",
        "- Contributed to technical documentation and knowledge sharing"
    ]
    pdf.add_section("PROFESSIONAL EXPERIENCE", experience)
    
    # Education
    education = [
        "Bachelor of Science in Computer Science | University Name | Location | Graduation Year"
    ]
    pdf.add_section("EDUCATION", education)
    
    # Projects
    projects = [
        "[Project Name] - Brief description of the project, technologies used, and key achievements or impact",
        "[Project Name] - Brief description of the project, technologies used, and key achievements or impact"
    ]
    pdf.add_section("PROJECTS", projects)
    
    # Certifications
    certifications = [
        "[Certification Name] - Issuing Organization - Year",
        "[Certification Name] - Issuing Organization - Year"
    ]
    pdf.add_section("CERTIFICATIONS", certifications)
    
    # Save the PDF
    pdf.output('resume_victor_espinoza.pdf', 'F')
    print("Resume created successfully as 'resume_victor_espinoza.pdf'")

if __name__ == "__main__":
    create_resume_pdf()