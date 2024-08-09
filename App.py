import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(layout='wide')

df = pd.read_csv('india.csv')

list_of_states = list(df['State'].unique())
list_of_states.insert(0,'Overall India')

st.sidebar.title('India overall censes analysis')

selected_states = st.sidebar.selectbox('Select a State',list_of_states)
Primary = st.sidebar.selectbox('Select Primary Parameter',sorted(df.columns[2:6]))
secondary = st.sidebar.selectbox('Select secondary Parameter',sorted(df.columns[6:14]))
third = st.sidebar.selectbox('Select Third Parameter',sorted(df.columns[14:24]))

plot = st.sidebar.button('Overall Analysis')

if plot:
    if selected_states == 'Overall India':
        #plot for india
        fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude",size=third , color=secondary, zoom=4,size_max=35,
                                mapbox_style="carto-positron",width=1200,height=700,hover_name='District')

        st.plotly_chart(fig,use_container_width=True)
    
    else:
          # plot for state
        state_df = df[df['State'] == selected_states]

        fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude",size=Primary, color=secondary, zoom=6, size_max=35,
                                mapbox_style="carto-positron", width=1200, height=700,hover_name='District')

        st.plotly_chart(fig, use_container_width=True)

    
