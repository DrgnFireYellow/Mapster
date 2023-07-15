import streamlit as st
import redis
import uuid
import json
st.set_page_config("Upload | Mapster", ":earth_americas:")
redisconnection = redis.Redis()
st.write("# Upload")
project_name = st.text_input("*Project Name:")
project_description = st.text_area("*Project Description:")
minecraft_edition = st.radio(
    "*Minecraft Edition:", ["Java", "Java w/ Forge", "Java w/ Fabric", "Bedrock"]
)
minecraft_version = st.text_input("*Minecraft Version:")
project_file = st.file_uploader("*Project File:", ["zip", "mcworld"])
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
                    try:
                        with open(f"project_files/{project_file.name}", "xb") as f:
                            f.write(project_file.getvalue())
                        redisconnection.set(str(uuid.uuid4()), json.dumps(project_data))
                    except:
                        raise Exception("Project already exists")

submit_button = st.button("Submit", on_click=submit)
