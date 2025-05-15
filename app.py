import streamlit as st
import csv
import pandas as pd

# Page principale
st.title("Bienvenue sur l’assistant retraite")
st.write("Voici votre outil pour simuler et gérer votre retraite.")


# === CONTENU PRINCIPAL ===
st.title("Bienvenue sur l'assistant retraite")
st.write("Voici votre espace pour simuler, suivre et optimiser votre retraite.")

# Configuration de la page
st.set_page_config (page_title="Accompagnement Retraite", page_icon="🧓",layout="centered")

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
def load_css(file):
    with open(file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("styles.css")
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
import streamlit as st

menu = ["Accueil", "Tableau de bord", "mémos"]
choix = st.sidebar.selectbox("Navigation", menu)
dashboard_section()
if choix == "Tableau de bord":
    dashboard_section()
else:
    st.write("Bienvenue dans votre application !")

def dashboard_section():
    st.title("Tableau de Bord - Retraite")
    st.subheader("Informations essentielles pour démarrer votre dossier retraite")

    # Ajouter des sections interactives avec des boutons
    menu = ["Conditions Générales", "Documents à préparer", "Étapes à suivre", "Conseils pratiques", "Échéances importantes"]
    choice = st.radio("Choisissez une rubrique", menu)

    if choice == "Conditions Générales":
        show_conditions()

    elif choice == "Documents à préparer":
        show_documents()

    elif choice == "Étapes à suivre":
        show_steps()

    elif choice == "Conseils pratiques":
        show_tips()

    elif choice == "Échéances importantes":
        show_deadlines()

# Sections de contenu
def show_conditions():
    st.header("Conditions Générales")
    st.write("""
        Pour pouvoir faire une demande de retraite, voici les critères essentiels :
        - **Âge minimum** : 62 ans pour la retraite de base.
        - **Durée de cotisation** : minimum 166 trimestres.
    """)

def show_documents():
    st.header("Documents à préparer")
    st.write("""
        Avant de commencer votre demande de retraite, voici les documents à rassembler :
        - **Carte d'identité ou passeport**
        - **Justificatifs de vos périodes travaillées**
    """)

def show_steps():
    st.header("Étapes à suivre")
    st.write("""
        Voici les grandes étapes pour demander votre retraite :
        1. **Préparer vos documents**
        2. **Calculer votre retraite**
        3. **Faire votre demande**
        4. **Envoyer les pièces justificatives**
    """)

def show_tips():
    st.header("Conseils pratiques")
    st.write("""
        Quelques conseils pour éviter les erreurs fréquentes :
        - **Vérifiez vos trimestres cotisés**
        - **Anticipez votre demande**
    """)

def show_deadlines():
    st.header("Échéances importantes")
    st.write("""
        Assurez-vous de respecter ces dates importantes :
        - **5 mois avant la retraite** : Déposez votre demande.
    """)













