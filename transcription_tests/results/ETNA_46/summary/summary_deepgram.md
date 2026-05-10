# Compte‑rendu de la réunion du **46ᵉ comité de marge**
**Date** : 28 avril 2026
**Durée** : ≈ 2 h (estimation basée sur le déroulement)

---

## Participants
| Nom | Fonction / Rôle |
|-----|-----------------|
| **Audran** | Responsable DNE |
| **Benoît** | Chef de projet – Nextcloud / Visio Agent |
| **Frédéric** | Responsable intégration / BGB |
| **Nicolas** | Responsable support & formation |
| **Maxime** | Responsable technique Nextcloud |
| **Hugo** | Développeur – portail apps / QR‑code |
| **Michael** | Développeur – BBB |
| **Benjamin** | Développeur – BBB |
| **JFR** | Animateur du comité |
| **Autres** | Membres du comité référent, équipes support, prestataires externes |

---

## Objet de la réunion
Faire le point sur :

1. L’impact de la **réduction budgétaire DNE** sur les projets en cours.
2. La **maîtrise des dates de livraison** des nouvelles fonctionnalités (Nextcloud, Collabora, Tribu, etc.).
3. L’avancement des **projets majeurs** (refonte UX/UI de Tribu, migration Nextcloud, intégration Visio Agent, portail apps, wifi académies).
4. Les **questions en suspens** et les **tâches à réaliser** avant le prochain comité.

---

## Sujets abordés & décisions prises

| Sujet | Points clés | Décision / Action |
|-------|-------------|-------------------|
| **Réduction du budget DNE** | - Réduction globale annoncée, montants à confirmer.<br>- Impact « indolore » mais risque de petits ajustements projet. | - Audran doit fournir les chiffres définitifs d’ici la fin du mois.<br>- Suivi du budget dans le tableau de pilotage. |
| **Visibilité des jalons** | - Demande forte de la direction pour des dates précises (septembre / octobre).<br>- Actuellement seules des fourchettes (avant/après été). | - Le PM doit établir un **planning détaillé** (date +/‑ 1 semaine) pour chaque release et le diffuser d’ici le 10 mai. |
| **Nextcloud** | - Version 30 en prod, 31 disponible mais **régression fonctionnelle** (liens internes).<br>- Déploiement prévu en production impossible tant que le correctif n’est pas testé. | - **Report du déploiement** de la 31 à début juin, après validation de Maxime.<br>- Maxime teste la version 31 en pré‑prod et rend compte vendredi. |
| **Collabora** | - Livraison des versions 3.0, 3.1, 4.0 attendues, mais pas de financement dédié. | - Aucun financement supplémentaire prévu ; on continue à **suivre la roadmap publique**. |
| **Tribu – refonte graphique (UX/UI)** | - Chiffrage en cours, 3 lots (accueil, outils/recherche, admin).<br>- Durée totale estimée ≈ 200 jours, cible fin novembre / début décembre. | - Validation du **planning** dès réception du chiffrage final (prévu mi‑mai).<br>- Mise en place d’environnements pré‑prod pour chaque lot. |
| **Visio Agent (BBB)** | - Intégration validée avec Frédéric.<br>- Déploiement d’un bouton « Rejoindre la réunion » dans le chat. | - Frédéric finalise le **déploiement** d’ici le 15 mai.<br>- Tests utilisateurs prévus la semaine suivante. |
| **Licences Microsoft** | - Renouvellement effectué la semaine dernière (≈ 50 k €). | - Aucun suivi supplémentaire requis. |
| **Comité référent ATNA** | - Réunion prévue **mardi prochain** (date exacte à confirmer). | - Nicolas prépare les slides d’information d’ici le 5 mai. |
| **Dotation & étude de volumétries** | - En cours d’étude avec Frédéric. | - Point prévu avec Frédéric la semaine prochaine pour réévaluer les profils. |
| **Support utilisateur** | - Mise à jour en cours, incidents (groupement, déploiement d’applications). | - Ticket ouvert, suivi par l’équipe support ; mise à jour prévue fin mai. |
| **Enquête de satisfaction** | - Initialement prévue début juin, reportée au **27‑28 juin** à cause d’un chevauchement d’enquête. | - Questionnaire finalisé, communication prête ; lancement le 27 juin. |
| **Choix d’outils (libre vs propriétaire)** | - Discussion sur l’outil de visioconférence, le chat, le SIP, etc. | - Pas de décision immédiate ; besoin d’une **analyse de besoins** (action à planifier). |
| **Portail Apps** | - 82 k vidéos, 121 k comptes, stats Matomo installées.<br>- Développement d’un raccourcisseur URL/QR‑code en cours (Hugo). | - Hugo livre le **module QR‑code** d’ici le 3 mai.<br>- Mise en production prévue le 1 juillet. |
| **Architecture micro‑applications** | - Avancement sur le “rancher” pré‑prod, mais déploiement encore limité. | - Continuer la formation interne ; objectif de **déploiement fonctionnel** d’ici fin mai. |
| **Wifi académies** | - Questionnaire envoyé, réponses attendues. | - Relancer les académies le 10 mai, analyser les réponses avant le prochain comité. |
| **Conformité & RAM serveur BDD** | - +4 Go RAM obtenus (passage 8 → 12 Go).<br>- Objectif 16 Go prévu avec le prochain atelier Optimus Green. | - Planifier le **déploiement de +4 Go** supplémentaires avant fin mai, surveiller la stabilité. |

---

## Questions en suspens
| Question | Responsable / Suivi |
|----------|---------------------|
| Dates précises (septembre / octobre) des nouvelles fonctionnalités. | PM – à fournir le planning détaillé. |
| Quand la version 31 de **Nextcloud** sera‑t‑elle stable ? | Maxime – test en cours, compte rendu vendredi. |
| Livraison du **script de migration** Nantes → central (correctif). | Benoît – suivi du correctif, prévu ce week‑end. |
| Augmentation RAM serveur BDD à **16 Go**. | Équipe infra – planification atelier Optimus Green. |
| Retour du questionnaire **wifi académies**. | Responsable questionnaire – relance le 10 mai. |
| Validation du **module QR‑code** du portail apps. | Hugo – livrable 3 mai. |
| Décision finale sur l’outil de visioconférence (privé vs libre). | Comité technique – analyse à planifier (prochaine réunion). |

---

## Tâches à effectuer (avec responsables)

| Tâche | Responsable | Échéance |
|-------|-------------|----------|
| Fournir les montants définitifs de la réduction budgétaire DNE. | Audran | 31 mai |
| Élaborer le planning détaillé des livraisons (semaine ±1 j). | PM (non nommé) | 10 mai |
| Tester la version 31 de **Nextcloud** en pré‑prod et valider le déploiement. | Maxime | 5 mai |
| Suivi du correctif du script de migration (Nantes). | Benoît | 30 avril (week‑end) |
| Finaliser l’intégration de **Visio Agent** (bouton réunion). | Frédéric | 15 mai |
| Livrer le module **QR‑code** pour le portail apps. | Hugo | 3 mai |
| Préparer les slides d’information pour le **comité référent ATNA**. | Nicolas | 5 mai |
| Planifier et exécuter l’atelier **Optimus Green** pour +4 Go RAM (total 12 Go déjà atteint). | Équipe infra | 31 mai |
| Relancer les académies pour le questionnaire **wifi** et compiler les réponses. | Responsable questionnaire | 10 mai |
| Mettre à jour les documents de formation (tutoriels) suite à la refonte Tribu. | Équipe formation | 20 mai |
| Suivi du ticket d’incident **groupement** (déploiement d’applications). | Support (Nicolas) | 30 mai |

---

## Prochaine rencontre
- **Comité référent ATNA** – **Mardi prochain** (date à confirmer, probable 2 mai).
- Un **point de suivi** sur les livraisons et les actions en cours sera organisé **le 12 mai** (réunion courte de 30 min, invitation à venir).

---

*Le présent compte‑rendu sera diffusé à tous les participants et archivé dans le répertoire partagé du comité.*
