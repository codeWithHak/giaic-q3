import streamlit as st
import os
# st.write is a magic command which will figure out by itself how to display different data types 
# Playing with st.write()

# """
# st.write("Hello World 123")
# st.write("Number: ",123)
# st.write("Object: ",{"name":"huzair", "age": 20})
# st.write([1,2,3,4,5])
# st.write(["apple", "pine", "orange"])
# st.write((5,6,7,8,9))
# st.write(3+4)
# "helloo" if True else "No"

# """

# Playing with st.button()
# remember the whole file will re run from top to bottom whenever you interact with a widegt and button's default state is flase
# it become true for a moment only when script runs, after running script it become True immediately and then when script has run it will again become false

# button1 = st.button("Button")
# button2 = st.button("Button 2")
# output = st.empty()

# if button1:
#     st.write("Button 1 was clicked")
    
# elif button2:
#     st.write("Button 2 was clicked")

# PLaying with some text 

st.title("This is a title")
st.header("This is header smaller than title")
st.subheader("This is subheader smaller than header")
st.markdown('**Bold** _italic_  #Heading ##Heading##')
code = """
def main(a,b):
    return a+b
    """
st.code(code, language="python")
st.divider()

#easy way
st.image("./non/image.png", width=300)
# best way
# st.image(os.path.join(os.getcwd(),'non','image.png'))