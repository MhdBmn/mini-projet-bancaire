# etape4_mvc/controleurs/controleur_compte.py
# Solution 1: Import direct avec le chemin complet
from modele.compte_mvc import CompteModele

class ControleurCompte:
    """Contrôleur principal (façade du modèle)"""
    
    def __init__(self):
        self.modele = CompteModele()
    
    # ========== OPÉRATIONS ==========
    def effectuer_depot(self, montant: float) -> bool:
        """Effectue un dépôt via le modèle"""
        return self.modele.deposer(montant)
    
    def effectuer_retrait(self, montant: float) -> bool:
        """Effectue un retrait via le modèle"""
        return self.modele.retirer(montant)
    
    # ========== GETTERS ==========
    def get_solde(self) -> float:
        """Retourne le solde actuel"""
        return self.modele.solde
    
    def get_historique(self):
        """Retourne l'historique des transactions"""
        return self.modele.historique
    
    def get_modele(self):
        """Retourne le modèle (pour les observateurs)"""
        return self.modele