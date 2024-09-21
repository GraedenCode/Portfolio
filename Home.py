import streamlit as st
import pandas

# Set up the pages configuration
st.set_page_config(
    page_icon="Images/Icon.webp",
    page_title="Graeden Boyer",
    layout="centered",
    initial_sidebar_state='collapsed'
)


def print_projects(index):
    st.header(title_list[index], anchor=False)
    st.image('Images/' + image_list[index])
    st.write(desc_list[index])
    st.link_button("Source Code", url_list[index])

st.write("<center><h1><u>Graeden Boyer</u></h1></center>", unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.image("Images/Snow.png", width=350)


with col2:
    content = '''
    Hi, I’m Graeden, a dedicated and self-driven professional with 3 years of sales experience, consistently outperforming peers in my market.
     While I’ve excelled in sales, my true passion lies in software development and technology. Despite financial barriers that prevented me from attending college,
     I’ve taken it upon myself to learn and grow in the tech field. I’m currently self-educating by developing applications,
      staying up-to-date with industry best practices, and continually improving my skills. 
     I’m highly motivated to land my first role in tech, where I can apply my knowledge, contribute to innovative projects,
     and eventually mentor others who share my passion for development.'''
    st.info(content)

st.write("<center><h1><u>Projects</u></h1></center>", unsafe_allow_html=True)

col3,col4 = st.columns(2, vertical_alignment="top")

df = pandas.read_csv("data.csv", sep=";")

title_list = []
image_list = []
desc_list = []
url_list = []

for i,row in df.iterrows():
    title_list.append(row['title'])
    image_list.append(row['image'])
    desc_list.append(row['description'])
    url_list.append(row['url'])

count = True
index = 0

while count == True:
    if index == len(title_list):
        count = False
    else:
        if index%2 == 0:
            with col3:
                print_projects(index)
        else:
            with col4:
                print_projects(index)
    index += 1