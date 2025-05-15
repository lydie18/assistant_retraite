import streamlit as st
import csv
import pandas as pd

# Configuration de la page
st.set_page_config(
    page_title="Accompagnement Retraite",
    page_icon="🧓",
    layout="centered"
)

# Barre latérale pour la navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Aller vers :", ["🏠 Accueil", "📄 Formulaire retraite", "📊 Voir les demandes"])

# PAGE D'ACCUEIL
if page == "🏠 Accueil":
    st.title("🧓 Accompagnement Retraite – Permanence Sociale")
    st.markdown("""
    Bienvenue sur notre plateforme d'accompagnement retraite dédiée aux usagers.

    Nous vous aidons à :
    - Comprendre vos droits à la retraite
    - Compléter vos dossiers CARSAT
    - Prendre rendez-vous avec un médiateur social

    > Ce service est **gratuit et confidentiel**.  
    Pour commencer, rendez-vous sur l'onglet **Formulaire retraite** dans le menu de gauche.
    """)

# PAGE FORMULAIRE
elif page == "📄 Formulaire retraite":
    st.title("📄 Formulaire de demande d'accompagnement")
    
    with st.form(key='retraite_form'):
        # Champs du formulaire
        nom = st.text_input("Nom")
        prenom = st.text_input("Prénom")
        date_naissance = st.date_input("Date de naissance")
        num_secu = st.text_input("Numéro de sécurité sociale")
        adresse = st.text_area("Adresse")
        
        # Bouton de soumission
        submit_button = st.form_submit_button(label="Soumettre")
        
        if submit_button:
            # Sauvegarder les données dans un fichier CSV
            with open("retraite_demandes.csv", mode="a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([nom, prenom, date_naissance, num_secu, adresse])
                
            st.success("Demande envoyée ! Nous vous contacterons sous peu.")

# PAGE POUR VOIR LES DEMANDES ENREGISTRÉES
elif page == "📊 Voir les demandes":
    st.title("📊 Liste des demandes reçues")
    
    # Lire le fichier CSV pour afficher les demandes
    try:
        df = pd.read_csv("retraite_demandes.csv")
        st.dataframe(df)
    except FileNotFoundError:
        st.warning("Aucune demande enregistrée pour le moment.")
import streamlit as st
import pandas as pd
import datetime

# Fonction pour vérifier si le rendez-vous est disponible
def est_disponible(date_rdv, heure_rdv):
    try:
        df = pd.read_csv("rendezvous.csv")
    except FileNotFoundError:
        return True  # Si aucun rendez-vous n'est enregistré, tout est disponible
    
    # Vérifier si un rendez-vous existe déjà pour la même date et heure
    if any((df['Date'] == str(date_rdv)) & (df['Heure'] == str(heure_rdv))):
        return False
    return True

# Fonction pour enregistrer un rendez-vous dans le CSV
def enregistrer_rdv(nom, prenom, date_rdv, heure_rdv):
    # Ouvrir (ou créer si nécessaire) un fichier CSV pour stocker les rendez-vous
    try:
        df = pd.read_csv("rendezvous.csv")
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Nom", "Prénom", "Date", "Heure"])
    
    # Ajouter le nouveau rendez-vous
    df = df.append({"Nom": nom, "Prénom": prenom, "Date": date_rdv, "Heure": heure_rdv}, ignore_index=True)
    df.to_csv("rendezvous.csv", index=False)

# Page pour prendre un rendez-vous
if page == "📅 Prendre un rendez-vous":
    st.title("📅 Prendre un rendez-vous")
    
    # Champs de formulaire pour le rendez-vous
    nom = st.text_input("Nom")
    prenom = st.text_input("Prénom")
    
    # Sélectionner la date et l'heure du rendez-vous
    date_rdv = st.date_input("Choisissez une date pour votre rendez-vous", min_value=datetime.date.today())
    heure_rdv = st.time_input("Choisissez une heure pour votre rendez-vous", value=datetime.time(9, 0))
    
    # Vérifier la disponibilité
    if not est_disponible(date_rdv, heure_rdv):
        st.error("Désolé, cette date et heure sont déjà réservées. Veuillez choisir une autre horaire.")
    else:
        # Bouton de soumission
        submit_button = st.button("Confirmer le rendez-vous")
        
        if submit_button:
            # Enregistrer le rendez-vous
            enregistrer_rdv(nom, prenom, date_rdv, heure_rdv)
            st.success(f"Rendez-vous confirmé pour le {date_rdv} à {heure_rdv}.")
st.title("Assistant Retraite 🧓")
st.header("Bienvenue sur le simulateur de retraite !")
st.subheader("Estimez votre pension avec simplicité")

import streamlit as st

# Charger le CSS personnalisé
def load_css(file):
    with open(file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("styles.css")  # Appliquer le CSS

# Titre principal
st.title("Assistant Retraite 🧓")

# Disposition avec colonnes
col1, col2 = st.columns([1, 2])
with col1:
    st.image("logo.png", width=100)  # Remplacer par ton logo
with col2:
    st.subheader("Bienvenue sur votre simulateur de retraite !")
    st.markdown("Ce service vous aide à estimer votre future pension de manière simple et rapide.")

# Formulaire de collecte d'informations
st.header("💼 Vos informations")
nom = st.text_input("Nom")
age = st.slider("Âge actuel", 18, 67, 45)
revenu = st.number_input("Revenu annuel brut (€)", min_value=0)

# Estimation de la retraite
if st.button("Estimer ma retraite"):
    pension = revenu * 0.5  # Calcul simplifié
    st.success(f"Bonjour {nom}, votre pension estimée est de **{pension:.2f} €** par an.")




