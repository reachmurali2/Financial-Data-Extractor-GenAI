import streamlit as st                 # imports streamline, a python library for creating web applications.
import pandas as pd                    # Imports pandas for handling tabular data.
from data_extractor import extract     # Imports the extract function from data_extractor.py, which processes financial text.import

# Title
st.title("Financial Data Extractor")  # Displays the title of the Streamlit app

# input Box
paragraph = st.text_area("Enter financial paragraph")  # provides a text area where users can enter financial data.

# buttton to extract data
if st.button("Extract"):                       # Creates a button labeled "Extract"; if clicked, triggers data extraction.
    if paragraph:                              # Ensures the user has entered text befor extracting data
        extracted_data = extract(paragraph)    # Calls the extract function from data_extrctor.py, passing the user-input paragraph
        data = {                               # Stores the extracted Revenue and EPS(both actual and Expected) in a structured format
            'Measure':['Revenue','EPS'],
            'Estimated':[extracted_data['revenue_expected'], extracted_data['eps_expected']],
            'Actual':[extracted_data['revenue_actual'],extracted_data['eps_actual']]
        }
        df = pd.DataFrame(data)                  # Converts the extracted data into a Pandas DataFrame
        st.table(df)                          # Displays the extracted financial data in a table format.
    else:                                     # Hansles the case where no text is entered
        st.warning("Please enter a paragraph to extract data from.") # Displays a warning message if the user clicks "Extract" without entering text.

