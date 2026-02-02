# etape3_observer/main.py
from modele.compte_observable import CompteObservable
from vues.afficheur_solde import AfficheurSolde
from vues.alerte_negatif import AlerteNegatif
from vues.historique_viewer import HistoriqueViewer

def demarrer_systeme_etape3():
    """Système complet étape 3 - Pattern Observer"""
    
    print("\n" + "="*60)
    print("ÉTAPE 3 : PATTERN OBSERVER")
    print("="*60)
    print("Fonctionnalités:")
    print("• Singleton: une seule instance")
    print("• Observer: notifications automatiques")
    print("• 3 observateurs différents")
    print("="*60)
    
    # Initialisation du modèle
    compte = CompteObservable()
    
    # Création des observateurs
    print("\n📡 CRÉATION DES OBSERVATEURS:")
    afficheur = AfficheurSolde()
    alerte = AlerteNegatif()
    historique = HistoriqueViewer()
    
    # Enregistrement des observateurs
    compte.add_observer(afficheur)
    compte.add_observer(alerte)
    compte.add_observer(historique)
    
    # Démonstration
    print("\n" + "-"*50)
    print("DÉMONSTRATION DES NOTIFICATIONS AUTOMATIQUES")
    print("-"*50)
    
    print("\n1. Dépôt de 500€:")
    compte.deposer(500)
    
    print("\n2. Retrait de 200€:")
    compte.retirer(200)
    
    print("\n3. Tentative de retrait important (déclencherait alerte):")
    compte.retirer(2000)
    
    # Menu interactif
    menu_interactif(compte, afficheur, alerte, historique)

def menu_interactif(compte, afficheur, alerte, historique):
    """Menu interactif principal"""
    
    while True:
        print("\n" + "="*50)
        print("MENU PRINCIPAL - SYSTÈME OBSERVER")
        print("="*50)
        print("1. Effectuer une opération")
        print("2. Consulter le solde")
        print("3. Voir l'historique")
        print("4. Ajouter un nouvel observateur")
        print("5. Tester le Singleton")
        print("6. Quitter")
        print("-" * 50)
        
        choix = input("Votre choix (1-6): ").strip()
        
        if choix == "1":
            print("\nType d'opération:")
            print("1. Dépôt")
            print("2. Retrait")
            type_op = input("Choix: ").strip()
            
            try:
                montant = float(input("Montant: "))
                
                if type_op == "1":
                    if compte.deposer(montant):
                        print("✅ Dépôt effectué avec succès")
                    else:
                        print("❌ Erreur: montant invalide")
                elif type_op == "2":
                    if compte.retirer(montant):
                        print("✅ Retrait effectué avec succès")
                    else:
                        print("❌ Erreur: montant invalide ou solde insuffisant")
                else:
                    print("❌ Type d'opération invalide")
                    
            except ValueError:
                print("❌ Erreur: veuillez entrer un nombre valide")
                
        elif choix == "2":
            solde = compte.get_solde()
            print(f"\n💳 SOLDE ACTUEL: {solde:.2f}€")
            if solde < 0:
                print("⚠️  Attention: solde négatif!")
                
        elif choix == "3":
            historique_list = compte.get_historique()
            print("\n📋 HISTORIQUE DES TRANSACTIONS:")
            if not historique_list:
                print("Aucune transaction effectuée.")
            else:
                for trans in historique_list:
                    date_str = trans['date'].strftime('%d/%m/%Y %H:%M:%S')
                    print(f"{trans['id']:3d}. {date_str} | "
                          f"{trans['type']:8} | "
                          f"{trans['montant']:8.2f}€ | "
                          f"Solde: {trans['nouveau_solde']:.2f}€")
                          
        elif choix == "4":
            print("\n🎯 AJOUT D'UN NOUVEL OBSERVATEUR")
            print("Démonstration de l'extensibilité du pattern Observer")
            
            class NouvelObservateur:
                """Observateur personnalisé ajouté dynamiquement"""
                def __init__(self, nom):
                    self.nom = nom
                
                def on_transaction(self, transaction):
                    print(f"[{self.nom}] Transaction détectée: {transaction['type']}")
            
            nom_obs = input("Nom du nouvel observateur: ").strip() or "ObservateurPerso"
            nouvel_obs = NouvelObservateur(nom_obs)
            compte.add_observer(nouvel_obs)
            
            # Test
            print(f"\nTest avec le nouvel observateur '{nom_obs}':")
            compte.deposer(10)
            
        elif choix == "5":
            print("\n🔍 TEST DU SINGLETON:")
            print("Création d'une 'nouvelle' instance...")
            
            autre_instance = CompteObservable()
            print(f"ID instance originale: {id(compte)}")
            print(f"ID 'nouvelle' instance: {id(autre_instance)}")
            print(f"Même instance? {compte is autre_instance}")
            print("✅ Singleton fonctionne: c'est la même instance!")
            
        elif choix == "6":
            print("\n" + "="*50)
            print("RÉCAPITULATIF ÉTAPE 3 - OBSERVER")
            print("="*50)
            print("Patterns démontrés:")
            print("1. Singleton → Une instance unique")
            print("2. Observer → Notifications automatiques")
            print("3. Extensibilité → Ajout dynamique d'observateurs")
            print("\nAu revoir! 👋")
            break
            
        else:
            print("❌ Choix invalide. Veuillez choisir 1-6.")

if __name__ == "__main__":
    demarrer_systeme_etape3()