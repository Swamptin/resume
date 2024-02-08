from pathlib import Path

import streamlit as st
from PIL import Image

# --- Path settings ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile.png"


# --- General Settings ---
PAGE_TITLE = "Digital CV | Eoghan O'Brien"
PAGE_ICON = ":wave:"
NAME = "Eoghan O'Brien"
DESCRIPTION = """
Developer and Support Engineer with an interest in Information Security.
"""
EMAIL = "hello@eoghanobrien.ie"
SOCIAL_MEDIA = {
        "LinkedIn": "https://linkedin.com",
        "Github": "https://github.com/Swamptin",
        "Mastodon": "https://freeradical.zone",
}
PROJECTS = {
        "A command-line TODO app written in Rust - https://github.com/Swamptin/rust_todo_cli_tool/",
        "A website used for my wedding - "
        "An image checker app - https://github.com/Swamptin/ImageChecker"
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- Load CSS, PDF, & Profile Pic ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- Hero Section ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
            label="Download Resume",
            data=PDFbyte,
            file_name="EoghanOBrien.pdf",
            mime="application/octet=stream",
    )
    st.write("Email:", EMAIL)

# --- Social Links ---
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- Experience & Qualifications ---
st.write("#")
st.subheader("Experience & Qualifications")
st.write(
        """
    - 8 years working across various aspects of IT
    - Developer, Operations, QA, & Support Engineering
    - InfoSec and IT security enthusiast
    """
    )

# --- Skills ---
st.write("#")
st.subheader("Technologies")
st.write(
        """
    - Programming: Python, Bash, Javascript, Java, C#, Rust
    - Databases: MySQL, MS SQL, PostgreSQL
    - OS: Linux, Window Server, Active Directory
    - AWS: EC2, S3, Aurora
    - BI Tools: Metabase
    """
    )

# --- Work History ---
st.write("#")
st.subheader("Work History")
st.write("---")

# --- Job 1
st.write("**Engineering Operations/Tier3 Support | HMH Publishing**")
st.write("11/2019 - Present")
st.write(
        """
    - Triage tickets and resolve or assign them. Track issue trends across
      products and provide tools to help resolve them faster or pre-emptively
      fix them.
    - Generate runbooks, documentation, and tools to help remediate issues. 
      Enhance existing tools used across support to allow efficient and
      effective triaging of issues.
    - Maintain existing Operations infrastructure including EC2 instances, S3
      Buckets, and Aurora PostgreSQL instances. This includes patching and
      reviewing resource provisioning
      """
      )


# --- Job 2
st.write("**System Test Engineer | Blackbox**")
st.write("08/2018 - 09/2019")
st.write(
        """
    - Design, develop and execute test cases.
    - Develop tools to replicate Tier3 support issues.
    - Write concise and descriptive bugs detailing steps to reproduce from a
      user perspective.
    - Update and maintain software used for flashing firmware and testing boards
      before shipping.
    - Maintain a cluster of Windows 2012/2016 VM servers as part of the test
      infrastructure. This included configuring Active Directory users for the
      network
      """
      )


# --- Job 3
st.write("**High Performance Computing Operations Engineer/Developer | General Motors**")
st.write("06/2016 - 07/2018")
st.write(
        """
    - Java and Bash development and maintenance. Projects included remediation
      of issues or building feature requests. The tools delivered were used by
      engineers scheduling jobs to run on the HPC infrastructure.
    - HPC Operations and ticket resolution/reduction.
    - Responsible for middleware software development in Java.
    - Maintenance and patching of HPC environment (1000+ servers) using Chef and
      Puppet
    - Hadoop Operations - providing server management support through Ambari.
      Managing monthly patch cycles across the Hadoop clusters.
    - PHP/MySQL - Maintain, enhance, and secure Operations tools for network
      health monitoring and triggering upgrades when needed.
      """
      )
