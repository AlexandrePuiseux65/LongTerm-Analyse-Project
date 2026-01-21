from function.domain.stock import Stock
from function.domain.ratios import per, payout_ratio, roe, leverage
from datetime import datetime

def calculate_global_score(stock: Stock):
    """
    Calcule un score sur 10 basé sur la stratégie de rendement.
    """
    year = datetime.now().year - 1 # On analyse l'année fiscale complète la plus récente
    score = 0
    total_points = 5

    # 1. Valorisation (PER < 15)
    val_per = per(stock, year)
    if val_per and val_per < 15:
        score += 1
    
    # 2. Sécurité (Payout Ratio < 70%)
    payout = payout_ratio(stock, year)
    if payout and payout < 0.7:
        score += 2 # Plus de poids car crucial pour les dividendes
    
    # 3. Rentabilité (ROE > 10%)
    val_roe = roe(stock, year)
    if val_roe and val_roe > 0.1:
        score += 1
        
    # 4. Dette (Leverage < 3)
    # Note : Assure-toi que get_ebitda est défini dans metrics.py
    debt_ratio = leverage(stock, year)
    if debt_ratio and debt_ratio < 3:
        score += 1

    # Normalisation sur 10 (on a 5 points max ici)
    return (score / total_points) * 10