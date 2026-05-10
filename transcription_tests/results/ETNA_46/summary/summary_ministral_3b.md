# **Compte rendu de réunion – [Nom du projet/équipe]**
**Date** : [À préciser dans le suivi]
**Durée estimée** : ~2h30 (avec pauses et interventions)
**Participants** :
- **Didier** (animateur)
- **Hugo**, **Benoît**, **Simon**, **Frédéric**, **Nicolas**, **Joanne**, **Aurélien**, **Yann**, **Mickaël**, **Benjamin**, **Hugo** (Dijon), **Bruno**, **Frédéric Cognès**, **Paul Fouad**, **Maxime Leherici**, **Valérie**, **Frédéric** (DNE), **Johan**, **François**, **Sophie**
- **Absents** : **Mickaël** (congé), **Benjamin** (formation), **Benoît** (présent en partie), **Maxime** (support Nextcloud)

---

## **1. Objet de la réunion**
- **Point projet quinquennal** : Bilan des avancées, défis et perspectives des projets en cours (Tribu, Nuage/Nextcloud, BGB, V2V, messagerie, Wi-Fi, etc.).
- **Suivi des jalons** : Précision des dates de livraison et coordination avec les prestataires/éditeurs.
- **Retours d’expérience** (ex : migration académique Nextcloud, refonte Tribu, déploiements Wi-Fi).
- **Préparation des prochaines étapes** : Comités, réunions ciblées (référents régionaux, DRAZI/SGRAS).

---

## **2. Sujets abordés**

### **A. Budget et suivi des jalons**
- **Réduction budgétaire** :
  - Réduction globale sur la **DLE** (Direction du Numérique Éducatif). Impact variable selon les projets.
  - **Risque** : Coup de rabot possible sur certains produits. À surveiller.
- **Précision des dates de livraison** :
  - **Problématique** : Manque de visibilité sur les dates exactes (ex : "T4" ou "été" comme horizon).
  - **Demande** : Audran (comité de domaine) exige des dates **plus précises** (ex : "septembre/octobre" plutôt que "T4").
  - **Enjeux** :
    - **Transparence** envers la direction pour rassurer sur les livraisons.
    - **Coordination avec les prestataires** : Certains éditeurs (ex : Collaborat) ne respectent pas les roadmaps annoncées.
    - **Risque** : Décalages fréquents (ex : version 3.1 de DBV, migration Nextcloud 31).
  - **Solutions proposées** :
    - **Pour les développements financés** : Exiger des engagements clairs des prestataires (ex : livraison en patch sur version précédente).
    - **Pour les versions publiques** : Clarifier la distinction entre ce que l’on paie (support) et ce que l’on attend (fonctionnalités).
    - **Améliorer la relation avec les éditeurs** : Obtenir des roadmaps réalistes et des prérequis techniques (ex : Kubernetes, Terraform).

### **B. Projets spécifiques**

#### **1. Tribu**
- **Refonte graphique (UX8)** :
  - **Objectif** : Mise en production prévue **fin 2025** (décembre).
  - **Planning** :
    - 3 lots identifiés (accueil/tableaux de bord, outils/recherche, administration).
    - **Lot 1** (80 jours) : Validation en cours, retours sur les spécifications.
    - **Environnements** : Pré-prod et dev dédiés pour éviter les conflits.
  - **Risques** : Retards liés aux congés et ajustements techniques.
  - **Prochaine étape** : Chiffrage finalisé → lancement des développements.

#### **2. Nuage/Nextcloud**
- **Migration vers la version 31** :
  - **Problème** : Régression fonctionnelle sur les **liens de partage** (passage des liens internes aux externes).
  - **Impact** : Impossible de déployer en prod sans correction. Attente d’un correctif de Nextcloud (Maxime Leherici).
  - **Décalage** : Migration reportée au **mois prochain** pour tester la version corrigée.
- **Global Scale** :
  - Prérequis : Nextcloud 31 → bloqué en attendant la résolution du bug.
- **Migration académique** :
  - **Équipe pilote** (Nantes) en attente d’un script corrigé (évolution demandée).
  - **Académie de Paris** : Différence de migration reportée en raison de l’attente de Nantes.
- **Optimisation serveurs** :
  - **+4 Go de RAM** sur les bases de données (PostgreSQL) → résolution des plantages récurrents.
  - Prochaine étape : Ajout de RAM sur les serveurs applicatifs (Nextcloud) fin mai.

#### **3. Messagerie (Aetna)**
- **Migration académique** :
  - **Pilote en Corse** : Succès global (99% des comptes migrés sans incident), mais :
    - Problèmes sur les comptes **AGA/ASGA** (erreur de configuration).
    - **Boîte aux lettres** : 94 Go de données → risque de saturation.
  - **Leçons** :
    - Nécessité d’un **accompagnement renforcé** (usages locaux, habitudes de 20+ ans avec Convergence).
    - Exemples de résistances :
      - Utilisation des **FGRA** (adresses mail fonctionnelles) pour le tri des mails.
      - Export manuel des mails (format EML) → incompatible avec le webmail.
    - **Prochaines académies** (Nantes, Poitiers, Paca) : Déploiements en accélération (octobre 2024).
- **Thunderbird** :
  - **Plugin existant** pour les académies utilisant encore Thunderbird.
  - **Stratégie** : Inciter à migrer vers le **webmail** (meilleure compatibilité, automatisation des contacts).
  - **Question ouverte** : Faut-il fournir le plugin sur des postes non soutenus ?

#### **4. BigBlueButton (V2V)**
- **Version 3.0** :
  - **Livrée depuis un mois**, mais **fonctionnalités disparues** (ex : sous-titrage manuel, sélection aléatoire de participants).
  - **Réponses de l’éditeur** : Certaines fonctionnalités reléguées en **plugins** (ex : sélection aléatoire).
  - **Demandes du CNET** :
    - **Délégation de salles** (ex : secrétaire gère les réunions pour un responsable).
    - **Priorisation** : À discuter en interne (coût, faisabilité).
- **VisioAgent 1.3** :
  - **Fonctionnalités ajoutées** : Bandeau d’informations, gestion des favoris, tri alphabétique des salons.
  - **Prochaine étape** : 35 jours de développement validés (commande passée).

#### **5. Portail Apps**
- **Statistiques** :
  - **80 000 vidéos** hébergées, **221 000 comptes** ouverts (hors accès directs).
  - **73 000 comptes** actifs depuis décembre (1/3 des utilisateurs).
- **Améliorations** :
  - **Matomo** : Suivi des parcours utilisateurs (terminaux, origines).
  - **Raccourcisseur d’URL** : En développement (démonstration prévue fin juin).
  - **Cycle de vie des utilisateurs** : Architecture en **micro-applications** pour sécuriser les accès.

#### **6. Wi-Fi et bornes**
- **Questionnaire aux académies** (Île-de-France) : En attente des retours sur les usages et problèmes.

#### **7. Communication unifiée**
- **Déménagement à Gentilly** : Besoin d’un outil **privé ou libre** (ex : Cisco Webex vs. solutions libres comme BBB).
- **Enjeux** :
  - Intégration avec **CHAP** (téléphonie SIP) et **BigBlueButton**.
  - **Paul Fouad** travaille sur la compatibilité matériel (DVB, CHAP).

#### **8. Autres points**
- **Déploiements en cours** :
  - **Réseau de l’Aînés** : Recadrage avec l’UNISA pour des dates précises.
  - **Cine des Yéhouètes** : Réinstallation réussie (Mickaël/Benjamin), développements supplémentaires avec Renater.
- **Audit et conformité** :
  - **CPT** : Préparation d’une mise à jour pour éviter les interruptions.
  - **Conformité des postes** : Rencontre avec Cisco/Magenta pour évaluer les solutions.

---

## **3. Décisions prises**
| **Décision**                                                                 | **Responsable**               | **Échéance**               |
|-------------------------------------------------------------------------------|-------------------------------|----------------------------|
| **Report de la migration Nextcloud 31**                                      | Frédéric (Nuage)              | Mois prochain              |
| **Correction du bug de partage** (Nextcloud)                                 | Maxime Leherici (éditeur)     | À confirmer                |
| **Validation du chiffrage Tribu** et lancement des développements            | Simon (Tribu)                 | Cette semaine              |
| **Démonstration du raccourcisseur d’URL (Portail Apps)**                     | Hugo (Dijon)                  | Fin juin                   |
| **Recadrage des dates avec l’UNISA (Réseau de l’Aînés)**                     | Frédéric (DNE)                | Prochain point              |
| **Discussion interne sur la délégation de salles (V2V)**                      | Frédéric Cognès / Équipe V2V  | Avant la prochaine réunion |
| **Intégration de DBV dans Cap Education** (développement validé)              | Frédéric Cognès               | Début des travaux           |
| **Amélioration de la relation avec les éditeurs** (roadmaps réalistes)        | Didier (coordination)         | Prochaines réunions        |
| **Organisation d’un retour d’expérience Squash avec Tribu**                   | Simon                        | Comité suivant (Simon)     |
| **Comité des référents régionaux (mardi prochain)**                          | Didier                       | Distanciel                 |

---

## **4. Questions en suspens**
1. **Nextcloud 31** :
   - Quand le correctif pour les liens de partage sera-t-il disponible ?
   - Peut-on tester une version parallèle pour Global Scale ?
2. **Thunderbird** :
   - Faut-il fournir le plugin sur des postes non soutenus, ou privilégier le webmail ?
3. **Délégation de salles (V2V)** :
   - Comment prioriser les demandes du CNET (coût, faisabilité) ?
4. **Wi-Fi** :
   - Quand recevrons-nous les retours des académies sur le questionnaire ?
5. **Migration académique** :
   - Quels sont les **processus d’accompagnement** à mettre en place pour les prochains déploiements (Poitiers, Nantes) ?
6. **Communication unifiée** :
   - Quel outil choisir (Cisco, Webex, solution libre) et comment intégrer BBB/CHAP ?

---

## **5. Tâches à effectuer**
| **Tâche**                                                                     | **Responsable**               | **Priorité** | **Échéance**          |
|-------------------------------------------------------------------------------|-------------------------------|--------------|-----------------------|
| **Finaliser le chiffrage Tribu** et lancer les développements                  | Simon (Tribu)                 | Haute        | Cette semaine         |
| **Contacter les académies pour le retour sur le questionnaire Wi-Fi**         | Frédéric (Wi-Fi)               | Moyenne      | 1 semaine             |
| **Valider les devis pour la cyclonomie des comptes (Tube)**                   | Nicolas (Tube)                | Moyenne      | 2 semaines            |
| **Organiser un point avec Maxime Leherici (Nextcloud 31)**                    | Frédéric (Nuage)              | Haute        | Avant le 19 juin      |
| **Préparer les slides pour le comité des référents (mardi prochain)**        | Équipe projet                 | Haute        | 48h avant la réunion  |
| **Recadrer les dates avec l’UNISA (Réseau de l’Aînés)**                      | Frédéric (DNE)                | Moyenne      | Prochain point        |
| **Discuter avec l’éditeur V2V sur la délégation de salles**                  | Frédéric Cognès               | Moyenne      | Avant la réunion suivante |
| **Déployer la transcription des vidéos (Tube)**                             | Nicolas (Tube)                | Moyenne      | Juillet               |
| **Tester l’automatisation des déploiements (Tube)**                          | Équipe Tube                   | Moyenne      | Juillet               |
| **Mettre à jour les documents d’accompagnement pour la refonte Tribu**         | Simon (Tribu)                 | Moyenne      | Juin                  |

---

## **6. Prochaine rencontre**
- **Date** : [À préciser, probablement le mardi suivant pour le comité des référents].
- **Ordre du jour provisoire** :
  - Bilan du comité des référents (DRAZI/SGRAS).
  - Avancées sur les projets (Tribu, Nuage, V2V).
  - Suivi des questions en suspens (Nextcloud, Thunderbird, délégation de salles).
  - Préparation de la réunion de lancement pour l’**académie de France** (octobre 2024).

---
**Remarques générales** :
- **Thème récurrent** : La **précision des dates** et la **maîtrise des prestataires/éditeurs** sont des enjeux critiques.
- **Accompagnement des utilisateurs** : Nécessité de renforcer l’accompagnement au changement (ex : migration messagerie, refonte Tribu).
- **Coopération inter-académies** : Partage des bonnes pratiques (ex : retour d’expérience Corse pour les déploiements futurs).

**Prochaine étape** : Envoi des slides pour le comité des référents et point technique sur Nextcloud 31.
