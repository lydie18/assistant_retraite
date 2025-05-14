import streamlit as st

st.set_page_config(page_title="Assistant Retraite", page_icon="🧾", layout="centered")

st.title("🧾 Assistant Retraite – CARSAT")
st.markdown("Bienvenue dans votre outil d'accompagnement pour préparer votre dossier retraite avec la CARSAT.")

st.header("✅ Étapes à suivre")

steps = [
    "Créer un compte sur [lassuranceretraite.fr](https://www.lassuranceretraite.fr/)",
    "Télécharger votre relevé de carrière",
    "Vérifier que toutes vos périodes de travail y figurent",
    "Contacter la CARSAT en cas d’erreur ou d’oubli",
    "Remplir votre demande de retraite en ligne",
    "Scanner et envoyer vos justificatifs",
    "Suivre l’avancement de votre dossier dans votre espace personnel"
]

for step in steps:
    st.checkbox(step)

st.header("🆘 Besoin d’aide ?")
with st.expander("Je suis perdu(e)"):
    st.markdown("""
    - Appelez la CARSAT au **3960**
    - Demandez un rendez-vous avec un conseiller retraite
    - Rapprochez-vous de votre **CCAS** ou centre social
    - Contactez une **médiatrice sociale** pour vous aider
    """)

st.header("🧘 Pause bien-être")
if st.button("1 minute pour souffler"):
    st.success("Fermez les yeux. Inspirez lentement... Expirez... Faites-le 5 fois. Vous pouvez le faire ! 😊")

st.markdown("---")
st.caption("Projet réalisé dans le cadre de la formation MSADS – Prototype v0.1")import streamlit as st
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

