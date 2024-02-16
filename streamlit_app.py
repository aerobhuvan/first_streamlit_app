import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('Bhuvi First app');
streamlit.header('Bhuvi header');
streamlit.text('Bhuvi text');
streamlit.text('Bhuvi text2');

my_pandas_df = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt');
my_pandas_df=my_pandas_df.set_index('Fruit');
fruit_selected = streamlit.multiselect("Pick some fruits:", list(my_pandas_df.index), ["Avocado","Strawberries"]);
fruit_to_show = my_pandas_df.loc[fruit_selected]
streamlit.dataframe(fruit_to_show);

streamlit.header('Fruity Vice Advice');
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

#New section to display fruitviceapi
#import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized);

streamlit.stop()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

add_my_fruit = streamlit.text_input('What fruit would you like to add?','Jackfruit')
streamlit.write('Thanks alot for adding ', add_my_fruit)
my_cur.execute("insert into fruit_load_list values ('"+add_my_fruit+"')")
