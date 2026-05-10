# Compte Rendu de Réunion - 46ème Réunion du Programme

## Participants

- Animateur principal
- Didier, Hugo, Benoît (en vacances)
- Simon
- Frédéric
- Nicolas
- Olivier
- Johan
- Samir
- Aurélien
- Yann
- Manon
- Et autres membres de l'équipe

## Objet de la Réunion

Point projet global du programme couvrant l'ensemble des services et projets en cours.

---

## Sujets Abordés

### 1. **Comité de Domaine - Enjeux Majeurs**

#### Réduction budgétaire
- Réduction du budget sur toute la DLE confirmée
- Impact à évaluer selon les projets
- Risque de "coup de rabot" sur les produits

#### Suivi des jalons et précision des dates
- **Enjeu principal** : Améliorer la précision des dates de livraison des nouvelles fonctionnalités
- Actuellement : dates imprécises ou décalages récurrents
- Besoin de meilleure visibilité auprès de la direction
- **Problématique identifiée** : Dépendance aux éditeurs externes (Collabora, Nextcloud, Bluebird Network, etc.) avec roadmaps peu fiables
- Nécessité d'améliorer les relations avec les prestataires pour obtenir des engagements plus réalistes

### 2. **Renouvellement des Licences Microsoft**
- Réalisé la semaine précédente
- Concerne 30 000 agents

### 3. **Projet Tribu - Refonte Graphique UX8**

**Statut** : En phase de chiffrage et validation du planning

**Détails** :
- Refonte ergonomique complète
- Découpage en 3 lots :
  - **Lot 1** : Accueils, tableaux de bord, dossiers (~80 jours)
  - **Lot 2** : Outils et recherche
  - **Lot 3** : Administration
- **Total estimé** : ~200 jours
- Mise en production envisagée : **fin 2025** (novembre-décembre)
- Spécifications partielles livrées fin avril
- Préparation d'environnements de pré-prod en parallèle
- Montées de versions techniques en cours pour supporter la charge

**Confiance** : Équipe de développement confiante pour une version finalisée fin d'année

### 4. **Projet Éducation (Éduc)**
- 99% de consommation de MCO (maintenance corrective)
- Peu d'évolutions en cours

### 5. **Projet Joanne (Gestion des Caminos)**
- 10 400 caminos envoyés ce matin
- Passage en production en cours
- 2 incidents identifiés :
  - Classement des terminaux dans les dossiers OG
  - Déploiement d'applications lent (problème identifié sur les tâches planifiées)
- Conformité des postes de travail : rencontre avec Cisco et Magenta
- Mise à jour de CPT planifiée

### 6. **Projet Nuage (Nextcloud)**

**Problème majeur** : Nextcloud 31
- Grosse régression fonctionnelle sur le partage de fichiers introduite par l'éditeur
- Impossible de déployer en production en l'état
- Prérequis pour Global Scale
- **Action** : Travail avec le support éditeur (Maxime Leherici) pour trouver une solution

**Autres points** :
- Migration académique : en attente du correctif du script de migration (Nantes = académie pilote)
- Augmentation RAM serveurs Postgres : passage de 8 Go à 12 Go (recommandation audit)
  - Résultat positif : arrêt des plantages des services de métrologie
- Prévision : augmentation RAM frontaux applicatifs fin mai

### 7. **Projet Visio Agent**

**Intégrations validées** :
- Intégration de BBB dans Cap Education (commande validée)
- Lien particulier pour ajouter utilisateurs dans CHAP

**Visio Agent 1.3** :
- Nouveau frontal livré avec :
  - Bandeau d'informations
  - Tri des salons (alphabétique/création)
  - Gestion des favoris
- Commande de 35 jours de développement validée ce matin

**BBB 3.0** :
- Livrée il y a plus d'un mois
- Recette en cours
- Nouvelles fonctionnalités : système de plugins
- Demandes du CMED : délégation de salons (complexe, non priorisée)

**Cinéma des Yéhouètes (POC)** :
- Réinstallation complète réalisée
- Travail en cours avec Renater
- Développements supplémentaires : intégration RCMP
- Enjeu : montée en charge de la Sydney Gateway

### 8. **Portail Apps**

**Statistiques** :
- 221 000 comptes ouverts
- 73 000 comptes actifs depuis décembre
- ~80 000 vidéos

**Évolutions** :
- Matomo installé (analytics détaillées)
- Portail 6.4.1 en production
- Raccourcisseur d'URL : en développement (2 devs, fin de semaine prochaine)
- Cycle de vie des utilisateurs : architecture en micro-applications

**Infrastructure** :
- Rancher pré-prod : livré mais pas encore fonctionnel
- Problèmes : certificats, déploiement d'outils

### 9. **Projet Tube (PeerTube)**

**Thématisation** :
- Thème graphique non supporté en version 7.1.1
- Travaux en cours pour nouvelle approche (masquer instances, afficher thématiques)
- Déploiement prévu après rentrée (3-4 mois)

**Transcription** :
- Opérationnelle en test
- Déploiement généralisé prévu après passage en 7.1.1
- Externalisation transcription/transcodage envisagée

**Cycle de vie des vidéos** :
- Attente de devis
- Répartition : cœur PeerTube (Pramasoft) + plugins spécifiques (ministère)

**Automatisation déploiements** : En attente de tests

### 10. **Projet Aetna (Messagerie)**

**Déploiement Corse** : Premier pilote complet
- 99% de succès
- Quelques problèmes : comptes AGA/ASGA, boîtes surdimensionnées (94-96 Go)
- Basculement complet sur WebMate (fin Thunderbird)
- Débit limité (200 Mbps)

**Enseignements** :
- Changement d'usage après 20-25 ans de Convergence
- Besoin d'accompagnement au changement important
- Cas métiers spécifiques (exports EML, boîtes fonctionnelles)
- Nécessité de solutions fluides et proactives

**Suites des déploiements** :
- Nantes, Poitiers, Paca : reprises en cours
- Nantes : libération écoles/collèges avant juin
- Reims : réunion début juin
- Accélération prévue T3-T4 2024

**Sujets en cours** :
- Usine d'import contacts/archives testée par utilisateurs Corse
- Plugin Visio Agent demandé
- Latences résolues (allègement détections corps messages)
- Dictionnaires académies : consolidation en cours

**Questions ouvertes** :
- Support Thunderbird : plugin en place, compatibilité en cours
- Stratégie : webmail vs clients lourds

### 11. **Bornes Wi-Fi**
- Questionnaire envoyé aux académies Île-de-France
- En attente de retours sur usages et problèmes

### 12. **Portail Intranet Académique**
- Refonte en cours
- Implication académies à confirmer semaine prochaine
- Considéré comme porte d'entrée des services

---

## Décisions Prises

1. **Tribu** : Lancement développement dès validation du chiffrage
2. **Nextcloud 31** : Report de la mise à jour majeure, travail avec éditeur pour correctif
3. **Visio Agent** : Commande de 35 jours de développement validée
4. **Aetna** : Accélération des déploiements T3-T4 2024
5. **Portail intranet** : Confirmation implication académies semaine prochaine

---

## Questions en Suspens

1. **Dates précises de livraison** : Nécessité d'améliorer la communication sur les jalons (dépendance éditeurs)
2. **Nextcloud 31** : Solution pour Global Scale à définir avec éditeur
3. **Migration académies Aetna** : Attente correctif script migration (Nantes)
4. **Thunderbird** : Stratégie de support à clarifier (webmail vs clients lourds)
5. **Rancher** : Mise en fonctionnement en pré-prod
6. **Thématisation Tube** : Validation approche masquage instances

---

## Tâches à Effectuer

| Tâche | Responsable | Délai |
|-------|-------------|-------|
| Validation chiffrage Tribu | Équipe dev | Cette semaine |
| Lancement développement Tribu | Simon | Après validation chiffrage |
| Travail correctif Nextcloud 31 | Frédéric/Maxime Leherici | Urgent |
| Déploiement transcription Tube | Nicolas | Après 7.1.1 |
| Retours questionnaire Wi-Fi | Académies Île-de-France | À définir |
| Confirmation implication portail intranet | Équipe projet | Semaine prochaine |
| Point avec UNISA | Responsable UNISA | À planifier |
| Raccourcisseur URL Portail Apps | 2 devs | Fin de semaine |
| Recontact éditeur Omnisa | Olivier | Urgent (prérequis installation) |
| Mise à jour slides Frédéric | Frédéric | Après réunion |

---

## Prochaine Rencontre

- **Comité des Référents** : Mardi prochain (en distanciel)
- **Réunion support Nextcloud** : Même jour (avec démonstration problème partage)
- **Réunion GSA** : Début juin (Bordeaux)
- **Réunion lancement Île-de-France** : Semaine prochaine

---

## Points Clés à Retenir

- **Enjeu majeur** : Améliorer la précision des dates de livraison et la maîtrise des roadmaps éditeurs
- **Accompagnement** : Besoin critique d'améliorer le suivi du terrain et l'accompagnement au changement
- **Accélération** : Déploiements Aetna s'accélèrent T3-T4 2024
- **Confiance** : Équipes confiantes sur Tribu et autres projets malgré les défis
