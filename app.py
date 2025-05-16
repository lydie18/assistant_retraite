import streamlit as st
import base64
import datetime
import pandas as pd
import csv

# --- Configuration de la page ---
st.set_page_config(
    page_title="Assistant Retraite",
    page_icon="🧓",
    layout="centered"
)


try:
    load_css("styles.css")
except FileNotFoundError:
    pass

# --- Affichage bannière HTML ---
st.markdown(
    """
    <div class="banniere-custom">
        <div class="logo-part">
            <img src="assets/logo.png" width="60">
        </div>
        <div class="text-part">
            <h1>Assistant Retraite 🧓</h1>
            <p>Simulez votre pension simplement</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Barre latérale Navigation ---
st.sidebar.title("Navigation")
page = st.sidebar.radio("Aller vers :", [
    "🏠 Accueil",
    "📄 Formulaire retraite",
    "📊 Voir les demandes",
    "📅 Prendre un rendez-vous"
])

def est_disponible(date_rdv, heure_rdv):
    try:
        df = pd.read_csv("rendezvous.csv")
    except FileNotFoundError:
        return True
    return not any((df['Date'] == str(date_rdv)) & (df['Heure'] == str(heure_rdv)))

def enregistrer_rdv(nom, prenom, date_rdv, heure_rdv):
    try:
        df = pd.read_csv("rendezvous.csv")
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Nom", "Prénom", "Date", "Heure"])
    df = df.append({"Nom": nom, "Prénom": prenom, "Date": str(date_rdv), "Heure": str(heure_rdv)}, ignore_index=True)
    df.to_csv("rendezvous.csv", index=False)

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

elif page == "📄 Formulaire retraite":
    st.title("📄 Formulaire de demande d'accompagnement")
    with st.form(key='retraite_form'):
        nom = st.text_input("Nom")
        prenom = st.text_input("Prénom")
        date_naissance = st.date_input("Date de naissance")
        num_secu = st.text_input("Numéro de sécurité sociale")
        adresse = st.text_area("Adresse")
        submit_button = st.form_submit_button(label="Soumettre")
        if submit_button:
            with open("retraite_demandes.csv", mode="a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([nom, prenom, date_naissance, num_secu, adresse])
            st.success("Demande envoyée ! Nous vous contacterons sous peu.")

elif page == "📊 Voir les demandes":
    st.title("📊 Liste des demandes reçues")
    try:
        df = pd.read_csv("retraite_demandes.csv", names=["Nom", "Prénom", "Date de naissance", "N° Sécurité sociale", "Adresse"])
        st.dataframe(df)
    except FileNotFoundError:
        st.warning("Aucune demande enregistrée pour le moment.")

elif page == "📅 Prendre un rendez-vous":
    st.title("📅 Prendre un rendez-vous")
    nom = st.text_input("Nom")
    prenom = st.text_input("Prénom")
    date_rdv = st.date_input("Choisissez une date", min_value=datetime.date.today())
    heure_rdv = st.time_input("Choisissez une heure", value=datetime.time(9, 0))

    if not est_disponible(date_rdv, heure_rdv):
        st.error("Cette date et heure sont déjà réservées, veuillez choisir une autre.")
    else:
        if st.button("Confirmer le rendez-vous"):
            enregistrer_rdv(nom, prenom, date_rdv, heure_rdv)
            st.success(f"Rendez-vous confirmé pour le {date_rdv} à {heure_rdv}.")















