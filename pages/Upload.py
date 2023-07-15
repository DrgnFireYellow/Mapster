import streamlit as st
import json
with open("projects.json") as projectsfile:
    projects = json.load(projectsfile)
st.write("# Upload")
project_name = st.text_input("*Project Name:")
project_description = st.text_area("*Project Description:")
minecraft_edition = st.radio(
    "*Minecraft Edition:", ["Java", "Java w/ Forge", "Java w/ Fabric", "Bedrock"]
)
minecraft_version = st.text_input("*Minecraft Version:")
project_file = st.file_uploader("*Project File:")
project_data = {}


def submit():
    if project_name:
        if project_description:
            if project_file:
                if minecraft_version:
                    project_data["name"] = project_name
                    project_data["description"] = project_description
                    project_data["edition"] = minecraft_edition
                    project_data["minecraft_version"] = minecraft_version
                    project_data["project_file"] = project_file.name
                    with open(f"project_files/{project_file.name}", "wb") as f:
                        f.write(project_file.getvalue())
                    projects.append(project_data)
                    with open("projects.json", "w") as projectsfile:
                        json.dump(projects, projectsfile)
                    st.write("Uploaded Succesfully")


submit_button = st.button("Submit", on_click=submit)
