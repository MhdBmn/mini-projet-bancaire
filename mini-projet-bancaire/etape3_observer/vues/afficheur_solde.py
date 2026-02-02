# etape3_observer/vues/afficheur_solde.py
class AfficheurSolde:
    """Affiche le solde à chaque transaction"""
    
    def on_transaction(self, transaction):
        print(f"\n[AFFICHEUR SOLDE] {transaction['type']} de {transaction['montant']}€")
        print(f"   📊 Solde: {transaction['ancien_solde']:.2f}€ → {transaction['nouveau_solde']:.2f}€")
        print("-" * 40)