# etape4_mvc/main.py
# Solution 2: Imports depuis le package courant
import sys
import os

# Ajouter le dossier parent au path si nécessaire
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from controleurs.controleur_compte import ControleurCompte
from vues import VueConsole

def main():
    print("="*60)
    print("🏦 SYSTÈME BANCAIRE MVC - ÉTAPE 4")
    print("="*60)
    print("Design patterns implémentés:")
    print("  • Singleton: Une seule instance du compte")
    print("  • Observer: Notifications automatiques")
    print("  • MVC: Architecture claire et modulaire")
    print("="*60)
    
    # Initialisation MVC
    print("\nInitialisation du système...")
    controleur = ControleurCompte()
    vue = VueConsole(controleur)
    
    # Lancement
    print("Système prêt! Solde initial: 1000.00€")
    vue.afficher_menu()

if __name__ == "__main__":
    main()