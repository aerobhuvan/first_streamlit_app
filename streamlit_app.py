import streamlit
import pandas

streamlit.title('Bhuvi First app');
streamlit.header('Bhuvi header');
streamlit.text('Bhuvi text');
streamlit.text('Bhuvi text2');

my_pandas_df = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt');
my_pandas_df=my_pandas_df.set_index('Fruit')
streamlit.multiselect("Pick some fruits:", list(my_pandas_df.index))
streamlit.dataframe(my_pandas_df);
