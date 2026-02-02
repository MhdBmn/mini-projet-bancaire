// ==================== CONFIGURATION ====================
const API_URL = '/api';
let tousLesEmployes = [];
let currentId = null;
let employeToDelete = null;

// ==================== INITIALISATION ====================
document.addEventListener('DOMContentLoaded', function() {
    console.log('🚀 Application démarrée');
    
    // Tester la connexion API
    testerAPI();
    
    // Charger les employés
    chargerEmployes();
    
    // Configurer les événements
    configurerEvenements();
});

// ==================== TESTS API ====================
async function testerAPI() {
    try {
        const response = await fetch(API_URL + '/test');
        const data = await response.json();
        console.log('✅ API OK:', data);
        mettreAJourStatusServeur(true);
    } catch (error) {
        console.error('❌ API erreur:', error);
        mettreAJourStatusServeur(false);
    }
}

function mettreAJourStatusServeur(enLigne) {
    const serverStatus = document.getElementById('serverStatus');
    if (serverStatus) {
        if (enLigne) {
            serverStatus.innerHTML = '<i class="fas fa-circle" style="color: #4cc9f0"></i> <span>Serveur: En ligne</span>';
        } else {
            serverStatus.innerHTML = '<i class="fas fa-circle" style="color: #dc3545"></i> <span>Serveur: Hors ligne</span>';
        }
    }
}

// ==================== GESTION EMPLOYÉS ====================

// Charger les employés
async function chargerEmployes() {
    try {
        console.log('📥 Chargement employés...');
        
        const response = await fetch(API_URL + '/employes');
        if (!response.ok) throw new Error('Erreur ' + response.status);
        
        tousLesEmployes = await response.json();
        console.log('✅ ' + tousLesEmployes.length + ' employé(s) chargé(s)');
        
        afficherEmployes(tousLesEmployes);
        
    } catch (error) {
        console.error('❌ Erreur chargement:', error);
        afficherMessage('Erreur de chargement: ' + error.message, 'error');
    }
}

// Afficher les employés - AVEC BOUTONS EN HAUT À DROITE
function afficherEmployes(employes) {
    const container = document.getElementById('employesList');
    
    if (!container) {
        console.error('❌ Container employesList non trouvé');
        return;
    }
    
    if (!employes || employes.length === 0) {
        container.innerHTML = `
            <div class="empty-state">
                <i class="fas fa-users-slash"></i>
                <h3>Aucun employé trouvé</h3>
                <p>Commencez par ajouter votre premier employé !</p>
            </div>
        `;
        
        // Mettre à jour les statistiques
        mettreAJourStatistiques(0, 0);
        return;
    }
    
    let html = '';
    
    employes.forEach(employe => {
        // Formater les données
        const tel = employe.tel ? employe.tel.toString().replace(/(\d{2})(?=\d)/g, '$1 ') : 'Non renseigné';
        const prime = employe.prime || 0;
        const anciennete = employe.anciennete || 0;
        
        // Badge ancienneté
        let ancienneteBadge = '';
        if (anciennete >= 10) {
            ancienneteBadge = '<span class="badge badge-success">Senior</span>';
        } else if (anciennete >= 5) {
            ancienneteBadge = '<span class="badge badge-primary">Confirmé</span>';
        } else if (anciennete >= 1) {
            ancienneteBadge = '<span class="badge badge-warning">Junior</span>';
        }
        
        // ID court pour l'affichage
        const idCourt = employe._id ? employe._id.substring(0, 8) + '...' : '';
        
        html += `
            <div class="employe-card">
                <!-- HEADER AVEC BOUTONS EN HAUT À DROITE -->
                <div class="employe-header">
                    <div class="employe-info">
                        <h3><i class="fas fa-user-circle"></i> ${employe.prenom || ''} ${employe.nom || ''}</h3>
                        <div class="employe-title">Employé</div>
                        ${ancienneteBadge}
                        <div class="employe-id">
                            <i class="fas fa-fingerprint"></i> ID: ${idCourt}
                        </div>
                    </div>
                    <div class="employe-actions">
                        <button class="btn btn-warning" onclick="editerEmploye('${employe._id}')">
                            <i class="fas fa-edit"></i> Modifier
                        </button>
                        <button class="btn btn-danger" onclick="demanderSuppression('${employe._id}')">
                            <i class="fas fa-trash-alt"></i> Supprimer
                        </button>
                    </div>
                </div>
                
                <!-- CONTENU DE LA CARTE -->
                <div class="employe-content">
                    <div class="employe-details">
                        <div class="detail-section">
                            <h4><i class="fas fa-info-circle"></i> Informations</h4>
                            <div class="detail-list">
                                <div class="detail-item">
                                    <span class="detail-label"><i class="fas fa-calendar-alt"></i> Ancienneté</span>
                                    <span class="detail-value">${anciennete} ans</span>
                                </div>
                                <div class="detail-item">
                                    <span class="detail-label"><i class="fas fa-money-bill-wave"></i> Prime</span>
                                    <span class="detail-value">${prime} €</span>
                                </div>
                            </div>
                        </div>
                        
                        <div class="detail-section">
                            <h4><i class="fas fa-home"></i> Adresse</h4>
                            <div class="detail-list">
                                <div class="detail-item">
                                    <span class="detail-label">Adresse</span>
                                    <span class="detail-value">${employe.adresse?.numero || ''} ${employe.adresse?.rue || 'Non renseignée'}</span>
                                </div>
                                <div class="detail-item">
                                    <span class="detail-label">Ville</span>
                                    <span class="detail-value">${employe.adresse?.codepostal || ''} ${employe.adresse?.ville || ''}</span>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="contact-info">
                        <h4><i class="fas fa-phone-alt"></i> Contact</h4>
                        <div class="detail-list">
                            <div class="detail-item">
                                <span class="detail-label">Téléphone</span>
                                <span class="detail-value">${tel}</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        `;
    });
    
    container.innerHTML = html;
    
    // Mettre à jour les statistiques
    mettreAJourStatistiques(tousLesEmployes.length, employes.length);
}

function mettreAJourStatistiques(total, resultats) {
    const totalElement = document.getElementById('totalEmployes');
    const searchElement = document.getElementById('searchResults');
    
    if (totalElement) totalElement.textContent = total;
    if (searchElement) searchElement.textContent = resultats;
}

// ==================== FORMULAIRE ====================

// Afficher le formulaire en modal
function afficherFormulaire() {
    reinitialiserFormulaire();
    document.getElementById('formModal').classList.remove('hidden');
    
    // Focus sur le premier champ après un court délai
    setTimeout(() => {
        document.getElementById('nom').focus();
    }, 100);
}

// Cacher le formulaire modal
function cacherFormulaire() {
    document.getElementById('formModal').classList.add('hidden');
    reinitialiserFormulaire();
}

// Soumettre le formulaire
async function soumettreFormulaire(e) {
    e.preventDefault();
    console.log('📝 Soumission formulaire');
    
    // Validation
    const nom = document.getElementById('nom').value.trim();
    const prenom = document.getElementById('prenom').value.trim();
    
    if (!nom || !prenom) {
        afficherMessage('Le nom et le prénom sont obligatoires', 'error');
        return;
    }
    
    // Préparer données
    const employeData = {
        nom: nom,
        prenom: prenom,
        anciennete: parseInt(document.getElementById('anciennete').value) || 0,
        tel: document.getElementById('tel').value ? parseInt(document.getElementById('tel').value) : undefined,
        prime: parseInt(document.getElementById('prime').value) || 0,
        adresse: {
            numero: parseInt(document.getElementById('numero').value) || 0,
            rue: document.getElementById('rue').value.trim(),
            codepostal: parseInt(document.getElementById('codepostal').value) || 0,
            ville: document.getElementById('ville').value.trim()
        }
    };
    
    try {
        let url = API_URL + '/employes';
        let method = 'POST';
        
        if (currentId) {
            url = API_URL + '/employes/' + currentId;
            method = 'PUT';
        }
        
        const response = await fetch(url, {
            method: method,
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(employeData)
        });
        
        const resultat = await response.json();
        
        if (!response.ok) {
            if (response.status === 409) {
                // Conflit - employé existe déjà
                afficherMessage(resultat.message || 'Cet employé existe déjà', 'error');
            } else {
                throw new Error(resultat.message || 'Erreur ' + response.status);
            }
            return;
        }
        
        console.log('✅ Succès:', resultat);
        
        // Réinitialiser, cacher et recharger
        cacherFormulaire();
        await chargerEmployes();
        
        afficherMessage(
            currentId ? 'Employé modifié avec succès !' : 'Employé ajouté avec succès !',
            'success'
        );
        
    } catch (error) {
        console.error('❌ Erreur:', error);
        afficherMessage('Erreur: ' + error.message, 'error');
    }
}

// Éditer un employé
async function editerEmploye(id) {
    console.log('✏️ Édition employé:', id);
    
    try {
        const response = await fetch(API_URL + '/employes/' + id);
        if (!response.ok) throw new Error('Employé non trouvé');
        
        const employe = await response.json();
        
        // Remplir formulaire
        currentId = employe._id;
        document.getElementById('nom').value = employe.nom || '';
        document.getElementById('prenom').value = employe.prenom || '';
        document.getElementById('anciennete').value = employe.anciennete || '';
        document.getElementById('tel').value = employe.tel || '';
        document.getElementById('prime').value = employe.prime || '';
        document.getElementById('numero').value = employe.adresse?.numero || '';
        document.getElementById('rue').value = employe.adresse?.rue || '';
        document.getElementById('codepostal').value = employe.adresse?.codepostal || '';
        document.getElementById('ville').value = employe.adresse?.ville || '';
        
        // Changer mode formulaire
        document.getElementById('formTitle').textContent = 'Modifier un employé';
        document.getElementById('btnAjouter').classList.add('hidden');
        document.getElementById('btnModifier').classList.remove('hidden');
        
        // Afficher le modal
        document.getElementById('formModal').classList.remove('hidden');
        
        // Focus sur le premier champ
        setTimeout(() => {
            document.getElementById('nom').focus();
        }, 100);
        
    } catch (error) {
        console.error('❌ Erreur:', error);
        afficherMessage('Impossible de charger l\'employé', 'error');
    }
}

// ==================== SUPPRESSION ====================

function demanderSuppression(id) {
    const employe = tousLesEmployes.find(e => e._id === id);
    if (!employe) return;
    
    employeToDelete = id;
    document.getElementById('deleteMessage').textContent = 
        `Êtes-vous sûr de vouloir supprimer ${employe.prenom} ${employe.nom} ?`;
    document.getElementById('deleteModal').classList.remove('hidden');
}

async function confirmerSuppression() {
    if (!employeToDelete) return;
    
    try {
        const response = await fetch(API_URL + '/employes/' + employeToDelete, {
            method: 'DELETE'
        });
        
        if (!response.ok) throw new Error('Erreur ' + response.status);
        
        document.getElementById('deleteModal').classList.add('hidden');
        await chargerEmployes();
        afficherMessage('Employé supprimé avec succès !', 'success');
        
    } catch (error) {
        console.error('❌ Erreur suppression:', error);
        afficherMessage('Erreur lors de la suppression', 'error');
    }
    
    employeToDelete = null;
}

function annulerSuppression() {
    employeToDelete = null;
    document.getElementById('deleteModal').classList.add('hidden');
}

// ==================== RECHERCHE ====================

function rechercherEmployes() {
    const recherche = document.getElementById('searchInput').value.toLowerCase();
    
    if (!recherche) {
        afficherEmployes(tousLesEmployes);
        return;
    }
    
    const resultats = tousLesEmployes.filter(employe => 
        (employe.nom && employe.nom.toLowerCase().includes(recherche)) ||
        (employe.prenom && employe.prenom.toLowerCase().includes(recherche)) ||
        (employe.tel && employe.tel.toString().includes(recherche))
    );
    
    afficherEmployes(resultats);
}

function reinitialiserRecherche() {
    document.getElementById('searchInput').value = '';
    afficherEmployes(tousLesEmployes);
}

// ==================== UTILITAIRES ====================

function reinitialiserFormulaire() {
    document.getElementById('employeForm').reset();
    currentId = null;
    document.getElementById('formTitle').textContent = 'Ajouter un employé';
    document.getElementById('btnAjouter').classList.remove('hidden');
    document.getElementById('btnModifier').classList.add('hidden');
}

function afficherMessage(texte, type) {
    const couleur = type === 'error' ? '#dc3545' : '#28a745';
    const messageDiv = document.createElement('div');
    messageDiv.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: ${couleur};
        color: white;
        padding: 15px 20px;
        border-radius: 8px;
        z-index: 10000;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        animation: slideIn 0.3s ease;
    `;
    messageDiv.textContent = texte;
    document.body.appendChild(messageDiv);
    
    setTimeout(() => {
        messageDiv.style.animation = 'slideOut 0.3s ease';
        setTimeout(() => document.body.removeChild(messageDiv), 300);
    }, 3000);
}

// ==================== CONFIGURATION ÉVÉNEMENTS ====================

function configurerEvenements() {
    console.log('🔧 Configuration événements');
    
    // Bouton pour afficher le formulaire
    document.getElementById('btnShowForm').addEventListener('click', afficherFormulaire);
    
    // Formulaire
    document.getElementById('employeForm').addEventListener('submit', soumettreFormulaire);
    
    // Boutons formulaire
    document.getElementById('btnAnnuler').addEventListener('click', cacherFormulaire);
    document.getElementById('btnCloseForm').addEventListener('click', cacherFormulaire);
    
    // Bouton Modifier dans le formulaire
    document.getElementById('btnModifier').addEventListener('click', function(e) {
        e.preventDefault();
        document.getElementById('employeForm').dispatchEvent(new Event('submit'));
    });
    
    // Recherche
    document.getElementById('btnSearch').addEventListener('click', rechercherEmployes);
    document.getElementById('btnReset').addEventListener('click', reinitialiserRecherche);
    
    // Suppression
    document.getElementById('confirmDelete').addEventListener('click', confirmerSuppression);
    document.getElementById('cancelDelete').addEventListener('click', annulerSuppression);
    
    // Recherche en temps réel
    document.getElementById('searchInput').addEventListener('input', function() {
        clearTimeout(this.timer);
        this.timer = setTimeout(rechercherEmployes, 300);
    });
    
    // Fermer modals en cliquant à l'extérieur
    document.getElementById('formModal').addEventListener('click', function(e) {
        if (e.target === this) {
            cacherFormulaire();
        }
    });
    
    document.getElementById('deleteModal').addEventListener('click', function(e) {
        if (e.target === this) {
            annulerSuppression();
        }
    });
    
    // Fermer modals avec la touche Échap
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            cacherFormulaire();
            annulerSuppression();
        }
    });
}

// ==================== FONCTIONS GLOBALES ====================
window.editerEmploye = editerEmploye;
window.demanderSuppression = demanderSuppression;

// Ajouter les animations CSS pour les messages
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from { transform: translateX(100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    @keyframes slideOut {
        from { transform: translateX(0); opacity: 1; }
        to { transform: translateX(100%); opacity: 0; }
    }
`;
document.head.appendChild(style);