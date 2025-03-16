import streamlit as st

# Set page title and icon
st.set_page_config(page_title="Unit Converter", page_icon="📏")

# Custom CSS for styling
st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        padding: 10px 24px;
        border-radius: 8px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stSelectbox>div>div>select {
        padding: 10px;
        border-radius: 8px;
        border: 1px solid #ccc;
    }
    .stNumberInput>div>div>input {
        padding: 10px;
        border-radius: 8px;
        border: 1px solid #ccc;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title and description
st.title("📏 Unit Converter")
st.write("Convert between different units easily!")

# Define available units
length_units = ["Metre", "Centimetre", "Kilometre", "Millimetre", "Inch", "Foot", "Yard", "Mile"]
weight_units = ["Kilogram", "Gram", "Milligram", "Pound", "Ounce"]
temperature_units = ["Celsius", "Fahrenheit", "Kelvin"]

# Dropdown to select conversion type
conversion_type = st.selectbox("Select Conversion Type", ["Length", "Weight", "Temperature"])

# Dropdowns for "From" and "To" units
if conversion_type == "Length":
    from_unit = st.selectbox("From", length_units)
    to_unit = st.selectbox("To", length_units)
elif conversion_type == "Weight":
    from_unit = st.selectbox("From", weight_units)
    to_unit = st.selectbox("To", weight_units)
else:
    from_unit = st.selectbox("From", temperature_units)
    to_unit = st.selectbox("To", temperature_units)

# Input for value to convert
value = st.number_input("Enter Value", min_value=0.0, value=1.0)

# Conversion logic
def convert_length(value, from_unit, to_unit):
    conversions = {
        "Metre": 1,
        "Centimetre": 100,
        "Kilometre": 0.001,
        "Millimetre": 1000,
        "Inch": 39.3701,
        "Foot": 3.28084,
        "Yard": 1.09361,
        "Mile": 0.000621371,
    }
    return value * (conversions[to_unit] / conversions[from_unit])

def convert_weight(value, from_unit, to_unit):
    conversions = {
        "Kilogram": 1,
        "Gram": 1000,
        "Milligram": 1e6,
        "Pound": 2.20462,
        "Ounce": 35.274,
    }
    return value * (conversions[to_unit] / conversions[from_unit])

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "Kelvin":
            return value + 273.15
        else:
            return value
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        else:
            return value
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        else:
            return value

# Convert button
if st.button("Convert"):
    if conversion_type == "Length":
        result = convert_length(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = convert_weight(value, from_unit, to_unit)
    else:
        result = convert_temperature(value, from_unit, to_unit)
    
    # Display result
    st.success(f"Converted Value: **{result:.2f} {to_unit}**")