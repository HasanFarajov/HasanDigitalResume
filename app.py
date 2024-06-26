from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Hasan Farajov"
PAGE_ICON = ":wave:"
NAME = "Hasan Farajov"
DESCRIPTION = """
SAP ABAP developer @ CIC | Master's in AI (ASOIU).
"""
EMAIL = "hfaracov321@gmail.com"
SOCIAL_MEDIA = {
    "YouTube": "https://youtube.com",
    "LinkedIn": "https://www.linkedin.com/in/hasan-farajov-a7b875210/",
    "GitHub": "https://github.com/HasanFaracov",
    "Kaggle": "https://www.kaggle.com/hasanfaracov",
}
PROJECTS = {
    "🏆 1": "https://github.com/HasanFaracov",
    "🏆 2": "https://github.com/HasanFaracov",
    "🏆 3": "https://github.com/HasanFaracov",
    "🏆 4": "https://github.com/HasanFaracov",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 1 Years expereince extracting actionable insights from data.
- ✔️ Strong hands on experience and knowledge in SAP(ABAP) and Python.
- ✔️ Good understanding of statistical principles and their respective applications.
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks.
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Pandas, Numpy, Matplotlib,Seaborn Scikit-learn) SQL
- 📊 Data Visulization: PowerBi, MS Excel, Plotly
- 📚 Modeling: Logistic regression, linear regression, decition trees.
- 🗄️ Databases: Oracle,MySQL, MongoDB. 
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**SAP/ABAP Developer (Application Consultant) | Caspian Innovation Center LLC**")
st.write("02/2023 - Present")
st.write(
    """
- ► Complex ABAP programming, testing and debugging functions related to the implementation of SAP modules
- ► Understand the requirements from provided functional designs and transform these requirements into the technical designs
- ► Close communication with functional teams /designers and build professional relationships with clients
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Back-end Developer(Internship) | Deirvlon Technologies**")
st.write("08/2022 - 10/2022")
st.write(
    """
- ► Upgraded PHP Laravel and other framework applications to fit adapting client needs.
- ► Created and used a prototype library for AJAX development. Launched an internal order management system utilizing primarily PHP and
MySQL to introduce a more scalable and reliable solution that allowed 100%
deadline compliance.
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Transportation Coordinator | E&O Global Inc in USA**")
st.write("05/2021 - 05/2022")
st.write(
    """
- ► Scheduling transportation services, allocating drivers, and planning routes.
- ► Processing transportation documentation and monitoring drivers' logbook entries. Liaising between management, drivers, and customers
- ► Collaborating with internal departments to optimize transportation services
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
