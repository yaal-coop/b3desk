# Compte rendu de réunion

## Participants
- Didier
- Hugo
- Benoît
- Simon
- Frédéric
- Nicolas
- Joanne
- Samir
- Aurélien
- Manon
- Olivier
- Johan
- Sophie
- François
- Audran (mentionné, comité de domaine)

---

## Objet de la réunion
Point projet quinzinal portant sur l'avancement de l'ensemble des projets du programme (Tribu, Nuage, Visio Agent / BBB, Tube, portail Apps, messagerie, dotation, bornes Wi-Fi, communication unifiée).

---

## Sujets abordés

### Comité de domaine (avec Audran)
- Réduction budgétaire annoncée sur l'ensemble de la DLE ; impact sur le programme en attente de confirmation des montants.
- Demande de suivi plus précis des jalons et des dates de mise en production : Audran souhaite disposer d'une meilleure visibilité sur les livraisons à venir, notamment pour communiquer auprès d'autres directions et instances.
- Constat partagé : les décalages fréquents des éditeurs rendent difficile la communication de dates fiables. Un travail de fond est identifié pour obtenir des engagements plus réalistes de la part des prestataires.

### Renouvellement des licences Microsoft
- Renouvellement des licences IES Microsoft réalisé la semaine précédente, pour l'ensemble des agents disposant d'un poste standard.

### Dotation (projet 4)
- Toujours en phase d'étude des volumétries.
- Prévu : point avec Frédéric pour remettre le contexte du projet, réévaluer la liste des profils à doter et préparer le positionnement pour le comité référent.
- Mise à jour en cours côté CRT et team pour le support.
- Des projets commencent à être travaillés sur l'accompagnement et la formation des équipes support en académie.

### BNA (enquête)
- Décalage d'un mois de la campagne, du fait d'une autre enquête menée par la DELCOM sur la même période.
- Nouveau créneau : du 16 au 27 ou 28 juin.
- Questionnaire finalisé, première communication prête, deux suivantes à intégrer ; anticipation du traitement des données à prévoir.

### Communication unifiée
- Sujet en cours lié notamment au déménagement du ministère à Gentilly.
- Réflexion en cours sur le choix entre outils propriétaires (Cisco/Webex) et outils libres pour la téléphonie et la visioconférence.
- Travaux en cours avec Paul Fouad sur l'intégration BBB dans les salles de vidéo via SIP, et sur la compatibilité du matériel.

### Tribu
- Lancement du chantier de refonte graphique (UX).
- Chiffrage en cours avec les prestataires ; découpage en 3 lots :
  - Lot 1 : accueils, tableaux de bord, dossiers (~80 jours)
  - Lot 2 : outils et recherche
  - Lot 3 : administration
- Total estimé : environ 200 jours.
- Première partie des spécifications livrée fin avril.
- Mise en production visée : fin novembre / début décembre 2025, avec une quinzaine de jours de marge avant les congés de Noël.
- Préparation de plusieurs environnements en parallèle : pré-prod isoprod, dev refonte graphique, qualité.
- Montées de versions techniques réalisées pour préparer la charge.
- Mise à jour des tutoriels et documents prévue en parallèle de la mise en production.

### Nuage (Nextcloud)
- Version en production : Nextcloud 30. La version 31 est disponible mais ne peut pas être déployée en l'état.
- Régression fonctionnelle majeure introduite unilatéralement par l'éditeur dans la version 31 sur la gestion des liens de partage de fichiers.
- Conséquence : impossibilité de déployer Global Scale (dont le prérequis est Nextcloud 31).
- Contact à prendre avec le support éditeur (Maxime Leherici) pour obtenir un correctif rétablissant les fonctionnalités de partage.
- Toujours en attente du correctif sur le script de migration (Nextcloud académique vers Nuage centralisé) suite aux retours de l'équipe de Nantes.
- L'équipe de Paris (pôle Socle, Irina) attend le retour de Nantes avant d'envisager sa propre migration académique.
- Augmentation de la RAM des serveurs PostgreSQL réalisée : passage de 8 Go à 12 Go via les ateliers Optimus Green. Les plantages récurrents des services de métrologie ont cessé.
- Prévu fin mai : restitution de 4 Go de RAM sur les frontaux applicatifs Nextcloud, avec surveillance renforcée.

### Visio Agent / BBB
- Intégration de BBB dans Cap Éducation validée avec Frédéric Cognès ; commande lancée.
- POC de la passerelle SIP (Janus Gateway) remis en place par Benjamin et Mickaël, en collaboration avec Renater. Fonctionne correctement.
- Développements supplémentaires demandés à Renater : intégration RCMP et montée en charge de la passerelle SIP.
- Visio Agent 1.3 mis en production : nouveau bandeau d'informations, gestion des favoris sur les salons, tri alphabétique et par ordre de création.
- Commande de 35 jours de développement validée ce matin (par Valérie) pour reprendre les travaux avec le développeur Yann.
- BBB 3.0 livré par Bitesite Network ; recette réalisée par Nicolas. Quelques fonctionnalités manquantes remontées à l'éditeur (ex. : sous-titrage SME, sélection aléatoire d'un participant désormais en plugin). Mise en production de la 3.0 envisagée prochainement.
- Nouveau système de plugins dans BBB 3.0 : possibilité de faire développer des fonctionnalités spécifiques par des prestataires tiers.
- Demande d'évolutions reçue du CMED (ex. : délégation de salles) ; traitement à discuter en interne avec Frédéric.

### Portail Apps
- Plus de 221 000 comptes ouverts sur le portail (hors comptes créés directement sur les applications).
- 73 000 comptes reconnectés depuis décembre.
- Matomo installé sur le portail depuis environ trois semaines ; premières statistiques en cours de consolidation.
- Portail mis à jour en version 6.4.1.
- Travaux sur le raccourcisseur d'URL en cours avec deux développeurs à Dijon ; démonstration espérée la semaine prochaine, déploiement visé avant l'été.
- Avancement sur l'architecture du cycle de vie des utilisateurs (micro-applications par service).
- Rancher de pré-prod livré mais toujours non fonctionnel pour le déploiement des applications ; avancement lent.

### Tube (PeerTube)
- Thème graphique non supporté depuis la mise à jour forcée en version 7.1.1 (faille de sécurité). Toutes les instances ont la même apparence.
- Travaux de refonte du thème en cours (avec la DRAJE Grand Est, Hugo, Manon) ; nouvelle approche centrée sur les thématiques plutôt que les instances. Résultat attendu à la rentrée prochaine.
- Transcription des vidéos opérationnelle en environnement de test ; déploiement à généraliser (un deuxième serveur à préparer).
- Déploiement de la mise à jour de sécurité (asset 1.1) en priorité.
- Travaux sur le cycle de vie des comptes et vidéos : descriptif finalisé, en attente de devis et identification du marché. Développements partagés entre Framasoft (fonctionnalités génériques) et un plugin spécifique au ministère.

### Messagerie (Aetna)
- Premier déploiement pilote en conditions réelles : Académie de Corse, basculement complet sur le webmail (abandon de Thunderbird).
- Bilan : 99 % des comptes migrés sans difficulté majeure ; quelques problèmes sur des comptes spécifiques (boîte fonctionnelle de l'ASGA, boîte de 96 Go).
- Enseignements : importance de l'accompagnement au changement, des usages métiers spécifiques (délégation de boîte, exports de mails, règles de tri), et de la proximité avec les VIP et les équipes locales.
- Déploiements à venir : Nantes, Poitiers, PACA, Académie de Reims (établissements du premier degré en cours), Île-de-France (lancement prévu en octobre).
- Réunion de 100 référents prévue le lendemain pour valider le plan de déploiement.
- Réunion de lancement avec Île-de-France prévue la semaine suivante.
- Usine d'import des contacts et archives en cours de test par les utilisateurs de Corse.
- Côté Francis (antispam) : latences en cours d'investigation ; travaux sur les règles de détection dans les corps de messages.
- Question ouverte sur la pertinence de diffuser le plugin Thunderbird ou de concentrer les efforts sur le webmail.

### Bornes Wi-Fi
- Questionnaire envoyé aux académies d'Île-de-France pour recueillir les retours sur les usages et problèmes de connectivité. En attente de réponses.

### Portail intranet académique
- Refonte du portail intranet académique à l'étude ; tentative d'impliquer une académie la semaine suivante.

---

## Décisions prises
- Décalage de la campagne BNA du fait d'un conflit de calendrier avec une enquête DELCOM ; nouveau créneau : 16 au 27 ou 28 juin.
- Intégration de BBB dans Cap Éducation validée ; commande lancée.
- La mise à jour vers Nextcloud 31 est différée dans l'attente d'un correctif de l'éditeur sur les liens de partage.
- La mise en production de BBB 3.0 est envisagée prochainement, sous réserve de vérification des fonctionnalités manquantes.
- Commande de 35 jours de développement pour Visio Agent validée ce matin.
- RAM des serveurs PostgreSQL de Nuage augmentée de 8 Go à 12 Go.

---

## Questions en suspens
- Montants précis de la réduction budgétaire sur le programme : en attente de confirmation.
- Correctif Nextcloud 31 sur les liens de partage : en attente de livraison par l'éditeur.
- Correctif du script de migration Nuage : en attente de livraison par Benoît.
- Passage en mode INSAS : plus de nouvelles depuis l'annonce de fin février / début mars.
- Prérequis d'installation fournis par Omnisa : toujours sans réponse.
- Retours des académies d'Île-de-France sur le questionnaire bornes Wi-Fi : en attente.
- Traitement de la demande d'évolutions du CMED sur Visio Agent (dont la délégation de salles) : à discuter en interne avec Frédéric.
- Pertinence de diffuser le plugin Thunderbird ou de concentrer les efforts sur le webmail : question ouverte.
- Implication d'une académie dans la refonte du portail intranet : à confirmer la semaine suivante.

---

## Tâches à effectuer

| Tâche | Responsable |
|---|---|
| Obtenir la confirmation des montants de réduction budgétaire sur le programme | Non précisé |
| Organiser un retour d'expérience Squash avec Tribu | Simon |
| Préparer les slides pour le comité référents (réunion la semaine suivante) | Équipe (slides à envoyer dans les prochains jours) |
| Faire un point avec Frédéric pour remettre le contexte du projet dotation et réévaluer la liste des profils | Non précisé |
| Faire un point collectif sur la maturité des projets vis-à-vis de la formation des équipes support en académie | Ensemble de l'équipe |
| Intégrer les deux communications suivantes pour la campagne BNA et anticiper le traitement des données | Non précisé |
| Contacter le support éditeur Nextcloud (Maxime Leherici) pour obtenir un correctif sur les liens de partage de la version 31 | Frédéric / Benoît |
| Planifier avec le CRTH la restitution de 4 Go de RAM sur les frontaux Nextcloud (fin mai) et surveiller la stabilité | Frédéric |
| Répondre au ticket support Omnisa (déploiement d'applications, tâche planifiée défaillante) | Joanne / Samir |
| Recontacter le responsable INSAS pour recaler un point et obtenir des dates | Non précisé |
| Déployer la transcription vidéo sur les serveurs Tube (préparer un deuxième serveur, paramétrer tous les serveurs) | Nicolas / Benoît |
| Déployer la mise à jour de sécurité asset 1.1 sur Tube | Non précisé |
| Finaliser les devis et identifier le marché pour les développements cycle de vie des comptes/vidéos sur Tube | Non précisé |
| Faire un point sur l'avancement de l'automatisation des déploiements Tube | Benoît |
| Faire une démonstration du raccourcisseur d'URL la semaine prochaine | Hugo / développeurs |
| Faire un point avec Benoît sur les interactions avec Maxime (support Nextcloud) lors de la réunion de support | Frédéric / Benoît |
| Discuter en interne avec Frédéric du traitement de la demande d'évolutions du CMED sur Visio Agent | Benoît / Frédéric |
| Rappeler au GSR qu'Aetna ne se limite pas à la messagerie | Johan / équipe présente au GSR |
| Travailler avec Nicolas et le pôle identité sur la compatibilité du plugin Thunderbird avec l'authentification actuelle | Nicolas / Olivier |
| Tenter d'impliquer une académie dans la refonte du portail intranet la semaine suivante | Non précisé |

---

## Prochaine rencontre
- **Comité référents** : mardi suivant la réunion, en distanciel.
- **Réunion de lancement Île-de-France** : la semaine suivante.
- **Réunion des 100 référents** (validation du plan de déploiement) : le lendemain de la réunion.
- **GSR à Bordeaux** : début juin (Johan, Benoît, Nicolas, François, Sophie, Frédéric).
