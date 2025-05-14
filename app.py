import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="Accompagnement Retraite",
    page_icon="🧓",
    layout="centered"
)

# Barre latérale pour la navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Aller vers :", ["🏠 Accueil", "📄 Formulaire retraite"])

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
 


