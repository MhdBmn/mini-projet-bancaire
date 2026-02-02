# etape4_mvc/vues/__init__.py
from .afficheur_solde import AfficheurSolde
from .alerte_negatif import AlerteNegatif
from .historique_viewer import HistoriqueViewer

# Vue console principale
class VueConsole:
    """Vue principale avec interface console"""
    
    def __init__(self, controleur):
        self.controleur = controleur
        
        # Initialisation des observateurs
        self.afficheur = AfficheurSolde()
        self.alerte = AlerteNegatif()
        self.historique = HistoriqueViewer()
        
        # Enregistrement des observateurs
        modele = self.controleur.get_modele()
        modele.add_observer(self.afficheur)
        modele.add_observer(self.alerte)
        modele.add_observer(self.historique)
    
    def afficher_menu(self):
        """Affiche le menu principal"""
        while True:
            print("\n" + "="*50)
            print("🏦 SYSTÈME BANCAIRE MVC")
            print("="*50)
            print("1. Consulter le solde")
            print("2. Effectuer un dépôt")
            print("3. Effectuer un retrait")
            print("4. Voir l'historique")
            print("5. Quitter")
            print("-" * 50)
            
            choix = input("Votre choix (1-5): ").strip()
            
            if choix == "1":
                self.afficher_solde()
            elif choix == "2":
                self.effectuer_depot()
            elif choix == "3":
                self.effectuer_retrait()
            elif choix == "4":
                self.afficher_historique()
            elif choix == "5":
                print("\nMerci d'avoir utilisé notre système bancaire!")
                print("Au revoir! 👋")
                break
            else:
                print("Choix invalide! Veuillez réessayer.")
    
    def afficher_solde(self):
        """Affiche le solde actuel"""
        solde = self.controleur.get_solde()
        print(f"\n💳 VOTRE SOLDE ACTUEL: {solde:.2f}€")
    
    def effectuer_depot(self):
        """Gère un dépôt"""
        try:
            montant = float(input("Montant à déposer: "))
            if self.controleur.effectuer_depot(montant):
                print(f"✅ Dépôt de {montant}€ réussi!")
            else:
                print("❌ Erreur: Montant invalide")
        except ValueError:
            print("❌ Erreur: Veuillez entrer un nombre valide")
    
    def effectuer_retrait(self):
        """Gère un retrait"""
        try:
            montant = float(input("Montant à retirer: "))
            if self.controleur.effectuer_retrait(montant):
                print(f"✅ Retrait de {montant}€ réussi!")
            else:
                print("❌ Erreur: Montant invalide ou solde insuffisant")
        except ValueError:
            print("❌ Erreur: Veuillez entrer un nombre valide")
    
    def afficher_historique(self):
        """Affiche l'historique complet"""
        historique = self.controleur.get_historique()
        
        print("\n" + "="*60)
        print("📋 HISTORIQUE DES TRANSACTIONS")
        print("="*60)
        
        if not historique:
            print("Aucune transaction effectuée.")
        else:
            for trans in historique:
                date_str = trans['date'].strftime('%d/%m/%Y %H:%M:%S')
                print(f"{trans['id']:3d} | {date_str} | "
                      f"{trans['type']:8} | "
                      f"{trans['montant']:8.2f}€ | "
                      f"Solde: {trans['nouveau_solde']:.2f}€")