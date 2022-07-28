"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st
# Import for images
from PIL import Image

# Data handling dependencies
import pandas as pd
import numpy as np

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System","EDA","Models","Solution Overview","About us","Contact us"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == "EDA":
        st.title("EXPLORITORY DATA ANALYSIS (EDA)")
        image = Image.open("./resources/imgs/distribution of the rating.jpg")
        st.image(image)
        st.caption("Observation from the bar graph of ratings")
        st.markdown("We see half scores (0.5,1.5,2.5,3.5 and 4.5) are less commonly used then integer score values.")

        image = Image.open("./resources/imgs/the highest rated movies.jpg")
        st.image(image)
        st.caption("Observation from the bar graph of ratings")
        st.markdown("We see half scores (0.5,1.5,2.5,3.5 and 4.5) are less commonly used then integer score values.")

        image = Image.open("./resources/imgs/Most popular genres.jpg")
        st.image(image)
        st.caption("Observation from the bar graph of ratings")
        st.markdown("We see half scores (0.5,1.5,2.5,3.5 and 4.5) are less commonly used then integer score values.")



    
    if page_selection == "Models":
        st.title("Solution Overview")
        st.write("Describe your winning approach on this page")

    if page_selection == "About us":
        st.title("AI Fanatic Company")
        st.markdown("We are an innovative technological company, established in 2022. We specialize in providing accurate and robust tech solutions\n'")
        #team list
        st.title('Meet Our Team')
        st.markdown('Our team is made up of enthusiastic data scientists who are passionate about data and solving challenging problems.')

        image = Image.open('./resources/imgs/hendrick.jpeg')
        st.image(image,'CEO: Hendrick Makau,\n''Data Scientist', width=250)

        image = Image.open('./resources/imgs/kgotso.jpeg')
        st.image(image,'Co-Founder: Kgotso Matotoka,\n''Data Scientist', width=250)

        image = Image.open('./resources/imgs/tshili.jpeg')
        st.image(image,'Co-Founder: Tshilisanani Mudau,\n''Data Scientist', width=250)

        image = Image.open('./resources/imgs/fm.jpg')
        st.image(image,'CTO: Fortune Mwenda,\n''Data Scientist', width=250)

        image = Image.open('./resources/imgs/zama.jpeg')
        st.image(image,'Co-Founder: Zanele Myeni,\n''Data Scientist', width=250)

        
    if page_selection == "Contact us":
        st.title("GET IN TOUCH")
        st.caption("If you have questions or just want to get in touch, use the form below. We look forward to hearing from you!")
        st.header("Message Us")
        with st.form("form",clear_on_submit = True):
          name = st.text_input("Enter full name")
          email = st.text_input("Enter Email Address")
          message = st.text_area("message")
          submit = st.form_submit_button("Submit")
        col1,col2,col3 = st.columns(3)
        col1,col2,col3 = st.columns(3)
        with col1:
            st.subheader("Address")
           
            st.markdown("South Africa – Gauteng (Head Office)")
            st.markdown("JHB")
            st.markdown("2022")
            with col2:
                st.subheader("Phone")
              
                st.markdown("(+27) 7835 68974")
                st.markdown("(+27) 9452 25117")
               
                with col3:
                    st.subheader("Emails")
                    st.markdown("aifanatic@gmail.com")
                    st.markdown("mokgonyana@gmail.com")

    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("In this project, we succeeded in building an unsupervised machine learning model that is able to recommend movies based on content-based or collaborative filtering and is capable of accurately predicting how a user will rate a movie they have not yet viewed, based on their historical preferences.")

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


if __name__ == '__main__':
    main()
