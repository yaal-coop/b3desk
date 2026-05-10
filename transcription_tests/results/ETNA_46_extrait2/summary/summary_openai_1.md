# Compte rendu de réunion

**Date** : 4 mai 2026
**Durée** : *non précisée* (environ 1 h estimée)
**Objet** : Point d’avancement sur le portail Apps, le raccourcisseur d’URL, l’architecture micro‑applications, le déploiement Rancher, la refonte des thèmes Tube et les travaux de transcription/transcodage.

---

## Participants
| Nom | Rôle / Fonction |
|-----|-----------------|
| Hugo | Chef de projet / référent technique |
| Manon | Responsable UX & communication |
| Nicolas | Responsable infrastructure / déploiement |
| 2 développeurs | Développement du raccourcisseur d’URL (équipe Dijon) |
| Équipe « Rancher » | Support technique (contact externe) |
| Représentants Framasoft | Partenaire plugin expiration vidéo |
| Autres membres de l’équipe produit | (non nommés explicitement) |

---

## Sujets abordés & décisions prises

| Sujet | Points clés | Décisions / orientations |
|-------|-------------|--------------------------|
| **Statistiques du portail Apps** | 221 000 comptes ouverts (hors comptes directs), 73 000 ré‑activations depuis déc. ; Matomo installé depuis 3 semaines. | Continuer le suivi des parcours utilisateurs avec Matomo. |
| **Raccourcisseur d’URL** | Deux devs à Dijon, travail en cours depuis 2 semaines, prévision de 3 semaines d’affilée. | - Démonstration prévue **semaine prochaine**.<br>- Mise en production visée **avant le 14 août**.<br>- Hugo assure le suivi avec l’équipe Dijon. |
| **Architecture « micro‑applications »** | Passage du portail à des appels de micro‑apps sécurisées via tokens (ex. gestion des comptes/tubes). | Poursuivre le design ; aucune décision finale, mais validation du principe. |
| **Rancher (Tradeprod)** | Livré il y a 2 semaines, non fonctionnel, problèmes de certificats et de droits de déploiement. | - Demande de clarification en cours.<br>- Recherche d’une procédure de déploiement autonome (logiciel libre). |
| **Thèmes / identité graphique du Tube** | 11 thèmes existants, incompatibilité avec la version 7.1.1 (mise à jour urgente). | - Travail de refonte lancé avec DRAM Grand Est, Hugo & Manon.<br>- Passage de la notion « instance » à « thème ».<br>- **Mise en place prévue à la rentrée** (3‑4 mois). |
| **Transcription vidéo** | Fonctionnelle en environnement de test, prête à être généralisée avec la version 7. | - Nicolas doit déployer le serveur de transcription sur tous les serveurs Tube.<br>- Préparer un second serveur et paramétrer les tubes. |
| **Externalisation du transcodage** | Proposition de centraliser transcodage et transcription sur deux gros serveurs (Dynium, Conseil national du numérique). | Prioriser la mise en place après généralisation de la transcription. |
| **Sécurité & cycle de vie (v7.1.1)** | Déploiement urgent à cause de failles cycloniques. | - Priorité absolue au déploiement de la 7.1.1.<br>- Gestion des expirations vidéo via plugin Framasoft (durée limitée) et plugin interne (déclaration de mineurs). |
| **Gestion des plugins** | Collaboration avec Framasoft et éditeur de plugins existants. | - Framasoft s’occupe du plugin « expiration standard ».<br>- Plugin interne pour les règles spécifiques (ex. vidéos contenant des mineurs).<br>- Rédaction du descriptif terminée, il reste à **gérer les devis** et **définir le marché**. |

---

## Questions en suspens
| Question | Responsable / Suivi |
|----------|---------------------|
| Clarification du fonctionnement du **Rancher** (certificats, droits de déploiement). | Contact technique Rancher (à suivre par l’équipe infrastructure). |
| Calendrier exact de la **mise à jour des thèmes** (passage à la notion de « thème »). | Hugo & Manon – à confirmer lors du prochain point. |
| Validation du **budget et du marché** pour les plugins (Framasoft & interne). | Responsable projet (non nommé) – à finaliser. |
| Détails du **plan de déploiement du transcodage externalisé** (infrastructure, coûts). | Nicolas – à préciser dans le prochain sprint. |

---

## Tâches à effectuer

| Tâche | Responsable | Échéance |
|-------|-------------|----------|
| Suivi du développement du **raccourcisseur d’URL** et organisation de la démonstration. | **Hugo** | Semaine prochaine |
| Déploiement de la **version 7.1.1** (sécurité) sur tous les services. | **Équipe infra** | Immédiat (avant fin août) |
| Finaliser le **design micro‑applications** et préparer le cahier des charges. | **Architecte technique** | Fin juin 2026 |
| Clarifier l’utilisation du **Rancher** (certificats, droits). | **Contact Rancher** | 15 mai 2026 |
| Déployer le **serveur de transcription** sur l’ensemble des serveurs Tube et préparer le second serveur. | **Nicolas** | Avant fin juin 2026 |
| Planifier la **centralisation du transcodage** (infrastructure Dynium). | **Nicolas** | Juillet 2026 |
| Réaliser les **devis** et choisir le **marché** pour les plugins d’expiration vidéo. | **Chef de projet** | Fin mai 2026 |
| Continuer les travaux de **refonte des thèmes Tube** (communication « thème » vs « instance »). | **Hugo & Manon** | Rentrée septembre 2026 |
| Suivi des **statistiques Matomo** et production d’un rapport d’usage. | **Équipe data** | Mensuel, premier rapport fin mai 2026 |

---

## Prochaine rencontre
- **Date proposée** : *à définir* (idéalement fin mai ou début juin 2026)
- **Objectif** : Faire le point sur le raccourcisseur d’URL, le déploiement de la 7.1.1, l’avancement du Rancher et la mise en production de la transcription.

---

*Fin du compte rendu.*
