# etape2_singleton/compte_singleton.py
from datetime import datetime

class CompteBancaireSingleton:
    """Pattern Singleton: solution au problème des instances multiples"""
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if not self._initialized:
            self.numero = "FR7630001007941234567890185"
            self.titulaire = "Client Principal"
            self.solde = 1000.0
            self.historique = []
            self._initialized = True
            print("[Singleton] Compte initialisé une seule fois")
    
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
    
    def consulter_solde(self) -> float:
        return self.solde
    
    def afficher_historique(self):
        return self.historique
    
    def afficher_infos(self):
        print(f"\n=== COMPTE SINGLETON ===")
        print(f"Titulaire: {self.titulaire}")
        print(f"Numéro: {self.numero}")
        print(f"Solde: {self.solde:.2f}€")
        print(f"Nombre transactions: {len(self.historique)}")