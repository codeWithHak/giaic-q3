import streamlit as st
def main():
    st.title("Easy Unit Converter")
    st.header("That Even your grandma could use ;)")
    
    # Dropdown Menu Options 
    options = ["Kilometre", "Meter", "Centimetre", "Micrommetre", "Nano", "Mile", "Yard", "Foot", "inch"," Nauctical Mile"]
    
    # To use two elemnts in one lines create colums
    col1, col2 = st.columns(2)
    
    # col 1 is left column
    with col1:
       from_option = st.multiselect("From", options, max_selections=1)
    
    # col2 is right column
    with col2:
        to_option = st.multiselect("To", options, max_selections=1)

    with col1:
        length = st.number_input("Select Legnth")
    with col2:
        st.text_input(length * 1000)
        if from_option and to_option is not None: 
            if from_option[0] == "Kilomtre" and to_option[0] == "Meter":

    # print(type(from_option))    
    # print(type(to_option))    
    # print(length)    
    


if __name__ == "__main__":
    main()
    
