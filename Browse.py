import streamlit as st
import json

with open("projects.json") as projectsfile:
    projects = json.load(projectsfile)

for project in projects:
    st.write(f"""## {project['name']}
### {project['edition']} {project['minecraft_version']}
{project['description']}""")
    with open(f"project_files/{project['project_file']}", "rb") as project_file:
        st.download_button("Download", project_file.read(), project["project_file"])