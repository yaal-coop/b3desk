# Compte rendu de réunion

**Date** : 30 avril 2026
**Durée** : non précisée (environ 1 h)

## Participants
| Nom | Rôle / Fonction |
|-----|-----------------|
| **Loan** | (prévu, absent au début) |
| **Mickaël** | Développeur / responsable du repo B3desk |
| **Benoît** | Responsable du backlog et du processus produit |
| **Sébastien** | Développeur (migration DB) |
| **Benjamin** | Responsable des migrations / déploiement |
| **Zin** | (intervenant ponctuel) |
| **Autres** | Participants non nommés (ex. interlocuteur qui traduit la doc) |

## Objet de la réunion
- Faire le point sur l’avancement du **déploiement** du projet *SerpentDoc* (repo B3desk).
- Nettoyer et structurer le tableau de suivi (backlog).
- Formaliser le **processus de release** (branches, tags, notes).
- Clarifier la gestion des **migrations** et des changements de configuration.

## Sujets abordés
| N° | Sujet | Points clés |
|----|-------|-------------|
| 1 | Présence de Loan | Loan devait être présent, mais la réunion a pu démarrer sans lui. |
| 2 | Traduction / documentation | Une version traduite de la documentation a été présentée pour la rendre plus claire. |
| 3 | Tableau de suivi (B3desk) | - Colonnes « Backlog », « Redis », « Dawn » mal utilisées. <br>- Risque de duplication entre *Redis* et *Dawn*. <br>- Proposition de nettoyer la colonne « Ready » et de créer une colonne « À trier ». |
| 4 | Processus de merge & branches | - `main` = branche de développement (features, tests). <br>- `production` = branche de release. <br>- Pour chaque version, on merge `main` → `production`, puis on crée un tag. |
| 5 | Gestion des conflits de merge | Conflits attendus sur `__init__` et `pyproject.toml` (numéros de version). |
| 6 | Création du tag & publication de la release | Utilisation de `git tag` + `git push --follow-tags`. <br>- La page *Releases* de GitHub montre les commits et permet de comparer les versions. |
| 7 | Contenu des notes de release | - Lister les tickets (avec lien et titre). <br>- Indiquer les changements de base et de configuration. <br>- Ajouter les identifiants de migration. |
| 8 | Gestion des migrations | - Les IDs sont générés par une librairie et servent à ordonner les migrations. <br>- Chaque fonctionnalité distincte possède son propre fichier de migration. |
| 9 | Améliorations à venir | - Créer un ticket Kanban par version (ex. colonne `1.3.0`) regroupant toutes les infos de release. <br>- Mettre à jour la documentation avec les nouvelles procédures. |
| 10 | Points divers | - Problème d’affichage d’écran (effet “words”); <br>- Discussion sur les prompts ZSH/Spaceship (hors sujet principal). |

## Décisions prises
| Décision | Responsable(s) | Commentaire |
|----------|----------------|-------------|
| Démarrer la réunion même si Loan est absent. | Tous | Loan pourra être briefé après. |
| Nettoyer le tableau de suivi : déplacer les tickets de la colonne « Ready » vers les colonnes adéquates (InProgress, Backlog) et créer une colonne « À trier ». | Mickaël (avec Benoît) | Mickaël effectuera le tri, Benoît validera. |
| Utiliser le workflow **main → production → tag** pour chaque release. | Benjamin (déploiement) | Benjamin gérera les merges et résoudra les conflits. |
| Les notes de release contiendront : <br>• lien + titre du ticket <br>• changements de base <br>• changements de configuration <br>• ID de migration. | Mickaël (rédaction) | Mickaël ajoutera ces éléments dans chaque release. |
| Créer un ticket Kanban dédié à chaque version (ex. `1.3.0`) qui regroupe toutes les infos de la release. | Benoît | Benoît ouvrira le ticket et y consistera les informations. |
| Mettre à jour la documentation avec les procédures de merge, tag, release et les IDs de migration. | Interlocuteur qui a traduit la doc (nom non précisé) | Documentation à finaliser avant la prochaine release. |
| Aucun changement de configuration n’est prévu pour la version courante (v1.3). | Tous | Confirmation donnée pendant la réunion. |

## Questions en suspens
1. **Pourquoi la colonne « reddit » existe‑t‑elle dans le tableau ?** – À clarifier avec Benoît.
2. **Y a‑t‑il d’autres changements de configuration prévus pour la prochaine version (3.1 dev) ?** – À vérifier avant le prochain merge.
3. **Quel format exact doit prendre la description des tickets dans les notes de release ?** – Décision à finaliser (titre seul ou titre + courte description).
4. **Qui sera le garant du suivi des conflits récurrents lors du merge `main → production` ?** – Confirmation du rôle de Benjamin.

## Tâches à effectuer
| Tâche | Responsable | Échéance |
|-------|-------------|----------|
| Nettoyer le tableau B3desk (déplacer tickets, créer colonne « À trier ») | Mickaël (avec Benoît) | Avant la prochaine release |
| Fusionner `main` dans `production`, résoudre les conflits (`__init__`, `pyproject.toml`) | Benjamin | Immédiat (release v1.3) |
| Créer le tag `v1.3` et pousser avec `--follow-tags` | Benjamin | Immédiat |
| Rédiger les notes de release (tickets, config, migrations) | Mickaël | Avant publication de la release |
| Ouvrir un ticket Kanban `1.3.0` regroupant toutes les infos de la release | Benoît | Avant la fin du sprint |
| Mettre à jour la documentation (procédure de release, IDs migration) | [Nom non précisé] (traducteur) | Avant la prochaine réunion |
| Vérifier l’existence éventuelle de nouvelles configurations pour la version 3.1 dev | Tous (validation) | Avant le merge de la branche dev |
| Ajouter les IDs de migration dans les notes de release (ex. `migration‑2024‑03‑12‑add‑isFavorite`) | Mickaël | Dès la rédaction des notes |
| Préparer la prochaine réunion de suivi (date/heure) | Sébastien | À planifier |

## Prochaine rencontre
- **Date / heure** : à définir (à planifier).
- **Objectif** : Faire le point sur le nettoyage du backlog, valider la release v1.3 et préparer la version 3.1 dev.

---

*Ce compte rendu a été rédigé à partir de la transcription de la réunion et synthétise les points essentiels pour le suivi du projet.*
