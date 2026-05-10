# Compte rendu de réunion

**Date** : 30 avril 2026
**Durée estimée** : ~1 heure

---

## Participants
| Nom | Rôle / Fonction |
|-----|-----------------|
| Mickaël | Responsable du suivi du backlog et des releases |
| Loan | (prévu) Expert produit & process (absent au début) |
| Benoît | Responsable du tableau Kanban / produit |
| Benjamin | Développeur, suivi des migrations |
| Sébastien | Contributeur aux scripts de migration |
| Autres (non nommés) | Participants aux échanges techniques |

---

## Objet de la réunion
- Revoir l’état du **backlog** et la structure du tableau Kanban (colonnes *Backlog, Ready, In‑Progress, Done*).
- Valider le **processus de release** (branches `main` / `production`, tags, création de releases sur GitHub).
- Définir les **informations à inclure** dans les notes de release (tickets, changements de configuration, migrations).
- Identifier les actions de nettoyage et de documentation à réaliser.

---

## Sujets abordés

| Sujet | Points clés |
|-------|-------------|
| **État du tableau Kanban** | - Colonne *Done* remplie de tickets anciens et non triés.<br>- Ambiguïté entre colonnes *Ready* et *In‑Progress*.<br>- Proposition de créer une colonne « À trier » pour libérer le backlog. |
| **Responsabilités de tri** | - Mickaël s’engage à nettoyer la colonne *Done* et à reclasser chaque ticket dans la colonne adéquate.<br>- Benoît sera consulté pour ne pas perturber son workflow. |
| **Processus de release** | - `main` = branche de développement.<br>- `production` = branche de release, mise à jour par merge depuis `main`.<br>- Utilisation de `git tag` (ex. `v1.3.0`) + option `--follow-tags` pour pousser le tag.<br>- Création de la release sur GitHub à partir du tag. |
| **Contenu des notes de release** | - Lister les tickets (avec lien) et un titre descriptif.<br>- Indiquer les **modifications de base** et les **modifications de configuration**.<br>- Ajouter l’**ID de migration** lorsqu’une migration est incluse.<br>- Pas besoin de détailler chaque ticket, le titre suffit pour la vue d’ensemble. |
| **Migrations** | - Les IDs sont des hash générés par la librairie de migration, servant à ordonner les scripts.<br>- Chaque fonctionnalité distincte possède son propre fichier de migration.<br>- Besoin d’afficher ces IDs dans les notes de release pour faciliter le suivi (Benjamin & Mickaël). |
| **Documentation & formation** | - Mise à jour du document de procédure (inclure le workflow de branches, le tagging, la création de release, les infos à reporter).<br>- Enregistrement d’une courte vidéo démonstrative pour référence future. |
| **Gestion des corrections post‑release** | - Corrections mineures (orthographe, texte) seront directement appliquées sur le code déployé, puis une MR sera ouverte pour mettre à jour les sources. |
| **Prochaine itération** | - Point de suivi prévu dans deux semaines (voir section *Prochaine rencontre*). |

---

## Décisions prises
1. **Nettoyage du tableau Kanban**
   - Créer une colonne « À trier » et y déplacer les tickets obsolètes de *Done*.
2. **Structure des releases**
   - Les notes de release contiendront : titre du ticket, lien, indication « modif. base » / « modif. config », ID de migration le cas échéant.
3. **Gestion des branches**
   - Continuer à développer sur `main`, merger dans `production` pour chaque version.
4. **Documentation**
   - Mettre à jour le guide de release (workflow, tags, création de release) et ajouter la vidéo de démonstration.
5. **Responsabilité des corrections**
   - Les petites corrections seront appliquées directement sur le code en production, suivies d’une MR pour la base de code.

---

## Questions en suspens
| Question | Responsable / Suivi |
|----------|---------------------|
| Quels éléments de configuration doivent impérativement être mentionnés dans chaque release ? | Mickaël (définir un format standard) |
| Faut‑il automatiser l’ajout de l’ID de migration dans les notes de release ou le faire manuellement ? | Benjamin (évaluer automatisation) |
| Confirmation du rôle exact de la colonne *Ready* dans le workflow actuel. | Benoît (clarifier et éventuellement réorganiser) |

---

## Tâches à effectuer

| Tâche | Responsable | Échéance |
|-------|-------------|----------|
| Nettoyer la colonne *Done* et reclasser les tickets (création colonne « À trier ») | Mickaël | 1 semaine |
| Mettre à jour le tableau Kanban avec les nouvelles colonnes et le workflow validé | Benoît | 1 semaine |
| Ajouter les IDs de migration aux tickets concernés et les reporter dans les notes de release | Benjamin & Mickaël | 2 semaines |
| Rédiger le guide de release (branches, tags, création de release, format notes) | Mickaël | 2 semaines |
| Enregistrer et partager une vidéo de démonstration du processus de release | Mickaël | 2 semaines |
| Vérifier et documenter les changements de configuration pour la version 3.1.dev | Mickaël | Avant la prochaine release |
| Créer le ticket récapitulatif « Release 3.1.0 » incluant toutes les infos (tickets, config, migrations) | Mickaël | Avant la prochaine release |

---

## Prochaine rencontre
- **Date prévue** : dans deux semaines (à confirmer).
- **Objectif** : Faire le point sur le nettoyage du backlog, valider le nouveau format des notes de release et vérifier la mise à jour de la documentation.

---

*Fin du compte rendu.*
