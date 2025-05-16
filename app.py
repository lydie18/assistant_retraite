import streamlit as st
import pandas as pd
import csv
import datetime
from PIL import Image

# --- Configuration de la page (TOUT EN PREMIER) ---
st.set_page_config(
    page_title="Assistant Retraite",
    page_icon="🧓",
    layout="centered"
)


load_css("styles.css")

# --- Fonctions pour le tableau de bord ---
def show_conditions():
    st.header("📌 Conditions Générales")
    st.write("""
    Pour pouvoir faire une demande de retraite, voici les critères essentiels :
    - **Âge minimum** : 62 ans pour la retraite de base.
    - **Durée de cotisation** : minimum 166 trimestres.
    """)

def show_documents():
    st.header("📁 Documents à préparer")
    st.write("""
    Avant de commencer votre demande de retraite, voici les documents à rassembler :
    - **Carte d'identité ou passeport**
    - **Justificatifs de vos périodes travaillées**
    """)

def show_steps():
    st.header("🧭 Étapes à suivre")
    st.write("""
    Voici les grandes étapes pour demander votre retraite :
    1. **Préparer vos documents**
    2. **Calculer votre retraite**
    3. **Faire votre demande**
    4. **Envoyer les pièces justificatives**
    """)

def show_tips():
    st.header("💡 Conseils pratiques")
    st.write("""
    Quelques conseils pour éviter les erreurs fréquentes :
    - **Vérifiez vos trimestres cotisés**
    - **Anticipez votre demande**
    """)

def show_deadlines():
    st.header("⏰ Échéances importantes")
    st.write("""
    Assurez-vous de respecter ces dates importantes :
    - **5 mois avant la retraite** : Déposez votre demande.
    """)

def dashboard_section():
    st.title("📊 Tableau de Bord - Retraite")
    st.subheader("Informations essentielles pour démarrer votre dossier retraite")

    sous_menu = [
        "Conditions Générales", 
        "Documents à préparer", 
        "Étapes à suivre", 
        "Conseils pratiques", 
        "Échéances importantes"
    ]
    choix_sous_menu = st.radio("Choisissez une rubrique :", sous_menu)

    if choix_sous_menu == "Conditions Générales":
        show_conditions()
    elif choix_sous_menu == "Documents à préparer":
        show_documents()
    elif choix_sous_menu == "Étapes à suivre":
        show_steps()
    elif choix_sous_menu == "Conseils pratiques":
        show_tips()
    elif choix_sous_menu == "Échéances importantes":
        show_deadlines()

# --- Fonctions pour la gestion des rendez-vous ---
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

# --- Menu principal ---
st.sidebar.title("Navigation")
page = st.sidebar.radio("Aller vers :", [
    "🏠 Accueil",
    "📄 Formulaire retraite",
    "📊 Tableau de bord",
    "📊 Voir les demandes",
    "📅 Prendre un rendez-vous"
])

# --- Pages ---

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

elif page == "📊 Tableau de bord":
    dashboard_section()

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
















