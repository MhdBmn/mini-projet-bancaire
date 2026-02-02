# etape1_sans_pattern/main.py
from compte_bancaire import CompteBancaire

def demarrer_systeme_etape1():
    """Système complet étape 1 - Sans patterns"""
    
    print("\n" + "="*60)
    print("ÉTAPE 1 : SYSTÈME SANS DESIGN PATTERNS")
    print("="*60)
    print("Problèmes identifiés:")
    print("• Chaque module crée sa propre instance")
    print("• Pas de cohérence des données")
    print("• Pas de notifications automatiques")
    print("="*60)
    
    # PROBLÈME : création multiple du même compte
    print("\n🔴 PROBLÈME : Création de plusieurs instances")
    
    # Module 1 : Gestion des opérations
    print("\n--- Module Gestion ---")
    compte_gestion = CompteBancaire("FR123", "Alice", 1000)
    compte_gestion.deposer(500)
    print(f"Solde (gestion): {compte_gestion.consulter_solde()}€")
    
    # Module 2 : Affichage
    print("\n--- Module Affichage ---")
    compte_affichage = CompteBancaire("FR123", "Alice", 1000)
    print(f"Solde (affichage): {compte_affichage.consulter_solde()}€")
    print("⚠️  Incohérence: le dépôt n'apparaît pas ici!")
    
    # Module 3 : Surveillance
    print("\n--- Module Surveillance ---")
    compte_surveillance = CompteBancaire("FR123", "Alice", 1000)
    compte_surveillance.retirer(200)
    print(f"Solde (surveillance): {compte_surveillance.consulter_solde()}€")
    
    print("\n" + "="*60)
    print("ANALYSE DU PROBLÈME:")
    print(f"compte_gestion is compte_affichage: {compte_gestion is compte_affichage}")
    print(f"compte_gestion is compte_surveillance: {compte_gestion is compte_surveillance}")
    print("=> 3 instances différentes pour le MÊME compte!")
    print("=> Données incohérentes entre modules")
    
    # Menu interactif pour tester
    while True:
        print("\n" + "-"*40)
        print("MENU INTERACTIF - ÉTAPE 1")
        print("-"*40)
        print("1. Créer un nouveau compte (problème!)")
        print("2. Voir les problèmes d'architecture")
        print("3. Quitter")
        
        choix = input("Votre choix: ").strip()
        
        if choix == "1":
            print("\n🔄 Création d'une nouvelle instance...")
            nouveau_compte = CompteBancaire("FR123", "Alice", 1000)
            print(f"Nouvelle instance créée: id={id(nouveau_compte)}")
            print(f"Comparaison avec compte_gestion: {nouveau_compte is compte_gestion}")
            
        elif choix == "2":
            print("\n📊 ÉTAT DES INSTANCES:")
            print(f"compte_gestion: id={id(compte_gestion)}, solde={compte_gestion.solde}€")
            print(f"compte_affichage: id={id(compte_affichage)}, solde={compte_affichage.solde}€")
            print(f"compte_surveillance: id={id(compte_surveillance)}, solde={compte_surveillance.solde}€")
            print("\n🔴 CONCLUSION: 3 soldes différents pour le même compte!")
            
        elif choix == "3":
            print("\nFin de l'étape 1.")
            break

if __name__ == "__main__":
    demarrer_systeme_etape1()