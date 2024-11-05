import streamlit as st
import random

# Affichage de l'image : 
st.image("piste.jpg") 

# Affichage du titre :
st.markdown("<h1 style='text-align: center;'>⏱️ Mon temps au tour</h1>", unsafe_allow_html=True)

# Description du calculateur :
st.write("Cet outil calcule vos temps de passage au tour de stade en fonction de votre allure cible.  \nPar défaut, la taille du stade est réglé sur 400m, n'oubliez pas de modifier ce paramètre si vous vous entraînez sur un autre type de piste.")
         
# Affichage du titre :
st.title("Allure cible (en min/km)")
# Explicatif :
st.write("Entrez ci-dessous l'allure (en minutes et secondes par km) à laquelle vous souhaitez travailler : ")


# Création de deux colonnes
col1, col2 = st.columns(2)

# Champ d'entrée pour les minutes
with col1:
    minutes = st.number_input("Minutes :", min_value=0, max_value=59, value=6, step=1)

# Champ d'entrée pour les secondes dans la deuxième colonne
with col2:
    secondes = st.number_input("Secondes :", min_value=0, max_value=59, step=1)

# Champ d'entrée pour la longueur du stade
longueur_stade = st.number_input("Taille du stade (en mètres) :", min_value=0, max_value=500, value=400, step=1)
longueur_stade = longueur_stade / 1000

# Calcul du temps au tour pour l'allure cible donnée
Allure_cible = minutes + (secondes / 60)
Temps_au_tour = Allure_cible * longueur_stade
Temps_au_tour_min = int (Temps_au_tour)
Temps_au_tour_sec = int(((Temps_au_tour - Temps_au_tour_min)*60))

st.write (f"**Temps au tour :** {Temps_au_tour_min} min {Temps_au_tour_sec} s")

# Deuxième partie : Clacul des allures en fonction de la VMA
st.title("🏃‍♀️ VMA et Allures")

# Présentation de l'outil et explication des allures :
st.write("Connaître votre VMA permet de calculer 3 allures d'entraînements spécifiques pour progresser :  \n"
         "**Allure 1 :** 80% de l'entraînement pour développer l'endurance de base.  \n"
         "**Allure 2 :** Améliore la résistance et la capacité à soutenir l'effort sur la durée.  \n"
         "**Allure 3 :** Accroît la vitesse et la puissance de course.")
st.write("\n") 
st.write("À partir de votre VMA, ce calculateur détermine vos 3 allures et vous donne le temps qui vous devez faire sur un tour de stade pour les respecter.")
         
# L'utilisateur entre sa VMA :
st.markdown("<h3 style='font-size:24px;'>Ma VMA en km/h :</h3>", unsafe_allow_html=True)

vma = (st.number_input("Entrez votre VMA en km/h pour calculer vos 3 allures d'entraînement :", min_value = 5.0, max_value = 25.0, step=0.1))
vma = round(vma, 1)

longueur_stade_vma = st.number_input ("Taille du stade (mètres) :", min_value=0, max_value=500, value=400, step=1)
longueur_stade_vma = longueur_stade_vma / 1000

# Fonction pour calculer et afficher allure et temps de passage pour une vma donnée
def afficher_allure_et_temps(vma, ratio_vma, type_d_allure):
    vma_ratio = vma * ratio_vma
    allure = 60 / vma_ratio
    allure_min = int(allure)
    allure_sec = int((allure - allure_min) * 60)

    # Calcul et affichage du temps de passage par tour de stade
    temps_tds = allure * longueur_stade_vma
    temps_tds_min = int(temps_tds)
    temps_tds_sec = int((temps_tds - temps_tds_min) * 60)
    
    # Affichage de l'allure
    st.write(f"**{type_d_allure} : {allure_min} min {allure_sec} sec/km**")

    #Affichage du temps de passage au 400m
    st.markdown(f"<p style='text-indent: 2em;'>Soit {temps_tds_min} min {temps_tds_sec} sec au tour.</p>", unsafe_allow_html=True)


# Calcul et affichage des allures et temps de passage pour les trois niveaux
st.write("Voici vos 3 allures d'entraînements, have fun :")

afficher_allure_et_temps(vma, 0.7, "Allure 1")
afficher_allure_et_temps(vma, 0.85, "Allure 2")
afficher_allure_et_temps(vma, 1.0, "Allure 3")

# L'utilisateur obtient une phrase inspirationelles :

phrases_motivationelles = [
    "Chaque goutte de sueur est un pas de plus vers l'excellence. 💧",
    "Repoussez vos limites ! 🚀",
    "L'effort d'aujourd'hui construit la force de demain. 💪",
    "Ne laissez pas la douleur vous arrêter, laissez-la vous propulser ! 🔥",
    "La seule façon d'échouer est de ne pas essayer : l'effort est la clé. 🗝️",
    "Chaque limite que vous franchissez fait de vous un guerrier ! 🏆",
    "L'effort n'est pas une option, c'est un passage obligé vers la victoire. 👟",
    "La seule limite, c'est le ciel 🚀",
    "Le potentiel est infini. ✨",
    "La victoire vous tend les bras 🏆",
    "Vous allez le faire ! 💪",
    "Chaque foulée compte 👟",
    "Vous allez vous étonner. 💥",
    "N'oubliez jamais que vous êtes un champion 🌟",
    "Impossible is nothing 🔥"
]

phrase_aleatoire = random.choice(phrases_motivationelles)
st.markdown(f"<h4>{phrase_aleatoire}</h4>", unsafe_allow_html=True)
