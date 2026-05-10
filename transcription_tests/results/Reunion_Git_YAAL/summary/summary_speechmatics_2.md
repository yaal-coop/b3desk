# Compte rendu de réunion

**Date** : 5 mai 2026
**Durée estimée** : ~1 h (début ≈ 09 h 30 – fin ≈ 10 h 30)

---

## Participants
| Nom | Rôle / fonction |
|-----|-----------------|
| **Laurent** | Expert produit & process |
| **Loan** | (absent, prévu) |
| **Benoît** | Responsable du Kanban / backlog |
| **Benjamin** | Développeur, suivi des migrations |
| **Michael** | Développeur |
| **Sébastien** | Développeur (questions sur les migrations) |
| **Intervenant principal** (vous) | Responsable documentation, tests de déploiement |

---

## Objet de la réunion
Passer en revue le **processus de release** (branches, tags, notes), **nettoyer le tableau Kanban** (colonnes « Down », « Ready », etc.) et **formaliser la documentation** afin que les équipes de développement et d’exploitation disposent d’une procédure claire et reproductible.

---

## Sujets abordés

| N° | Sujet | Points clés |
|----|-------|-------------|
| 1 | **Présence de Loan** | Décision d’attendre Loan avant de commencer le travail. |
| 2 | **Partage de la documentation** | Écran partagé, mise à jour du doc de déploiement, ajout de nouvelles commandes si besoin. |
| 3 | **Kanban – colonne « Down »** | - Accumulation d’anciennes tâches. <br>- Confusion avec les colonnes *Backlog* et *Ready*. <br>- Proposition de créer une colonne « À trier » ou de nettoyer la colonne existante. |
| 4 | **Flux de travail Git** | - `main` = branche de développement. <br>- `production` = branche de release. <br>- Processus de merge : création de branche feature → merge dans `main` → merge de `main` → `production`. |
| 5 | **Création de tags & releases** | - Tagger chaque release (ex. `v1.3`). <br>- Utiliser l’option `--follow-tags` lors du push. <br>- Rédiger les notes de release : titres des tickets, liens, changements de config/base, ID de migration. |
| 6 | **Gestion des migrations** | - Les IDs sont générés par une librairie interne. <br>- Chaque migration possède son propre fichier (ex. classement salons, code unique). <br>- Nécessité d’indiquer l’ID et le nom de version dans les notes de release. |
| 7 | **Documentation & formation** | - Vidéo de démonstration du processus de release à créer. <br>- Ajout d’une section « Migrations » dans la doc. |
| 8 | **Responsabilités entre dev & ops** | - Développeurs créent les releases. <br>- Intervenant teste la livraison, signale les retours. <br>- Aucun besoin d’interférer dans le process de dev sauf corrections mineures. |

---

## Décisions prises

| Décision | Responsable(s) | Commentaire |
|----------|----------------|-------------|
| Attendre Loan avant de démarrer le travail. | Tous | Le meeting a été mis en pause jusqu’à son arrivée. |
| Nettoyer la colonne « Down » du Kanban et, si besoin, créer une colonne « À trier ». | **Intervenant principal** (avec Benoît) |
| Utiliser `main` pour le développement et `production` pour les releases. | Tous |
| Rédiger les notes de release avec : <br>• Titre du ticket + lien <br>• Modifications de base et de config <br>• ID de migration (le cas‑échéant) | **Intervenant principal** (mise à jour) |
| Créer un ticket récapitulatif dans le Kanban pour chaque version (regroupant config/base + migrations). | **Benjamin** (proposition) – à valider par l’équipe |
| Produire une courte vidéo tutorielle du processus de release. | **Intervenant principal** |
| Benoît reste le référent pour le ré‑organisation du Kanban. | **Benoît** |

---

## Questions en suspens

| Question | Responsable(s) | État |
|----------|----------------|------|
| Pourquoi la colonne « Down » est‑elle remplie de tickets anciens ? | **Benoît** | En attente d’explication. |
| Niveau de détail souhaité dans les notes de release (juste titres vs description complète). | **Intervenant principal** & **Équipe** | Décision partielle : titres + lien suffisent, mais on garde la possibilité d’ajouter une courte description. |
| Suivi des changements de configuration : où les consigner de façon fiable ? | **Équipe** | Proposition d’utiliser le ticket récapitulatif par version. |
| Gestion des corrections rapides (ex. texte affiché) par Benoît : procédure à formaliser. | **Benoît** | À préciser lors du prochain point. |

---

## Tâches à effectuer

| Tâche | Responsable | Échéance |
|-------|-------------|----------|
| Nettoyer la colonne « Down » du Kanban (déplacer ou supprimer les tickets). | **Intervenant principal** (avec Benoît) | Avant la prochaine release. |
| Ajouter les tickets (titre + lien) et les IDs de migration dans les notes de release. | **Intervenant principal** | Pour la release `v1.3` (déjà faite) et les suivantes. |
| Mettre à jour la documentation de déploiement (process Git, création de tags, migrations). | **Intervenant principal** | D’ici 1 semaine. |
| Créer la vidéo de démonstration du processus de release. | **Intervenant principal** | D’ici 2 semaines. |
| Créer un ticket récapitulatif « Release X.Y » contenant config/base + migrations. | **Benjamin** (ou équipe) | À chaque version. |
| Discuter avec Benoît du ré‑agencement du Kanban (colonne « À trier », suppression de doublons). | **Intervenant principal** | Lors du prochain point. |
| Vérifier et documenter les IDs de migration générés par la librairie interne. | **Sébastien** & **Benjamin** | Avant la prochaine release. |

---

## Prochaine rencontre
Un point de suivi sera envoyé **dans deux semaines** (vers le 19 mai 2026). La date exacte de la prochaine réunion sera fixée à ce moment‑là.

---

*Fin du compte rendu.*
