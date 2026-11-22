import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
import PyPDF2

def build_pdf(filename="Resume.pdf"):
    # 0.5 in margins = 36 pt. Printable width = 612 - 72 = 540 pt. Height = 792 - 72 = 720 pt.
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=32,
        bottomMargin=32
    )

    styles = getSampleStyleSheet()

    # Color definitions
    DARK_BLUE = colors.HexColor("#0f172a") # Slate 900
    CRIMSON = colors.HexColor("#b74b4b")   # Signature Crimson
    TEXT_DARK = colors.HexColor("#1e293b") # Slate 800
    TEXT_MUTED = colors.HexColor("#475569")# Slate 600
    LINK_COLOR = colors.HexColor("#0284c7")# Sky 600

    styles.add(ParagraphStyle(
        'MainTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=21,
        alignment=TA_CENTER,
        textColor=DARK_BLUE,
    ))

    styles.add(ParagraphStyle(
        'SubTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=12,
        alignment=TA_CENTER,
        textColor=CRIMSON,
    ))

    styles.add(ParagraphStyle(
        'ContactLine',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.2,
        leading=11,
        alignment=TA_CENTER,
        textColor=TEXT_MUTED,
    ))

    styles.add(ParagraphStyle(
        'SectionHeading',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=12,
        textColor=DARK_BLUE,
        spaceAfter=2,
    ))

    styles.add(ParagraphStyle(
        'ItemTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.8,
        leading=11,
        textColor=DARK_BLUE,
    ))

    styles.add(ParagraphStyle(
        'ItemRight',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.2,
        leading=11,
        alignment=TA_RIGHT,
        textColor=TEXT_MUTED,
    ))

    styles.add(ParagraphStyle(
        'ItemSub',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=8.2,
        leading=10.5,
        textColor=CRIMSON,
    ))

    styles.add(ParagraphStyle(
        'ItemSubRight',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.2,
        leading=10.5,
        alignment=TA_RIGHT,
        textColor=TEXT_MUTED,
    ))

    styles.add(ParagraphStyle(
        'ResumeBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.2,
        leading=10.5,
        alignment=TA_LEFT,
        textColor=TEXT_DARK,
    ))

    styles.add(ParagraphStyle(
        'BulletText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.1,
        leading=10.5,
        textColor=TEXT_DARK,
        leftIndent=10,
        firstLineIndent=-10,
    ))

    story = []

    # 1. HEADER
    story.append(Paragraph("DEEPAK MOURIYA M.", styles['MainTitle']))
    story.append(Spacer(1, 2))
    story.append(Paragraph("AI &amp; Data Science Undergraduate | Full-Stack &amp; AI Solutions Developer", styles['SubTitle']))
    story.append(Spacer(1, 3))
    
    contact_p = ("+91 7418499564 &nbsp;|&nbsp; "
                 "<a href='mailto:deepakmouriya2006@gmail.com' color='#0284c7'>deepakmouriya2006@gmail.com</a> &nbsp;|&nbsp; "
                 "Harur, Dharmapuri, TN &nbsp;|&nbsp; Coimbatore")
    story.append(Paragraph(contact_p, styles['ContactLine']))

    links_p = ("<a href='https://www.linkedin.com/in/deepak-mouriya-ma7919327/' color='#0284c7'>linkedin.com/in/deepak-mouriya</a> &nbsp;|&nbsp; "
               "<a href='https://github.com/Deepak-Mouriya-M' color='#0284c7'>github.com/Deepak-Mouriya-M</a> &nbsp;|&nbsp; "
               "<a href='https://brandvault-ai-1.onrender.com/' color='#0284c7'>Live Project: BrandVault AI</a>")
    story.append(Paragraph(links_p, styles['ContactLine']))
    story.append(Spacer(1, 4))

    def add_section_header(title):
        t = Table(
            [[Paragraph(title.upper(), styles['SectionHeading']), ""]],
            colWidths=[540, 0]
        )
        t.setStyle(TableStyle([
            ('LINEBELOW', (0, 0), (-1, -1), 1.0, CRIMSON),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
            ('TOPPADDING', (0, 0), (-1, -1), 1),
            ('LEFTPADDING', (0, 0), (-1, -1), 0),
            ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ]))
        story.append(t)
        story.append(Spacer(1, 3))

    # 2. PROFESSIONAL SUMMARY
    add_section_header("Professional Summary")
    summary_text = (
        "Passionate AI &amp; Data Science undergraduate at KPRIET with hands-on experience in full-stack web development, "
        "deep learning neural networks, and embedded hardware systems. Winner of the STEM 2025 Competition for an autonomous "
        "3-Axis Robotic Arm prototype. Dedicated to architecting robust, intelligent applications bridging predictive machine learning "
        "models with intuitive, real-world user interfaces."
    )
    story.append(Paragraph(summary_text, styles['ResumeBody']))
    story.append(Spacer(1, 4))

    # 3. TECHNICAL SKILLS
    add_section_header("Technical Skills")
    skills_data = [
        [Paragraph("<b>Programming Languages:</b>", styles['ResumeBody']),
         Paragraph("Python, C++, JavaScript (ES6+), HTML5, CSS3", styles['ResumeBody'])],
        [Paragraph("<b>AI &amp; Machine Learning:</b>", styles['ResumeBody']),
         Paragraph("Machine Learning, Deep Learning, CNNs, LSTMs, TensorFlow, Keras, Scikit-Learn, Ollama Local LLMs, OpenCV", styles['ResumeBody'])],
        [Paragraph("<b>Web &amp; Backend:</b>", styles['ResumeBody']),
         Paragraph("React, Node.js, Express, Flask, MongoDB, RESTful APIs, JSON, Responsive Design", styles['ResumeBody'])],
        [Paragraph("<b>Hardware &amp; Tooling:</b>", styles['ResumeBody']),
         Paragraph("Arduino Microcontrollers, Servo Kinematics, Git, GitHub, Linux Shell, Full-Stack Debugging", styles['ResumeBody'])],
    ]
    skills_table = Table(skills_data, colWidths=[130, 410])
    skills_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 1),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
    ]))
    story.append(skills_table)
    story.append(Spacer(1, 4))

    # 4. EXPERIENCE
    add_section_header("Professional Experience")
    exp_header = Table([
        [Paragraph("<b>Skillchemy</b> - Full Stack Development Intern", styles['ItemTitle']),
         Paragraph("Salem, Tamil Nadu", styles['ItemRight'])],
        [Paragraph("Full-Stack Web Development | Node.js | Client-Server Systems", styles['ItemSub']),
         Paragraph("22 Dec 2025 - 20 Jan 2026", styles['ItemSubRight'])]
    ], colWidths=[390, 150])
    exp_header.setStyle(TableStyle([
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
    ]))
    story.append(exp_header)
    story.append(Spacer(1, 2))

    story.append(Paragraph(
        "&bull;&nbsp; Developed and deployed responsive, user-centric web modules using semantic HTML5, modern CSS3 styling, and modular JavaScript.",
        styles['BulletText']
    ))
    story.append(Paragraph(
        "&bull;&nbsp; Engineered backend routing and asynchronous request processing pipelines using Node.js runtime and REST architecture.",
        styles['BulletText']
    ))
    story.append(Paragraph(
        "&bull;&nbsp; Implemented foundational database structures and data persistence routines, reinforcing structured software debugging and problem-solving.",
        styles['BulletText']
    ))
    story.append(Spacer(1, 4))

    # 5. PROJECTS
    add_section_header("Featured Technical Projects")

    # Project 1: BrandVault AI
    p1 = Table([
        [Paragraph("<b>BrandVault AI</b> - <i>AI-Powered Branding &amp; Visual Identity Platform</i>", styles['ItemTitle']),
         Paragraph("<a href='https://github.com/roshanvikram/BRANDVAULT-AI.git' color='#0284c7'>GitHub</a> | <a href='https://brandvault-ai-1.onrender.com/' color='#0284c7'>Live Demo</a>", styles['ItemRight'])],
        [Paragraph("Tech: Full-Stack Web, AI Branding Engine, Cloud Deployment (Render)", styles['ItemSub']),
         Paragraph("Cloud Deployed", styles['ItemSubRight'])]
    ], colWidths=[370, 170])
    p1.setStyle(TableStyle([('TOPPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 1), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0)]))
    story.append(p1)
    story.append(Paragraph("&bull;&nbsp; Built an AI platform generating automated color palettes, typographic hierarchies, and brand guideline systems in real-time.", styles['BulletText']))
    story.append(Spacer(1, 3))

    # Project 2: VoiceOS
    p2 = Table([
        [Paragraph("<b>VoiceOS</b> - <i>AI-Powered Voice Assistant with Local Intelligence (Ongoing)</i>", styles['ItemTitle']),
         Paragraph("<a href='https://github.com/Deepak-Mouriya-M/VoiceOS-AI-Powered-Voice-Assistant.git' color='#0284c7'>GitHub Repository</a>", styles['ItemRight'])],
        [Paragraph("Tech: Python, Ollama, Local LLMs, SpeechRecognition, Text-to-Speech (TTS)", styles['ItemSub']),
         Paragraph("Desktop Automation", styles['ItemSubRight'])]
    ], colWidths=[390, 150])
    p2.setStyle(TableStyle([('TOPPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 1), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0)]))
    story.append(p2)
    story.append(Paragraph("&bull;&nbsp; Developed a local-first voice assistant running offline Ollama LLMs for private voice command execution and system automation.", styles['BulletText']))
    story.append(Spacer(1, 3))

    # Project 3: 3-Axis Robotic Arm
    p3 = Table([
        [Paragraph("<b>3-Axis Robotic Arm</b> - <i>Hardware Prototype (1st Place Winner - STEM 2025)</i>", styles['ItemTitle']),
         Paragraph("<a href='https://github.com/Deepak-Mouriya-M/3-Axis-Robotic-Arm.git' color='#0284c7'>GitHub Repository</a>", styles['ItemRight'])],
        [Paragraph("Tech: Arduino, C++, Forward/Inverse Kinematics, Servo Actuators", styles['ItemSub']),
         Paragraph("Awarded 1st Prize", styles['ItemSubRight'])]
    ], colWidths=[390, 150])
    p3.setStyle(TableStyle([('TOPPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 1), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0)]))
    story.append(p3)
    story.append(Paragraph("&bull;&nbsp; Engineered a 3-DOF articulated robotic manipulator using calibrated servo kinematics and Arduino C++ for precision pick-and-place.", styles['BulletText']))
    story.append(Spacer(1, 3))

    # Project 4: Image Caption Generator
    p4 = Table([
        [Paragraph("<b>Image Caption Generator</b> - <i>Deep Learning Vision-to-Language Model</i>", styles['ItemTitle']),
         Paragraph("<a href='https://github.com/Deepak-Mouriya-M/Image-Caption-Generator.git' color='#0284c7'>GitHub Repository</a>", styles['ItemRight'])],
        [Paragraph("Tech: Python, TensorFlow, Keras, CNNs, LSTMs, Image Processing", styles['ItemSub']),
         Paragraph("Deep Learning", styles['ItemSubRight'])]
    ], colWidths=[390, 150])
    p4.setStyle(TableStyle([('TOPPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 1), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0)]))
    story.append(p4)
    story.append(Paragraph("&bull;&nbsp; Implemented a CNN-LSTM neural pipeline extracting high-dimensional visual features to generate descriptive natural language captions.", styles['BulletText']))
    story.append(Spacer(1, 3))

    # Project 5: Personal Budget and Expense Tracker
    p5 = Table([
        [Paragraph("<b>Personal Budget &amp; Expense Tracker</b> - <i>MERN Stack Financial Analytics</i>", styles['ItemTitle']),
         Paragraph("<a href='https://github.com/Deepak-Mouriya-M/Personal-Budget-and-Expense-Tracker.git' color='#0284c7'>GitHub Repository</a>", styles['ItemRight'])],
        [Paragraph("Tech: React, Node.js, Express, MongoDB, RESTful APIs", styles['ItemSub']),
         Paragraph("Full-Stack Web", styles['ItemSubRight'])]
    ], colWidths=[390, 150])
    p5.setStyle(TableStyle([('TOPPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 1), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0)]))
    story.append(p5)
    story.append(Paragraph("&bull;&nbsp; Created a full-stack personal finance platform enabling transaction tracking, monthly budget limits, and visual expenditure metrics.", styles['BulletText']))
    story.append(Spacer(1, 4))

    # 6. EDUCATION
    add_section_header("Education")
    edu_table = Table([
        [Paragraph("<b>B.E. in Artificial Intelligence and Data Science</b> - KPRIET, Coimbatore", styles['ItemTitle']),
         Paragraph("<b>CGPA: 7.62 / 10</b>", styles['ItemRight'])],
        [Paragraph("KPR Institute of Engineering and Technology | Anna University Affiliated", styles['ItemSub']),
         Paragraph("Batch: 2024 - 2028", styles['ItemSubRight'])],
        [Paragraph("<b>Higher Secondary Certificate (HSC) &amp; SSLC</b> - Jayam Vidhyalaya Matric HSS", styles['ItemTitle']),
         Paragraph("<b>Score: 87.83%</b>", styles['ItemRight'])],
        [Paragraph("Harur, Dharmapuri, Tamil Nadu | 12th: 512/600 | 11th: 506/600 | 10th: 419/500", styles['ItemSub']),
         Paragraph("Completed: 2024", styles['ItemSubRight'])],
    ], colWidths=[400, 140])
    edu_table.setStyle(TableStyle([
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
    ]))
    story.append(edu_table)
    story.append(Spacer(1, 4))

    # 7. HONORS & ACHIEVEMENTS
    add_section_header("Honors &amp; Achievements")
    story.append(Paragraph(
        "&bull;&nbsp; <b>Winner (1st Prize), STEM 2025 Competition:</b> Awarded First Place for innovative engineering, mechanical design, and embedded control of a 3-Axis Robotic Arm Prototype.",
        styles['BulletText']
    ))
    story.append(Paragraph(
        "&bull;&nbsp; <b>Participant &amp; Showcase, Innovosence 2025:</b> Selected to demonstrate operational kinematics and real-time servo manipulation of an Arduino-powered Robotic Arm.",
        styles['BulletText']
    ))

    doc.build(story)

    # Check page count
    reader = PyPDF2.PdfReader(filename)
    num_pages = len(reader.pages)
    print(f"Generated {filename} successfully with {num_pages} page(s).")
    return num_pages

if __name__ == "__main__":
    build_pdf("Resume.pdf")
