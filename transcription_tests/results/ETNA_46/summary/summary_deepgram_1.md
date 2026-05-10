# Compte‑rendu de la 46ᵉ réunion du **Comité de marge**
**Date** : 29 avril 2026
**Durée estimée** : ~ 1 h 30

---

## Participants
| Nom | Fonction / Rôle |
|-----|-----------------|
| **Audran** | Responsable suivi budget DNE |
| **Frédéric** | Chef de projet / Validation des commandes |
| **Benoît** | Responsable support & suivi éditeurs |
| **Nicolas** | Responsable formation & suivi académies |
| **Maxime** | Responsable technique Nextcloud |
| **Hugo** | Développeur (QR‑code / micro‑apps) |
| **Michael** | Développeur (BBB) |
| **Benjamin** | Développeur (BBB) |
| **Johan** | Support production |
| **Irina** (Pôle Paris) | Responsable socle technique |
| **Autres** | Membres du comité, représentants des académies, etc. |

---

## Objet de la réunion
Faire le point sur :

1. L’impact de la **réduction budgétaire DNE**.
2. La **maîtrise des plannings** et la visibilité des livraisons fonctionnelles (Collabora, Nextcloud, Tribu, etc.).
3. L’avancement des projets majeurs (Tribu UI, Visio Agent, BNA, migration Nextcloud, etc.).
4. Les **questions en suspens** et les **tâches à réaliser** avant les prochains comités.

---

## Sujets abordés & décisions prises

| # | Sujet | Points clés | Décision / Action |
|---|-------|-------------|-------------------|
| 1 | **Réduction du budget DNE** | - Réduction globale attendue (montants à confirmer). <br>- Impact limité mais risque de « coup de rabot » sur certains projets. | ✅ Audran doit fournir les chiffres définitifs d’ici la prochaine réunion. |
| 2 | **Visibilité des jalons fonctionnels** | - Besoin d’estimer les dates de mise en production (été, sept/oct). <br>- Difficulté à donner des dates précises (ex. Collabora, Nextcloud). | ✅ Mise en place d’un tableau de suivi partagé (deadline : 15 mai). |
| 3 | **Collabora** | - Livraison de la version 3.0 1 non financée, dépend du support. | ✅ Aucun financement supplémentaire prévu ; on reste sur le support standard. |
| 4 | **Nextcloud** | - Version 30 → 31 : régression fonctionnelle (partage de fichiers). <br>- Version 31 requise pour le *global‑scale* test. | ✅ Report de la mise à jour majeure jusqu’à validation de Maxime (prévu fin mai). |
| 5 | **Licence Microsoft** | Renouvellement effectué la semaine dernière (≈ 50 k €). | ✅ Aucun suivi supplémentaire requis. |
| 6 | **Comité des référents ATNA** | Réunion prévue **mardi prochain**. Slides à préparer. | ✅ Frédéric envoie les slides d’ici le 3 mai. |
| 7 | **Dotation / étude de volumétries** | En cours, besoin de valider les profils avec Frédéric. | ✅ Nicolas organise une réunion avec Frédéric (début mai). |
| 8 | **Support utilisateur & formation** | - Mise à jour en cours. <br>- Préparer des académies pour la montée en compétences. | ✅ Point formation à planifier (responsable : Nicolas, deadline : 10 mai). |
| 9 | **Campagne BNA** | Décalage du lancement du **16 juin** au **27‑28 juin** (conflit avec autre enquête). | ✅ Communication mise à jour par l’équipe communication (déploiement : 20 mai). |
|10| **Choix outils (libres vs privés)** | Discussion sur l’outil de visioconférence, chat, SIP, etc. | ✅ Poursuivre l’étude d’impact ; décision finale prévue lors du comité référent. |
|11| **Projet Tribu – refonte graphique (UX/UI)** | - Chiffrage en cours, 3 lots (accueil, outils/recherche, admin). <br>- Planning cible : fin 2025 (déploiement fin nov. / début déc.). | ✅ Validation du chiffrage prévue fin mai ; lancement du dev courant mai. |
|12| **Visio Agent** | Intégration du lien de visioconférence dans le chat (BBB). | ✅ Validation de l’intégration avec Frédéric ; dev à démarrer dès que la commande sera passée (déjà validée). |
|13| **Base de données – RAM** | +4 GiB sur chaque serveur (passage de 8 → 12 GiB) via ateliers Optimus Green. | ✅ Surveillance active à mettre en place (responsable : Benoît, dès la semaine prochaine). |
|14| **Portail Apps – stats & QR‑code** | - 82 k comptes, 73 k connexions depuis déc. <br>- Déploiement du raccourcisseur QR prévu fin juin. | ✅ Hugo livrera le rapport RM le **1 juillet** et finalisera le QR‑code d’ici fin juin. |
|15| **Architecture micro‑apps** | Déploiement progressif, besoin de finaliser le Rancher en pré‑prod. | ✅ Poursuivre les tests d’intégration (responsable : Hugo, deadline : fin mai). |
|16| **Thématiques « Tubes »** | Travail sur la nouvelle identité graphique, reporté à la rentrée prochaine. | ✅ Aucun livrable immédiat ; suivi lors du comité référent. |
|17| **Transcription vidéo** | Service fonctionnel en test, déploiement prévu avec Nicolas. | ✅ Déploiement complet d’ici fin mai. |
|18| **Wi‑Fi académies** | Questionnaire envoyé, en attente de réponses. | ✅ Relancer les académies le **5 mai** (responsable : Nicolas). |
|19| **Portail intranet académique** | Projet de refonte à acter la semaine prochaine avec les académies. | ✅ Point à l’ordre du jour du comité référent (mardi prochain). |

---

## Questions en suspens
| Question | Responsable / Suivi |
|----------|---------------------|
| Dates précises (sept/oct) des nouvelles fonctionnalités (Collabora, Nextcloud, Tribu). | Audran & équipe planning – tableau de suivi à mettre à jour d’ici 15 mai. |
| Quand la version 31 de Nextcloud sera‑telle stable ? | Maxime – tests pré‑prod, retour prévu fin mai. |
| Correction du script de migration académique → central (Nextcloud). | Benoît – correctif attendu ce week‑end, validation prévue début juin. |
| Quand le support éditeur (Collabora) pourra‑t‑il garantir les livraisons ? | Benoît – négociation d’engagements plus stricts, suivi mensuel. |
| Validation du budget exact de la réduction DNE. | Audran – à communiquer avant le prochain comité (d’ici 10 mai). |
| Retour du questionnaire Wi‑Fi des académies. | Nicolas – relance le 5 mai, synthèse avant le comité référent. |
| Date de mise en production du QR‑code shortener. | Hugo – livrable 1 juillet. |

---

## Tâches à effectuer (avec responsable)

| Tâche | Responsable | Échéance |
|-------|-------------|----------|
| Fournir les montants définitifs de la réduction budgétaire DNE. | **Audran** | 10 mai |
| Créer et partager le tableau de suivi des jalons fonctionnels. | **Benoît** | 15 mai |
| Envoyer les slides du comité référent ATNA. | **Frédéric** | 3 mai |
| Tester la version 31 de Nextcloud et valider le correctif de partage. | **Maxime** | fin mai |
| Organiser la réunion dotation avec Frédéric. | **Nicolas** | début mai |
| Préparer le support de formation pour les académies (modules, tutoriels). | **Nicolas** | 10 mai |
| Mettre à jour la communication de la campagne BNA (dates, questionnaire). | **Équipe communication** | 20 mai |
| Suivi de la RAM augmentée sur les serveurs BDD (alertes). | **Benoît** | dès la semaine prochaine |
| Livrer le rapport de développement QR‑code et plan de mise en production. | **Hugo** | 1 juillet |
| Finaliser le chiffrage et le planning du projet Tribu UI. | **Équipe Tribu** | fin mai |
| Lancer le développement Visio Agent (intégration chat). | **Équipe dev** | dès validation de la commande (déjà faite) |
| Relancer les académies pour le questionnaire Wi‑Fi. | **Nicolas** | 5 mai |
| Tester le Rancher en pré‑prod et préparer le guide de déploiement. | **Hugo** | fin mai |
| Préparer le point « refonte portail intranet académique » pour le comité référent. | **Frédéric** | mardi prochain |

---

## Prochaine rencontre
| Réunion | Date prévue | Objectif principal |
|---------|-------------|--------------------|
| **Comité des référents ATNA** | **Mardi 2 mai 2026** | Validation des slides, suivi des actions de dotation et de la refonte du portail intranet. |
| **Comité de marge (suivi)** | **Jeudi 16 mai 2026** (proposé) | Point sur le budget DNE, avancement des projets critiques (Nextcloud, Tribu, Visio Agent). |

---

*Le présent compte‑rendu sera diffusé aux participants et archivé dans le dossier partagé du comité.*
