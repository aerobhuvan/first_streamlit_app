import streamlit
import pandas

streamlit.title('Bhuvi First app');
streamlit.header('Bhuvi header');
streamlit.text('Bhuvi text');
streamlit.text('Bhuvi text2');

my_pandas_df = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt');
streamlit.dataframe(my_pandas_df);
