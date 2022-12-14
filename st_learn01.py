# ------------------------------ Streamlit MyWebsite Project ------------------------------
#Project_Date : 04.08.2022
#Project Purpose : Make a website with streamlit dictionary
#Project Process :
    #0 -  Install and Import Packages (streamlit, Pillow, streamlit_lottie)
    #1 - Set Page Configrations title, icon, layout
    #2 - Use Local Css to config. Website (create style directory)
    #3 - Load Assets (lottie, images) (Create images directory and put the images here)
    # 4 - Header Section01
# 5- What I do Section02
# 6 - Projects
# 6.1 - Project01 Section03
# 6.2 - Project02 Section04
# 7 - Search Button (Need to add someting)
# 8 - Contact Form (Send Mail to You)
# ------------------------------ ------------------------------ ------------------------------

import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image


# 1 - Set Page Configrations
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# 2 - Use Local Css to config. Website
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}<style>", unsafe_allow_html=True)

local_css("style/style.css")

# 3 - Load Assets (lottie, images)
lottie_coding =load_lottieurl('https://assets10.lottiefiles.com/packages/lf20_0yfsb3a1.json')
img01_contact_form = Image.open('images/coding01.jpg')
img02_contact_form = Image.open(('images/coding02.jpg'))


# 4 - Headers Section01
st.subheader("Hi, I am Abdullah Cay :wave:")
st.title("A Data Analyst from Germany")
st.write("I am passionate about finding ways to use Python ")
st.write("[Learn More >](https://github.com/abdullahcayde)")


# 5- What I do Section02
st.write('---')
with st.container():
    left_column, right_column = st.columns(2)

    with left_column:
        st.header('What I do ?')
        st.write('##')
        st.write(
            '''
            I am learning everyday Coding with Python : 
            - I am on a new project because of that i have to learn streamlit.
            - I have to learn joblib.
            - I have to learn lightgm.
            ''')
        st.write('[Learn more>](https://github.com/abdullahcayde)')

        with right_column:
            st_lottie(lottie_coding, height=300, key='coding')

# 6 - Projects
# 6.1 - Project01 - Pandas Visualization - Section03
with st.container():
    st.write('---')
    st.header('Pandas Visualization')
    st.write('##')
    image_column , text_column = st.columns((1,2))

    with image_column:
        st.image(img01_contact_form)
    with text_column:
        st.subheader('Learn How to visualize your Data with Pandas')
        st.write(
            '''
            Learn how to use Lottie Files in Streamlit !!!!!
        ''')
        st.markdown("[Github Link ...](https://github.com/abdullahcayde/Trainings/blob/main/Pandas_Visualization/Pandas_Visualization_05.ipynb)")

# 6.2 - Project02 - Statistics for Machine Learning - Section04
with st.container():
    st.write('---')
    st.header('Statistics for Machine Learning')
    st.write('##')
    image_column, text_column = st.columns((1, 2))

    with image_column:
        st.image(img02_contact_form)
    with text_column:
        st.subheader('Basic Hypothesis Testing, A/B Testing, Varieance Testing ... ')
        st.write(
            '''
            Learn how to use Lottie Files in Streamlit !!!!!
        ''')
        st.markdown("[Github Link ...](https://github.com/abdullahcayde/Trainings/tree/main/istatistik)")

# 7 - Search Button (Need to add someting)
st.button('Search')

# 8 - Contact Form (Send Mail to You)
with st.container():
    st.write('--')
    st.header('Get In Touch With Me!')
    st.write('##')

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = '''
    <form action="https://formsubmit.co/abdullahcaysa@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    '''
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()







