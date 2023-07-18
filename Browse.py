import json

import redis
import streamlit as st

import config

st.set_page_config("Browse | Mapster", "mapster_logo_small.png")
st.image("mapster_logo.png")
redisconnection = redis.Redis(host=config.REDIS_HOST, port=config.REDIS_PORT)

projects = redisconnection.scan_iter()

for project in projects:
    project = json.loads(redisconnection.get(project))
    st.write(
        f"""## {project['name']}
### {project['edition']} {project['minecraft_version']}
{project['description']}"""
    )
    with open(f"project_files/{project['project_file']}", "rb") as project_file:
        st.download_button("Download", project_file.read(), project["project_file"])
