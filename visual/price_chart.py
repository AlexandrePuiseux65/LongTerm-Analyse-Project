import plotly.graph_objects as go
import streamlit as st

def plot_stock_history(stock):
    """Génère un graphique interactif du prix de l'action."""
    df = stock.prices
    
    if df.empty:
        st.warning("Aucune donnée historique disponible.")
        return None

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df.index, 
        y=df['Close'], 
        mode='lines', 
        name='Prix de clôture',
        line=dict(color='#1f77b4', width=2)
    ))

    fig.update_layout(
        title=f"Historique de cours : {stock.ticker}",
        xaxis_title="Date",
        yaxis_title="Prix (€)",
        template="plotly_dark", # S'accorde bien avec VS Code/Streamlit dark
        margin=dict(l=20, r=20, t=40, b=20),
        height=400
    )
    
    return fig