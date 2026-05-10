# Compte rendu de réunion - Point projet DLE
**Date** : Non précisée
**Durée estimée** : ~1h30

---

## Participants
- Audran (mentionné)
- Benoît
- Didier
- Hugo
- Simon
- Frédéric
- Nicolas
- Johan
- Joanne
- Samir
- Aurélien
- Olivier
- Autres membres de l'équipe (non nommés explicitement)

---

## Objet de la réunion
Point d'avancement sur les projets de la DLE (Direction du Numérique pour l'Éducation), incluant :
- Suivi des budgets et jalons
- Avancement des projets techniques (Tribu, Nuage, VisioAgent, etc.)
- Gestion des prestataires et éditeurs
- Planification des déploiements et migrations

---

## Sujets abordés

### 1. Budget et jalons
- **Réduction du budget DLE** : Confirmation attendue sur les montants impactant le programme. Risque de "rabot" sur certains produits.
- **Suivi des jalons** :
  - Besoin d'améliorer la précision des dates de livraison pour les nouvelles fonctionnalités.
  - Problématique de visibilité avec les prestataires (ex. : dates floues comme "avant l'été").
  - **Décision** : Travailler avec les prestataires pour obtenir des engagements plus réalistes et des roadmaps fiables.

### 2. Projets techniques

#### Tribu
- **Refonte graphique (UX8)** :
  - Chiffrage en cours avec les prestataires (3 lots : accueil/tableaux de bord, outils/recherche, administration).
  - Planning visé : Mise en production fin 2025 (objectif fin novembre/début décembre).
  - Environnements de pré-production en préparation.
- **Prochaines étapes** :
  - Finaliser le chiffrage et lancer les développements.
  - Prévoir une période de tests en décembre avant les congés.

#### Nuage (Nextcloud)
- **Problème avec la version 31** :
  - Régression fonctionnelle sur les liens de partage (non compatible avec la version actuelle).
  - **Décision** : Reporter la mise à jour en production jusqu'à correction par l'éditeur.
- **Migration académique** :
  - Script de migration testé avec Nantes (correctif en attente).
  - Audit de base de données : augmentation de la RAM pour PostgreSQL (de 8 Go à 12 Go).
- **Prochaines étapes** :
  - Planifier la migration avec le CRTH fin mai.
  - Surveiller les performances après l'augmentation de RAM sur les frontaux.

#### VisioAgent (BBB)
- **Version 3.0** :
  - Fonctionnalités disparues (ex. : sous-titrage SME) et nouveaux plugins (ex. : sélection aléatoire de participants).
  - **Décision** : Vérifier les fonctionnalités critiques avant mise en production.
- **Demandes du CNET** :
  - Délégation de salles (complexe à implémenter).
  - **Question en suspens** : Qui finance les développements non prioritaires ?

#### Portail Apps
- **Statistiques** :
  - 221 000 comptes ouverts (dont 73 000 actifs depuis décembre).
  - 80 000 vidéos sur PodÉdu.
- **Avancements** :
  - Installation de Matomo pour des stats précises.
  - Raccourcisseur d'URL en développement (livraison prévue avant l'été).
  - Architecture en micro-applications pour le cycle de vie des comptes.

#### Messagerie (Aetna)
- **Déploiement en Corse** :
  - Premier pilote à grande échelle (académie entière).
  - Bilan mitigé : 99% de succès, mais difficultés avec certains usages (ex. : boîtes fonctionnelles, exports EML).
  - **Décision** : Améliorer l'accompagnement au changement et automatiser les processus.
- **Prochains déploiements** :
  - Accélération prévue au T3/T4 2024 (Nantes, Poitiers, PACA, etc.).
  - Réunion avec les référents pour valider le plan global.

#### Autres projets
- **BNA** : Décalage de la campagne du 16 au 27/28 juin (éviter les sollicitations concurrentes).
- **Communication unifiée** : Réflexion sur les outils (Webex, Cisco, etc.) pour le déménagement à Gentilly.
- **Wi-Fi** : Questionnaire envoyé aux académies d'Île-de-France pour évaluer les usages.

---

## Décisions prises
1. **Précision des jalons** : Exiger des prestataires des roadmaps plus fiables et des dates réalistes.
2. **Nuage** : Reporter la mise à jour vers Nextcloud 31 jusqu'à correction des régressions.
3. **Tribu** : Valider le chiffrage et lancer les développements pour une MEP fin 2025.
4. **Messagerie** : Renforcer l'accompagnement au changement pour les prochains déploiements.
5. **VisioAgent** : Prioriser les fonctionnalités critiques avant mise en production de la version 3.0.

---

## Questions en suspens
- **Financement des évolutions VisioAgent** : Comment traiter les demandes du CNET non prioritaires ?
- **Compatibilité Thunderbird** : Faut-il maintenir le plugin pour les académies ou les orienter vers le webmail ?
- **Roadmap des éditeurs** : Comment obtenir plus de visibilité sur les sorties des versions (ex. : Collaborat, BBB) ?

---

## Tâches à effectuer
| Tâche | Responsable | Échéance |
|-------|-------------|----------|
| Finaliser le chiffrage de la refonte Tribu | Simon | Cette semaine |
| Organiser un retour d'expérience Squash avec Tribu | Simon | À planifier |
| Planifier la migration Nuage avec le CRTH | Frédéric | Fin mai |
| Préparer les slides pour le comité référents | Équipe | Prochains jours |
| Contacter l'UNISA pour recaler un point | Benoît | À faire |
| Déployer la transcription des vidéos sur Tube | Équipe | Priorité |
| Tester l'usine d'apport des contacts/archives (messagerie) | Équipe | En cours |

---

## Prochaine rencontre
- **Comité des référents** : Mardi prochain (en distanciel).
- **Prochaine réunion projet** : Non précisée (à confirmer).
- **Événement** : Participation à GFR Bordeaux début juin (Benoît, Nicolas, Johan, etc.).
