import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np

#mining Data
df = pd.read_csv('practice.csv')
st.title("Data Analysis")

#df1 = df.drop(['species', 'island', 'bill_length_mm', 'bill_depth',
     #'flipper_length', 'body_mass_g', 'sex'], axis='columns')


if st.button('load dataset'):
    st.write(df)

if st.button('Description dataset'):
    st.write(df.describe())

#a1 = pd.DataFrame(df['species'], df['island'])
#st.line_chart(df['species'], df['island'])

#df2= df.head(10)

#fig = plt.fig(figsize=(10,8))
#plt.plot(df['species'], df['island'])
#st.pyplot(fig)


#st.dataframe(df)
#st.dataframe(df, height=300, width=800)

#import streamlit as st
#st.title('My data Analytics Dashboard')
#st.header('Dataset')
#st.subheader('tyggu')