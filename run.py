from dis import dis
#from interact import chat
import streamlit as st
import pydaisi as pyd
import subprocess

default_txt = '''
Mahendra Singh Dhoni, commonly known as MS Dhoni and Mahi, is an Indian cricket player and was a former captain of the Indian cricket team. Dhoni is a right-handed batsman.

The Indian cricket team won the 2011 Cricket World Cup under his captainship. His Test cricket and One Day International records are the best of all Indian captains to date. He took over the ODI captaincy from Rahul Dravid in 2007 and led the team to its first ever inter-country ODI series wins in Sri Lanka and New Zealand. Dhoni also holds the post of Vice-President of India Cements Ltd. after resigning from Air India. India Cements is the owner of the Indian Premier League team Chennai Super Kings, and Dhoni has been its captain since the first edition of IPL.

Dhoni was given many awards, such as the ICC ODI Player of the Year award in 2008 and 2009 (the first Indian player to achieve this), the Rajiv Gandhi Khel Ratna award in 2007 and the Padma Shri, India's fourth-highest civilian honour, in 2009.

On 6 February 2015, Dhoni's daughter was born. He retired from international cricket in 2020.
'''
def display():
    st.set_page_config(layout = "wide")
    paragraph = st.text_area('Paragraph/Document', default_txt)
    question = st.text_input('Question', "In which year dhoni got award?")

    output = subprocess.check_output("ls", shell=True)
    print (output)
    st.subheader(output)

    #prediction = chat(paragraph, question)
    #st.subheader('answer: {}'.format(prediction))



if __name__ == "__main__":
    display()