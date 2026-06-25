<h1 align="center">
🤖 AI-Powered ATS Resume Screening & Candidate Ranking System
</h1>

<p align="center">
An intelligent Applicant Tracking System (ATS) built with <b>Natural Language Processing (NLP)</b>, <b>Machine Learning</b>, and <b>Streamlit</b> to automate resume screening, candidate ranking, and skill gap analysis.
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![NLTK](https://img.shields.io/badge/NLTK-154F73?style=for-the-badge)
![spaCy](https://img.shields.io/badge/spaCy-09A3D5?style=for-the-badge)
![TF-IDF](https://img.shields.io/badge/TF--IDF-FF9800?style=for-the-badge)
![Cosine Similarity](https://img.shields.io/badge/Cosine_Similarity-4CAF50?style=for-the-badge)

</p>

---

# 📌 Project Overview

Recruiters often spend only a few seconds reviewing each resume, making manual screening both time-consuming and inconsistent. This project addresses that challenge by providing an AI-powered Applicant Tracking System (ATS) capable of automatically analyzing resumes, comparing them against job descriptions, and ranking candidates based on their relevance.

The application leverages **Natural Language Processing (NLP)** techniques such as **text preprocessing**, **TF-IDF vectorization**, and **Cosine Similarity** to measure how closely a candidate's resume matches the required job description. It also performs **skill extraction**, identifies **missing skills**, and presents the results through an intuitive **Streamlit dashboard**.

The primary objective of this project is to simplify the recruitment process by reducing manual effort, improving screening consistency, and helping recruiters identify the most suitable candidates more efficiently.

---
# ✨ Key Features

<table>
<tr>
<td width="50%">

### 📄 Resume Parsing
- Extracts text from PDF resumes
- Cleans and preprocesses resume content
- Supports multiple candidate resumes

</td>

<td width="50%">

### 🤖 NLP Processing
- Text preprocessing and tokenization
- TF-IDF vectorization
- Cosine Similarity matching

</td>
</tr>

<tr>
<td width="50%">

### 📊 Candidate Ranking
- Calculates ATS match percentage
- Ranks candidates automatically
- Identifies High, Medium and Low matches

</td>

<td width="50%">

### 🎯 Skill Gap Analysis
- Detects missing skills
- Compares resume with job description
- Highlights improvement areas

</td>
</tr>

<tr>
<td width="50%">

### 📈 Interactive Dashboard
- Built using Streamlit
- Candidate search
- ATS score filtering
- CSV download support

</td>

<td width="50%">

### ⚡ Machine Learning Pipeline
- Resume Parsing
- Feature Extraction
- TF-IDF Matching
- Candidate Ranking
- Skill Gap Analysis

</td>
</tr>
</table>

---

## 🖥️ Dashboard Overview

<p align="center">
<img src="screenshots/9288709a-3652-4e4e-81f6-6cc343a8c675.png" width="95%">
</p>

<p align="center">
<b>Main dashboard displaying candidate overview, ATS filtering, and search functionality.</b>
</p>

---

## 📊 Candidate Ranking Dashboard

<p align="center">
<img src="screenshots/d85bfee8-fb50-4ef9-945b-8cd558c9be51.png" width="95%">
</p>

<p align="center">
<b>Automatically ranks candidates based on ATS score and displays key recruitment metrics.</b>
</p>
---

## 📈 Analytics Dashboard

<p align="center">
<img src="screenshots/e5d74e4c-2479-429d-82b5-a21a2783982a.png" width="95%">
</p>

<p align="center">
<b>Visualizes top candidates, skill distribution, and recruitment insights.</b>
</p>

## 🎯 Skill Gap Analysis

<p align="center">
<img src="screenshots/b1db2c7b-cfc8-48eb-b343-bf656098fab4.png" width="95%">
</p>

<p align="center">
<b>Highlights matched skills and missing skills for each candidate.</b>
</p>

---

<p align="center">
  <img src="screenshots/workflow image.png" width="100%">
</p>

---

## ⚙️Technical Workflow

The following diagram illustrates the complete workflow of the AI-Powered ATS Resume Screening & Candidate Ranking System.

```mermaid
flowchart LR

subgraph INPUT
A[📄 Resume PDFs]
J[📋 Job Description]
end

subgraph NLP_PIPELINE
B[📑 PDF Text Extraction]
C[🧹 Text Cleaning & Preprocessing]
D[🧠 Skill Extraction]
E[📊 TF-IDF Vectorization]
F[🎯 Cosine Similarity Matching]
end

subgraph ANALYSIS
G[🏆 ATS Score Calculation]
H[🥇 Candidate Ranking]
I[📈 Skill Gap Analysis]
end

subgraph OUTPUT
K[💻 Interactive Streamlit Dashboard]
L[📥 CSV Export]
M[✅ Recruiter Decision Support]
end

A --> B
B --> C
C --> D
D --> E
J --> E
E --> F
F --> G
G --> H
H --> I
I --> K
K --> L
K --> M
``` 

---

# 🛠️ Tech Stack

| Category | Technologies |
|-----------|--------------|
| Programming Language | Python |
| Machine Learning | Scikit-Learn |
| Natural Language Processing | NLTK, spaCy |
| Data Processing | Pandas, NumPy |
| Data Visualization | Matplotlib, Plotly |
| Web Framework | Streamlit |
| Development Environment | Jupyter Notebook, PyCharm |
| Version Control | Git & GitHub |

---


# 📂 Project Structure

```text
AI-ATS-Resume-Screening-System/
│
├── 📁 app/
│   └── 🐍 app.py                     # Main Streamlit application
│
├── 📁 jupyter_notebooks/
│   ├── 📓 01_Text_Extraction.ipynb
│   ├── 📓 02_NLP_Preprocessing.ipynb
│   ├── 📓 03_Skill_Extraction.ipynb
│   ├── 📓 04_Skill_Matching.ipynb
│   ├── 📓 05_Skill_Gap_Analysis.ipynb
│   ├── 📓 06_Data_Visualization.ipynb
│   └── 📓 07_Streamlit_Integration.ipynb
│
├── 📁 resume/
│   ├── 📂 sample_resumes/
│   ├── 📂 extracted_text/
│   └── 📂 processed_data/
│
├── 📁 screenshots/
│   ├── 🖼️ dashboard_overview.png
│   ├── 🖼️ candidate_ranking.png
│   ├── 🖼️ analytics_dashboard.png
│   ├── 🖼️ skill_gap_analysis.png
│   └── 🖼️ workflow_diagram.png
│
├── 📁 docs/
│   ├── 📄 AI_ATS_Project_Report.pdf
│   └── 📄 AI_ATS_Project_Presentation.pdf
│
├── 📄 README.md
├── 📄 requirements.txt
└── 📄 LICENSE
```

---

# 📈 Project Highlights

- Resume Parsing using Natural Language Processing
- TF-IDF based Resume Matching
- Cosine Similarity Candidate Scoring
- Automatic ATS Ranking
- Skill Gap Identification
- Candidate Search & Filtering
- Interactive Streamlit Dashboard
- Download Results as CSV

---

# 🔮 Future Scope

- Multi-language Resume Support
- OCR Support for Scanned Resumes
- Deep Learning Based Resume Matching
- Resume Recommendation System
- Recruiter Authentication Portal
- Cloud Deployment (AWS / Azure)
- Large Language Model (LLM) Integration
- AI Interview Recommendation Engine

---

## 📜 License

This project is developed for educational and academic purposes as part of the Bachelor's Degree in Data Science & Business Analytics.

© 2026 Chaitanya Dhavale. All Rights Reserved.

⭐ If you found this project useful, consider giving it a star!



