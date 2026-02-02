# etape2_singleton/main.py
from compte_singleton import CompteBancaireSingleton

def simuler_modules():
    """Simule plusieurs modules accédant au même compte"""
    
    print("\n--- Simulation des modules ---")
    
    # Module 1 : Gestion
    print("\n[MODULE GESTION]")
    module_gestion = CompteBancaireSingleton()
    module_gestion.deposer(300)
    print(f"Solde vu par Gestion: {module_gestion.consulter_solde()}€")
    
    # Module 2 : Affichage
    print("\n[MODULE AFFICHAGE]")
    module_affichage = CompteBancaireSingleton()
    print(f"Solde vu par Affichage: {module_affichage.consulter_solde()}€")
    
    # Module 3 : Surveillance
    print("\n[MODULE SURVEILLANCE]")
    module_surveillance = CompteBancaireSingleton()
    module_surveillance.retirer(150)
    print(f"Solde vu par Surveillance: {module_surveillance.consulter_solde()}€")
    
    # Vérification
    print("\n" + "="*50)
    print("VÉRIFICATION SINGLETON:")
    print(f"module_gestion is module_affichage: {module_gestion is module_affichage}")
    print(f"module_gestion is module_surveillance: {module_gestion is module_surveillance}")
    print("✅ TOUS LES MODULES UTILISENT LA MÊME INSTANCE!")

def menu_interactif_singleton():
    """Menu interactif pour tester le Singleton"""
    
    while True:
        print("\n" + "="*50)
        print("MENU SINGLETON - ÉTAPE 2")
        print("="*50)
        print("1. Effectuer un dépôt")
        print("2. Effectuer un retrait")
        print("3. Consulter le solde")
        print("4. Voir l'historique")
        print("5. Tester l'accès multiple (Singleton)")
        print("6. Quitter")
        print("-" * 50)
        
        choix = input("Votre choix: ").strip()
        compte = CompteBancaireSingleton()  # Toujours la même instance
        
        if choix == "1":
            try:
                montant = float(input("Montant à déposer: "))
                compte.deposer(montant)
            except ValueError:
                print("❌ Erreur: Montant invalide")
                
        elif choix == "2":
            try:
                montant = float(input("Montant à retirer: "))
                compte.retirer(montant)
            except ValueError:
                print("❌ Erreur: Montant invalide")
                
        elif choix == "3":
            solde = compte.consulter_solde()
            print(f"\n💳 SOLDE ACTUEL: {solde:.2f}€")
            
        elif choix == "4":
            historique = compte.afficher_historique()
            print("\n📋 HISTORIQUE DES TRANSACTIONS:")
            if not historique:
                print("Aucune transaction.")
            else:
                for i, trans in enumerate(historique, 1):
                    date_str = trans['date'].strftime('%d/%m/%Y %H:%M')
                    print(f"{i:3d}. {date_str} | {trans['type']:8} | "
                          f"{trans['montant']:7.2f}€ | "
                          f"Solde: {trans['solde']:.2f}€")
                          
        elif choix == "5":
            print("\n🔍 TEST DU PATTERN SINGLETON:")
            print("Création de plusieurs 'nouvelles' instances...")
            
            instance1 = CompteBancaireSingleton()
            instance2 = CompteBancaireSingleton()
            instance3 = CompteBancaireSingleton()
            
            print(f"ID instance1: {id(instance1)}")
            print(f"ID instance2: {id(instance2)}")
            print(f"ID instance3: {id(instance3)}")
            
            print(f"\ninstance1 is instance2: {instance1 is instance2}")
            print(f"instance1 is instance3: {instance1 is instance3}")
            print("✅ Ce sont toutes la MÊME instance!")
            
        elif choix == "6":
            print("\nFin de l'étape 2 - Singleton")
            break
            
        else:
            print("❌ Choix invalide")

def demarrer_systeme_etape2():
    """Système complet étape 2 - Avec Singleton"""
    
    print("\n" + "="*60)
    print("ÉTAPE 2 : PATTERN SINGLETON")
    print("="*60)
    print("Solution au problème des instances multiples:")
    print("• Une seule instance pour toute l'application")
    print("• Cohérence des données garantie")
    print("• Tous les modules accèdent au même compte")
    print("="*60)
    
    # Démonstration du Singleton
    simuler_modules()
    
    # Menu interactif
    menu_interactif_singleton()

if __name__ == "__main__":
    demarrer_systeme_etape2()