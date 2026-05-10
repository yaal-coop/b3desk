# Compte rendu de réunion

**Date** : 28 avril 2026
**Durée estimée** : ~1 h 15 min

## Participants
| Nom | Rôle / Fonction |
|-----|-----------------|
| Michael | Développeur / Responsable du déploiement |
| Benoît | Responsable du backlog / Process produit |
| Lohan | Expert produit (présence incertaine au début) |
| Mickaël | (intervenant ponctuel) |
| Benjamin | Expert migrations / Bases de données |
| Autres (non nommés) | Participants occasionnels |

## Objet de la réunion
Mise au point du processus de **déploiement et de release** du projet *Surbandoc* : gestion du backlog, workflow Git, création des tags/releases, documentation et suivi des migrations.

---

## Sujets abordés

| # | Sujet | Points clés |
|---|-------|-------------|
| 1 | **Présence de Lohan** | Décision de commencer la réunion et de reprendre le travail dès son arrivée. |
| 2 | **Backlog & Kanban** | - Confusion entre les colonnes *Ready*, *In Progress* et *Done*.<br>- Proposition de créer une colonne **« À trier »** pour les tickets anciens dans *Done*.<br>- Nettoyage de la colonne *Done* prévu. |
| 3 | **Workflow Git** | - Branches : `main` (développement) → `production` (release).<br>- Merge‑requests validées puis mergées dans `main` puis `production`.<br>- Utilisation de **tags** (`v1.3`, etc.) pour déclencher les releases sur GitHub. |
| 4 | **Création de la release v1.3** | - Merge des changements depuis `main` vers `production` (conflits résolus sur `init` et `pyproject`).<br>- Tag `v1.3` créé et poussé avec l’option `--tags`.<br>- Publication de la release sur GitHub. |
| 5 | **Contenu des notes de release** | - Lister les tickets concernés (lien vers le ticket).<br>- Indiquer les **modifications de configuration** et les **modifications de base**.<br>- Ajouter l’**ID de migration** le cas échéant.<br>- Création d’un ticket Kanban dédié à chaque version (ex. colonne `1.3.0`) pour regrouper ces informations. |
| 6 | **Migrations** | - Les IDs de migration sont générés par une librairie et servent à ordonner les scripts.<br>- Chaque fonctionnalité distincte possède son propre fichier de migration.<br>- Décision d’inclure l’ID de migration dans les notes de release. |
| 7 | **Documentation** | - Explication du shell **ZSH** à ajouter.<br>- Mise à jour du document de procédure de release avec les nouveaux points (tickets, config, migrations). |
| 8 | **Points de vigilance** | - Ne pas casser le workflow de Benoît sur le backlog.<br>- Vérifier que les changements de config sont bien documentés.<br>- S’assurer que les tickets de migration sont correctement liés aux releases. |

---

## Décisions prises

1. **Démarrer la réunion** même si Lohan n’est pas encore présent.
2. **Nettoyer la colonne *Done*** du Kanban et créer une colonne **« À trier »** pour les tickets anciens.
3. **Passer les tickets** de *Ready* à *In Progress* lorsqu’ils sont réellement en cours.
4. **Utiliser le workflow Git** suivant : `main` → merge‑request → `main` → merge vers `production` → tag → release.
5. **Structurer les notes de release** :
   - Lien vers chaque ticket.
   - Brève description (optionnelle).
   - Indication des changements de config et de base.
   - ID de migration le cas échéant.
6. **Créer un ticket Kanban** par version (ex. colonne `1.3.0`) pour centraliser toutes les infos de la release.
7. **Inclure les IDs de migration** dans les notes de release.
8. **Mettre à jour la documentation** (ex. explication ZSH, procédure de release).

---

## Questions en suspens

| Question | Responsable / Suivi |
|----------|---------------------|
| Doit‑on conserver la colonne *Done* telle quelle ou la nettoyer entièrement ? | Benoît (à valider) |
| Niveau de détail souhaité dans les notes de release : lien ticket uniquement ou description supplémentaire ? | Décision collective – à confirmer lors de la prochaine release |
| Validation finale du processus de migration (ordre, regroupement) ? | Benjamin (confirmation technique) |
| Gestion des corrections rapides (ex. fautes d’orthographe) directement en production ? | Accord à obtenir avec l’équipe dev (process à formaliser) |

---

## Tâches à effectuer

| Tâche | Responsable | Échéance |
|-------|-------------|----------|
| Nettoyer la colonne *Done* du Kanban | Michael | Immédiat |
| Créer la colonne **« À trier »** et y déplacer les tickets anciens | Michael | Immédiat |
| Re‑classer les tickets *Ready* → *In Progress* selon leur état réel | Michael | Immédiat |
| Créer le tag `v1.3` et pousser le tag sur le repo | Michael | Déjà fait (vérifier) |
| Publier la release `v1.3` sur GitHub avec les notes (tickets, config, migrations) | Michael | Avant la fin de la journée |
| Ajouter l’explication du shell ZSH dans la documentation | Michael | Avant la prochaine release |
| Mettre à jour le document de procédure de release (inclure les points décidés) | Michael | Avant la prochaine release |
| Vérifier avec Benoît le nouveau workflow Kanban et obtenir son aval | Michael & Benoît | Prochaine réunion |
| Benoît : confirmer la gestion des colonnes *Ready / In Progress / Done* | Benoît | Prochaine réunion |
| Benjamin : fournir un rappel sur la génération des IDs de migration | Benjamin | Prochaine réunion |
| Créer un ticket Kanban « Release 1.3.0 » regroupant toutes les infos | Michael | Avant la publication de la release |
| Envoyer le compte rendu et le planning des actions aux participants | Michael | Aujourd’hui |

---

## Prochaine rencontre

- **Date prévue** : dans **2 semaines** (date exacte à confirmer).
- **Objet** : suivi des actions de nettoyage du Kanban, validation du nouveau format de notes de release et revue du processus de migration pour la version suivante.

---

*Compte rendu rédigé par Michael, 28 avril 2026.*
