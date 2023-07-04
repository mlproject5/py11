import streamlit as st
import math


st.set_page_config(page_title='Unit Converter', page_icon='cal.png', layout="centered", initial_sidebar_state="auto", menu_items=None)


hide_streamlit_style = """
    <style>
    footer {visibility: hidden;}
    </style>
    """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


def tempr():
    def celsius_to_kelvin(celsius):
        return celsius + 273.15

    def celsius_to_fahrenheit(celsius):
        return (celsius * 9 / 5) + 32

    def kelvin_to_celsius(kelvin):
        return kelvin - 273.15

    def kelvin_to_fahrenheit(kelvin):
        return (kelvin - 273.15) * 9 / 5 + 32

    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5 / 9

    def fahrenheit_to_kelvin(fahrenheit):
        return (fahrenheit - 32) * 5 / 9 + 273.15

    conversion_options = {
        "Celsius": {
            "Kelvin": celsius_to_kelvin,
            "Fahrenheit": celsius_to_fahrenheit
        },
        "Kelvin": {
            "Celsius": kelvin_to_celsius,
            "Fahrenheit": kelvin_to_fahrenheit
        },
        "Fahrenheit": {
            "Celsius": fahrenheit_to_celsius,
            "Kelvin": fahrenheit_to_kelvin
        }
    }

    st.markdown("<center><h1 style='font-family: Comic Sans MS; font-weight: 300; font-size: 32px;'>Temperature "
                "Converter</h1></center>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        from_conversion = st.selectbox("From", list(conversion_options.keys()))
    with col2:
        if from_conversion == "Celsius":
            to_conversion = st.selectbox("To", list(conversion_options["Celsius"].keys()))
        else:
            to_conversion = st.selectbox("To", list(conversion_options[from_conversion].keys()))

    input_temperature = st.number_input("Enter the temperature to convert")
    convert_button = st.button("Convert")

    if convert_button:
        conversion_func = conversion_options[from_conversion][to_conversion]
        try:
            converted_temperature = conversion_func(input_temperature)
            converted_temperature_formatted = "{:.2f}".format(converted_temperature)
            st.success(f"Converted temperature: **{converted_temperature_formatted} {to_conversion}**")
        except (ValueError, TypeError):
            st.warning("Please input a valid temperature.")



def length():
    def meters_to_kilometers(meters):
        return meters / 1000

    def meters_to_centimeters(meters):
        return meters * 100

    def meters_to_millimeters(meters):
        return meters * 1000

    def meters_to_micrometers(meters):
        return meters * 1_000_000

    def meters_to_nanometers(meters):
        return meters * 1_000_000_000

    def meters_to_miles(meters):
        return meters * 0.000621371

    def meters_to_yards(meters):
        return meters * 1.094

    def meters_to_inches(meters):
        return meters * 39.37

    conversion_options = {
        "Meters": {
            "Kilometers": meters_to_kilometers,
            "Centimeters": meters_to_centimeters,
            "Millimeters": meters_to_millimeters,
            "Micrometers": meters_to_micrometers,
            "Nanometers": meters_to_nanometers,
            "Miles": meters_to_miles,
            "Yards": meters_to_yards,
            "Inches": meters_to_inches
        },
        "Kilometers": {
            "Meters": lambda x: x * 1000,
            "Centimeters": lambda x: x * 100000,
            "Millimeters": lambda x: x * 1e+6,
            "Micrometers": lambda x: x * 1e+9,
            "Nanometers": lambda x: x * 1e+12,
            "Miles": lambda x: x * 0.621371,
            "Yards": lambda x: x * 1094,
            "Inches": lambda x: x * 39370
        },
        "Centimeters": {
            "Meters": lambda x: x / 100,
            "Kilometers": lambda x: x / 100000,
            "Millimeters": lambda x: x * 10,
            "Micrometers": lambda x: x * 10000,
            "Nanometers": lambda x: x * 1e+7,
            "Miles": lambda x: x * 0.00000621371,
            "Yards": lambda x: x * 0.0109361,
            "Inches": lambda x: x * 0.393701
        },
        "Millimeters": {
            "Meters": lambda x: x / 1000,
            "Kilometers": lambda x: x / 1e+6,
            "Centimeters": lambda x: x / 10,
            "Micrometers": lambda x: x * 1000,
            "Nanometers": lambda x: x * 1e+6,
            "Miles": lambda x: x * 6.2137e-7,
            "Yards": lambda x: x * 0.00109361,
            "Inches": lambda x: x * 0.0393701
        },
        "Micrometers": {
            "Meters": lambda x: x / 1e+6,
            "Kilometers": lambda x: x / 1e+9,
            "Centimeters": lambda x: x / 10000,
            "Millimeters": lambda x: x / 1000,
            "Nanometers": lambda x: x * 1000,
            "Miles": lambda x: x * 6.2137e-10,
            "Yards": lambda x: x * 0.00000109361,
            "Inches": lambda x: x * 0.0000393701
        },
        "Nanometers": {
            "Meters": lambda x: x / 1e+9,
            "Kilometers": lambda x: x / 1e+12,
            "Centimeters": lambda x: x / 1e+7,
            "Millimeters": lambda x: x / 1e+6,
            "Micrometers": lambda x: x / 1000,
            "Miles": lambda x: x * 6.2137e-13,
            "Yards": lambda x: x * 1.0936e-9,
            "Inches": lambda x: x * 3.937e-8
        },
        "Miles": {
            "Meters": lambda x: x / 0.000621371,
            "Kilometers": lambda x: x / 0.621371,
            "Centimeters": lambda x: x / 0.00000621371,
            "Millimeters": lambda x: x / 6.2137e-7,
            "Micrometers": lambda x: x / 6.2137e-10,
            "Nanometers": lambda x: x / 6.2137e-13,
            "Yards": lambda x: x * 1760,
            "Inches": lambda x: x * 63360
        },
        "Yards": {
            "Meters": lambda x: x / 1.094,
            "Kilometers": lambda x: x / 1094,
            "Centimeters": lambda x: x / 0.0109361,
            "Millimeters": lambda x: x / 0.00109361,
            "Micrometers": lambda x: x / 0.00000109361,
            "Nanometers": lambda x: x / 1.0936e-9,
            "Miles": lambda x: x / 1760,
            "Inches": lambda x: x * 36
        },
        "Inches": {
            "Meters": lambda x: x / 39.37,
            "Kilometers": lambda x: x / 39370,
            "Centimeters": lambda x: x / 0.393701,
            "Millimeters": lambda x: x / 0.0393701,
            "Micrometers": lambda x: x / 0.0000393701,
            "Nanometers": lambda x: x / 3.937e-8,
            "Miles": lambda x: x / 63360,
            "Yards": lambda x: x / 36
        }
    }

    st.markdown(
        "<center><h1 style='font-family: Comic Sans MS; font-weight: 300; font-size: 32px;'>Length Converter</h1></center>",
        unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        from_conversion = st.selectbox("From",
                                       ["Please select one", "Meters", "Kilometers", "Centimeters", "Millimeters",
                                        "Micrometers", "Nanometers", "Miles", "Yards", "Inches"])
    with col2:
        if from_conversion == "Please select one":
            to_conversion_options = []
        else:
            to_conversion_options = list(conversion_options[from_conversion].keys())
            # if "Meters" in to_conversion_options:
            #     to_conversion_options.remove("Meters")
        to_conversion = st.selectbox("To", ["Please select one"] + to_conversion_options)

    input_length = st.number_input("Enter the length to convert")
    convert_button = st.button("Convert")

    if convert_button:
        if from_conversion == "Please select one" or to_conversion == "Please select one":
            st.warning("Please select a valid conversion.")
        else:
            conversion_func = conversion_options[from_conversion][to_conversion]

            try:
                converted_length = conversion_func(input_length)
                converted_length_formatted = "{:.2f}".format(converted_length)
                st.success(f"Converted length: **{converted_length_formatted} {to_conversion}**")
            except (ValueError, TypeError):
                st.warning("Please input a valid length.")


def numbConv():
    def decimal_to_binary(decimal):
        return bin(decimal)[2:]

    def decimal_to_octal(decimal):
        return oct(decimal)[2:]

    def decimal_to_hexadecimal(decimal):
        return hex(decimal)[2:].upper()

    def binary_to_decimal(binary):
        return int(binary, 2)

    def binary_to_octal(binary):
        decimal = binary_to_decimal(binary)
        return decimal_to_octal(decimal)

    def binary_to_hexadecimal(binary):
        decimal = binary_to_decimal(binary)
        return decimal_to_hexadecimal(decimal)

    def octal_to_decimal(octal):
        return int(octal, 8)

    def octal_to_binary(octal):
        decimal = octal_to_decimal(octal)
        return decimal_to_binary(decimal)

    def octal_to_hexadecimal(octal):
        decimal = octal_to_decimal(octal)
        return decimal_to_hexadecimal(decimal)

    def hexadecimal_to_decimal(hexadecimal):
        return int(hexadecimal, 16)

    def hexadecimal_to_binary(hexadecimal):
        decimal = hexadecimal_to_decimal(hexadecimal)
        return decimal_to_binary(decimal)

    def hexadecimal_to_octal(hexadecimal):
        decimal = hexadecimal_to_decimal(hexadecimal)
        return decimal_to_octal(decimal)

    conversion_options = {
        "Decimal": {
            "Binary": decimal_to_binary,
            "Octal": decimal_to_octal,
            "Hexadecimal": decimal_to_hexadecimal
        },
        "Binary": {
            "Decimal": binary_to_decimal,
            "Octal": binary_to_octal,
            "Hexadecimal": binary_to_hexadecimal
        },
        "Octal": {
            "Decimal": octal_to_decimal,
            "Binary": octal_to_binary,
            "Hexadecimal": octal_to_hexadecimal
        },
        "Hexadecimal": {
            "Decimal": hexadecimal_to_decimal,
            "Binary": hexadecimal_to_binary,
            "Octal": hexadecimal_to_octal
        }
    }

    st.markdown("<center><h1 style='font-family: Comic Sans MS; font-weight: 300; font-size: 32px;'>Number "
                "Converter</h1></center>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        from_conversion = st.selectbox("From", list(conversion_options.keys()))
    with col2:
        to_conversion = st.selectbox("To", list(conversion_options[from_conversion].keys()))

    input_number = st.text_input("Enter the number to convert")
    convert_button = st.button("Convert")

    if convert_button:
        conversion_func = conversion_options[from_conversion][to_conversion]

        if from_conversion == "Decimal":
            input_number = int(input_number) if input_number else 0
        else:
            input_number = input_number.upper() if input_number else "0"

        try:
            converted_number = conversion_func(input_number)
            st.success(f"Converted number:        **{converted_number}**")
        except (ValueError, TypeError):
            st.warning("Please input a valid number.")


def weight():
    def kilograms_to_grams(kilograms):
        return kilograms * 1000

    def kilograms_to_milligrams(kilograms):
        return kilograms * 1e+6

    def kilograms_to_metric_tons(kilograms):
        return kilograms / 1000

    def kilograms_to_long_tons(kilograms):
        return kilograms * 0.000984207

    def kilograms_to_short_tons(kilograms):
        return kilograms * 0.00110231

    def kilograms_to_pounds(kilograms):
        return kilograms * 2.20462

    def kilograms_to_ounces(kilograms):
        return kilograms * 35.274

    def kilograms_to_carats(kilograms):
        return kilograms * 5000

    def kilograms_to_atomic_mass_units(kilograms):
        return kilograms * 6.02214076e+26

    conversion_options = {
        "Kilograms": {
            "Grams": kilograms_to_grams,
            "Milligrams": kilograms_to_milligrams,
            "Metric Tons": kilograms_to_metric_tons,
            "Long Tons": kilograms_to_long_tons,
            "Short Tons": kilograms_to_short_tons,
            "Pounds": kilograms_to_pounds,
            "Ounces": kilograms_to_ounces,
            "Carats": kilograms_to_carats,
            "Atomic Mass Units": kilograms_to_atomic_mass_units
        },
        "Grams": {
            "Kilograms": lambda x: x / 1000,
            "Milligrams": lambda x: x * 1000,
            "Metric Tons": lambda x: x / 1e+6,
            "Long Tons": lambda x: x * 9.8421e-7,
            "Short Tons": lambda x: x * 1.10231e-6,
            "Pounds": lambda x: x * 0.00220462,
            "Ounces": lambda x: x * 0.035274,
            "Carats": lambda x: x * 5,
            "Atomic Mass Units": lambda x: x * 6.02214076e+23
        },
        "Milligrams": {
            "Kilograms": lambda x: x / 1e+6,
            "Grams": lambda x: x / 1000,
            "Metric Tons": lambda x: x / 1e+9,
            "Long Tons": lambda x: x * 9.8421e-10,
            "Short Tons": lambda x: x * 1.10231e-9,
            "Pounds": lambda x: x * 2.20462e-6,
            "Ounces": lambda x: x * 3.5274e-5,
            "Carats": lambda x: x * 0.005,
            "Atomic Mass Units": lambda x: x * 6.02214076e+20
        },
        "Metric Tons": {
            "Kilograms": lambda x: x * 1000,
            "Grams": lambda x: x * 1e+6,
            "Milligrams": lambda x: x * 1e+9,
            "Long Tons": lambda x: x * 0.984207,
            "Short Tons": lambda x: x * 1.10231,
            "Pounds": lambda x: x * 2204.62,
            "Ounces": lambda x: x * 35274,
            "Carats": lambda x: x * 5e+6,
            "Atomic Mass Units": lambda x: x * 6.02214076e+29
        },
        "Long Tons": {
            "Kilograms": lambda x: x / 0.000984207,
            "Grams": lambda x: x / 9.8421e-7,
            "Milligrams": lambda x: x / 9.8421e-10,
            "Metric Tons": lambda x: x / 0.984207,
            "Short Tons": lambda x: x * 1.12,
            "Pounds": lambda x: x * 2240,
            "Ounces": lambda x: x * 35840,
            "Carats": lambda x: x * 5080234.54,
            "Atomic Mass Units": lambda x: x * 6.02214076e+32
        },
        "Short Tons": {
            "Kilograms": lambda x: x / 0.00110231,
            "Grams": lambda x: x / 1.10231e-6,
            "Milligrams": lambda x: x / 1.10231e-9,
            "Metric Tons": lambda x: x / 1.10231,
            "Long Tons": lambda x: x / 1.12,
            "Pounds": lambda x: x * 2000,
            "Ounces": lambda x: x * 32000,
            "Carats": lambda x: x * 4535923.7,
            "Atomic Mass Units": lambda x: x * 6.02214076e+29
        },
        "Pounds": {
            "Kilograms": lambda x: x / 2.20462,
            "Grams": lambda x: x / 0.00220462,
            "Milligrams": lambda x: x / 2.20462e-6,
            "Metric Tons": lambda x: x / 2204.62,
            "Long Tons": lambda x: x / 2240,
            "Short Tons": lambda x: x / 2000,
            "Ounces": lambda x: x * 16,
            "Carats": lambda x: x * 2267.96,
            "Atomic Mass Units": lambda x: x * 2.73159734e+26
        },
        "Ounces": {
            "Kilograms": lambda x: x / 35.274,
            "Grams": lambda x: x / 0.035274,
            "Milligrams": lambda x: x / 3.5274e-5,
            "Metric Tons": lambda x: x / 35274,
            "Long Tons": lambda x: x / 35840,
            "Short Tons": lambda x: x / 32000,
            "Pounds": lambda x: x / 16,
            "Carats": lambda x: x * 141.748,
            "Atomic Mass Units": lambda x: x * 1.70724579e+25
        },
        "Carats": {
            "Kilograms": lambda x: x / 5000,
            "Grams": lambda x: x / 0.005,
            "Milligrams": lambda x: x / 0.005,
            "Metric Tons": lambda x: x / 5e+6,
            "Long Tons": lambda x: x / 5080234.54,
            "Short Tons": lambda x: x / 4535923.7,
            "Pounds": lambda x: x / 2267.96,
            "Ounces": lambda x: x / 141.748,
            "Atomic Mass Units": lambda x: x * 1.20347096e+23
        },
        "Atomic Mass Units": {
            "Kilograms": lambda x: x / 6.02214076e+26,
            "Grams": lambda x: x / 6.02214076e+23,
            "Milligrams": lambda x: x / 6.02214076e+20,
            "Metric Tons": lambda x: x / 6.02214076e+29,
            "Long Tons": lambda x: x / 6.02214076e+32,
            "Short Tons": lambda x: x / 6.02214076e+29,
            "Pounds": lambda x: x / 2.73159734e+26,
            "Ounces": lambda x: x / 1.70724579e+25,
            "Carats": lambda x: x / 1.20347096e+23
        }
    }

    st.markdown("<center><h1 style='font-family: Comic Sans MS; font-weight: 300; font-size: 32px;'>Weight "
                "Converter</h1></center>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        from_conversion = st.selectbox("From", list(conversion_options.keys()))
    with col2:
        to_conversion = st.selectbox("To", list(conversion_options[from_conversion].keys()))

    input_weight = st.number_input("Enter the weight to convert")
    convert_button = st.button("Convert")

    if convert_button:
        conversion_func = conversion_options[from_conversion][to_conversion]

        try:
            converted_weight = conversion_func(input_weight)
            converted_weight_formatted = "{:.2f}".format(converted_weight)
            st.success(f"Converted weight: **{converted_weight_formatted} {to_conversion}**")
        except (ValueError, TypeError):
            st.warning("Please input a valid weight.")




def main():
    st.sidebar.markdown("""
            <style>
                .sidebar-text {
                    text-align: center;
                    font-size: 32px;
                    font-weight: bold;
                    font-family: Comic Sans MS;
                }
            </style>
            <p class="sidebar-text">Calculator</p>
        """, unsafe_allow_html=True)
    st.sidebar.image(
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR2EXH8nlbxQrOvYjWF_r4uYYNLAYR4nr1Ugg&usqp=CAU",
        use_column_width=True)
    st.sidebar.markdown("<h1 style='font-family: Comic Sans MS; font-weight: 300; font-size: 24px;'>Unit "
                "Converter</h1></center>", unsafe_allow_html=True)
    selected_sidebar = st.sidebar.radio("Please Select One", ["Temperature Converter","Length Converter","Number Converter","Weight Converter"])

    if selected_sidebar == "Temperature Converter":
        tempr()
    elif selected_sidebar == "Length Converter":
        length()
    elif selected_sidebar == "Number Converter":
        numbConv()
    elif selected_sidebar == "Weight Converter":
        weight()


if __name__ == "__main__":
    main()
