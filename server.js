const express = require("express");
const mongoose = require("mongoose");
const path = require("path");
const cors = require("cors");
const Employe = require("./models/Employe");

const app = express();

// ==================== MIDDLEWARE ====================
app.use(cors());
app.use(express.json());

// Servir les fichiers statiques du dossier frontend
app.use(express.static(path.join(__dirname, "frontend")));

// ==================== CONNEXION MONGODB ====================
console.log("🔌 Connexion à MongoDB...");

mongoose.connect("mongodb://127.0.0.1:27017/employes", {
    useNewUrlParser: true,
    useUnifiedTopology: true
})
.then(() => {
    console.log("✅ MongoDB connecté avec succès !");
    console.log("📊 Base de données: employes");
})
.catch(err => {
    console.log("❌ Erreur de connexion MongoDB:", err.message);
    console.log("⚠️ L'application continuera sans MongoDB");
});

// ==================== ROUTES API ====================

// Route racine - sert index.html
app.get("/", (req, res) => {
    res.sendFile(path.join(__dirname, "frontend", "index.html"));
});

// Route de test
app.get("/api/test", async (req, res) => {
    try {
        const count = await Employe.countDocuments();
        res.json({
            status: "OK",
            message: "Serveur fonctionnel",
            mongodb: "Connecté",
            employes_count: count,
            timestamp: new Date().toISOString()
        });
    } catch (error) {
        res.json({
            status: "OK",
            message: "Serveur fonctionnel",
            mongodb: "Non connecté",
            timestamp: new Date().toISOString()
        });
    }
});

// GET tous les employés
app.get("/api/employes", async (req, res) => {
    try {
        console.log("📥 GET /api/employes");
        const employes = await Employe.find().sort({ nom: 1 });
        console.log(`✅ ${employes.length} employé(s) trouvé(s)`);
        res.json(employes);
    } catch (error) {
        console.error("❌ Erreur GET /api/employes:", error);
        res.status(500).json({ 
            error: "Erreur serveur",
            message: error.message 
        });
    }
});

// GET un employé par ID
app.get("/api/employes/:id", async (req, res) => {
    try {
        const id = req.params.id;
        console.log(`📥 GET /api/employes/${id}`);
        
        if (!mongoose.Types.ObjectId.isValid(id)) {
            return res.status(400).json({ error: "ID invalide" });
        }
        
        const employe = await Employe.findById(id);
        
        if (!employe) {
            return res.status(404).json({ error: "Employé non trouvé" });
        }
        
        console.log(`✅ Employé trouvé: ${employe.prenom} ${employe.nom}`);
        res.json(employe);
        
    } catch (error) {
        console.error("❌ Erreur GET /api/employes/:id:", error);
        res.status(500).json({ 
            error: "Erreur serveur",
            message: error.message 
        });
    }
});

// POST ajouter un employé
app.post("/api/employes", async (req, res) => {
    try {
        console.log("📥 POST /api/employes - Données:", req.body);
        
        const nouvelEmploye = new Employe(req.body);
        const employeSauvegarde = await nouvelEmploye.save();
        
        console.log(`✅ Employé ajouté: ${employeSauvegarde.prenom} ${employeSauvegarde.nom}`);
        console.log(`📊 ID: ${employeSauvegarde._id}`);
        
        res.status(201).json(employeSauvegarde);
        
    } catch (error) {
        console.error("❌ Erreur POST /api/employes:", error);
        res.status(400).json({ 
            error: "Erreur lors de l'ajout",
            message: error.message
        });
    }
});

// PUT modifier un employé
app.put("/api/employes/:id", async (req, res) => {
    try {
        const id = req.params.id;
        console.log(`📥 PUT /api/employes/${id}`);
        
        if (!mongoose.Types.ObjectId.isValid(id)) {
            return res.status(400).json({ error: "ID invalide" });
        }
        
        const employeModifie = await Employe.findByIdAndUpdate(
            id,
            req.body,
            { 
                new: true,
                runValidators: true
            }
        );
        
        if (!employeModifie) {
            return res.status(404).json({ error: "Employé non trouvé" });
        }
        
        console.log(`✅ Employé modifié: ${employeModifie.prenom} ${employeModifie.nom}`);
        res.json(employeModifie);
        
    } catch (error) {
        console.error("❌ Erreur PUT /api/employes/:id:", error);
        res.status(400).json({ 
            error: "Erreur lors de la modification",
            message: error.message 
        });
    }
});

// DELETE supprimer un employé
app.delete("/api/employes/:id", async (req, res) => {
    try {
        const id = req.params.id;
        console.log(`📥 DELETE /api/employes/${id}`);
        
        if (!mongoose.Types.ObjectId.isValid(id)) {
            return res.status(400).json({ error: "ID invalide" });
        }
        
        const employeSupprime = await Employe.findByIdAndDelete(id);
        
        if (!employeSupprime) {
            return res.status(404).json({ error: "Employé non trouvé" });
        }
        
        console.log(`✅ Employé supprimé: ${employeSupprime.prenom} ${employeSupprime.nom}`);
        res.json({
            success: true,
            message: "Employé supprimé avec succès"
        });
        
    } catch (error) {
        console.error("❌ Erreur DELETE /api/employes/:id:", error);
        res.status(500).json({ 
            error: "Erreur lors de la suppression",
            message: error.message 
        });
    }
});

// Route fallback pour SPA
app.get("*", (req, res) => {
    res.sendFile(path.join(__dirname, "frontend", "index.html"));
});

// ==================== DÉMARRAGE ====================
const PORT = 3000;
app.listen(PORT, () => {
    console.log("=".repeat(60));
    console.log("🚀 SERVEUR EXPRESS DÉMARRÉ !");
    console.log("=".repeat(60));
    console.log(`🌐 Accédez à: http://localhost:${PORT}`);
    console.log("=".repeat(60));
    console.log("\n📡 URLs disponibles:");
    console.log(`   📍 Interface: http://localhost:${PORT}`);
    console.log(`   📍 Test API: http://localhost:${PORT}/api/test`);
    console.log(`   📍 Employés: http://localhost:${PORT}/api/employes`);
    console.log("=".repeat(60));
});