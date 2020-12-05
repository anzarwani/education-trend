import streamlit as st 
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 


#loading data

def load_data():
    df = pd.read_csv('datafile.csv')
    df.rename(columns={ df.columns[0]: "education_level" }, inplace = True)
    df.rename(columns={ df.columns[1]: "95-96" }, inplace = True)
    df.rename(columns={ df.columns[2]: "2007-2008" }, inplace = True)
    df.rename(columns={ df.columns[3]: "2009-2010" }, inplace = True)
    df.rename(columns={ df.columns[4]: "growth_rate" }, inplace = True)

    return df

def raw():
    df_new = pd.read_csv('datafile.csv')
    df_new.rename(columns={ df_new.columns[0]: "education_level" }, inplace = True)
    df_new.rename(columns={ df_new.columns[1]: "95-96" }, inplace = True)
    df_new.rename(columns={ df_new.columns[2]: "2007-2008" }, inplace = True)
    df_new.rename(columns={ df_new.columns[3]: "2009-2010" }, inplace = True)
    df_new.rename(columns={ df_new.columns[4]: "growth_rate" }, inplace = True)

    df_new 
 
def plots():
    #load_data()
    
    selection = st.sidebar.selectbox('Choose year', ('1995', '2008', '2010'))

    if selection == '1995':
        sns.barplot(x = '95-96', y = 'education_level', data = load_data())
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()
    elif selection == '2008':
        sns.barplot(x = '2007-2008', y = 'education_level', data = load_data())
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()

    elif selection == '2010':
        sns.barplot(x = '2009-2010', y = 'education_level', data = load_data())
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()


def main():
    st.title("Education Enrollment Trend in India")

    st.subheader("Main data")
    

    #load_data()
    check = st.checkbox('Show plots')
    check1 = st.checkbox('Show raw data')
    if check1:
        raw()
        
        
    if check:
        plots()





if __name__ == "__main__":
	main()

