import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from collections import Counter
import ast

st.set_page_config(
    page_title="AI ATS Resume Screening System",
    layout="wide"
)
st.markdown(
    """
    <style>

    .main {
        background-color: #0E1117;
    }

    h1, h2, h3 {
        color: #FAFAFA;
    }

    .stMetric {
        background-color: #1E1E1E;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #333333;
    }

    .stDataFrame {
        border-radius: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.title("ATS Dashboard")

st.sidebar.markdown(
    "AI Resume Screening System"
)

st.sidebar.markdown("---")

st.title("AI-Powered ATS Resume Screening System")

st.markdown(
    "### Intelligent Candidate Ranking and Skill Gap Analysis"
)
filtered_df = pd.read_csv(
    r"D:\AI_ATS_Resume_Screening_System\resume\test\csv\final_ats_results.csv"
)

candidate_options = ["None"] + list(
    filtered_df["resume_name"]
)

selected_candidate = st.selectbox(

    "Select Candidate",

    candidate_options
)

if selected_candidate == "None":
    st.markdown("---")
    st.subheader("Overall Candidate Overview")

    overview_df = filtered_df[
        [
            "resume_name",
            "match_percentage"
        ]
    ].sort_values(
        by="match_percentage",
        ascending=False
    ).head(10)


    def categorize_candidate(score):

        if score >= 80:
            return "🟢 High Match"

        elif score >= 50:
            return "🟡 Medium Match"

        else:
            return "🔴 Low Match"


    overview_df["Category"] = (

        overview_df["match_percentage"]

        .apply(categorize_candidate)
    )

    st.dataframe(
        overview_df
    )

    csv = filtered_df.to_csv(index=False)

    st.download_button(

        label="Download Candidate Rankings CSV",

        data=csv,

        file_name="candidate_rankings.csv",

        mime="text/csv"
    )

else:

    candidate_data = filtered_df[

        filtered_df["resume_name"] == selected_candidate

    ].iloc[0]
    st.markdown("---")
    st.subheader("Candidate Details")

    st.write(
        f"### {candidate_data['resume_name']}"
    )

    st.write(
        f"ATS Match Score: {round(candidate_data['match_percentage'],2)}%"
    )

    st.write(
        f"Matched Skills: {candidate_data['matched_skills']}"
    )

    st.write(
        f"Missing Skills: {candidate_data['missing_skills']}"
    )

    st.write(
        f"Recommendation: {candidate_data['recommendation']}"
    )

total_candidates = len(filtered_df)

average_score = round(
    filtered_df["match_percentage"].mean(),
    2
)

minimum_score = st.sidebar.slider(

    "Minimum ATS Score",

    0,

    100,

    50
)
search_candidate = st.sidebar.text_input(
    "Search Candidate"
)

filtered_df = filtered_df[
    filtered_df["match_percentage"] >= minimum_score
    ]
if search_candidate:

    filtered_df = filtered_df[

        filtered_df["resume_name"]

        .str.contains(
            search_candidate,
            case=False,
            na=False
        )
    ]

top_candidate = filtered_df.iloc[0]["resume_name"]

highest_score = filtered_df["match_percentage"].max()

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Candidates",
    total_candidates
)

col2.metric(
    "Average ATS Score",
    f"{average_score}%"
)

col3.metric(
    "Top Candidate",
    top_candidate
)

col4.metric(
    "Highest Score",
    f"{highest_score}%"
)
st.subheader("Candidate Rankings")

st.dataframe(

    filtered_df[
        [
            "ATS_Rank",
            "resume_name",
            "match_percentage",
            "skill_count"
        ]
    ],

    use_container_width=True
)

st.markdown("---")
st.subheader("Top 10 Candidates")

top_10 = filtered_df.head(10)

fig, ax = plt.subplots(figsize=(10,5))

ax.barh(
    top_10["resume_name"],
    top_10["match_percentage"]
)

ax.set_xlabel("ATS Match Percentage")

ax.set_ylabel("Candidate")

ax.set_title("Top Matching Candidates")

st.pyplot(fig)

st.markdown("---")
st.subheader("Top Skills Across Candidates")

def convert_to_list(skill_string):

    try:
        return ast.literal_eval(skill_string)

    except:
        return []

filtered_df["skills_found"] = (
    filtered_df["skills_found"]
    .apply(convert_to_list)
)

all_skills = []

for skills in filtered_df["skills_found"]:

    all_skills.extend(skills)

skill_counts = Counter(all_skills)

top_skills = skill_counts.most_common(10)

skills = [skill[0] for skill in top_skills]

counts = [skill[1] for skill in top_skills]

fig2, ax2 = plt.subplots(figsize=(12,6))

ax2.barh(skills, counts)

ax2.set_xlabel("Frequency")

ax2.set_ylabel("Skills")

ax2.set_title("Top 10 Skills")

plt.tight_layout()

st.pyplot(fig2)

if selected_candidate == "None":
    st.markdown("---")
    st.subheader("Candidate Score Distribution")

    high_match = len(
        filtered_df[
            filtered_df["match_percentage"] >= 80
        ]
    )

    medium_match = len(
        filtered_df[
            (filtered_df["match_percentage"] >= 50)
            &
            (filtered_df["match_percentage"] < 80)
        ]
    )

    low_match = len(
        filtered_df[
            filtered_df["match_percentage"] < 50
        ]
    )

    labels = [
        "High Match",
        "Medium Match",
        "Low Match"
    ]

    sizes = [
        high_match,
        medium_match,
        low_match
    ]

    fig3, ax3 = plt.subplots(figsize=(6,6))

    ax3.pie(

        sizes,

        labels=labels,

        autopct='%1.1f%%'
    )

    ax3.set_title("Candidate Distribution by ATS Score")

    st.pyplot(fig3)

st.markdown("---")
st.subheader("Skill Gap Analysis")

st.dataframe(

    filtered_df[
        [
            "resume_name",
            "matched_skills",
            "missing_skills",
            "recommendation"
        ]
    ],

    use_container_width=True
)

st.markdown("---")

st.markdown(
    """
💡 AI ATS Resume Screening System | Final Year Project

    By Chaitanya Dhavale
"""
)

