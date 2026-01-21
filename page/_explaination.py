import streamlit as st

def show_explication_page():
    st.title("📚 Stratégie : La Magie des Dividendes")
    
    st.markdown("""
    Cette application analyse les actions selon les principes de l'investissement "Value" et de rendement. 
    Voici les piliers utilisés pour le scoring :
    """)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("1. Santé du Dividende")
        st.write("- **Rendement :** Doit être attractif mais pas irréaliste.")
        st.write("- **Payout Ratio :** La part des bénéfices reversée (idéalement < 60%).")
        st.write("- **Croissance :** Historique de hausse du dividende sur 5/10 ans.")

    with col2:
        st.subheader("2. Solidité de l'Entreprise")
        st.write("- **Dette :** Capacité de l'entreprise à rembourser (Net Debt/EBITDA).")
        st.write("- **Stabilité :** Bénéfices constants ou en croissance.")
        st.write("- **Valorisation :** Comparaison du PER historique.")

    st.info("💡 **Note :** Un score élevé indique une action qui respecte la majorité de ces critères de sécurité.")