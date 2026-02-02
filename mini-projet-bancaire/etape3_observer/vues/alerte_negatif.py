# etape3_observer/vues/alerte_negatif.py
class AlerteNegatif:
    """Alerte en cas de solde négatif"""
    
    def on_transaction(self, transaction):
        if transaction['nouveau_solde'] < 0:
            self.on_alerte_negatif(transaction['nouveau_solde'])
    
    def on_alerte_negatif(self, solde):
        print("\n🚨 [ALERTE NÉGATIF]")
        print(f"   ⚠️  SOLDE NÉGATIF DÉTECTÉ: {solde:.2f}€")
        print("   Veuillez régulariser votre situation immédiatement!")
        print("=" * 50)