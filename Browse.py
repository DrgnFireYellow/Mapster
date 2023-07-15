import streamlit as st
import redis
import json
st.set_page_config("Browse | Mapster", ":earth_americas:")
st.write("# Browse")
redisconnection = redis.Redis()

projects = redisconnection.keys("*")

for project in projects:
    project = json.loads(redisconnection.get(project))
    st.write(f"""## {project['name']}
### {project['edition']} {project['minecraft_version']}
{project['description']}""")
    with open(f"project_files/{project['project_file']}", "rb") as project_file:
        st.download_button("Download", project_file.read(), project["project_file"])