# **Compte rendu de réunion – 46ème comité de domaine**
*Date non précisée*

---

## **Participants**
- **Animateur** : [Nom non précisé]
- **Didier, Hugo, Benoît** (présents ou en distanciel)
- **Audran** (mentionné pour le comité de domaine)
- **Simon** (référent Tribu)
- **Aurélien** (mentionné pour le projet "regroupement")
- **Bruno** (mentionné pour la communication unifiée)
- **Frédéric Cognès** (mentionné pour l'intégration de DBV dans Cap Education)
- **Nicolas** (mentionné pour Nextcloud)
- **Maxime Leherici** (support Nextcloud)
- **Paul Fouad** (travaux sur CHAP)
- **Valérie** (validation de commandes)
- **Mickaël, Benjamin** (travaux sur la Cine des Yéhouètes)
- **Irina** (pôle Socle, Paris)
- **Charly** (mentionné pour Tribu)
- **Johan** (mentionné pour le raccourcisseur d'URL)
- **Aurélien** (mentionné pour le projet "regroupement")
- **Joanne, Samir** (mentionnés pour les incidents techniques)
- **Olivier** (mentionné pour les bornes Wi-Fi)
- **François, Sophie, Frédéric** (mentionnés pour le GSR)
- **Simon** (mentionné pour le Squash avec Tribu)

---

## **Objet de la réunion**
Point projet et comité de domaine, avec focus sur :
- Suivi des jalons et livraisons (Nextcloud, Collaborat, BBB, etc.).
- Refonte graphique de Tribu (UX/UI).
- Déploiements (messagerie, Nuage, etc.).
- Communication unifiée et outils collaboratifs.
- Gestion des prestataires et visibilité des roadmaps.

---

## **Durée estimée**
Non précisée (réunion longue, plusieurs sujets abordés).

---

## **Sujets abordés**

### **1. Comité de domaine (Audran)**
- **Réduction du budget DLE** : Confirmation attendue des montants, risque de "rabot" sur certains projets.
- **Suivi des jalons** :
  - **Points positifs** : Nouvelles fonctionnalités appréciées (ex : BBB, Nextcloud).
  - **Problèmes** :
    - Manque de **précision sur les dates de livraison** (ex : T4 2025 vs. reports fréquents).
    - Dépendance aux éditeurs (ex : Collaborat, Nextcloud) avec des délais non maîtrisés.
    - Exemple : **Nextcloud 31** a introduit des régressions fonctionnelles (liens de partage) sans préavis.
    - **BBB** : Livraisons tardives (ex : commandes BVB prévues pour fin 2024/début 2025).
    - **Collaborat** : Absence de visibilité sur la roadmap (ex : pas de dates pour la version 3.1).

### **2. Tribu**
- **Refonte graphique (UX/UI)** :
  - **Chiffrage en cours** (200 jours de développement, 3 lots : accueil/dossiers, outils/recherche, administration).
  - **Objectif** : Mise en production **fin 2025** (date précise à confirmer après validation du chiffrage).
  - **Environnements** : Pré-prod isoprod + dev pour la refonte.
  - **Risques** : Retards possibles sur les spécifications ou développements.

### **3. Nextcloud (Nuage)**
- **Version 31** :
  - **Problème** : Régression sur les liens de partage (fonctionnalités modifiées unilatéralement par l'éditeur).
  - **Solution** : Report de la migration en prod (attente d'un correctif).
  - **Global Scale** : Prérequis = Nextcloud 31 (impossible de tester en pré-prod).
- **Migration académique** :
  - **Nantes** : Script de migration en attente de correctifs.
  - **Paris** : Attente des retours de Nantes avant de démarrer.
- **Audit BDD** : Augmentation de RAM (8 Go → 12 Go) pour éviter les plantages.

### **4. BBB (VisioAgent)**
- **Nouveautés** :
  - Gestion des favoris, tri alphabétique des salons, bandeau d'informations.
  - **Plugins** : Possibilité de développer des fonctionnalités spécifiques (ex : sélection aléatoire de participants).
  - **Demandes CNET** : Délégation de salles (sujet complexe, non priorisé).
- **Problèmes** :
  - Fonctionnalités disparues dans la v3.0 (ex : sous-titrage SME).
  - **Commande validée** : 35 jours de développement pour des évolutions (visio agent 1.3).

### **5. Messagerie (Aetna)**
- **Déploiement pilote en Corse** :
  - **Bilan** :
    - 99% des comptes migrés sans incident majeur.
    - Problèmes résiduels : comptes fonctionnels (ex : AGA/ASGA) et usages locaux (ex : FGRA).
    - **Enjeux** : Accompagnement au changement (ex : exports PDF vs. EML pour les recteurs).
  - **Prochaines étapes** :
    - Nantes, Poitiers, PACA : reprise des déploiements.
    - **Lieux de France** : Migration prévue en **octobre 2025**.
    - **Automatisation** : Usine d'import des contacts/archives en test avec la Corse.

### **6. Portail Apps**
- **Chiffres** :
  - 80 000 vidéos (PodEduque).
  - 221 000 comptes ouverts (dont 73 000 reconnectés en 5 mois).
  - **Matomo** : Stats d'usage en cours de collecte.
- **Évolutions** :
  - **Raccourcisseur d'URL** : Développement en cours (livraison prévue avant l'été).
  - **Architecture** : Micro-applications pour le cycle de vie des utilisateurs.
- **Rancher (Créprod)** :
  - **Problèmes** : Certificats, documentation incomplète, déploiement complexe.

### **7. PeerTube**
- **Transcription automatique** : Opérationnelle sur test (v7), généralisation prévue.
- **Cyclonomie** :
  - **Fonctionnalités** :
    - Suppression automatique des vidéos après X mois (plugin Pramasoft).
    - Gestion des mineurs (plugin spécifique au ministère).
  - **En attente** : Devis et marché public.

### **8. Communication unifiée**
- **Enjeux** :
  - **Outils** : Cisco, Webex, BBB, CHAP (téléphonie SIP).
  - **Déménagement du ministère** : Besoin de définir une stratégie (ex : EVT Cisco vs. outils libres).
  - **Intégration** : BBB dans CHAP, Webex dans BBB (travaux en cours avec Paul Fouad).
- **Problème** : Matériel compatible non testé.

### **9. Autres sujets**
- **Renouvellement licences Microsoft** : Réalisé pour 30 000 agents.
- **BNA** : Campagne reportée au **16–27/06/2025** (éviter la superposition avec une enquête DELCOM).
- **Wi-Fi** : Questionnaire envoyé aux académies d'Île-de-France (retours en attente).
- **Intranet académique** : Refonte en discussion (projet stratégique).

---

## **Décisions prises**
1. **Nextcloud 31** :
   - Report de la migration en prod jusqu’à correction des régressions.
   - Point avec **Maxime Leherici** (support Nextcloud) pour valider les correctifs.
2. **Tribu** :
   - Validation du chiffrage et lancement des développements après accord.
   - Mise en prod **fin 2025** (date précise à confirmer).
3. **BBB** :
   - Commande de **35 jours de développement** validée pour les évolutions (VisioAgent 1.3).
4. **Messagerie** :
   - Poursuite des déploiements pilotes (Corse, Nantes, Poitiers, PACA).
   - **Lieux de France** : Migration prévue en **octobre 2025**.
5. **Portail Apps** :
   - Livraison du **raccourcisseur d’URL** avant l’été.
   - Déploiement de **Matomo** pour les stats utilisateurs.
6. **PeerTube** :
   - Généralisation de la transcription automatique après tests.
   - Lancement des devis pour la cyclonomie (plugins).

---
## **Questions en suspens**
1. **Précision des roadmaps éditeurs** :
   - Comment obtenir des engagements réalistes de la part de **Collaborat**, **Nextcloud**, et **BBB** ?
   - Exemple : **BBB v3.1** (date de livraison inconnue).
2. **Global Scale (Nextcloud)** :
   - Comment tester en pré-prod avec la version 31 ?
3. **Migration académique (Nuage)** :
   - Quand **Nantes** aura-t-il terminé ses tests pour que **Paris** puisse démarrer ?
4. **Communication unifiée** :
   - Quel outil choisir (Cisco, Webex, BBB, outils libres) ?
   - Stratégie pour le **SIP** et la téléphonie.
5. **Aetna** :
   - Faut-il fournir des plugins pour **Thunderbird** ou se concentrer sur le webmail ?
6. **Rancher (Créprod)** :
   - Comment déployer les applications malgré les problèmes de documentation ?

---
## **Tâches à effectuer**
| **Tâche** | **Responsable** | **Échéance** |
|-----------|----------------|--------------|
| Valider le chiffrage Tribu | Simon | Semaine en cours |
| Corriger les régressions Nextcloud 31 | Maxime Leherici (support) | À confirmer |
| Finaliser le questionnaire Wi-Fi | Olivier | Retour académies Île-de-France |
| Préparer les slides pour le comité référent | [Non précisé] | J-7 avant la réunion |
| Lancer les devis PeerTube (cyclonomie) | [Non précisé] | À définir |
| Tester l’usine d’import des contacts (Corse) | [Non précisé] | En cours |
| Clarifier la stratégie communication unifiée | Bruno | À organiser |
| Suivre l’avancement du Rancher | [Non précisé] | À définir |

---
## **Prochaine rencontre**
- **Comité référent** : **Mardi prochain** (en distanciel).
- **Point Squash avec Tribu** : À organiser avec **Simon**.
- **Réunion de lancement "Lieux de France"** : **Octobre 2025** (date à confirmer).
