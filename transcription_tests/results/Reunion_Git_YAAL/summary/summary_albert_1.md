# Compte‑rendu de réunion

**Date** : 30 avril 2026
**Durée estimée** : ~1 heure

---

## Participants
| Nom | Rôle / Fonction |
|-----|-----------------|
| **Loan** | Développeur (maîtrise du produit) |
| **Mickaël** | Responsable du Kanban / suivi des tickets |
| **Benoît** | Responsable produit / workflow du tableau |
| **Benjamin** | Responsable des migrations et de la base de données |
| **Sébastien** | Contributeur (questions sur les migrations) |
| **Présentateur** (vous) | Responsable documentation & coordination release |
| Autres (participants non nommés) | Équipe de développement / déploiement |

---

## Objet de la réunion
- Faire le point sur l’avancement de la documentation et son accessibilité.
- Nettoyer et harmoniser le tableau Kanban du dépôt **B3desk**.
- Valider le processus de **release** (branches, merges, tags, notes).
- Définir les informations à inclure dans les notes de release (tickets, configs, migrations).
- Clarifier les responsabilités entre développement, tests et déploiement.

---

## Sujets abordés

| N° | Sujet | Points clés |
|----|-------|-------------|
| 1 | **Présence de Loan** | Loan devrait être présent, mais la réunion peut commencer sans lui. |
| 2 | **Documentation** | Traduction et clarification pour les non‑experts ; mise à jour prévue. |
| 3 | **Kanban B3desk** | - Colonne *Backlog* remplie progressivement.<br>- Colonne *Ready* jugée superflue ou mal placée.<br>- Colonne *Done* (appelée « d’âne ») très encombrée.<br>- Proposition de créer une colonne **« à trier »** pour libérer le tableau. |
| 4 | **Processus de release** | - Branches : `main` (développement) → `production` (releases).<br>- Merge de `main` dans `production` avec gestion des conflits (versions, `pyproject`, `init`).<br>- Création du tag `v1.3.0` puis `git push --follow-tags`. |
| 5 | **Notes de release** | Doivent contenir : <br>• Liens vers les tickets (titre suffisant).<br>• Modifications de base.<br>• Modifications de configuration (le cas échéant).<br>• Identifiant de chaque migration. |
| 6 | **Migrations** | - Les IDs sont des hachages générés par une librairie de migration.<br>- Chaque migration possède son propre fichier et doit être exécutée dans l’ordre.<br>- Besoin d’ajouter ces IDs dans les notes de release. |
| 7 | **Responsabilités** | - Développeurs → merges, résolutions de conflits.<br>- Présentateur → tests de livraison, retours, mise à jour doc.<br>- Benoît → validation du workflow Kanban.<br>- Benjamin → suivi des migrations. |
| 8 | **Communication & pérennité** | - Formaliser le processus de release pour faciliter la prise en main par d’autres équipes ou prestataires.<br>- Créer un ticket récapitulatif par version dans le Kanban. |

---

## Décisions prises

| Décision | Responsable(s) | Commentaire |
|----------|----------------|-------------|
| Démarrer la réunion même si Loan n’est pas présent. | Tous | Possibilité d’attendre si besoin. |
| Nettoyer la colonne **Done** (« d’âne ») et créer une colonne **« à trier »**. | Mickaël (avec l’aide de l’équipe) |
| Conserver la colonne **Ready** tant que le workflow de Benoît n’est pas impacté ; réévaluer ultérieurement. | Benoît & Mickaël |
| Processus de release officiel : merge `main → production`, résolution des conflits, création du tag, publication sur GitHub. | Développeurs (Mickaël, Benoît) |
| Les notes de release incluront tickets, modifications de base, config et ID de migration. | Présentateur (mise à jour) + Benjamin (IDs) |
| Créer un ticket récapitulatif dans le Kanban pour chaque version (ex. : 1.3.0). | Mickaël |
| Mettre à jour la documentation avec le nouveau processus et les exemples de release. | Présentateur |
| Vérifier s’il y a de nouvelles configurations pour la version 1.3.0. | Benoît (ou développeur concerné) |
| Ajouter les IDs de migration dans les notes de release. | Benjamin |

---

## Questions en suspens

1. **Rôle exact de la colonne « Ready »** – pourquoi elle existe et où doit‑elle se placer ?
2. **Présence de nouvelles configurations** dans la release v1.3.0 (ticket 39) – confirmation attendue.
3. **Format final des notes de release** : titre uniquement vs description succincte.
4. **Clarification du flux entre `main` et `production`** pour les équipes moins familières.
5. **Gestion des écrans de démonstration** (effet « démo ») – impact éventuel sur la présentation des releases.

---

## Tâches à effectuer

| Tâche | Responsable | Échéance |
|-------|-------------|----------|
| Nettoyer la colonne **Done** et créer la colonne **« à trier »**. | Mickaël | Prochaine réunion |
| Mettre à jour la documentation (processus de release, usage du Kanban). | Présentateur | 2 semaines |
| Ajouter les IDs de migration dans les notes de release. | Benjamin | Avant la prochaine release |
| Créer un ticket récapitulatif pour la version 1.3.0 dans le Kanban. | Mickaël | Immédiat |
| Vérifier et confirmer l’absence/presence de nouvelles configurations pour la release 1.3.0. | Benoît | Avant le merge final |
| Formaliser le format des notes de release (titre + lien ticket). | Mickaël & Présentateur | Avant la prochaine release |
| Communiquer le processus de release à l’ensemble des équipes (démo + documentation). | Présentateur | 2 semaines |

---

## Prochaine rencontre

- **Date prévue** : dans **deux semaines** (à confirmer).
- **Objectif** : Faire le point sur le nettoyage du Kanban, valider la documentation mise à jour et préparer la prochaine release.

---

*Fin du compte‑rendu.*
