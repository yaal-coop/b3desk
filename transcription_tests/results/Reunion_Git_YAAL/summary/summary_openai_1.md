# Compte rendu de réunion

**Date** : 4 mai 2026
**Durée estimée** : ~45 minutes

---

## Participants
- **Lohan** (prévu mais absent au début)
- **Benoît** (responsable du tableau Kanban)
- **Benjamin** (gestion des migrations)
- **Sébastien** (intervenant technique)
- **Mickaël** (intervenant technique)
- **Vous** (présentateur de la documentation)
- Autres membres de l’équipe (non nommés explicitement)

---

## Objet de la réunion
Revoir et améliorer le processus de documentation, de gestion du backlog et de publication des releases (branches, tags, notes de version) pour le projet **B3desk**.

---

## Sujets abordés

| N° | Sujet | Points clés |
|----|-------|-------------|
| 1 | **Présence de Lohan** | Décision d’attendre ou de commencer sans lui. |
| 2 | **Documentation** | Traduction et clarification pour les non‑experts ; ajout de commandes manquantes. |
| 3 | **Backlog / Kanban** | - Problème de la colonne **Don** (trop remplie, tickets anciens). <br>- Confusion entre colonnes **Don**, **Redis**, **In Progress**. <br>- Proposition de créer une colonne **« A trier »** pour les tickets à nettoyer. |
| 4 | **Environnement de travail** | Utilisation de ZSH avec le thème *Spaceship* ; discussion sur la customisation du prompt. |
| 5 | **Workflow Git** | - Branches : **main** (développement) → **production** (releases). <br>- Merge de `main` vers `production` avec résolution de conflits (ex. `init`, `pyproject`). <br>- Création de tags (ex. `v1.3.0`). |
| 6 | **Création des releases GitHub** | - Contenu des notes : liens vers tickets, titres, résumés, modifications de configuration et de base, identifiants de migration. <br>- Décision d’inclure uniquement le titre + lien du ticket (suffisant pour la vue d’ensemble). |
| 7 | **Migrations** | - IDs générés par la librairie de migration, importance de l’ordre. <br>- Chaque fonctionnalité distincte → fichier de migration séparé. <br>- Besoin d’ajouter les IDs de migration dans les notes de version. |
| 8 | **Responsabilités & communication** | - Benoît : gestion du tableau Kanban. <br>- Vous : mise à jour de la documentation et nettoyage du backlog. <br>- Benjamin : veiller à ce que les IDs de migration soient renseignés dans les releases. |
| 9 | **Prochaine itération** | Planification d’une réunion de suivi dans deux semaines. |

---

## Décisions prises

1. **Début de la réunion** : on peut démarrer sans Lohan, mais on attendra s’il arrive rapidement.
2. **Backlog** :
   - Nettoyer la colonne **Don** immédiatement.
   - Créer une colonne **« A trier »** pour les tickets anciens/non‑classés.
3. **Workflow Git** :
   - `main` reste la branche de développement, `production` la branche de release.
   - Après chaque merge de `main` → `production`, créer un tag (ex. `v1.3.0`).
4. **Notes de release** :
   - Inclure le titre du ticket + lien.
   - Mentionner les changements de configuration et de base.
   - Ajouter l’identifiant de chaque migration concernée.
5. **Responsabilités** :
   - Benoît : valider l’organisation du Kanban.
   - Vous : mettre à jour la doc, nettoyer le backlog, préparer le modèle de notes de release.
   - Benjamin : s’assurer que les IDs de migration sont renseignés dans les releases.
6. **Suivi** : une nouvelle réunion sera programmée dans deux semaines.

---

## Questions en suspens

| Question | Responsable / Action |
|----------|----------------------|
| Quelle est la fonction exacte de la colonne **Redis** vs **Don** ? | Clarifier avec Benoît. |
| Y a‑t‑il des nouvelles configurations à ajouter pour la version en cours ? | Vérifier les tickets associés (ex. ticket de configuration). |
| Quels tickets de la colonne **Don** ont déjà été inclus dans des releases précédentes ? | Benoît / vous (revue du tableau). |
| Peut‑on automatiser l’inclusion du diff de fichiers dans les notes de release ? | Étudier les options GitHub (ex. `release-drafter`). |
| Qui finalisera la publication de la release après le push du tag ? | À confirmer (probablement Benoît). |

---

## Tâches à effectuer

| Tâche | Responsable | Échéance |
|-------|--------------|----------|
| Nettoyer la colonne **Don** et déplacer les anciens tickets vers **« A trier »** | Vous | Immédiate |
| Mettre à jour la documentation avec les nouvelles étapes de release (branches, tags, notes) | Vous | Avant la prochaine release |
| Discuter avec Benoît du workflow des colonnes **Don / Redis / In Progress** | Vous | Dans les 2 jours |
| Ajouter les IDs de migration dans les notes de release (ex. `20231215_add_meeting_fields`) | Benjamin | À chaque release |
| Créer la release `v1.3.0` sur GitHub avec les tickets, configs, migrations | Benoît (ou équipe release) | Dès que le merge `main → production` est résolu |
| Vérifier et documenter les éventuels changements de configuration pour la version actuelle | Vous / Mickaël | Avant la publication |
| Programmer la prochaine réunion de suivi (dans 2 semaines) | Vous | D’ici fin de semaine |

---

## Prochaine rencontre

- **Date** : dans deux semaines (date précise à confirmer).
- **Objectif** : faire le point sur le nettoyage du backlog, valider le nouveau modèle de notes de release et vérifier la bonne mise en place des migrations.

---

*Fin du compte rendu.*
