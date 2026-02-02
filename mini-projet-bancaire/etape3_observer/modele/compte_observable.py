# etape3_observer/modele/compte_observable.py
from datetime import datetime
from typing import List, Dict

class CompteObservable:
    """Modèle observable avec Singleton + Observer"""
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if not self._initialized:
            self.solde = 1000.0
            self.historique = []
            self._observers = []
            self._initialized = True
            print("[Modèle] Compte observable initialisé")
    
    # === OPÉRATIONS ===
    def deposer(self, montant: float) -> bool:
        if montant <= 0:
            return False
        
        ancien_solde = self.solde
        self.solde += montant
        
        transaction = self._creer_transaction("DÉPÔT", montant, ancien_solde)
        self.historique.append(transaction)
        
        # Notification à tous les observateurs
        for observer in self._observers:
            observer.on_transaction(transaction)
        
        return True
    
    def retirer(self, montant: float) -> bool:
        if montant <= 0 or montant > self.solde:
            return False
        
        ancien_solde = self.solde
        self.solde -= montant
        
        transaction = self._creer_transaction("RETRAIT", montant, ancien_solde)
        self.historique.append(transaction)
        
        # Notification à tous les observateurs
        for observer in self._observers:
            observer.on_transaction(transaction)
        
        # Alerte spéciale si solde négatif
        if self.solde < 0:
            for observer in self._observers:
                if hasattr(observer, 'on_alerte_negatif'):
                    observer.on_alerte_negatif(self.solde)
        
        return True
    
    def get_solde(self) -> float:
        return self.solde
    
    def get_historique(self) -> List[Dict]:
        return self.historique.copy()
    
    # === OBSERVATEURS ===
    def add_observer(self, observer):
        """Ajoute un observateur"""
        if observer not in self._observers:
            self._observers.append(observer)
            print(f"[Modèle] Observateur ajouté: {observer.__class__.__name__}")
    
    def remove_observer(self, observer):
        """Retire un observateur"""
        if observer in self._observers:
            self._observers.remove(observer)
    
    # === PRIVÉ ===
    def _creer_transaction(self, type_op: str, montant: float, ancien_solde: float) -> Dict:
        """Crée une transaction"""
        return {
            'id': len(self.historique) + 1,
            'type': type_op,
            'montant': montant,
            'date': datetime.now(),
            'ancien_solde': ancien_solde,
            'nouveau_solde': self.solde
        }