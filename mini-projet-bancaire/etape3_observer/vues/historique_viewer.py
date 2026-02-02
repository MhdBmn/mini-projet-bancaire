# etape3_observer/vues/historique_viewer.py
class HistoriqueViewer:
    """Enregistre chaque transaction dans l'historique"""
    
    def on_transaction(self, transaction):
        date_str = transaction['date'].strftime('%H:%M:%S')
        print(f"   📝 [HISTORIQUE] {date_str} - "
              f"{transaction['type']}: {transaction['montant']}€")