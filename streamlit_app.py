import streamlit as st
import numpy as np
from PIL import Image
from sklearn.cluster import KMeans


# ---------------------------------------------------------------------
# Config streamlit
#-----------------------------------------------------------------------------------
st.set_page_config(page_title="Kmeans", page_icon=":tada:", layout="wide")


# ---------------------------------------------------------------------
# SIDEBAR
#-----------------------------------------------------------------------
st.sidebar.header("Segmentation d'image")
K_means=st.sidebar.slider('Nombre de couleurs',2,20,10)
uploaded_file = st.sidebar.file_uploader("Choisissez un fichier jpg", type="jpg")

# ---------------------------------------------------------------------
# Page principale
#-----------------------------------------------------------------------
if uploaded_file is not None:
    image = Image.open(uploaded_file)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader('Image d\'origine')

        # Charge l'image
        image= np.array(image)
        st.image(image)
        # Redimensionne l'image pour qu'elle soit un tableau à deux dimensions
        w, h, d = tuple(image.shape)
        image_array = np.reshape(image, (w * h, d))

        # Effectue le clustering avec KMeans
        n_colors = K_means
        kmeans = KMeans(n_clusters=n_colors, random_state=0).fit(image_array)

        # Recrée l'image avec les couleurs trouvées par KMeans
        labels = kmeans.predict(image_array)
        codebook = kmeans.cluster_centers_
        d_image = np.zeros((w, h, codebook.shape[1]))
        label_idx = 0
        for i in range(w):
            for j in range(h):
                d_image[i][j] = codebook[labels[label_idx]]
                label_idx += 1
    with col2:
        st.subheader('Image clustering')
        st.image(d_image.astype(np.uint8))

else : 
    st.header("Segmentation d'image")
    st.markdown("- Telacharger votre fichier depuis la sidebar")
    st.markdown("- Choisissez le nombre de segmentation voulues")