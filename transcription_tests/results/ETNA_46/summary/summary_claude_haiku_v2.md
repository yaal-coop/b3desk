# Compte rendu de réunion - 46ème réunion du programme

## Participants

- Didier, Hugo, Benoît, Nicolas, Frédéric, Simon, Johan, Olivier, Samir, Aurélien, Benjamin, Mickaël, Yann, Manon, et autres membres de l'équipe

## Objet de la réunion

Point projet sur l'avancement des différents projets du programme (Tribu, Nuage, Visio Agent, Tube, Aetna, etc.)

## Sujets abordés

### Comité de domaine et enjeux transversaux

**Réduction budgétaire**
- Réduction du budget sur toute la DLE annoncée
- Confirmations des montants attendues pour le programme
- Possibilité de « coups de rabot » sur les produits

**Précision des jalons de livraison**
- Enjeu majeur : améliorer la précision des dates de livraison des nouvelles fonctionnalités
- Actuellement : soit dates imprécises, soit ordres d'idées (avant/après l'été)
- Besoin de meilleure visibilité pour la direction et les communications externes
- Sujet de fond : maîtriser les plannings avec les prestataires et éditeurs
- Différences selon les éditeurs : Collaborat (zéro vision), BigBlueButton (vision décalée), Nextcloud (plus clair)

**Gestion des relations avec les éditeurs**
- Décalages fréquents entre les promesses et les livraisons
- Nécessité d'améliorer les engagements réalistes des éditeurs
- Distinction à faire entre développements financés et versions publiques

### Projet Tribu

**Refonte graphique UX8**
- Lancement du chantier de refonte ergonomique
- Chiffrage en cours avec les prestataires
- Découpage en 3 lots :
  - Lot 1 : accueils, tableaux de bord, dossiers (~80 jours)
  - Lot 2 : outils et recherche
  - Lot 3 : administration
- Total : environ 200 jours
- Spécifications livrées fin avril, retours en cours
- Mise en production prévue fin 2025 (fin novembre/début décembre)
- Environnements de pré-prod en préparation
- Montées de versions techniques effectuées
- Mise en production en transparence (pas de maintenance longue)
- Mise à jour des tutoriels et documents prévue

### Projet Nuage (Nextcloud)

**Problème critique version 31**
- Grosse modification des liens de partage introduite unilatéralement par l'éditeur
- Liens internes retrouvés dans les liens externes
- Mise à jour majeure prévue le 15 juin reportée
- Impossible de déployer en production en l'état
- Prérequis pour Global Scale : version 31 obligatoire
- Nécessité de travailler avec le support éditeur pour une version parallèle compatible

**Migration académique**
- Attente du correctif du script de migration (Nantes pilote)
- Équipe de Paris en attente du retour de Nantes avant de commencer
- Préférence pour différer plutôt que de se lancer immédiatement

**Infrastructure**
- Augmentation de RAM réussie via ateliers Optimus Green : passage de 8 Go à 12 Go sur serveurs BDD
- Résolution des plantages récurrents des services de métrologie
- Prévision : augmentation de 4 Go sur frontaux applicatifs fin mai

### Projet Aetna (Messagerie)

**Déploiement Corse**
- Premier pilote en conditions réelles (académie complète)
- 99% de consommation de musée
- Passage complet à WebMate (fin de Thunderbird)
- Déploiement en one shot avec débit limité (200 Mbps)
- Quelques difficultés : comptes AGA/ASGA, boîtes à lettres volumineuses (94-96 Go)
- Bilan positif globalement, apprentissages importants

**Accompagnement du changement**
- Enjeu majeur : usages différents après 20-25 ans de Convergence
- Cas métiers identifiés : exports de mails, boîtes fonctionnelles (FGRA), etc.
- Nécessité d'améliorer l'accompagnement du terrain
- Sujet transversal à tous les projets (Nuage, Tribu, Visio Agent)

**Déploiements suivants**
- Nantes : libération de tous les établissements publics/privés d'ici juin
- Poitiers, Paca : reprise des déploiements
- Reims : réunion début juin
- Accélération prévue sur T3 et T4 2024
- Réunion de 100 des référents demain pour valider le plan de déploiement
- Réunion de lancement Île-de-France (basculement octobre)

**Usine d'apport**
- Tests en cours avec utilisateurs corses migrés
- Contacts et archives en collection

**Difficultés techniques**
- Latences résolues (allègement des détections dans les corps de messages)
- Dictionnaires académiques consolidés (peut causer latence)
- Thunderbird : plugin en cours de mise à jour pour compatibilité

### Projet Visio Agent

**Intégration BigBlueButton dans CHAP**
- Commande validée avec Frédéric Cognès
- Lien particulier permettant d'ajouter BBB dans CHAP
- Bouton de rejointe de réunion pour participants

**Cine des Yéhouètes (POC)**
- Réinstallation complète effectuée
- Collaboration avec Renater
- Développements supplémentaires demandés (RCMP)
- Enjeu : montée en charge de la Sydney Gateway (actuellement 3 salons par serveur)
- Objectif : démonstrateur pour Eugran

**Visio Agent 1.3**
- Frontal mis à jour
- Nouveau bandeau d'informations
- Gestion des favoris sur salons
- Tri alphabétique et par création
- Commande de 35 jours de développement validée ce matin

**BigBlueButton 3.0**
- Livré il y a plus d'un mois par Bitesite Network
- Recette validée
- Quelques fonctionnalités disparues (sous-titrage SME notamment)
- Système de plugins introduit
- Demande du CMED : délégation de salles (complexe à mettre en œuvre)
- Prochaine mise en production : date à définir après livraison éditeur

### Portail Apps

**Statistiques**
- 221 000 comptes ouverts
- 73 000 comptes reconnectés depuis décembre (1/3 des utilisateurs)
- Presque 80 000 vidéos
- Matomo installé depuis 3 semaines

**Portail 6.4.1**
- Mise en production effectuée
- Cycle de vie des utilisateurs amélioré

**Raccourcisseur d'URL**
- Deux développeurs travaillent dessus à Dijon
- Échanges productifs avec Hugo
- Démonstration prévue la semaine prochaine
- Déploiement avant l'été
- Outil en API disponible pour autres services

**Cycle de vie des comptes et vidéos**
- Architecture en micro-applications par service
- Chaque service responsable de ses actions (suppression, transfert, etc.)
- Déploiement de Rancher en pré-prod : toujours non fonctionnel
- Certificats et déploiement d'outils : sujets à clarifier
- Progression lente mais en cours

### Projet Tube (PeerTube)

**Thématisation**
- Thème préparé par Drame du Grand Est il y a 3 ans non supporté en 7.1.1
- Réunion productive avec Drame du Grand Est, Hugo, Manon
- Nouvelle approche : masquer les instances, parler de thématiques
- Implémentation prévue après la rentrée (3-4 mois)
- Message temporaire : « Le thème a disparu mais il reviendra bientôt »

**Transcription**
- Opérationnelle sur test
- Généralisation prévue après passage en 7
- Déploiement de serveur supplémentaire nécessaire
- Paramétrisation de tous les serveurs tubes

**Transcodage externalisé**
- Objectif : diminuer la puissance des machines tubes
- Deux grosses machines dédiées au transcodage et transcription
- Déploiement en priorité

**Cycle de vie des vidéos**
- Attente de devis du développeur
- Partie générique (durée de vie des vidéos) : chez Pramasoft (cœur PeerTube)
- Partie spécifique (mineurs, description après 1 an) : plugin
- Descriptif finalisé, en attente de gestion des devis et marché

**Automatisation des déploiements**
- Attente du grand test
- Avancées récentes sur automatisation des mises à jour

### Autres sujets

**Renouvellement licences Microsoft**
- Effectué la semaine précédente
- Concerne 30 000 agents

**Dotation**
- Étude des volumiers en cours
- Point prévu avec Frédéric pour réévaluer la liste des profils
- Mise à jour CRT et team en cours
- Montée en compétences des académies sur les projets

**BNA (Enquête)**
- Décalage d'un mois : du 16 au 27-28 juin
- Raison : éviter déclouement avec enquête DELCOM
- Questionnaire finalisé
- Première communication prête
- Intégration des deux communications suivantes en cours

**Communication unifiée**
- Sujet lié au déménagement ministériel à Gentilly
- Choix à faire : Cisco/Webex vs outils libres
- Enjeu : téléphonie unifiée (SIP, chat, vidéo)
- Travaux en cours avec Paul Fouad sur intégration BBB dans salles vidéo
- Objectif : matériel tout intégré (BBB, CHAP, SIP)

**Bornes Wi-Fi**
- Questionnaire envoyé aux académies Île-de-France
- Attente des retours sur usages et problèmes

**Portail intranet académique**
- Refonte en cours
- Implication d'académies prévue la semaine prochaine
- Porte d'entrée de tous les services

## Décisions prises

- Mise à jour de Nextcloud 31 reportée (attente du correctif des liens de partage)
- Commande Visio Agent 1.3 validée (35 jours de développement)
- Intégration BBB dans CHAP validée
- Décalage BNA d'un mois (16 au 27-28 juin)
- Passage en RAM 12 Go sur serveurs BDD approuvé
- Augmentation RAM 4 Go sur frontaux applicatifs prévue fin mai

## Questions en suspens

- Date précise de mise en production Tribu (fin novembre/début décembre à confirmer)
- Résolution du problème de liens de partage Nextcloud 31
- Compatibilité Global Scale avec version Nextcloud corrigée
- Statut du passage en mode INSAS (mentionné comme fin février/début mars, plus de nouvelles)
- Prérequis d'installation UNISA (Kubernetes, Kafka, Terraform, etc.)
- Stratégie Thunderbird : maintien du plugin ou passage exclusif WebMate ?
- Financement et priorisation des demandes CMED pour BBB

## Tâches à effectuer

| Tâche | Responsable | Délai |
|-------|-------------|-------|
| Fournir date précise MEP Tribu | Simon | Après validation chiffrage |
| Tester et corriger version Nextcloud 31 | Frédéric/Maxime | Avant 15 juin |
| Mettre à jour slides pour comité référent | Équipe | Prochains jours |
| Point avec Frédéric sur dotation et profils | Frédéric | Avant comité référent |
| Montée en compétences équipes support académies | Équipe | En cours |
| Intégrer communications BNA | Équipe | Avant 27-28 juin |
| Recontacter responsable UNISA | Olivier | Rapidement |
| Finaliser chiffrage Tribu | Prestataires/Simon | Cette semaine |
| Préparer démonstration raccourcisseur URL | Hugo/Devs | Semaine prochaine |
| Valider plan de déploiement Aetna | Équipe | Demain (réunion 100 référents) |
| Surveiller RAM frontaux applicatifs | Frédéric | Fin mai |
| Travailler compatibilité Thunderbird | Nicolas/Pôle identité | En cours |
| Préparer présentation GSA Bordeaux | Équipe | Début juin |
| Implication académies portail intranet | Équipe | Semaine prochaine |

## Prochaine rencontre

- **Comité référents** : mardi prochain (en distanciel)
- **Réunion 100 référents** : demain (validation plan déploiement Aetna)
- **Réunion lancement Île-de-France** : semaine prochaine
- **GSA Bordeaux** : début juin
- **Prochaine réunion projet** : date non précisée dans la transcription
