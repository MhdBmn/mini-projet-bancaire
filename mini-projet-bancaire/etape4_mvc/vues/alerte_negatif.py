# etape4_mvc/vues/alerte_negatif.py
class AlerteNegatif:
    """Alerte en cas de solde négatif"""
    
    def on_transaction(self, transaction):
        """Vérifie si le solde devient négatif après la transaction"""
        if transaction['nouveau_solde'] < 0:
            print("🚨 ALERTE: SOLDE NÉGATIF!")
            print(f"   ⚠️  Votre solde est maintenant de {transaction['nouveau_solde']:.2f}€")
            print("   Contactez votre banque immédiatement!")
            print("=" * 50)