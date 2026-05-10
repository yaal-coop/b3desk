# Compte rendu de réunion — Point projet (46ème édition)

---

## Participants mentionnés

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
- **Audran** (comité de domaine, non présent)
- **Yann / Yal** (développeur externe)
- **Maxime Leherici** (support éditeur Nextcloud)
- **Paul Fouad** (travaux SIP/vidéo)
- **Irina** (pôle Paris, équipe Socle)

---

## Objet de la réunion

Point projet quinzomadaire couvrant l'ensemble des projets du programme : Tribu, Nuage, Visio Agent / BBB, Portail Apps, Tube, messagerie (déploiement académique), dotation, bornes Wi-Fi et communication unifiée.

---

## Sujets abordés

### 1. Comité de domaine (avec Audran)

- **Réduction budgétaire** sur l'ensemble de la DLE : un coup de rabot sur les projets du programme est possible. Les montants précis sont en attente de confirmation.
- **Suivi des jalons** : Audran souhaite davantage de précision sur les dates de livraison et de mise en production des nouvelles fonctionnalités. Actuellement, les estimations sont trop vagues (« avant l'été », « T4 »), voire sujettes à des reports répétés.
  - Problème structurel identifié : dépendance aux éditeurs (Collabora, Nextcloud, BBB/Bitesite Network) dont les roadmaps sont peu fiables ou peu communicées.
  - Distinction faite entre les développements financés en propre (sur lesquels on peut être plus exigeant) et les versions publiques des éditeurs (sur lesquelles la maîtrise est limitée).
  - Piste évoquée : améliorer la relation contractuelle avec les prestataires pour obtenir des engagements plus réalistes et stables.

### 2. Renouvellement des licences Microsoft

- Renouvellement des licences IES Microsoft effectué la semaine précédente, pour l'ensemble des agents (environ 30 000 postes).

### 3. Prochains jalons

- **Retour d'expérience Squash / Tribu** : à organiser avec Simon, probablement au prochain comité.
- **Comité des référents** (DRAZI / SGRAS) : prévu **mardi prochain**, en distanciel. Des slides sont à préparer et à transmettre en amont.

### 4. Dotation (projet 4)

- Toujours en phase d'étude des volumétries.
- Point à organiser avec **Frédéric** pour remettre le contexte du projet et réévaluer la liste des profils à doter.
- Positionnement à définir pour le comité référent.
- Mise à jour en cours côté CRT et teams.
- Formation des équipes support académiques à planifier : un point collectif est à organiser pour identifier les projets mûrs.

### 5. BNA (enquête)

- Décalage d'un mois de la campagne : lancement repoussé **du 16 au 27-28 juin**, pour éviter un chevauchement avec une enquête DELCOM.
- Questionnaire finalisé, première communication prête, deux suivantes à intégrer.
- Anticipation du traitement des données à démarrer.

### 6. Communication unifiée

- Sujet en cours, lié notamment au déménagement du ministère à Gentilly (regroupement sur un seul site).
- Enjeux autour du soft-phone : Cisco/Webex vs outils libres.
- Travaux en cours avec Paul Fouad sur l'intégration BBB + SIP dans les salles de vidéoconférence (matériel compatible, tests en cours).
- Bruno à inviter pour présenter les enjeux lors d'un prochain point.

### 7. Tribu

- Lancement du chantier de **refonte graphique (UX)** : chiffrage en cours avec les prestataires, en finalisation cette semaine.
- Découpage en **3 lots** :
  - Lot 1 : accueil, tableaux de bord, dossiers (~80 jours)
  - Lot 2 : outils et recherche
  - Lot 3 : administration
- Total estimé : **~200 jours**
- Première partie des specs livrée fin avril, retours en cours.
- Objectif de mise en production : **fin novembre / début décembre 2025**, avec une quinzaine de jours de marge avant les congés de Noël.
- Préparation de plusieurs environnements parallèles (iso-prod, dev refonte, qualité).
- Montées de versions techniques réalisées en parallèle pour assurer la stabilité.
- Mise à jour des tutoriels et documents prévue en même temps que la MEP.

### 8. Nuage (Nextcloud)

- **Régression fonctionnelle majeure dans la version 31** : les liens de partage ont été entièrement refondus par l'éditeur sans information préalable suffisante. La mise à jour vers la v31 est **suspendue** jusqu'à correction par Nextcloud (interlocuteur : Maxime Leherici).
- La v31 était un prérequis pour le déploiement de **Global Scale** en prod, ce qui bloque également ce chantier.
- **Migration Nextcloud académique → Nuage** : en attente d'un correctif sur le script de migration (annoncé prochainement par Benoît). L'académie de Paris (Irina) attend le retour de Nantes avant d'envisager sa propre migration.
- **Audit BDD** : augmentation de la RAM des serveurs Postgres de 8 Go à 12 Go (via ateliers Optimus Green). Les plantages quotidiens des services de métrologie ont cessé.
- Prochaine étape : restitution de 4 Go de RAM sur les frontaux applicatifs Nextcloud, prévue fin mai, avec surveillance renforcée.

### 9. Visio Agent / BBB

- **Intégration BBB dans CHAP (Cap Éducation)** : commande validée avec Frédéric Cognès, développement à démarrer avec l'éditeur.
- **POC Cinéma des Yéhouètes** (SIP Gateway) : réinstallation effectuée par Benjamin et Mickaël, fonctionne en collaboration avec Renater. Développements supplémentaires demandés (RCMP, montée en charge de la Sydney Gateway).
- **Visio Agent v1.3** : mis en production. Nouveautés : bandeau d'information, tri alphabétique et par date de création des salons, gestion des favoris.
- **Commande de 35 jours de développement** avec Yann : validée ce matin, les travaux vont reprendre.
- **BBB v3.0** : livrée par Bitesite Network. Recette effectuée par Nickel. Quelques fonctionnalités disparues (ex. : sous-titrage SME, sélection aléatoire passée en plugin). Mise en production envisagée prochainement, sous réserve de vérifications finales.
- **Système de plugins BBB** : nouvelle architecture permettant de faire développer des fonctionnalités spécifiques par des tiers (ex. : boîtes françaises), indépendamment de l'éditeur.
- **Demande du CNED** : liste d'évolutions souhaitées sur le frontal (dont la délégation de salles, sujet complexe). À discuter en interne avec Frédéric pour priorisation et financement.

### 10. Portail Apps

- **221 000 comptes** ouverts sur le portail (hors comptes créés directement sur les applications).
- **73 000 comptes** reconnectés depuis décembre (soit environ un tiers).
- **Matomo** installé sur le portail depuis ~3 semaines : premières statistiques exploitables à venir.
- **Portail v6.4.1** mis en production (cycle de vie des utilisateurs, divers correctifs).
- **Raccourcisseur d'URL** : deux développeurs travaillent dessus depuis Dijon (échange avec Hugo). Démonstration espérée la semaine prochaine, mise en production avant l'été. L'outil sera disponible en API pour d'autres services (QR code inclus).
- **Architecture cycle de vie** : avancement sur le déploiement de micro-applications par service (sécurisées par token).
- **Rancher pré-prod** : livré depuis plus de deux semaines, toujours non fonctionnel pour le déploiement des applications (problèmes de certificats, documentation incomplète, découvertes progressives).

### 11. Tube (PeerTube)

- **Thème graphique** : la v7.1.1 (déployée en urgence pour faille de sécurité) ne supporte plus le thème graphique précédent. Travaux de refonte en cours (Hugo, Manon, Drâle du Grand Est). Nouvelle approche : masquer les instances, ne parler que de thématiques. Résultat attendu **après la rentrée** (~3-4 mois).
- **Transcription vidéo** : opérationnelle en environnement de test. Déploiement à généraliser avec Nicolas (un second serveur à préparer).
- **Transcodage externalisé** : à généraliser en parallèle de la transcription pour alléger les serveurs tubes.
- **Cycle de vie des comptes et vidéos** : descriptif finalisé, devis en attente. Répartition des développements entre Framasoft (fonctionnalités génériques dans le cœur PeerTube) et un plugin spécifique ministère (ex. : vidéos avec mineurs, durée de conservation d'un an).
- **Automatisation des déploiements** : avancement signalé, point à faire avec l'équipe.
- **Déploiement de l'asset v1.1** : mis en priorité (failles de sécurité).
- Environ **80 000 vidéos** sur Pod Éducation (chiffres d'avant les vacances).

### 12. Messagerie — Déploiement académique

- **Académie de Corse** : premier pilote en conditions réelles sur une académie entière. 99 % des comptes migrés sans incident majeur. Quelques difficultés sur les comptes de l'ASGA (boîte de 96 Go, délégations de boîtes fonctionnelles).
- Enseignements tirés :
  - Après 20-25 ans d'utilisation de Convergence, les usages sont très ancrés et variés (délégations, exports EML, règles de tri, etc.).
  - Nécessité d'un accompagnement au changement renforcé, notamment pour les VIP et les usages locaux spécifiques.
  - Ce constat vaut pour tous les projets du programme (Nuage, Tribu, Visio Agent).
- **Usine de portage des contacts et archives** : en cours de test par les utilisateurs corses migrés.
- **Plugin Visio Agent** : demande en attente, attendu prochainement.
- **Saint-Francis (antispam)** : latences en cours de résolution. Travaux sur les règles de détection et les dictionnaires académiques.
- **Prochains déploiements** :
  - Académie de Reims : en cours.
  - Nantes : envisage de libérer tous les établissements publics et privés (écoles, collèges) d'ici juin.
  - Poitiers : communication du calendrier des sites pilotes.
  - Île-de-France : réunion de lancement prévue la semaine prochaine, bascule envisagée en octobre.
  - Réunion de 100 référents le lendemain pour valider le plan de déploiement global.
- **Plugin Thunderbird** : question ouverte sur l'opportunité de le diffuser ou de le réserver au webmail pour inciter à la migration.

### 13. Bornes Wi-Fi

- Questionnaire envoyé aux académies d'Île-de-France pour recueillir les retours sur les usages et problèmes de connectivité. En attente de réponses.

### 14. Portail intranet académique

- Refonte du portail intranet académique : implication d'une académie à valider la semaine prochaine. Projet identifié comme porte d'entrée de l'ensemble des services.

### 15. GSR Bordeaux

- Événement prévu début juin. Participants confirmés : Johan, Benoît, Nicolas, François, Sophie, Frédéric.
- Point à rappeler : **Atena n'est pas uniquement la messagerie** — message à porter lors du GSR.

---

## Décisions prises

- Décalage de la campagne BNA : lancement repoussé au **27-28 juin**.
- Suspension de la mise à jour Nextcloud v31 jusqu'à correction de la régression sur les liens de partage.
- Intégration BBB dans CHAP : commande validée, développement à lancer.
- Commande de 35 jours de développement Visio Agent validée ce matin.
- Répartition des développements cycle de vie Tube entre Framasoft (cœur) et plugin spécifique ministère.
- Augmentation RAM serveurs Postgres de 8 Go à 12 Go (déjà réalisée).

---

## Questions en suspens

- Montants précis de la réduction budgétaire sur le programme : en attente de confirmation.
- Mise à jour Nextcloud v31 : conditionnée à la livraison d'un correctif par l'éditeur sur les liens de partage.
- Déploiement de Global Scale : bloqué par le prérequis v31.
- Passage en mode INSAS : plus de nouvelles depuis fin février / début mars, à reclarifier.
- Opportunité de diffuser le plugin Thunderbird ou de le réserver au webmail : question ouverte.
- Prise en compte des demandes du CNED sur Visio Agent (dont délégation de salles) : à discuter avec Frédéric (priorisation et financement).
- Rancher pré-prod : toujours non opérationnel pour le déploiement des applications.
- Restitution de 4 Go de RAM sur les frontaux Nextcloud : à surveiller attentivement lors de l'opération.

---

## Tâches à effectuer

| Tâche | Responsable |
|---|---|
| Confirmer les montants de réduction budgétaire sur le programme | Johan |
| Organiser un retour d'expérience Squash / Tribu (prochain comité) | Simon / Johan |
| Préparer et transmettre les slides pour le comité référents (mardi prochain) | Équipe (tous) |
| Faire un point avec Frédéric pour recaler le projet dotation et réévaluer les profils | À organiser |
| Organiser un point collectif pour identifier les projets mûrs pour la formation des équipes support académiques | Johan / équipe |
| Intégrer les deux communications suivantes pour la campagne BNA et anticiper le traitement des données | À confirmer |
| Inviter Bruno pour un point sur la communication unifiée | Johan |
| Finaliser le chiffrage de la refonte graphique Tribu et lancer les développements | Simon |
| Préparer les environn
