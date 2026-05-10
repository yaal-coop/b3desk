# Compte rendu de réunion

**Date** : 28 avril 2026
**Heure** : non précisée (durée estimée ≈ 1 h)
**Lieu** : visioconférence

---

## Participants
| Nom | Rôle / Fonction |
|-----|-----------------|
| Johan | Chef de projet |
| Benjamin | Développeur / testeur |
| Benoît | Responsable financier / juridique |
| Mickaël | Product Owner |
| Sébastien | Responsable des releases |
| Autres (présents en écoute) | – |

---

## Objet de la réunion
Suivi des travaux en cours sur le produit **B3Desk** : points d’avancement techniques, planification des réunions de suivi, gestion des livraisons (release 1.3), résolution de bugs et préparation des prochains développements (salon silencieux, intégration CIP, stabilisation de la connexion Nuage/Nextcloud).

---

## Sujets abordés

| # | Sujet |
|---|-------|
| 1 | **Planification d’un point de suivi bi‑hebdomadaire** (mercredi 11h30). |
| 2 | **Livraison du code unique** – besoin de préciser la configuration à changer (ScaleLight/BBB) et de fournir un scénario de test. |
| 3 | **Configuration « BBB Dial Number »** – validation du paramètre et de son affichage dans B3Desk. |
| 4 | **Migrations de base de données** – ordre des migrations, inclusion dans la prochaine release. |
| 5 | **Ticket 166 – erreur 500 salons** – correction côté Arawa, conservation de la remontée de logs. |
| 6 | **Connexion Nuage / Nextcloud** – lenteur/instabilité du WebDAV, durée du token, pistes d’investigation. |
| 7 | **Salon silencieux** – validation du devis, budget 2025, lancement des commandes. |
| 8 | **Projet CIP (SibMediaGateway)** – besoin d’une réunion dédiée, dépendances avec Renater. |
| 9 | **Backlog & estimation des tâches** – utilisation de tags (Medium, Large…) et besoin d’un tableau de correspondance. |
|10| **Création de la release 1.3** – procédure, planning (14 h), contenus prévus (classement des salles, URL questionnaire, etc.). |

---

## Décisions prises

| Décision | Responsable / Commentaire |
|----------|----------------------------|
| Instaurer un point de suivi toutes les 2 semaines, le **mercredi à 11h30**. | Johan (organisation du calendrier). |
| Ajouter dans la PR la description du paramètre **ScaleLight** à modifier et l’inclure dans la release. | Développeur (non nommé). |
| Conserver la remontée de log du ticket 166 dans la prochaine release. | Équipe de développement. |
| Lancer le **salon silencieux** dès que le devis (déjà validé) est transmis au service financier. | Benoît (suivi du budget et du support juridique). |
| Prioriser la **release 1.3** avec : <br>• Classement alphabétique / favoris des salles <br>• URL questionnaire <br>• Corrections de migration <br>• Log du ticket 166 | Sébastien (coordination release). |
| Prévoir une **release 1.3.1** ultérieure pour le code unique / numéro unique. | Mickaël (planification produit). |
| Reproduire le problème de connexion Nuage et identifier la cause (WebDAV, surcharge, lib. obsolète). | **Benjamin** (tests + rapport). |
| Fournir **d’ici la fin de journée** un tableau de correspondance *tags ↔ estimation (heures/jours)*. | **Mickaël**. |
| Accompagner Johan dans la création de la release à **14 h** l’après‑midi. | **Sébastien**. |

---

## Questions en suspens

| Question | Responsable / Prochaine action |
|----------|--------------------------------|
| Dans quelle version (1.3 ou ultérieure) le **code unique** sera‑t‑il intégré ? | À clarifier avec Benoît (décision post‑release 1.3). |
| Confirmation du **nom exact du paramètre** ScaleLight à modifier (variable à préciser). | Développeur (mise à jour PR). |
| Quelle version de **Nextcloud** est la plus stable pour le WebDAV ? | Analyse de l’équipe Nuage (suite des tests). |
| Besoin de **support juridique** définitif pour le devis du salon silencieux. | Benoît. |
| Détails du **scénario de test** B3Desk ↔ BBB (affichage PIN, Dial Number). | Johan (rédaction du scénario). |
| Validation du **budget 2025** dédié au développement B3Desk. | Benoît (validation finale). |
| Coordination avec **Renater** pour les évolutions CIP (technologies différentes). | Mickaël (organisation réunion dédiée). |

---

## Tâches à effectuer

| Tâche | Responsable | Échéance |
|-------|-------------|----------|
| Envoyer le planning de la réunion bi‑hebdomadaire (mercredi 11h30). | **Johan** | Immédiate |
| Mettre à jour la PR avec la description du paramètre ScaleLight à changer. | Développeur | Avant la release 1.3 |
| Vérifier la migration de la base de données (ordre, exécution). | Équipe dev | Avant la release 1.3 |
| Intégrer la remontée de log du ticket 166 dans la branche `main`. | Équipe dev | Avant la release 1.3 |
| Réaliser les tests de connexion Nuage, reproduire le problème et fournir un rapport. | **Benjamin** | 1 semaine |
| Rédiger le scénario de test B3Desk/BBB (PIN, Dial Number). | **Johan** | Avant la release 1.3 |
| Envoyer le tableau de correspondance tags ↔ estimation (heures/jours). | **Mickaël** | Fin de journée |
| Accompagner Johan dans la création de la release 1.3 (14 h). | **Sébastien** | Aujourd’hui, 14 h |
| Vérifier le budget et le support juridique pour le salon silencieux. | **Benoît** | Avant le prochain point budgétaire |
| Planifier une réunion dédiée à l’intégration CIP avec Renater. | **Mickaël** | À définir |

---

## Prochaine rencontre

- **Réunion de suivi bi‑hebdomadaire** : chaque **mercredi à 11h30** (première occurrence à confirmer).
- **Release 1.3** : création prévue à **14 h** le même jour que la réunion (aujourd’hui).
- Un point dédié sera planifié ultérieurement pour le **projet CIP** et la **stabilisation de la connexion Nuage** (date à fixer).

---

*Fin du compte rendu.*
