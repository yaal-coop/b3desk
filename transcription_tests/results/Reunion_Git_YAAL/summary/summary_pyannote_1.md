# Compte‑rendu de réunion
**Date** : 30 avril 2026
**Durée estimée** : ~1 h 30

---

## Participants
| Nom | Rôle / Fonction |
|-----|-----------------|
| **Lohan** | (absent au début, prévu) |
| **Michael** | Développeur / responsable du suivi Kanban |
| **Benoît** | Responsable du backlog et du processus de release |
| **Benjamin** | Expert migrations / base de données |
| **Mickey** | (intervenant ponctuel) |
| **Autres** | Participants non nommés (présents à l’appel) |

---

## Objet de la réunion
- Faire le point sur le **déploiement** du projet **Surbandoc** (repo *B3 Desk*).
- Nettoyer le tableau Kanban (colonnes *Ready*, *In Progress*, *Done*).
- Formaliser le **processus de release** (branches Git, tags, notes de version).
- Clarifier la gestion des **migrations** et de la **configuration** dans les releases.

---

## Sujets abordés

| # | Sujet | Points clés |
|---|-------|-------------|
| 1 | **Présence de Lohan** | Décision de commencer sans lui, attendre si besoin. |
| 2 | **Problème de vue projet / backlog** | - Le tableau a été modifié par Benoît (suppression de versions mineures). <br>- Confusion entre colonnes *Ready* et *In Progress*. |
| 3 | **Nettoyage du Kanban** | - Déplacer les tickets *Ready* → *In Progress*.<br>- Créer une colonne **« à trier »** pour les items anciens dans *Done*.<br>- Vider la colonne *Done* après tri. |
| 4 | **Workflow Git** | - Branches : `main` (développement), `production` (release). <br>- Merge Requests sont validées puis mergées dans `main`. <br>- `production` est mise à jour à partir de `main` lors d’une release. |
| 5 | **Création d’une release (v1.3)** | - Résolution des conflits (`init`, `pyproject`). <br>- Tag `v1.3` créé et poussé avec `git push --tags`. <br>- Publication via l’interface GitHub (choix du tag). |
| 6 | **Contenu des notes de version** | - Lister les tickets associés (liens). <br>- Indiquer les **modifs de configuration** et **migrations**. <br>- Pas besoin de description détaillée si le ticket est consultable. |
| 7 | **Gestion des migrations** | - Chaque migration possède un **ID** généré par la librairie de migration. <br>- Les IDs permettent de savoir quelles migrations ont été appliquées sur chaque instance. <br>- Les migrations sont séparées par fonctionnalité (ex. classement salons vs code unique). |
| 8 | **Améliorations à apporter** | - Ajouter l’ID de migration dans les notes de release. <br>- Créer un ticket dédié à la release 1.3.0 (colonne *1.3.0*) regroupant config & base changes. <br>- Mettre à jour la documentation du processus de release. |
| 9 | **Points divers** | - Erreurs 500 et de connexion déjà résolues dans `main`. <br>- Gestion des petites corrections (texte, orthographe) directement dans le code déployé, suivi d’une PR ultérieure. |

---

## Décisions prises
| Décision | Responsable(s) | Commentaire |
|----------|----------------|-------------|
| Démarrer la réunion sans Lohan. | – | Lohan pourra rejoindre plus tard si besoin. |
| Déplacer les tickets *Ready* → *In Progress* et créer la colonne **« à trier »**. | Michael (avec l’aide de l’équipe) | Nettoyage du Kanban. |
| Utiliser les tags Git (`vX.Y`) pour chaque release et publier via GitHub. | Michael | Processus standardisé. |
| Les notes de version contiendront : <br>• liens vers les tickets <br>• bref descriptif (si nécessaire) <br>• ID de migration (le cas échéant). | Michael | Conformité avec les attentes de Benoît/Benjamin. |
| Créer un ticket « Release 1.3.0 » regroupant toutes les infos de config et de base. | Michael | Facilite le suivi futur. |
| Mettre à jour la documentation du workflow (branches, merges, tags, migrations). | Michael | Documentation à diffuser à l’équipe. |
| Les petites corrections de texte seront appliquées directement sur le code déployé, puis suivies d’une PR. | Toute l’équipe | Gain de temps, suivi assuré. |

---

## Questions en suspens
| Question | Responsable | État |
|----------|-------------|------|
| Niveau de détail souhaité dans les notes de version (juste lien ticket ou description supplémentaire) ? | Benoît / Michael | À confirmer lors du prochain point. |
| Validation finale du format de la colonne **« à trier »** (critères de déplacement) ? | Michael | À valider avec Benoît. |
| Intégration automatisée de l’ID de migration dans les releases (script ou manuel) ? | Benjamin | À étudier. |

---

## Tâches à effectuer

| Tâche | Responsable | Échéance |
|-------|-------------|----------|
| Nettoyer le Kanban : déplacer les tickets, créer la colonne *à trier* et vider *Done*. | Michael | 2 mai 2026 |
| Ajouter les ID de migration aux notes de version de la release 1.3.0. | Michael | 3 mai 2026 |
| Créer le ticket **Release 1.3.0** (colonne *1.3.0*) avec les infos config/base. | Michael | 2 mai 2026 |
| Mettre à jour la documentation du processus de release (branches, tags, migrations). | Michael | 5 mai 2026 |
| Vérifier avec Benoît le positionnement des tickets dans les colonnes *Ready* / *In Progress*. | Michael | 2 mai 2026 |
| Confirmer le niveau de détail des notes de version (avec Benoît). | Michael | 3 mai 2026 |
| Étudier l’automatisation de l’inclusion de l’ID de migration dans les releases. | Benjamin | 10 mai 2026 |

---

## Prochaine rencontre
- **Date proposée** : 12 mai 2026 (ou à définir).
- **Objectif** : Faire le point sur le nettoyage du Kanban, valider la nouvelle structure des notes de version et vérifier l’intégration des IDs de migration.

---

*Fin du compte‑rendu.*
