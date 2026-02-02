# etape4_mvc/vues/afficheur_solde.py
class AfficheurSolde:
    """Affiche le solde à chaque transaction"""
    
    def on_transaction(self, transaction):
        """Méthode générique pour toutes les transactions"""
        print(f"\n{'💵' if transaction['type'] == 'DÉPÔT' else '💰'} "
              f"{transaction['type']}: "
              f"{'+' if transaction['type'] == 'DÉPÔT' else '-'}"
              f"{transaction['montant']}€")
        print(f"   📊 SOLDE: {transaction['ancien_solde']:.2f}€ → "
              f"{transaction['nouveau_solde']:.2f}€")
        print("-" * 40)