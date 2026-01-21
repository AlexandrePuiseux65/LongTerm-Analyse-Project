import plotly.graph_objects as go
import streamlit as st

def display_score_gauge(score):
    """
    Affiche une jauge interactive pour le score global.
    """
    # Détermination de la couleur en fonction du score
    if score >= 7:
        color = "#2ECC71"  # Vert (Excellent)
    elif score >= 5:
        color = "#F39C12"  # Orange (Moyen)
    else:
        color = "#E74C3C"  # Rouge (Risqué)

    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = score,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Score 'Magie des Dividendes'", 'font': {'size': 24}},
        gauge = {
            'axis': {'range': [0, 10], 'tickwidth': 1, 'tickcolor': "white"},
            'bar': {'color': color},
            'bgcolor': "rgba(0,0,0,0)",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 5], 'color': 'rgba(231, 76, 60, 0.1)'},
                {'range': [5, 7], 'color': 'rgba(243, 156, 18, 0.1)'},
                {'range': [7, 10], 'color': 'rgba(46, 204, 113, 0.1)'}
            ],
            'threshold': {
                'line': {'color': "white", 'width': 4},
                'thickness': 0.75,
                'value': score
            }
        }
    ))

    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font={'color': "white", 'family': "Arial"},
        height=300,
        margin=dict(l=20, r=20, t=50, b=20)
    )

    st.plotly_chart(fig, use_container_width=True)