# Compte rendu de réunion
**Date** : 28 avril 2026
**Durée** : ~ 2 h 30 (prévu 1 h, débordement)

---

## Participants
| Nom | Rôle / Fonction |
|-----|-----------------|
| **Johan** | Animateur de la réunion |
| **Benjamin** | Développeur B3Desk |
| **Michael** | Responsable technique / backlog |
| **Benoît** | Testeur / support infra |
| **Sébastien** | Responsable des releases |
| **Priscila** | (mentionnée pour les tests) |
| **Mickaël** | Responsable estimation des tâches |
| **Autres** | Participants ponctuels (ex. : personnes du service messagerie) |

---

## Objet de la réunion
Suivi d’avancement du projet **B3Desk** (code unique, configuration BBB/ScaleLight, ticket 166, stabilité Nextcloud, salon silencieux, planification des releases et estimation du backlog).

---

## Sujets abordés

| N° | Sujet | Points clés |
|----|-------|-------------|
| 1 | **Rythme des points de suivi** | Proposition d’un point toutes les 2 semaines. Décision : **mercredi 11 h 30**. |
| 2 | **Livraison du code unique** | - Pas de développement supplémentaire, seulement modification de configuration (ScaleLight/BBB). <br> - Besoin de préciser le paramètre dans la PR et la release. |
| 3 | **Configuration *BBB Dial Number*** | - Nécessité d’ajouter le numéro de téléphone dans la configuration Métroidesque. <br> - Variable `dialNumber` à documenter. |
| 4 | **Ticket 166 – Erreur 500 salon** | - Résolu côté Arawa (suppression d’un champ). <br> - Conserver la remontée de log dans la prochaine release. |
| 5 | **Stabilité de la connexion Nextcloud / Nuage** | - Analyse des captures de trames : problème possible de surcharge du serveur WebDAV ou de la bibliothèque Python. <br> - Actions : reproduire le bug, vérifier les versions des librairies, éventuellement allonger la durée du token (30 j → plus). |
| 6 | **Projet SIP Media Gateway** | - Financement DGFIP, besoin d’un connecteur SIP pour BBB. <br> - Dépendance vis‑à‑vis de Renater (développement interne). |
| 7 | **Salon silencieux & devis** | - Devis validé, budget 2025 alloué. <br> - Lancement possible dès que le support juridique sera confirmé. |
| 8 | **Backlog & estimation** | - Utilisation de tags (Small, Medium, Large) pour chiffrer les tâches. <br> - Demande d’un tableau de correspondance (jours/homme). |
| 9 | **Planification des releases** | - **Release 1.3** : inclure le classement des salles, favoris, etc. <br> - **Release 1.3.1** (ou ultérieure) : intégrer le code unique / numéro d’appel après validation. |
| 10 | **Procédure de création de release** | Sébastien présentera la procédure l’après‑midi; Benjamin la suivra en direct. |

---

## Décisions prises
| Décision | Responsable / Commentaire |
|----------|---------------------------|
| Instaurer un point de suivi bi‑hebdomadaire le **mercredi 11 h 30**. | Johan (organisation) |
| Ajouter la modification de configuration (ScaleLight/BBB) dans la PR et la release notes. | Johan (préciser) |
| Conserver la remontée de log du ticket 166 dans la prochaine release. | Benjamin |
| Poursuivre l’investigation Nextcloud / Nuage jusqu’à reproduction du problème. | Benoît & Benjamin |
| Lancer le **salon silencieux** dès validation du support juridique (budget déjà ok). | Michael |
| Publier la **release 1.3** avec le classement des salles / favoris ; reporter le code unique et le numéro d’appel à une release ultérieure (1.3.1). | Sébastien (release) |
| Fournir, d’ici la fin de journée, un tableau de correspondance **tags ↔ estimation (jours/homme)**. | Mickaël |
| Sébastien animera la session de création de release l’après‑midi (≈ 14 h). | Sébastien & Benjamin |

---

## Questions en suspens
1. **Intégration du code unique** : dans quelle release (1.3 ou 1.3.1) ?
2. **Ordre des migrations** : confirmation que la migration de tri sera exécutée avant celle du code unique.
3. **Mise à jour des librairies WebDAV** : quelles versions sont compatibles avec la version actuelle de Nextcloud ?
4. **Support juridique** pour le salon silencieux : délai d’obtention.
5. **Calendrier du projet SIP Media Gateway** : dates de démarrage et livrables attendus.

---

## Tâches à effectuer

| Tâche | Responsable | Échéance |
|-------|-------------|----------|
| Envoyer la proposition de créneau (mercredi 11 h 30) à tous les participants. | **Benjamin** | Lundi 28 avril |
| Ajouter le paramètre ScaleLight/BBB dans la PR et la release notes. | **Johan** | Avant la prochaine release |
| Documenter la variable `dialNumber` dans la PR. | **Johan** | Immédiat |
| Vérifier et, si besoin, mettre à jour la bibliothèque Python WebDAV. | **Benoît** | Avant le prochain test (début mai) |
| Reproduire le problème de connexion Nextcloud et fournir un rapport de logs. | **Benjamin** | 5 mai 2026 |
| Rédiger le tableau de correspondance **tags ↔ estimation** (jours/homme). | **Mickaël** | Fin de journée (28 avril) |
| Préparer la session de création de release (script, étapes). | **Sébastien** | 28 avril après‑midi |
| Valider le support juridique pour le salon silencieux. | **Michael** | Au plus tard 10 mai 2026 |
| Planifier une réunion de suivi du projet SIP Media Gateway avec Renater. | **Johan** | Semaine du 12 mai |

---

## Prochaine rencontre
**Date** : Mercredi 3 mai 2026
**Heure** : 11 h 30 (point bi‑hebdomadaire)

Ordre du jour prévu :
- Suivi des actions listées ci‑dessus
- Retour sur la reproduction du problème Nextcloud
- Validation du planning de la release 1.3
- Mise à jour du statut du salon silencieux et du projet SIP Media Gateway.
