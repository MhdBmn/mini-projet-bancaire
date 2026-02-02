# etape4_mvc/modele/compte_mvc.py
from datetime import datetime
from typing import List, Dict, Any

class CompteModele:
    """Modèle du compte avec Singleton + Observable"""
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if not self._initialized:
            self._solde = 1000.0
            self._historique: List[Dict] = []
            self._observers = []
            self._initialized = True
    
    # ========== PROPRIÉTÉS ==========
    @property
    def solde(self) -> float:
        return self._solde
    
    @property
    def historique(self) -> List[Dict]:
        return self._historique.copy()
    
    # ========== OPÉRATIONS ==========
    def deposer(self, montant: float) -> bool:
        """Effectue un dépôt"""
        if montant <= 0:
            return False
        
        ancien_solde = self._solde
        self._solde += montant
        
        transaction = self._creer_transaction("DÉPÔT", montant, ancien_solde)
        self._historique.append(transaction)
        
        # Notification générique à tous les observateurs
        for observer in self._observers:
            if hasattr(observer, 'on_transaction'):
                observer.on_transaction(transaction)
            elif hasattr(observer, 'on_depot'):
                observer.on_depot(transaction)
        
        return True
    
    def retirer(self, montant: float) -> bool:
        """Effectue un retrait"""
        if montant <= 0 or montant > self._solde:
            return False
        
        ancien_solde = self._solde
        self._solde -= montant
        
        transaction = self._creer_transaction("RETRAIT", montant, ancien_solde)
        self._historique.append(transaction)
        
        # Notification générique à tous les observateurs
        for observer in self._observers:
            if hasattr(observer, 'on_transaction'):
                observer.on_transaction(transaction)
            elif hasattr(observer, 'on_retrait'):
                observer.on_retrait(transaction)
        
        # Alerte si solde négatif (seulement pour les observateurs qui ont cette méthode)
        if self._solde < 0:
            for observer in self._observers:
                if hasattr(observer, 'on_alerte_negatif'):
                    observer.on_alerte_negatif(self._solde)
        
        return True
    
    # ========== OBSERVERS ==========
    def add_observer(self, observer):
        """Ajoute un observateur"""
        if observer not in self._observers:
            self._observers.append(observer)
    
    def remove_observer(self, observer):
        """Retire un observateur"""
        if observer in self._observers:
            self._observers.remove(observer)
    
    # ========== PRIVÉ ==========
    def _creer_transaction(self, type_op: str, montant: float, ancien_solde: float) -> Dict[str, Any]:
        """Crée une transaction"""
        return {
            'id': len(self._historique) + 1,
            'type': type_op,
            'montant': montant,
            'date': datetime.now(),
            'ancien_solde': ancien_solde,
            'nouveau_solde': self._solde
        }