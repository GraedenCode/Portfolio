import streamlit as st
import pandas

# Set up the pages configuration
st.set_page_config(page_icon="Images/Icon.webp", page_title="Graeden Boyer")


df = pandas.read_csv("data.csv", sep=";")

# Create two columns with the specified gap
col1, col2 = st.columns(2, gap="large")

# Add content to the first column
with col1:
    st.image("Images/Snow.png", width=350)

# Add content to the second column
with col2:
    st.title("Graeden Boyer")
    content = '''
    Hi, I’m Graeden, a dedicated and self-driven professional with 5 years of sales experience, consistently outperforming peers in my market.
     While I’ve excelled in sales, my true passion lies in software development and technology. Despite financial barriers that prevented me from attending college,
     I’ve taken it upon myself to learn and grow in the tech field. I’m currently self-educating by developing applications,
      staying up-to-date with industry best practices, and continually improving my skills. 
     I’m highly motivated to land my first role in tech, where I can apply my knowledge, contribute to innovative projects,
     and eventually mentor others who share my passion for development.'''
    st.info(content)

rowcol1, rowcol2, rowcol3 = st.columns(3,gap="large")
with rowcol2:
    st.write("<h1><u>Projects</u></h1>", unsafe_allow_html=True)

col3,col4 = st.columns(2, vertical_alignment="center")

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for i, row in df[10:].iterrows():
        container = st.container(border=True)
        with container:
            st.header(row["title"])
            st.image('Images/' + row["image"])
            st.write(row["description"])
            st.link_button(row["title"], row["url"])
            next

        with col4:
            for i, row in df[:10].iterrows():
                container = st.container(border=True)
                with container:
                    st.header(row["title"])
                    st.image('Images/' + row["image"])
                    st.write(row["description"])
                    st.link_button(row["title"], row["url"])

