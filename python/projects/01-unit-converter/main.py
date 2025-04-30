import streamlit as st

def main():
    st.title("Easy Unit Converter")
    st.header("That Even your grandma could use 😉")

    options = ["Kilometre", "Meter", "Centimetre", "Micrometre", "Nano", 
               "Mile", "Yard", "Foot", "Inch", "Nautical Mile"]

    # Base unit: Meter
    conversion_to_meters = {
        "Kilometre": 1000,
        "Meter": 1,
        "Centimetre": 0.01,
        "Micrometre": 1e-6,
        "Nano": 1e-9,
        "Mile": 1609.34,
        "Yard": 0.9144,
        "Foot": 0.3048,
        "Inch": 0.0254,
        "Nautical Mile": 1852
    }

    col1, col2 = st.columns(2)

    with col1:
        from_option = st.selectbox("From", options)

    with col2:
        to_option = st.selectbox("To", options)

    with col1:
        length = st.number_input("Enter Length", value=0.0)

    with col2:
        if length and from_option and to_option:
            # Convert input to meters first
            length_in_meters = length * conversion_to_meters[from_option]
            # Then convert to target unit
            result = length_in_meters / conversion_to_meters[to_option]

            rounded_result = round(result, 4)
            st.success(f"{length:.2f} {from_option} = {rounded_result} {to_option}")

        else:
            st.warning("Please enter a valid input.")

if __name__ == "__main__":
    main()
