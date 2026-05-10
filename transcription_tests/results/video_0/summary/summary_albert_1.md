# Compte rendu de réunion

**Date** : 30 avril 2026
**Durée** : *non précisée* (environ 1 h 30)

## Participants
- **Johan** (animateur)
- **Benjamin**
- **Benoît**
- **Mickaël**
- **Sébastien** (mentionné pour la procédure de release)
- Autres intervenants ponctuels (ex. « toi », « je »)

## Objet de la réunion
- Organisation d’un point de suivi bi‑hebdomadaire.
- Bilan des livraisons récentes (code unique, configuration BBB/ScaleLight).
- Points techniques en cours : migrations, logs, stabilité de la connexion Nuage/Nextcloud, ticket 166.
- Avancement des projets « salon silencieux », « CIP », et du backlog.
- Planification des releases 1.3 / 1.3.1 et des tâches associées.

## Sujets abordés

| # | Sujet | Principaux échanges |
|---|-------|---------------------|
| 1 | **Fréquence des points** | Proposition d’un point toutes les 2 semaines, le **mercredi à 11 h 30**. Tous les participants sont d’accord. |
| 2 | **Livraison du code unique** | - Deux‑trois questions de Johan sur la configuration nécessaire. <br>- Nécessité de modifier une variable de configuration (ScaleLight) – à préciser dans la PR et les notes de release. |
| 3 | **Scénario de test BBB / B3Desk** | - Explication du paramètre **Dial Number** (affichage du numéro de téléphone et du PIN). <br>- Le PIN affiché est uniquement pour l’accès téléphonique, distinct du code d’accès automatique. |
| 4 | **Migrations** | - La migration actuelle dépend d’une migration précédente (classement des salons). <br>- Dans la release, les migrations seront exécutées dans l’ordre, mais il faut s’assurer que le classement soit déjà présent dans Visiotest. |
| 5 | **Ticket 166 – Erreur 500 salon** | - Résolu par Arawa (suppression d’un champ). <br>- Conservation de la remontée de logs prévue dans la release. |
| 6 | **Stabilité de la connexion Nuage / Nextcloud** | - Tests de capture de trafic montrent que les requêtes passent, mais des lenteurs/instabilités subsistent. <br>- Hypothèses : surcharge du serveur, bibliothèque WebDAV obsolète. <br>- Besoin de reproduire le problème et d’analyser la cinématique. |
| 7 | **Projet « salon silencieux »** | - Devis validé, budget en cours de validation financière. <br>- Possibilité de lancer les commandes rapidement. |
| 8 | **Projet CIP & connecteur BBB** | - Projet porté par le MTE, financement BGFIP. <br>- Nécessité d’une réunion dédiée pour cadrer les spécifications et les limites techniques (développement interne Renater). |
| 9 | **Backlog & chiffrage** | - Discussion sur les tags (X‑large, Medium, …) et leur correspondance en jours/homme. <br>- Mickaël demande à recevoir un tableau de correspondance. |
|10| **Création de la release 1.3** | - Sébastien a présenté la procédure. <br>- Release prévue **aujourd’hui à 14 h** avec la participation de Benjamin et Mickaël. |
|11| **Divers** | - Confirmation que le numéro de téléphone utilisé par BBB provient d’Arawa et doit être renseigné dans la config B3Desk. <br>- Aucun autre point n’a été soulevé. |

## Décisions prises
| Décision | Responsable | Commentaire |
|----------|-------------|--------------|
| Instaurer un point de suivi **toutes les 2 semaines, le mercredi à 11 h 30** | Johan (envoi d’invitation) | Calendrier partagé. |
| Ajouter la description de la **configuration ScaleLight** (variable à modifier) dans la PR et les notes de release | Benjamin (ou l’auteur de la PR) | Garantir la traçabilité. |
| Conserver la **remontée de logs** du ticket 166 dans la prochaine release | Aucun (déjà intégré) | Aucun changement requis. |
| Lancer le **salon silencieux** dès que le devis est validé financièrement | Benoît (coordination avec l’équipe finance) | Le devis est déjà transmis. |
| Planifier la **release 1.3** (features : classement des salons, URL questionnaire, etc.) | Sébastien (guidage) + Benjamin + Mickaël | Réunion de mise en production à 14 h. |
| Produire un **tableau de correspondance tags ↔ durée** | Mickaël (ou Benjamin) | À fournir d’ici la fin de journée. |
| Poursuivre l’investigation sur la **connexion Nuage/Nextcloud** et reproduire le problème | Benoît (tests) + Benjamin (analyse) | Rapport à partager lors du prochain point. |
| Organiser une réunion **CIP / Renater** pour cadrer les développements supplémentaires | Johan (planification) | À fixer ultérieurement. |

## Questions en suspens
- **Scénario de test complet** pour les changements BBB (validation du PIN et du Dial Number).
- Confirmation que la **migration du classement des salons** est bien appliquée avant la migration du code unique.
- **Durée de validité du token applicatif** (30 jours) – envisager une extension en production.
- **Impact de la version de la bibliothèque WebDAV** sur la stabilité – besoin d’une mise à jour éventuelle.
- **Définition précise du périmètre fonctionnel** du connecteur CIP avec Renater.

## Tâches à effectuer

| Tâche | Responsable | Échéance |
|-------|-------------|----------|
| Envoyer l’invitation du point bi‑hebdomadaire (mercredi 11 h 30) | Johan | Immédiate |
| Mettre à jour la PR avec la description de la configuration ScaleLight | Benjamin | Avant la release 1.3 |
| Vérifier que la migration du classement des salons est bien présente dans Visiotest | Benjamin | Avant la release 1.3 |
| Réaliser des tests de reproduction du problème Nuage/Nextcloud et documenter les résultats | Benoît | Avant le prochain point (dans la semaine) |
| Fournir le tableau de correspondance **tags ↔ durée** (jours/homme) | Mickaël | Fin de journée |
| Effectuer la **release 1.3** (création de tags, commits, push) | Sébastien (guidage) + Benjamin | Aujourd’hui 14 h |
| Lancer les commandes d’achat pour le **salon silencieux** après validation du budget | Benoît | Dès que le financement est confirmé |
| Planifier une réunion de cadrage **CIP / Renater** | Johan | Prochaine quinzaine |
| Mettre à jour la durée du token applicatif (si besoin) pour la version production | Benjamin | À définir (post‑release) |

## Prochaine rencontre
- **Point bi‑hebdomadaire** : **mercredi 11 h 30** (date exacte à confirmer dans le calendrier).
- Une **réunion dédiée** sera programmée ultérieurement pour le projet CIP / Renater (date à définir).
