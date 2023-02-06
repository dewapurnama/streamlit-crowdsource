#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import pandas as pd
import time
import io
import xlsxwriter

# In[3]:

st.title('Crowdsource Automation')

tes_input = st.text_input('ini input ayo input')

excel_file = st.file_uploader("Upload File", type=['xls','xlsx'])

buffer = io.BytesIO()

if excel_file is not None:
    df = pd.read_excel(excel_file)
    st.dataframe(df)
    
    df.rename(columns={'Lat':'Lat_TBG','Long':'Long_TBG'}, inplace=True)
    
    st.dataframe(df)
    
    # download button 2 to download dataframe as xlsx

    with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
        # Write each dataframe to a different worksheet.
        df.to_excel(writer, sheet_name='Sheet1', index=False)
        # Close the Pandas Excel writer and output the Excel file to the buffer
        writer.save()

        download2 = st.download_button(
            label="Download data as Excel",
            data=buffer,
            file_name='large_df.xlsx',
            mime='application/vnd.ms-excel'
        )
