# etape4_mvc/vues/historique_viewer.py
class HistoriqueViewer:
    """Affiche l'historique des transactions"""
    
    def on_transaction(self, transaction):
        """Enregistre chaque transaction"""
        date_str = transaction['date'].strftime('%H:%M:%S')
        print(f"   📝 [{date_str}] {transaction['type']}: "
              f"{transaction['montant']}€ "
              f"(Solde: {transaction['nouveau_solde']:.2f}€)")