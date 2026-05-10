# Compte rendu de réunion

**Date** : 28 avril 2026
**Durée estimée** : ~1 h (heure approximative d’après le déroulement)

## Participants
| Nom | Rôle / Fonction |
|-----|-----------------|
| **Mickaël** | Responsable du suivi du backlog et des releases |
| **Loan** (ou *Loen*) | Expert produit / process, maîtrise du produit |
| **Benoît** | Responsable du tableau Kanban (backlog / releases) |
| **Benjamin** | Développeur, suivi des migrations |
| **Sébastien** | Développeur (intervention sur les migrations) |
| **Autre intervenant** | Rédacteur / testeur, responsable du déploiement et de la documentation |

## Objet de la réunion
- Faire le point sur la documentation du processus de release.
- Nettoyer et réorganiser le tableau Kanban (colonnes *Backlog, Ready, In‑Progress, Done*).
- Clarifier le workflow Git (branches *main* et *production*, tags, merges).
- Définir le contenu des notes de release (tickets, changements de configuration, migrations).
- Identifier les actions à réaliser avant la prochaine version (v1.3.0 → v3.0, puis v3.1.dev).

## Sujets abordés
| Sujet | Points clés |
|-------|-------------|
| **État du tableau Kanban** | - Colonne *Done* remplie de tickets anciens et non triés.<br>- Ambiguïté entre colonnes *Ready* et *In‑Progress*.<br>- Proposition de créer une colonne « À trier » pour libérer le backlog. |
| **Processus Git** | - `main` = branche de développement, `production` = branche de release.<br>- Merge de `main` → `production` avec gestion des conflits de version (ex. `init`, `myproject`).<br>- Utilisation de `git tag` (ex. `v1.3.0`) et `push --follow-tags` pour créer les releases sur GitHub. |
| **Notes de release** | - Inclure : <br>  • Liste des tickets (avec lien) <br>  • Modifications de base <br>  • Modifications de configuration <br>  • Identifiants de migration (si applicable).<br>- Décision de ne pas détailler chaque ticket dans la note, mais d’ajouter le titre pour une vue d’ensemble. |
| **Migrations** | - Chaque migration possède un ID généré par la librairie de migration.<br>- Les migrations sont rangées par ordre d’exécution et séparées par fonctionnalité.<br>- Besoin d’ajouter l’ID de migration dans les notes de release pour faciliter le suivi. |
| **Documentation & formation** | - Enregistrement vidéo du processus de release pour référence future.<br>- Mise à jour du document de procédure avec les points discutés (workflow, colonnes Kanban, format des releases). |
| **Points de vigilance** | - Vérifier les changements de configuration entre deux releases (ex. nouvelles configs pour le tri, gestion des erreurs de connexion).<br>- S’assurer que les tickets de migration sont correctement associés aux releases. |

## Décisions prises
1. **Nettoyage du tableau Kanban**
   - Créer une colonne « À trier » et y déplacer les tickets obsolètes de *Done*.
2. **Standardisation des releases**
   - Les notes de release contiendront : titre du ticket, lien, type de changement (base / config), ID de migration le cas échéant.
3. **Gestion des migrations**
   - Ajouter l’ID de chaque migration dans la note de release correspondante.
4. **Documentation**
   - Produire une vidéo tutoriaire du processus de release et mettre à jour le guide interne.
5. **Responsabilités de branche**
   - `main` reste la branche de développement ; `production` ne reçoit que les merges validés et taggés.

## Questions en suspens
| Question | Responsable / Suivi |
|----------|---------------------|
| Faut‑il ajouter une courte description du ticket dans la note de release (au‑delà du titre) ? | À valider par l’équipe (Benoît / Mickaël). |
| Comment automatiser l’ajout de l’ID de migration dans la note de release ? | Benjamin explore une éventuelle automatisation. |
| Quels sont les critères exacts pour placer un ticket dans la colonne *Ready* vs *In‑Progress* ? | Benoît doit clarifier le workflow avec l’équipe. |

## Tâches à effectuer
| Action | Responsable | Échéance |
|--------|-------------|----------|
| Créer la colonne « À trier » et y déplacer les tickets obsolètes | Mickaël (avec l’aide de Benoît) | Prochaine réunion |
| Nettoyer la colonne *Done* (déplacer ou supprimer les tickets) | Mickaël | ASAP |
| Ajouter les ID de migration aux notes de release de la version 1.3.0 | Benjamin | Avant la publication de la prochaine release |
| Rédiger / mettre à jour le document de procédure (incluant workflow Git, colonnes Kanban, format de release) | Intervenant (rédacteur) | Fin de semaine |
| Enregistrer une vidéo du processus complet de release | Intervenant | Avant la prochaine itération |
| Créer un ticket Kanban « Release 1.3.0 – agrégateur de changements » pour centraliser les infos de config/base | Mickaël | Immédiat |
| Vérifier les changements de configuration liés aux tickets *gérer les erreurs de connexion à BBB* et *log d’erreur de connexion service* | Sébastien | Avant la prochaine release |
| Confirmer la procédure de merge `main → production` (gestion des conflits) avec Benoît | Mickaël & Benoît | Avant le prochain merge |

## Prochaine rencontre
- **Date / heure** : à définir (proposition de se réunir avant la prochaine release majeure).
- **Objectif** : valider le nettoyage du Kanban, vérifier la conformité des notes de release et finaliser le processus de publication.

---

*Ce compte rendu a été rédigé à partir de la transcription de la réunion et pourra être complété ou corrigé par les participants.*
