# Compte rendu de réunion

**Date** : 29 avril 2026
**Durée** : ≈ 2 h 30 (prévue 1 h, s’est prolongée)

---

## Participants
| Nom | Rôle / Fonction |
|-----|-----------------|
| **Benjamin** | Chef de projet / coordinateur |
| **Miguel** | Développeur (BBB) |
| **Arwa** | Responsable configuration |
| **Benoît** | Testeur / support Nextcloud |
| **Pierre** | (mentionné pour décision) |
| **Michael** | Gestion des estimations & budget |
| **Mickaël** | (intervenant sur les tags) |
| **Sébastien** | Responsable procédure de release |
| **Renater** (organisation) | Partenaire technique |

---

## Objet de la réunion
- Faire le point sur l’avancement du projet **Betfridesk** (livraison du code unique, migrations, tests, stabilité Nextcloud, etc.).
- Organiser la cadence des réunions de suivi.
- Décider des prochaines étapes de release et de la mise en production de nouvelles fonctionnalités (pin BBB, salon silencieux, connecteur BBB).
- Aborder les questions de budget, de support juridique et de coordination avec les partenaires (DGFI, Renater).

---

## Sujets abordés

| # | Sujet | Principaux échanges |
|---|-------|----------------------|
| 1 | **Planification des points de suivi** | Proposition d’un point toutes les 2 semaines, le **mercredi à 11 h 30**. |
| 2 | **Livraison du code unique** | - Questions sur les développements complémentaires côté BBB.<br>- Nécessité d’ajouter un paramètre dans la PR et la release.<br>- Fournir un scénario de test pour la version 3. |
| 3 | **Gestion du PIN et du numéro de téléphone** | - Le PIN affiché dans l’invitation doit être configurable.<br>- Le numéro de téléphone est défini par **Arwa** et doit être injecté dans la configuration. |
| 4 | **Migrations** | - Ordre des migrations : le tri des salons doit précéder la migration actuelle.<br>- Confirmation que les fichiers de migration seront exécutés dans l’ordre dans la release. |
| 5 | **Ticket #666 (erreur de salon)** | - Problème résolu par modification d’un champ par Arwa.<br>- Décision de conserver la remontée de logs dans la prochaine release. |
| 6 | **Instabilité de Nextcloud (token)** | - Capture de trames réalisée sur *visiotest*.<br>- Hypothèses : surcharge du serveur, bibliothèque Python obsolète, durée du token (30 j).<br>- Benoît doit reproduire le problème et identifier la cause. |
| 7 | **Salon silencieux & budget** | - Le devis est validé, le salon peut être lancé en mode silencieux.<br>- Budget de **2 025 jours** à attribuer au développement Betfridesk ; recherche de financement. |
| 8 | **Connecteur BBB (financement DGFI)** | - Projet important, besoin de développer un connecteur BBB.<br>- Financement prévu par la DGFI, coordination avec le ministère de la Transition écologique. |
| 9 | **Estimation des tâches (tags)** | - Besoin d’un tableau de correspondance *tag → estimation (jours/heure)*.<br>- Michael doit le fournir rapidement. |
|10| **Création de la release 1.3** | - Sébastien a présenté la procédure.<br>- Release prévue **aujourd’hui à 14 h** (Benjamin & équipe). |

---

## Décisions prises

| Décision | Responsable | Délai |
|----------|-------------|-------|
| Instaurer un point de suivi bi‑hebdomadaire le mercredi à 11 h 30. | Benjamin (envoi d’invitation) | Immédiat |
| Ajouter le paramètre de configuration BBB dans la PR et la release. | Équipe dev (Benjamin) | Avant la release 1.3 |
| Fournir un scénario de test pour la version 3 (pin & numéro). | Benjamin / Miguel | Avant la release 1.3 |
| Respecter l’ordre des migrations (tri → migration actuelle). | Benjamin | Avant la prochaine release |
| Conserver la remontée de logs du ticket #666 dans la release. | Équipe dev | Release 1.3 |
| Benoît reproduira les problèmes de token Nextcloud et remontera les résultats. | Benoît | Au plus tard la semaine prochaine |
| Lancer le salon silencieux dès validation du devis. | Michael (coordination) | Dès que le budget est confirmé |
| Trouver le support financier pour les 2 025 jours de développement Betfridesk. | Michael | À définir |
| Démarrer le projet de connecteur BBB avec financement DGFI. | Michael / équipe projet | Dès validation du financement |
| Envoyer le tableau d’estimation des tags (jours/heure). | Michael | Avant la fin de journée |
| Effectuer la release **1.3** aujourd’hui à 14 h. | Benjamin & Sébastien | 14 h le 29/04/2026 |

---

## Questions en suspens

1. **Nom exact de la variable à modifier** pour le PIN BBB (clarifié mais à confirmer dans la PR).
2. **Intégration du code unique** : sera‑t‑il inclus dans la release 1.3 ou reporté à une version ultérieure ? (à valider avec Benoît / Pierre).
3. **Stabilité de Nextcloud** : cause exacte (surcharge, lib Python, durée du token) reste à identifier.
4. **Support juridique** pour le projet de messagerie nationale (salon silencieux).
5. **Adaptations nécessaires avec Renater** pour le connecteur BBB (technologies différentes).

---

## Tâches à effectuer

| Tâche | Responsable | Échéance |
|-------|-------------|----------|
| Envoyer l’invitation du point bi‑hebdomadaire. | **Benjamin** | Immédiat |
| Ajouter le paramètre BBB dans la PR + description. | **Équipe dev** (Benjamin) | Avant 14 h |
| Rédiger le scénario de test v3 (pin & numéro). | **Benjamin / Miguel** | Avant 14 h |
| Vérifier l’ordre des migrations dans la release. | **Benjamin** | Avant 14 h |
| Conserver la remontée de logs du ticket #666. | **Équipe dev** | Release 1.3 |
| Reproduire le problème de token Nextcloud et documenter. | **Benoît** | Semaine prochaine |
| Finaliser le budget et obtenir le financement pour les 2 025 jours. | **Michael** | À définir |
| Préparer le dossier de financement DGFI pour le connecteur BBB. | **Michael** | Dès validation |
| Envoyer le tableau d’estimation des tags (jours/heure). | **Michael** | Fin de journée |
| Effectuer la release 1.3 (déploiement, tests). | **Benjamin & Sébastien** | 14 h le 29/04/2026 |
| Organiser une réunion avec Renater pour les adaptations du connecteur. | **Michael** | Prochaine semaine |

---

## Prochaine rencontre
- **Date** : Mercredi **6 mai 2026**
- **Heure** : 11 h 30
- **Objet** : Suivi des actions listées ci‑dessus, état de la stabilité Nextcloud, avancement du salon silencieux et du connecteur BBB.

---

*Fin du compte rendu.*
