```markdown
# Compte rendu de réunion

## Participants
- Didier
- Hugo
- Benoît
- Simon
- Frédéric
- Nicolas
- Johan
- François
- Sophie
- Frédéric Cognès
- Autres intervenants : Audran, Hugo (Dijon), Hugo (académie), Manon, Mickaël, Benjamin, Aurélien, Nicolas (formation), Frédéric (CRTH), Maxime Leherici (support Nextcloud), Paul Fouad, Mickaël (Nidigate Web), Bruno (communication unifiée), Frédéric (DNE), Frédéric (GSR), Johan, Sophie

## Objet de la réunion
Point projet quinzaine, suivi des avancées et des sujets en cours sur les différents projets de la DLE (Direction des Logiciels Éducatifs).

---

## Sujets abordés

### 1. Comité de domaine et suivi des jalons
- **Réduction du budget** : Réduction du budget sur toute la DLE, impact potentiel sur les projets mais considéré comme "indolore" selon les projets.
- **Suivi des jalons** :
  - Audran apprécie les nouvelles fonctionnalités mais souligne un manque de précision sur les dates de livraison.
  - Difficultés à fournir des dates précises (reculs fréquents ou ordres d'idées vagues comme "avant l'été" ou "après l'été").
  - Nécessité d’améliorer la communication et la précision des dates pour rassurer la direction et les autres acteurs.
  - Exemples de problèmes avec les éditeurs (Collaborat, Nextcloud, BBB) et manque de visibilité sur leurs roadmaps.

### 2. Projets spécifiques
- **Tribu** :
  - Refonte graphique en cours (UX8) avec chiffrage et planning validés.
  - Découpage en trois lots (accueils/tableaux de bord, outils/recherche, administration) avec une estimation totale de 200 jours.
  - Objectif de mise en production pour fin 2025 (précision attendue après validation du chiffrage).
  - Préparation des environnements de pré-production pour tests et déploiement.
  - Mise à jour des tutoriels et documents en parallèle.

- **Nuage (Nextcloud)** :
  - Version 31 avec régression fonctionnelle sur les liens partagés (problème de partage de fichiers).
  - Difficultés à déployer Global Scale en production en raison de cette régression.
  - Attente d’un correctif de Nextcloud pour restaurer les fonctionnalités avant de procéder à la mise à jour.
  - Migration académique en attente de validation par Nantes (équipe pilote).
  - Augmentation de la RAM sur les serveurs BDD (passage de 8 à 12 Go) pour résoudre des plantages récurrents.

- **DBV et Cap Education** :
  - Validation du développement pour intégrer DBV dans Cap Education (lien particulier pour les arrivants sur CHAP).
  - Utilisation de VisioAgent pour accéder directement aux réunions BBB depuis CHAP.

- **BBB (BigBlueButton)** :
  - Version 3.0 livrée avec des fonctionnalités disparues (sous-titrage SME, sélection aléatoire de participants).
  - Introduction de plugins pour des fonctionnalités spécifiques (ex : sélection aléatoire).
  - Demande du CNET pour la délégation de salles (complexe à mettre en œuvre).
  - Commande de 35 jours de développement pour VisioAgent validée.

- **Portail Apps** :
  - 221 000 comptes ouverts (hors comptes directs sur les applications).
  - 73 000 comptes se sont reconnectés depuis décembre (1/3 des utilisateurs actifs).
  - Installation de Matomo pour analyser les parcours des utilisateurs.
  - Mise à jour 6.4.1 en production avec améliorations sur le cycle de vie des utilisateurs.
  - Travaux en cours sur le raccourcisseur d’URL et l’architecture des micro-applications.

- **Rancher (Créprod)** :
  - Livraison en attente malgré des discussions sur les certificats et le déploiement.
  - Difficultés techniques à déployer les applications dessus.

- **Tube (PeerTube)** :
  - Thèmes graphiques non supportés par la version 7.1.1 (nécessité de refonte avant la rentrée).
  - Transcription des vidéos opérationnelle en test, préparation du déploiement en production.
  - Travaux en cours sur les cycles de vie des comptes et des vidéos (développement de plugins spécifiques).

- **Messagerie (Aetna)** :
  - Bilan du déploiement pilote en Corse (succès global mais quelques difficultés techniques et d’accompagnement).
  - Nécessité d’améliorer l’accompagnement au changement pour les déploiements futurs.
  - Problèmes liés aux usages historiques (ex : FGRA, exports de mails sous format EML).
  - Migration vers le webmail en cours, avec des académies encore utilisant Thunderbird.

- **Wi-Fi et bornes** :
  - Questionnaire envoyé aux académies d’Île-de-France pour recueillir les retours sur les usages et problèmes.

- **Autres sujets** :
  - Renouvellement des licences Microsoft (utilisation sur 30 000 agents).
  - Communication unifiée (choix entre outils comme Cisco, Webex, ou solutions libres).
  - Projet de refonte du portail intranet académique en collaboration avec une académie pilote.

---

## Décisions prises
- **Précision des dates de livraison** :
  - Améliorer la communication avec les éditeurs pour obtenir des engagements plus réalistes et des dates précises.
  - Éviter de communiquer des dates trop éloignées sans garantie (ex : "avant l'été" sans précision).

- **Tribu** :
  - Finaliser le chiffrage et lancer les développements dès que validé.
  - Maintenir la mise en production pour fin 2025 (date à préciser après validation).

- **Nextcloud (Nuage)** :
  - Attendre le correctif de Nextcloud pour la version 31 avant toute mise à jour en production.
  - Planifier la migration académique après validation par Nantes.

- **BBB** :
  - Valider la commande de 35 jours de développement pour VisioAgent.
  - Explorer les plugins pour des fonctionnalités spécifiques (ex : délégation de salles).

- **Messagerie** :
  - Améliorer l’accompagnement des utilisateurs lors des déploiements (ex : migration vers le webmail).
  - Étudier les solutions pour les académies utilisant encore Thunderbird.

- **Prochaines étapes** :
  - Organiser un retour d’expérience (REX) avec Tribu et Simon pour le comité suivant.
  - Préparer le comité des référents (mardi prochain) avec les dernières actualités à partager.
  - Décaler la campagne BNA d’un mois (du 16 au 27 ou 28 juin) pour éviter un chevauchement avec une autre enquête.

---

## Questions en suspens
- **Dates précises des livraisons** :
  - Comment obtenir des engagements plus fiables des éditeurs (Collaborat, Nextcloud, BBB) pour les dates de sortie des versions ?
  - Comment gérer les décalages fréquents entre les roadmaps annoncées et les réalisations effectives ?

- **Problèmes techniques avec Nextcloud** :
  - Quand le correctif pour la version 31 sera-t-il disponible et testé ?
  - Comment procéder à la migration académique sans risque après validation par Nantes ?

- **Déploiement de Tribu** :
  - Quelle sera la date exacte de mise en production (précision attendue après validation du chiffrage) ?

- **Messagerie (Aetna)** :
  - Comment convaincre les académies encore utilisant Thunderbird de migrer vers le webmail ?
  - Quelles solutions proposer pour les usages spécifiques (ex : FGRA, exports de mails) ?

- **Wi-Fi** :
  - Quand les académies d’Île-de-France répondront-elles au questionnaire sur les bornes Wi-Fi ?

- **Communication unifiée** :
  - Quel outil choisir (Cisco, Webex, solutions libres) et comment intégrer les différents services (téléphonie, visioconférence) ?

---

## Tâches à effectuer

### Responsables identifiés ou actions prioritaires
- **Audran (Direction)** :
  - Exiger des dates plus précises et des engagements clairs des éditeurs sur les livraisons.

- **Équipe Tribu** :
  - Finaliser le chiffrage et lancer les développements dès que validé.
  - Préparer les environnements de pré-production (isoprod, dev, acuité).
  - Mettre à jour les tutoriels et documents en parallèle de la refonte.

- **Frédéric (Nuage/Nextcloud)** :
  - Coordonner avec le support Nextcloud (Maxime Leherici) pour obtenir le correctif de la version 31.
  - Planifier la migration académique après validation par Nantes.
  - Surveiller les serveurs BDD après augmentation de la RAM (risque de plantage).

- **Équipe BBB** :
  - Valider la commande de 35 jours de développement pour VisioAgent.
  - Explorer les plugins pour des fonctionnalités spécifiques (ex : délégation de salles).

- **Frédéric (Messagerie)** :
  - Améliorer l’accompagnement des utilisateurs lors des déploiements (ex : migration vers le webmail).
  - Étudier les solutions pour les académies utilisant Thunderbird.

- **Hugo (Portail Apps)** :
  - Finaliser le raccourcisseur d’URL et l’architecture des micro-applications avant l’été.
  - Préparer la mise à jour du portail (6.4.1) et déployer Matomo pour analyser les parcours utilisateurs.

- **Simon (Tube)** :
  - Préparer le déploiement de la transcription des vidéos en production.
  - Travailler sur les cycles de vie des comptes et des vidéos (développement de plugins).

- **Frédéric (DNE)** :
  - Rappeler aux académies que Aetna n’est pas uniquement une messagerie.
  - Préparer le comité des référents (mardi prochain) avec les dernières actualités.

- **Benoît/Nicolas (Wi-Fi)** :
  - Analyser les retours des académies d’Île-de-France sur le questionnaire des bornes Wi-Fi.

- **Bruno (Communication unifiée)** :
  - Fournir un topo sur les enjeux et les choix possibles pour la communication unifiée.

---

## Prochaine rencontre
- **Comité des référents** :
  - Date : Mardi prochain (en distanciel).
  - Objectif : Faire le point sur les sujets en cours et partager les dernières actualités.
  - Préparation : Réception de slides dans les prochains jours pour partager les infos.

- **Retour d’expérience (REX) avec Tribu et Simon** :
  - À organiser pour le comité suivant (date non précisée).

- **Réunion de lancement pour le déploiement de la messagerie (Aetna)** :
  - À organiser pour valider le plan de déploiement à grande échelle (3e et 4e trimestres).
```
