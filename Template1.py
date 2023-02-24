import streamlit as st
import re
with open("profile.txt",'r') as source:
    contents = source.read().split("\n")
    profile_image = contents[1]
    name = contents[0]
st.set_page_config(page_title='Resume_' + name,layout="wide",page_icon=profile_image)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                header {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

with st.container(): #Header Part name Image and about
    st.header(name)
    left,right = st.columns(2)
    with right:
        st.image(profile_image,width=100)
    with left:
        with open("about.txt","r") as about:
            for content in about.read().split("\n"):
                st.write(content)
    st.write("---")

with st.container(): #Contact details skill experience education certification
    left,right = st.columns(2)
    with right: #contact details and certification
        st.header("	:telephone_receiver: Contact details: ")
        with open("contact.txt","r") as contact:
            for element in contact.read().split("\n"):
                try:
                    st.write(element.split(" <> ")[0] + " : " + element.split(" <> ")[1])
                except Exception:
                    pass
        with open("certificates.txt","r") as skills_cert: #technical skill
            flag = 0
            for skill_cert in skills_cert.read().split("\n"):
                skill = skill_cert.split(":-")[0]
                if(skill):
                    if(flag == 0):
                        st.header(":man-running: Skills")
                        flag = 1
                    else:
                        pass
                    with st.expander(":man-running: " + skill):
                        try:
                            certificates = skill_cert.split(":-")[1]
                            for certificate in certificates.split(","):
                                st.write(":reminder_ribbon: " + certificate.split("<>")[0] + " : " + certificate.split("<>")[1])
                        except Exception:
                            st.write(" ")
        with open("languages.txt","r") as lang_certs: #Languages
            flag = 0
            for lang_cert in lang_certs.read().split("\n"):
                lang = lang_cert.split(":-")[0]
                if(lang):
                    if(flag == 0):
                        st.header(":ab: Languages Known")
                        flag = 1
                    else:
                        pass
                    with st.expander(":ab: " + lang):
                        try:
                            capabilities = lang_cert.split(":-")[1]
                            st.write(capabilities.split(" : ")[0])
                            certificates = capabilities.split(" : ")[1]
                            for certificate in certificates.split(","):
                                st.write(":reminder_ribbon: " + certificate.split("<>")[0] + " : " + certificate.split("<>")[1])
                        except Exception:
                            st.write(" ")
    with left: #job experience and Education
        with open("experience.txt",'r') as experiences: #job experience
            flag = 0
            for experience in experiences.read().split("\n"):
                company = experience.split(":-")[0]
                if(company):
                    if(flag == 0):
                        st.header(":briefcase: Job Experiences")
                        flag = 1
                    else:
                        pass
                    with st.expander(":briefcase: " + company):
                        try:
                            works_roles = experience.split(":-")[1]
                            location_roles = works_roles.split(" : ")[0]
                            st.info(":round_pushpin: " + location_roles.split(",")[0] + "   :weight_lifter: " + location_roles.split(",")[1])
                            works = works_roles.split(" : ")[1]
                            for work in works.split(","):
                                st.write(":diamond_shape_with_a_dot_inside: " + work)
                                if ("[video]" in work):
                                    video_link = re.findall(r'\(([^)]+)\)', work)
                                    for video in video_link:
                                        st.video(video)
                                if ("[audio]" in work):
                                    audio_link = re.findall(r'\(([^)]+)\)', work)
                                    for audio in audio_link:
                                        st.audio(audio)
                                if ("[image]" in work):
                                    image_link = re.findall(r'\(([^)]+)\)', work)
                                    for image in image_link:
                                        st.image(image)
                        except Exception as e:
                            st.write(" ")
        with open("projects.txt",'r') as projects: #projects undertaken
            flag = 0
            for project in projects.read().split("\n"):
                project_name = project.split(":-")[0]
                if(project_name):
                    if(flag == 0):
                        st.header(":bulb: Project Experiences")
                        flag = 1
                    else:
                        pass
                    with st.expander(":bulb: " + project_name):
                        try:
                            works = project.split(":-")[1]
                            location_org_name = works.split(" : ")[0]
                            st.info(":round_pushpin: " + location_org_name.split(",")[0] + "   :office: " + location_org_name.split(",")[1])
                            for work in works.split(" : ")[1].split(","):
                                st.write(":diamond_shape_with_a_dot_inside: " + work)
                                if("[video]" in work):
                                    video_link = re.findall(r'\(([^)]+)\)', work)
                                    for video in video_link:
                                        st.video(video)
                                if ("[audio]" in work):
                                    audio_link = re.findall(r'\(([^)]+)\)', work)
                                    for audio in audio_link:
                                        st.audio(audio)
                                if ("[image]" in work):
                                    image_link = re.findall(r'\(([^)]+)\)', work)
                                    for image in image_link:
                                        st.image(image)
                        except Exception as e:
                            st.write(" ")
        st.header(":classical_building: Education Background") #education
        with open("education.txt","r") as ed_certs:
            for ed_cert in ed_certs.read().split("\n"):
                board = ed_cert.split(":-")[0]
                with st.expander(":classical_building: " + board):
                    try:
                        details = ed_cert.split(":-")[1]
                        school = details.split("-")[0]
                        st.write(":school: " + " : " + school)
                        school_adress = details.split("-")[1]
                        st.write(":round_pushpin: " + " : " + school_adress)
                        stream = details.split("-")[2]
                        st.write(":books: " + " : " + stream)
                        score = details.split("-")[3]
                        st.write(":pencil: " + " : " + score)
                    except Exception:
                        st.write(" ")

