# etape1_sans_pattern/compte_bancaire.py
from datetime import datetime

class CompteBancaire:
    """Version sans design patterns - Problèmes d'architecture"""
    
    def __init__(self, numero: str, titulaire: str, solde_initial: float = 0):
        self.numero = numero
        self.titulaire = titulaire
        self.solde = solde_initial
        self.historique = []
    
    def deposer(self, montant: float) -> bool:
        if montant <= 0:
            print("❌ Erreur: Montant doit être positif")
            return False
        
        self.solde += montant
        transaction = {
            'type': 'DÉPÔT',
            'montant': montant,
            'date': datetime.now(),
            'solde': self.solde
        }
        self.historique.append(transaction)
        print(f"✅ Dépôt de {montant}€ effectué")
        return True
    
    def retirer(self, montant: float) -> bool:
        if montant <= 0:
            print("❌ Erreur: Montant doit être positif")
            return False
        
        if montant > self.solde:
            print("❌ Erreur: Solde insuffisant")
            return False
        
        self.solde -= montant
        transaction = {
            'type': 'RETRAIT',
            'montant': montant,
            'date': datetime.now(),
            'solde': self.solde
        }
        self.historique.append(transaction)
        print(f"✅ Retrait de {montant}€ effectué")
        return True
    
    def consulter_solde(self):
        return self.solde
    
    def afficher_historique(self):
        return self.historique
    
    def afficher_infos(self):
        print(f"\n=== COMPTE BANCAIRE ===")
        print(f"Titulaire: {self.titulaire}")
        print(f"Numéro: {self.numero}")
        print(f"Solde: {self.solde:.2f}€")