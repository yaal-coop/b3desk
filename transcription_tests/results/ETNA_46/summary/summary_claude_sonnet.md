# Compte rendu de réunion — Point projet (46ème édition)

---

## Participants

- **Johan** (animateur)
- **Benoît**
- **Hugo**
- **Didier**
- **Simon**
- **Frédéric**
- **Nicolas**
- **Joanne**
- **Samir**
- **Aurélien**
- **Manon**
- **Olivier**
- **François**, **Sophie** (mentionnés)
- Participants à distance (non nommés)

---

## Sujets abordés

### 1. Actualités générales du programme

#### Comité de domaine (avec Audran)
- **Réduction budgétaire** sur l'ensemble de la DLE : un coup de rabot sur les projets est possible, mais devrait rester indolore selon les projets concernés.
- **Suivi des jalons** : Audran souhaite davantage de précision sur les dates de livraison et de mise en production des nouvelles fonctionnalités. Actuellement, les estimations sont trop vagues (« avant l'été », « T4 »). Il a besoin de visibilité à plusieurs mois pour communiquer en interne et avec des partenaires externes.
- Discussion sur la difficulté à s'engager sur des dates précises lorsque celles-ci dépendent d'éditeurs tiers (Collabora, Nextcloud, BigBlueButton/BBB), dont les roadmaps sont peu fiables ou peu communicantes.
- **Consensus** : il faut améliorer la relation avec les prestataires pour obtenir des engagements plus réalistes, et distinguer ce qui est financé en propre (plus d'exigence possible) de ce qui dépend des versions publiques des éditeurs.

#### Autres actualités
- **Renouvellement des licences IES Microsoft** effectué la semaine précédente, pour 30 000 agents.
- **Retour d'expérience Squash / Tribu** : à organiser avec Simon, probablement au prochain comité.
- **Comité des référents** (DRAZI / SGRAS) : prévu le mardi suivant, en distanciel. Des slides sont à préparer et à transmettre avant la réunion.

---

### 2. Projet Dotation (projet 4)

- Toujours en phase d'étude des volumétries.
- Point à planifier avec **Frédéric** pour recadrer le contexte du projet et réévaluer la liste des profils à doter.
- Positionnement à définir pour le comité référent.
- Mise à jour en cours côté CRT et Team (supportisation).
- Montée en compétences des équipes support académiques à venir : un point collectif est à organiser pour identifier les projets mûrs.

---

### 3. BNA (enquête)

- **Décalage d'un mois** de la campagne : du 16 mai au 27-28 juin, pour éviter un chevauchement avec une enquête de la DELCOM.
- Questionnaire finalisé, première communication prête, deux suivantes à intégrer.
- Anticipation du traitement des données à prévoir.

---

### 4. Communication unifiée

- Sujet émergent lié au déménagement du ministère à Gentilly (regroupement en un seul site).
- Question ouverte sur le choix d'un outil de softphone/téléphonie unifiée : Cisco/Webex, outils libres (ex. : solution déployée en Normandie), ou autre.
- Travaux en cours avec Paul Fouad sur l'intégration BBB + CHAP + SIP dans les salles de visioconférence, avec du matériel compatible.

---

### 5. Tribu

- Lancement du chantier de **refonte graphique (UX)** : chiffrage en cours avec les prestataires, en attente de validation finale.
- Découpage en **3 lots** :
  - Lot 1 (~80 jours) : accueil, tableaux de bord, dossiers
  - Lot 2 : outils et recherche
  - Lot 3 : administration
- Total estimé : **~200 jours**
- Objectif de **mise en production : fin novembre / début décembre 2025**, avec une quinzaine de jours de marge avant les congés de Noël.
- Première partie des specs livrée fin avril ; retours en cours.
- Préparation de plusieurs environnements (pré-prod iso-prod, dev refonte, recette).
- Montées de version techniques réalisées en parallèle.
- Mise à jour des tutoriels et documents prévue en même temps que la MEP.

---

### 6. Éducnat (messagerie / déploiement)

- **10 400 comptes migrés** ce matin.
- **Académie de Corse** : premier pilote en conditions réelles sur une académie entière.
  - 99 % des comptes migrés sans incident majeur.
  - Quelques difficultés sur des comptes spécifiques (ASGA, boîtes fonctionnelles volumineuses ~96 Go).
  - Bascule complète sur le webmail (abandon de Thunderbird), en one shot, avec une bande passante contrainte (~200 Mbps).
  - Enseignements : fort besoin d'accompagnement au changement, usages métiers très ancrés (délégation de boîtes, exports de mails, etc.).
- **Prochains déploiements** :
  - Nantes, Poitiers, PACA : reprise des déploiements pilotes.
  - Nantes envisage de migrer tous les établissements publics/privés (écoles, collèges) d'ici juin.
  - Académie de Reims : en cours.
  - Île-de-France : réunion de lancement prévue la semaine suivante, bascule prévue en octobre.
  - Réunion de 100 référents le lendemain pour valider le plan de déploiement global.
- **Usine d'import contacts/archives** : en cours de test par les utilisateurs corses.
- **Plugin Thunderbird** (InnoTools, livré en 2022) : travaux de mise en conformité avec les nouvelles méthodes d'authentification en cours avec Nicolas et le pôle identité.
- **Débat** : faut-il diffuser le plugin Thunderbird ou orienter vers le webmail uniquement ? Pas de décision tranchée.
- **Côté antispam** : travaux pour identifier les règles provoquant des latences ; dictionnaires académiques consolidés.

---

### 7. Nuage (Nextcloud)

- **Problème majeur sur la version 31** : régression fonctionnelle importante sur les liens de partage, introduite unilatéralement par Nextcloud. La mise à jour majeure est **reportée** jusqu'à correction par l'éditeur (suivi avec Maxime Leherici).
- La version 31 était un prérequis pour le déploiement de **Global Scale** en prod : ce déploiement est donc également bloqué.
- **Script de migration** (Nextcloud académique → Nuage centralisé) : correctif attendu sous peu (confirmé par Benoît). L'académie de Nantes attend ce correctif avant de lancer sa migration. L'équipe de Paris (pôle Socle, Irina) attend également le retour de Nantes.
- **Audit BDD** : augmentation de la RAM des serveurs PostgreSQL de 8 Go à 12 Go (recommandation initiale : 16 Go) via les ateliers Optimus Green. Les plantages quotidiens des services de métrologie ont cessé.
- Prochaine étape fin mai : restitution de 4 Go de RAM sur les frontaux applicatifs Nextcloud (à surveiller de près).

---

### 8. Visio Agent (BBB)

- **Intégration BBB dans CHAP** validée avec Frédéric Cognès : commande lancée. Les agents arrivant sur CHAP via un lien spécifique pourront accéder directement à BBB (VisioAgent).
- **POC Cine des Yéhouètes** (SIP Gateway) : réinstallation effectuée, fonctionne en collaboration avec Renater. Développements supplémentaires demandés (RCMP). Travaux sur la montée en charge de la Sydney Gateway (actuellement 3 salons/serveur max).
- **Visio Agent 1.3** mis en production : nouveau bandeau d'informations, tri alphabétique des salons, gestion des favoris.
- **Commande de 35 jours de développement** (Yann) validée ce matin par Valérie.
- **BBB 3.0** livré par Bite.network : recette effectuée par Nickel, quelques fonctionnalités manquantes (ex. : sous-titrage SME, sélection aléatoire passée en plugin). Mise en production envisagée prochainement.
- **Système de plugins BBB 3.0** : possibilité de faire développer des plugins par des prestataires tiers (ex. : sociétés françaises), indépendamment de l'éditeur.
- **Demande du CMED** : liste d'évolutions souhaitées (dont la délégation de salles), à arbitrer avec Frédéric selon ce qui est déjà en feuille de route ou non.

---

### 9. Portail Apps

- **221 000 comptes** ouverts (hors comptes créés directement sur les applications).
- **73 000 comptes** reconnectés depuis décembre (soit ~1/3 en 5 mois).
- **Matomo** installé sur le portail depuis 3 semaines : premières statistiques exploitables à venir.
- **Portail 6.4.1** mis en production (cycle de vie des utilisateurs, autres améliorations).
- **Raccourcisseur d'URL** : deux développeurs travaillent dessus depuis Dijon, échange positif avec Hugo. Livraison espérée avant l'été. Outil disponible en API pour d'autres services (QR code inclus).
- **Architecture cycle de vie** : déploiement de micro-applications par service, sécurisées par token.
- **Rancher pré-prod** : livré depuis 2 semaines, toujours non fonctionnel (problèmes de certificats, documentation insuffisante, répartition des responsabilités à clarifier).

---

### 10. Tube (PeerTube)

- **Thème graphique** : la version 7.1.1 (déployée en urgence pour faille de sécurité) ne supporte plus le thème graphique précédent. Toutes les instances ont actuellement la même apparence.
- Travaux en cours (Hugo, Manon, Drâle du Grand Est) pour une nouvelle approche : masquer les instances et ne parler que de **thématiques**. Résultat attendu à la rentrée prochaine (~3-4 mois).
- **Transcription des vidéos** : opérationnelle en environnement de test. Déploiement à généraliser avec Nicolas (2 serveurs dédiés).
- Projet de **transcodage externalisé** sur 2 machines dédiées pour alléger les serveurs tubes.
- **Cycle de vie des comptes et vidéos** : descriptif prêt, devis en attente. Développements partagés entre Framasoft (cœur PeerTube : durée de vie des vidéos) et un plugin spécifique (ex. : présence de mineurs → suppression à 1 an).
- **Déploiement de l'asset 1.1** (failles de sécurité) : en priorité.
- ~**80 000 vidéos** sur Pod Éducation Nationale.

---

### 11. Bornes Wi-Fi

- Questionnaire envoyé aux académies d'Île-de-France pour recueillir les retours sur les usages et problèmes de connectivité.
- En attente de réponses. Pas d'autre avancée.

---

### 12. Portail intranet académique

- Refonte du portail intranet académique : tentative d'impliquer une académie la semaine suivante.
- Projet identifié comme **porte d'entrée de tous les services** du programme.

---

### 13. GSR Bordeaux (début juin)

- Présence confirmée : Johan, Benoît, Nicolas, François, Sophie, Frédéric.
- Point à rappeler : **Aetna n'est pas uniquement la messagerie** — message à réitérer auprès des académies.

---

## Décisions prises

| Décision | Détail |
|---|---|
| Décalage de la campagne BNA | Reportée du 16 mai au 27-28 juin |
| Report de la mise à jour Nextcloud 31 | En attente d'un correctif éditeur sur les liens de partage |
| Intégration BBB dans CHAP | Commande validée, développement lancé |
| Commande de 35 jours de dev Visio Agent | Validée ce matin |
| Augmentation RAM serveurs BDD Nuage | Passée de 8 Go à 12 Go |
| Mise en prod BBB 3.0 | Envisagée prochainement après vérification des fonctionnalités manquantes |

---

## Questions en suspens

- Montant exact de la réduction budgétaire sur le programme (en attente de confirmation).
- Correction par Nextcloud de la régression sur les liens de partage (version 31).
- Choix de l'outil de communication unifiée (Cisco/Webex vs. solution libre).
- Diffusion ou non du plugin Thunderbird pour les académies.
- Arbitrage sur les demandes d'évolution du CMED pour Visio Agent (délégation de salles, etc.).
- Fonctionnement du Rancher en pré-prod (certificats, documentation, responsabilités).
- Passage en mode INSAS (plus de nouvelles depuis février-mars).
- Marché sur lequel positionner les développements cycle de vie PeerTube.

---

## Tâches à effectuer

| Tâche | Responsable |
|---|---|
| Confirmer les montants de réduction budgétaire sur le programme | Johan |
| Organiser un REX Squash/Tribu (prochain comité) | Simon |
| Préparer les slides pour le comité des référents (mardi suivant) | Équipe (tous) |
| Planifier un point avec Frédéric sur le projet Dotation | À définir |
| Organiser un point collectif sur la maturité des projets pour la formation des équipes support | Johan / équipe |
| Intégrer les 2 dernières communications BNA et anticiper le traitement des données | À définir |
| Contacter le support Omnisa (ticket déploiement d'applications) | Joanne / Samir |
| Recontacter le responsable UNISA pour recaler un point réseau | À définir |
| Suivre la correction Nextcloud 31 avec Maxime Leherici | Frédéric / Benoît |
| Planifier la restitution de 4 Go RAM sur les frontaux Nextcloud (fin mai) | Frédéric / CRTH |
| Déployer la transcription vidéo sur tous les serveurs Tube | Benoît / Nicolas |
| Déployer l'asset PeerTube 1.1 (sécurité) | Benoît / Nicolas |
| Obtenir les devis pour le cycle de vie des vidéos PeerTube et identifier le marché | Benoît |
| Faire un point sur l'avancement de l'automatisation des déploiements Tube | Benoît |
|
