# **Compte rendu de réunion – 46ème comité de domaine**
**Date** : [À compléter]
**Durée estimée** : ~1h30

---

## **Participants**
- **Animateur** : [Nom non précisé]
- **Participants** :
  - Didier, Hugo, Benoît, Frédéric, Simon, Johan, Aurélien, Nicolas, Mickaël, Benjamin, Charly, Valérie, Frédéric Cognès, Irina, Paul Fouad, Yann, Mickaël, Bruno, Olivier, François, Sophie
  - Autres : [Noms non identifiés dans la transcription]

---

## **Objet de la réunion**
- Point projet et suivi des jalons pour les différents outils et services (Tribu, Nuage, BBB, Portail Apps, etc.).
- Bilan des actions post-vacances et préparation des prochains comités (référents, DNE, etc.).
- Sujets transverses : budget DLE, conformité, accompagnement au changement, et relations avec les prestataires.

---

## **Sujets abordés**

### **1. Comité de domaine (DLE) – Audran**
- **Budget** :
  - Réduction budgétaire confirmée sur la DLE (montants en attente de confirmation).
  - Risque de "coup de rabot" sur certains produits.
- **Suivi des jalons** :
  - Demande de **précision accrue** sur les dates de livraison des fonctionnalités (ex. : T4 2025).
  - Besoin de visibilité pour la direction (ex. : septembre/octobre pour les livraisons).
  - **Problème identifié** : Manque de maîtrise des plannings par les prestataires (ex. : Nextcloud, Collaborat).
  - **Solutions envisagées** :
    - Exiger des engagements plus réalistes des éditeurs.
    - Travailler sur la stabilité des roadmaps (ex. : BBB, Nextcloud).
    - Séparer les développements financés (ex. : DBV) des versions publiques.

### **2. Projets en cours**
#### **A. Tribu**
- **Refonte graphique (UX8)** :
  - Chiffrage en cours (200 jours de développement, 3 lots).
  - Mise en production prévue pour **fin 2025** (date précise à confirmer).
  - Environnements de test préparés (pré-prod, dev, acuité).
  - **Risques** : Retards possibles sur les spécifications ou les tests.
- **Mises à jour techniques** :
  - Montées de versions pour améliorer la stabilité et la charge.

#### **B. Nuage (Nextcloud)**
- **Problèmes majeurs** :
  - **Version 31** : Régression fonctionnelle unilatérale (liens de partage modifiés).
    - Mise à jour reportée pour éviter des impacts utilisateurs.
    - Attente d’un correctif de l’éditeur (Maxime Leherici).
  - **Migration académique** :
    - Script de migration en attente (correction en cours).
    - Déploiement différé (Nantes en pilote, autres académies en attente).
  - **Audit base de données** :
    - Augmentation de RAM (8 Go → 12 Go) pour éviter les plantages.
    - Gain observé sur les processus systèmes.

#### **C. BBB (BigBlueButton)**
- **VisioAgent 1.3** :
  - Fonctionnalités ajoutées : favoris, tri alphabétique, bandeau d’infos.
  - **Demandes CNET** :
    - Délégation de salles (complexe à implémenter).
    - Développement de plugins externes (ex. : sélection aléatoire).
  - **Problème** : Certaines fonctionnalités disparues dans la v3.0 (ex. : sous-titrage SME).
  - **Commande validée** : 35 jours de développement pour des évolutions spécifiques.

#### **D. Portail Apps**
- **Statistiques** :
  - 80 000 vidéos, 221 000 comptes ouverts (dont 73 000 actifs depuis décembre).
  - Matomo installé pour analyser les parcours utilisateurs.
- **Raccourcisseur d’URL** :
  - Développement en cours (livraison prévue avant l’été).
  - API disponible pour d’autres services.
- **Architecture** :
  - Migration vers des micro-applications (cycle de vie des utilisateurs).

#### **E. Autres projets**
- **BNA (Base Nationale des Agents)** :
  - Lancement reporté au **27-28 juin** pour éviter la surcharge (conflit avec une enquête DELCOM).
- **Communication unifiée** :
  - Choix d’outil (Cisco, Webex, solutions libres) en discussion (lié au déménagement du ministère).
- **Tube (PeerTube)** :
  - Thématisation des instances (masquage des instances techniques).
  - Transcription automatique des vidéos opérationnelle (déploiement prévu).
  - Travaux sur l’automatisation des déploiements (en attente de tests).
- **Webmail** :
  - Migration des académies vers WebMate (ex. : Corse en pilote).
  - Problèmes identifiés : usages locaux (ex. : FGRA), exports PDF pour les recteurs.
  - **Question ouverte** : Faut-il fournir des plugins pour Thunderbird ou se concentrer sur le webmail ?

---

### **3. Support et incidents**
- **Incidents récents** :
  - **Omniface** : Problème de déploiement d’applications (lié à une tâche planifiée non exécutée).
  - **Conformité poste de travail** : Besoin de produits Cisco/Magenta (discussion en cours avec M. Teresso).
  - **CPT** : Mise à jour planifiée (interruptions de service limitées à une demi-journée).
- **UNISA** :
  - Recadrage des dates de passage en mode "insas" (à confirmer).

---

### **4. Organisation et prochaines étapes**
- **Comité référents** :
  - Réunion prévue **mardi prochain** (distanciel).
  - Slides à préparer pour partager les dernières actualités.
- **Prochaine réunion** :
  - **Date** : [À confirmer].
  - **Points clés** :
    - Retour d’expérience Squash (avec Simon).
    - Bilan des déploiements (Corse, Nantes, Poitiers, etc.).
    - Avancement des projets (Tribu, Nuage, BBB).

---

## **Décisions prises**
1. **Validation de l’intégration de DBV dans Cap Education** :
   - Développement commandé pour ajouter un lien de visioconférence intégré (BBB via VisioAgent).
2. **Report du lancement de BNA** :
   - Du 16 juin au **27-28 juin** pour éviter la surcharge.
3. **Priorisation des correctifs** :
   - Nextcloud v31 : Attendre le correctif avant déploiement.
   - BBB : Commander des évolutions spécifiques (plugins, délégation de salles).
4. **Accélération des déploiements** :
   - Préparation des académies pilotes (Nantes, Poitiers, PACA) pour un déploiement massif au **T3-T4 2025**.

---

## **Questions en suspens**
1. **Précision des dates de livraison** :
   - Comment obtenir des engagements fermes des éditeurs (ex. : Nextcloud, Collaborat) ?
2. **Accompagnement au changement** :
   - Comment mieux former les utilisateurs aux nouveaux outils (ex. : Tribu, WebMate) ?
3. **Budget DLE** :
   - Quels produits seront impactés par la réduction budgétaire ?
4. **Communication unifiée** :
   - Quel outil choisir (Cisco, Webex, libre) et comment le déployer ?
5. **Migration académique Nuage** :
   - Quand les académies (hors Nantes) pourront-elles migrer ?

---
## **Tâches à effectuer**
| **Tâche** | **Responsable** | **Échéance** |
|-----------|----------------|-------------|
| Finaliser le chiffrage Tribu (refonte graphique) | Simon | [À confirmer] |
| Contacter Maxime Leherici (Nextcloud) pour le correctif v31 | Frédéric/Nicolas | [Urgent] |
| Préparer les slides pour le comité référents | Équipe projet | [D’ici mardi] |
| Valider le plan de déploiement académique (T3-T4) | Benoît/Frédéric | [Juillet 2025] |
| Finaliser le raccourcisseur d’URL (Portail Apps) | Équipe dev | [Avant l’été] |
| Travailler avec Renater sur la montée en charge de BBB | Mickaël/Benjamin | [À définir] |
| Étudier la compatibilité Thunderbird/Webmail | Olivier | [À définir] |
| Automatiser les mises à jour de Tube | Nicolas | [Rentrée 2025] |

---
## **Prochaine rencontre**
- **Date** : [À confirmer]
- **Format** : [Présentiel/Distanciel]
- **Points à aborder** :
  - Retour d’expérience Squash (Tribu).
  - Bilan des déploiements (Corse, Nantes, etc.).
  - Avancement des correctifs (Nextcloud, BBB).
  - Préparation du comité DNE.
