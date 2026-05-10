# Compte‑rendu de la réunion du 46ᵉ comité DNE
**Date** : 28 avril 2026
**Durée** : non précisée (environ 2 h)

---

## Participants
| Nom | Fonction / Rôle |
|-----|-----------------|
| Didier | Responsable de programme |
| Hugo | Chef de projet – Portail Apps / Raccourcisseur d’URL |
| Benoît | Responsable technique – Nextcloud, Tribu |
| Audran | Représentant du comité de domaine |
| Nicolas | Responsable formation & support |
| Frédéric | Responsable des référents ATNA |
| Simon | Animateur du « squash » Tribu |
| Maxime Leherici | Contact éditeur Nextcloud |
| … (autres intervenants ponctuels) |  |

---

## Objet de la réunion
Suivi des projets du **DNE** (budget, jalons, livrables), état des relations avec les prestataires, points d’avancement sur les chantiers techniques (Tribu, Nextcloud, VisioAgent, Portail Apps, communication unifiée, Wi‑Fi, etc.) et organisation des prochains comités de suivi.

---

## Sujets abordés

| # | Thème | Principaux éléments discutés |
|---|-------|------------------------------|
| 1 | **Budget DNE** | Réduction globale du budget ; attente des montants définitifs. |
| 2 | **Précision des jalons** | Besoin d’une planification plus fine (dates de mise en production, engagements des éditeurs). |
| 3 | **Relations prestataires** | Difficultés de visibilité sur les road‑maps (Nextcloud, Collaborat, BVB, etc.) ; exigence d’engagements plus réalistes. |
| 4 | **Formation & licences** | Renouvellement licences Microsoft effectué ; suivi des besoins de formation. |
| 5 | **Comité référent ATNA** | Réunion prévue mardi prochain (distanciel). |
| 6 | **BNA – campagne d’enquête** | Décalage du lancement du 16 juin au 27‑28 juin. |
| 7 | **Communication unifiée** | Étude des outils (Cisco, Webex, solutions libres) et choix entre outil privé ou libre. |
| 8 | **Refonte graphique Tribu (UX/UI)** | Chiffrage en cours, 3 lots (accueil, recherche, admin) → ≈ 200 jrs. Objectif MEP fin novembre/décembre 2025. |
| 9 | **Nextcloud – version 31** | Régression fonctionnelle sur le partage de fichiers ; mise en production reportée en attente du correctif. |
|10| **VisioAgent** | Intégration validée ; futur déploiement dans Cap Education. |
|11| **Portail Apps** | 221 k comptes, 73 k actifs depuis déc. 2022 ; Matomo installé, stats en cours. |
|12| **Raccourcisseur d’URL** | Développement en cours, démonstration prévue la semaine prochaine. |
|13| **Architecture micro‑applications** | Avancement sur le découpage fonctionnel (tokens, micro‑services). |
|14| **Thématiques des tubes (PeerTube)** | Refond graphique et nouvelle navigation thématique – mise en œuvre prévue à la rentrée. |
|15| **Transcription vidéo** | Fonctionnalité opérationnelle en test, déploiement prévu sur l’ensemble des serveurs tubes. |
|16| **Wi‑Fi** | Questionnaire envoyé aux académies Île‑de‑France, en attente de réponses. |
|17| **Portail intranet** | Reprise du projet, implication académies prévue la semaine prochaine. |

---

## Décisions prises

| Décision | Responsable(s) | Commentaire |
|----------|----------------|-------------|
| Appliquer la réduction budgétaire prévue. | Didier | Impact à gérer au niveau des projets. |
| Améliorer la précision des dates de livraison. | Audran + équipes projets | Mettre en place un suivi mensuel des engagements éditeurs. |
| Décaler la campagne BNA au 27‑28 juin. | Responsable BNA (non nommé) | Communication aux parties prenantes. |
| Reporter le déploiement de **Nextcloud 31** jusqu’à réception du correctif sur les partages. | Benoît / Maxime Leherici | Tests en pré‑prod avant mise en prod. |
| Valider l’intégration de **VisioAgent** dans Cap Education. | Frédéric | Démarrage du développement du front‑end. |
| Lancer le **chiffrage final** de la refonte Tribu et valider le planning. | Équipe dev Tribu (Benoît, Simon) | Objectif MEP fin novembre 2025. |
| Déployer le **raccourcisseur d’URL** après la démonstration. | Hugo | Déploiement prévu début juillet. |
| Augmenter la RAM des serveurs PostgreSQL à 12 Go (et prévoir 4 Go supplémentaires sur les frontaux). | Optimus Green / équipe infra | Suivi des performances post‑mise à jour. |
| Organiser le **squash Tribu** avec Simon. | Simon | À planifier après le chiffrage. |
| Envoyer les slides pour le prochain comité référent ATNA. | Simon | Diffusion d’ici la fin de semaine. |
| Continuer le suivi du questionnaire Wi‑Fi et relancer les académies. | Responsable Wi‑Fi (non nommé) | Relance prévue la semaine prochaine. |

---

## Questions en suspens

| Question | Responsable(s) | État |
|----------|----------------|------|
| Confirmation des montants exacts de la réduction budgétaire. | Didier | En attente des validations ministérielles. |
| Dates précises de livraison des nouvelles fonctionnalités (Collaborat, BVB, etc.). | Audran + prestataires | À affiner avec chaque éditeur. |
| Correctif du partage de fichiers dans **Nextcloud 31**. | Maxime Leherici / Benoît | En cours de développement, test prévu sous 2 semaines. |
| Validation du script de migration Nextcloud académique → centralisé. | Benoît | Correctif attendu ce week‑end. |
| Définition des usages et de la politique d’adoption du **outil de communication unifiée** (Cisco vs solution libre). | Responsable communication (non nommé) | Décision à prendre avant le prochain comité. |
| Compatibilité des plugins Thunderbird/Outlook avec la nouvelle authentification. | Nicolas + pôle identité | Études en cours, décision prévue Q3 2026. |
| Retour du questionnaire Wi‑Fi des académies Île‑de‑France. | Responsable Wi‑Fi | En attente des réponses. |
| Plan détaillé de la migration des comptes mineurs (Nuage). | Frédéric | À finaliser avant le déploiement de la version 31. |

---

## Tâches à effectuer

| Tâche | Responsable | Échéance |
|-------|-------------|----------|
| Transmettre les montants définitifs du budget. | Didier | 5 mai 2026 |
| Produire un planning détaillé des livrables (dates précises). | Audran + chefs de projet | 12 mai 2026 |
| Finaliser le chiffrage de la refonte Tribu et valider le planning. | Benoît / Simon | 15 mai 2026 |
| Tester et valider le correctif partage Nextcloud 31. | Maxime Leherici | 10 mai 2026 |
| Déployer le correctif de migration Nextcloud (script). | Benoît | 14 mai 2026 |
| Envoyer les slides du comité référent ATNA. | Simon | 30 avril 2026 |
| Organiser le squash Tribu. | Simon | 3 mai 2026 |
| Mettre à jour la RAM des serveurs PostgreSQL à 12 Go. | Optimus Green | 7 mai 2026 |
| Déployer le raccourcisseur d’URL (démo + mise en prod). | Hugo | 10 juillet 2026 |
| Relancer les académies pour le questionnaire Wi‑Fi. | Responsable Wi‑Fi | 8 mai 2026 |
| Finaliser la politique d’adoption de l’outil de communication unifiée. | Responsable communication | 20 mai 2026 |
| Vérifier la compatibilité des plugins mail (Thunderbird/Outlook). | Nicolas + pôle identité | Q3 2026 |

---

## Prochaine rencontre

- **Comité référent ATNA** – mardi prochain (date exacte à confirmer), en distanciel.
- **Suivi général DNE** – à planifier d’ici fin mai 2026 (prochaine réunion de pilotage).

---

*Fin du compte‑rendu.*
