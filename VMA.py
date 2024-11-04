import streamlit as st
import random



# Affichage de l'image : 
st.image("piste.jpg") 

# Affichage du titre :
st.markdown("<h1 style='text-align: center;'>⏱️ Mon temps au tour ⏱️</h1>", unsafe_allow_html=True)

st.write("Cet outil calcule vos temps de passage au tour de stade en fonction de votre allure cible. Par défaut, la taille du stade est réglé sur 400m, n'oubliez pas de modifier ce paramètre si vous vous entraînez sur un autre type de piste.")
         


# Affichage du titre :
st.title("Allure cible (en min/km)")
# Explicatif :
st.write("L'allure cible est l'allure à laquelle vous souhaitez vous entraîner, elle est fonction de votre VMA et du type de séance que vous souhaitez faire.  \nEntrez ci-dessous l'allure à laquelle vous souhaitez travailler en minutes-secondes par km. ")


# Création de deux colonnes
col1, col2 = st.columns(2)

# Champ d'entrée pour la longueur du stade
with col1:
    minutes = st.number_input("Minutes :", min_value=0, max_value=59, value=6, step=1)

# Champ d'entrée pour les secondes dans la deuxième colonne
with col2:
    secondes = st.number_input("Secondes :", min_value=0, max_value=59, step=1)

st.write("N'oubliez pas la taille du stade, ils ne font pas tous 400m !")

longueur_stade = st.number_input("Taille du stade (en mètre) :", min_value=0, max_value=500, value=400, step=1)
longueur_stade = longueur_stade / 1000

Allure_cible = minutes + (secondes / 60)
Temps_au_tour = Allure_cible * longueur_stade
Temps_au_tour_min = int (Temps_au_tour)
Temps_au_tour_sec = int(((Temps_au_tour - Temps_au_tour_min)*60))

st.write (f"Temps au tour : {Temps_au_tour_min} min {Temps_au_tour_sec} s")

# Calcul de l'allure totale en minutes
allure_total = minutes + (secondes / 60)

st.title("🏃‍♀️ VMA et Allure")

# Présentation de l'outil :
st.write("Déterminez vos 3 allures d'entraînements en fonction de votre VMA.")

# L'utilisateur entre sa VMA :
st.markdown("<h3 style='font-size:24px;'>Ma VMA en km/h :</h3>", unsafe_allow_html=True)
vma = (st.number_input("Entrez votre VMA en km/h pour calculer vos 3 allures d'entraînement :", min_value = 5.0, max_value = 25.0, step=0.1))
vma = round(vma, 1)

# L'utilisateur obtient sa VMA + une phrase inspirationelles :

phrases_motivationelles = [
    "la seule limite, c'est le ciel 🚀",
    "le potentiel est infini. ✨",
    "la victoire vous tend les bras 🏆",
    "vous allez le faire ! 💪",
    "chaque foulée vous fera gagner 👟",
    "vous allez vous étonner. 💥",
    "n'oubliez jamais que vous êtes un champion 🌟",
    "impossible is nothing 🔥"
]

phrase_aleatoire = random.choice(phrases_motivationelles)
st.write(f'Avec une VMA à {vma} km/h,', phrase_aleatoire)

# Fonction pour calculer et afficher allure et temps de passage pour une vma donnée
def afficher_allure_et_temps(vma, ratio_vma, type_d_allure):
    vma_ratio = vma * ratio_vma
    allure = 60 / vma_ratio
    allure_min = int(allure)
    allure_sec = int((allure - allure_min) * 60)

    # Calcul et affichage du temps de passage sur 400m
    temps_400m = allure * 0.4
    temps_400m_min = int(temps_400m)
    temps_400m_sec = int((temps_400m - temps_400m_min) * 60)
    
    # Affichage de l'allure
    st.write(f"**{type_d_allure} : {allure_min} min {allure_sec} sec/km**")

    #Affichage du temps de passage au 400m
    st.write(f"Soit {temps_400m_min} min {temps_400m_sec} sec au tour.")


# Calcul et affichage des allures et temps de passage pour les trois niveaux
afficher_allure_et_temps(vma, 0.7, "Allure 1")
afficher_allure_et_temps(vma, 0.85, "Allure 2")
afficher_allure_et_temps(vma, 1.0, "Allure 3")

