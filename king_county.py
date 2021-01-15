import pandas as pd 
import numpy as np
import streamlit as st
import seaborn as sns; sns.set(style = "ticks")
import matplotlib.pyplot as plt

df_kc = pd.read_csv("kc_house_data.csv")
df_kc2 = df_kc[['lat', 'long']]
df_kc2 = df_kc2.rename(columns={'long':'lon'})
df_kc_new = df_kc[['price', 'bedrooms', 'bathrooms', 'sqft_living', 'floors', 'waterfront', 'view', 'condition', 'grade']]
cor = df_kc_new.corr()

def run():
    st.title("King County Housing Project")
    from PIL import Image
    image = Image.open("kc.jpg")
    st.image(image, caption = "A beautiful view of King County", use_column_width = True)
    st.write("A dataframe showing the important variables of houses in King County")
    st.dataframe(df_kc.head())
    st.subheader("Map of King County")
    st.map(df_kc2)
    st.subheader("Price vs Square foot")
    fig, ax = plt.subplots(figsize=(16,8))
    new_plot = ax.scatter(x = 'sqft_living', y = 'price', data = df_kc, c = 'floors', cmap = 'viridis')    
    ax.set_xlabel("Square foot", fontsize = 12)
    ax.set_ylabel("price", fontsize = 12)
    ax.set_title("Price vs Square foot", fontsize = 18)
    plt.colorbar(new_plot)
    st.pyplot(fig)
    st.subheader("A correlation coefficient table of King County Housing Variables")
    fig2, ax2 = plt.subplots(figsize = (16,8))
    sns.heatmap(cor, annot = True, cmap = 'viridis')
    st.pyplot(fig2)


if __name__ == "__main__":
    run()