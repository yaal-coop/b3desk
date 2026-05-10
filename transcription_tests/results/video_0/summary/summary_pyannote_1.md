# Compte‑rendu de réunion

**Date** : 30 avril 2026
**Heure** : 13 h 30 – 15 h 00 (environ 1 h 30)
**Lieu** : Teams / Visio

---

## Participants
| Nom | Rôle / Fonction |
|-----|-----------------|
| Johan | Responsable produit |
| Sébastien | Lead développeur – présentateur de la PR |
| Benjamin | Développeur backend |
| Mickaël | Architecte technique |
| Benoît | Chef de projet / liaison messagerie |
| (autres) | Participants ponctuels (ex. : interlocuteurs Arawa) |

---

## Objet de la réunion
- Mettre en place un point de suivi **bi‑hebdomadaire**.
- Faire le point sur les développements en cours (code unique, configuration BBB/B3Desk, migrations, ticket 166).
- Discuter des incidents de connexion **Nuage / WebDAV** et du **salon silencieux**.
- Planifier la **release 1.3** et définir les prochaines étapes.

---

## Durée estimée
Environ **1 h 30** (début 13 h 30 – fin 15 h 00).

---

## Sujets abordés

| Sujet | Points clés |
|-------|-------------|
| **1. Point bi‑hebdomadaire** | - Accord pour un point toutes les 2 semaines.<br>- Sébastien enverra l’invitation. |
| **2. Code unique & configuration BBB** | - Nouvelle variable **dial‑number** à ajouter dans la config B3Desk.<br>- Le numéro de téléphone provient d’Arawa (BBB/Skylight).<br>- Le PIN affiché dans B3Desk sera généré aléatoirement, modifiable. |
| **3. Migration de base de données** | - Migration actuelle dépend d’une migration précédente (classement des salons).<br>- Risque d’ordre d’exécution incorrect dans la release. |
| **4. Ticket 166 – Erreur 500 salon** | - Résolu par Arawa (suppression d’un champ incohérent). |
| **5. Connexion Nuage / WebDAV** | - Le token applicatif (validité 30 jours) est utilisé.<br>- Instabilité possible : surcharge du serveur, bibliothèque Python obsolète.<br>- Nécessité de collecter des métriques de temps de réponse. |
| **6. Salon silencieux** | - Devis validé, financement par l’équipe messagerie.<br>- Passage en production dès que le budget 2025 est alloué. |
| **7. SIP Media Gateway** | - Projet de connecteur SIP à BBB.<br>- Besoin de cadrer le périmètre fonctionnel et les développements côté B3Desk. |
| **8. Estimation des tâches (tags)** | - Besoin d’une correspondance **tag ↔ durée** (ex. : `large`, `medium`, `small`).<br>- Mickaël doit fournir un tableau d’estimation. |
| **9. Création de la release 1.3** | - Décision de publier la release **sans** le numéro d’appel et le code unique.<br>- Sébastien et Benjamin prévoient de réaliser la release à **14 h** le même jour. |

---

## Décisions prises

| Décision | Responsable(s) |
|----------|----------------|
| Instaurer un point de suivi **toutes les 2 semaines**. | Sébastien (envoi invitation) |
| Ajouter la variable **dial‑number** dans la configuration B3Desk et la documenter dans la PR. | Benjamin & Mickaël |
| Valider que la **migration** s’exécute dans le bon ordre avant la release. | Mickaël (vérification) |
| Publier la **release 1.3** sans le numéro d’appel ni le code unique. | Sébastien (création) + Benjamin (validation) |
| Lancer le **salon silencieux** dès que le devis est confirmé (déjà validé). | Benoît / équipe messagerie |
| Produire un tableau d’estimation **tags ↔ durée**. | Mickaël (à fournir d’ici la fin de journée) |
| Planifier la **release 1.3** à 14 h le même jour. | Sébastien (exécution) |
| Continuer l’investigation sur l’instabilité **Nuage/WebDAV**. | Benoît (analyse) |
| Étudier l’extension de la validité du **token applicatif** (plus de 30 jours). | Mickaël (proposition) |
| Organiser une réunion de cadrage **SIP Media Gateway**. | Mickaël & contact Renater (à planifier) |

---

## Questions en suspens

1. **Intégration du code unique** – sera‑t‑il reporté à la prochaine release (post‑1.3) ou intégré dans une version ultérieure ?
2. **Ordre exact des migrations** – confirmation que toutes les migrations précédentes sont bien présentes en production.
3. **Stabilité Nuage / WebDAV** – quelle cause principale (surcharge serveur, bibliothèque obsolète, protocole) ?
4. **Durée de validité du token** – quelle durée optimale pour la production ?
5. **Portée fonctionnelle du connecteur SIP** – quels endpoints et quelles données doivent être exposés ?

---

## Tâches à effectuer

| Tâche | Responsable | Échéance |
|-------|-------------|----------|
| Envoyer l’invitation du point bi‑hebdomadaire. | Sébastien | 1 mai 2026 |
| Vérifier que la variable **dial‑number** est correctement renseignée dans la config B3Desk. | Benjamin | Avant la release 1.3 |
| Tester que les valeurs saisies dans B3Desk apparaissent correctement dans la visio (BBB). | Benjamin | Avant la release 1.3 |
| Contrôler le bon déroulement de la migration dépendante (classement des salons). | Mickaël | Avant la release 1.3 |
| Produire le tableau **tags ↔ estimation (jours/heure)**. | Mickaël | Fin de journée (30 avril) |
| Réaliser la **release 1.3** (création de tags, merge, déploiement). | Sébastien (avec Benjamin) | 14 h, 30 avril 2026 |
| Analyser les logs et temps de réponse de la connexion **Nuage/WebDAV**. | Benoît | Semaine du 2 mai |
| Proposer une nouvelle durée de validité du token applicatif. | Mickaël | Prochaine réunion |
| Préparer le **devis et la commande** pour le salon silencieux (budget 2025). | Benoît | Dès que possible |
| Organiser une réunion de cadrage **SIP Media Gateway** avec Renater. | Mickaël | À planifier (mi‑mai) |

---

## Prochaine rencontre
- **Date** : dans deux semaines (prochaine réunion bi‑hebdomadaire).
- **Heure** : à confirmer (proposition : même créneau, 13 h 30).
- **Ordre du jour prévisionnel** :
  1. Suivi des actions de la release 1.3.
  2. Retour sur l’étude de stabilité Nuage/WebDAV.
  3. Décision sur l’intégration du code unique.
  4. Avancement du salon silencieux et du projet SIP Media Gateway.

---

*Fin du compte‑rendu.*
