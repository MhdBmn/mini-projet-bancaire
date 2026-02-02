const mongoose = require("mongoose");

const EmployeSchema = new mongoose.Schema({
  nom: {
    type: String,
    required: [true, "Le nom est obligatoire"],
    trim: true
  },
  prenom: {
    type: String,
    required: [true, "Le prénom est obligatoire"],
    trim: true
  },
  anciennete: {
    type: Number,
    default: 0,
    min: [0, "L'ancienneté ne peut pas être négative"]
  },
  adresse: {
    numero: {
      type: Number,
      min: [1, "Le numéro doit être positif"]
    },
    rue: String,
    codepostal: Number,
    ville: String
  },
  tel: {
    type: Number,
    unique: true,
    sparse: true
  },
  prime: {
    type: Number,
    default: 0,
    min: [0, "La prime ne peut pas être négative"]
  }
}, {
  timestamps: true
});

// Index composé pour éviter les doublons nom/prénom
EmployeSchema.index({ nom: 1, prenom: 1 }, { unique: true });

module.exports = mongoose.model("Employe", EmployeSchema);