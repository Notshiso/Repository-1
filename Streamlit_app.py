import streamlit as st
st.write ("hello") 
name=st.text_input("Your name")
st.write("hello "+name)
genre = st.radio(
    "What's your favorite sport",
    [":rainbow[foot]", "***tennis***", "basket:basketball:"],
    captions = ["t'aime les pieds chef.", "t'as des bras en béton.", "MON GARSSSSS."])

if genre == ':rainbow[foot]':
    st.write('t gay chef.')
else:
    st.write("wallah jte bz.")

input="le meilleur brawler"
list_possibilities=["spike","léon","corbac","edgar"]
st.write("choisis ."+ input)
