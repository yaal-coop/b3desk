# Compte rendu de réunion

**Date** : 28 avril 2026
**Durée estimée** : ~1 heure

## Participants
| Nom | Rôle / Fonction |
|-----|-----------------|
| **Loan** | Développeur (présence incertaine) |
| **Mickaël** | Responsable du tableau Kanban / backlog |
| **Benoît** | Responsable produit & gestion du backlog |
| **Sébastien** | Développeur (migrations DB) |
| **Benjamin** | Développeur (migration scripts) |
| **Speaker** (animateur) | Documentation & coordination des releases |
| Autres (présents en appel) | Participants ponctuels |

## Objet de la réunion
- Faire le point sur le **processus de déploiement** (branches, merges, tags, releases) pour le projet **SerpentDoc**.
- Nettoyer et structurer le **tableau Kanban** (colonnes Backlog, Ready, In‑Progress, Done, etc.).
- Harmoniser la **rédaction des notes de release** (tickets, changements de configuration, migrations).
- Mettre à jour la **documentation** et les supports vidéo associés.

## Sujets abordés
| Sujet | Points clés |
|-------|-------------|
| **Présence de Loan** | Loan doit être présent pour valider les premières étapes, mais la réunion peut démarrer sans lui. |
| **Documentation** | Traduction et clarification des guides ; création d’une vidéo de démonstration. |
| **Tableau Kanban** | - Colonne *Backlog* remplie progressivement.<br>- Colonne *Redis* (ou *Dawn*) mal utilisée → doublon avec *In‑Progress*.<br>- Proposition de créer une colonne **« À trier »** pour les tickets en attente de classification. |
| **Gestion des tickets** | - Vérifier si les tickets en *Dawn* ont déjà été inclus dans une release.<br>- Répartir chaque ticket dans la colonne correspondant à son état (Ready, In‑Progress, Done). |
| **Stratégie de branches** | - Développement sur des branches **feature** → merge dans **main** après validation.<br>- **main** → branche **production** pour les releases.<br>- Production reste synchronisée avec main à chaque merge. |
| **Tagging & création de releases** | - Utilisation de `git tag` (ex. `v1.3.0`).<br>- Push avec `--follow-tags`.<br>- Les releases GitHub affichent les commits et permettent de comparer les versions. |
| **Contenu des notes de release** | - Lister les tickets (titre + lien).<br>- Indiquer les **modifications de base** et les **modifications de configuration**.<br>- Ajouter l’**identifiant de migration** (hash généré par la librairie de migration). |
| **Migrations DB** | - Chaque migration possède un ID unique (hash).<br>- Les migrations sont séparées par fonctionnalité et doivent être listées dans les notes de release. |
| **Responsabilités & flux de travail** | - Le speaker se charge de la documentation et de la vidéo.<br>- Mickaël nettoie le tableau Kanban.<br>- Sébastien ajoute les détails de migration dans les tickets.<br>- Benjamin veille à la bonne génération des IDs de migration. |
| **Gestion des corrections urgentes** | - Corrections mineures (orthographe, texte) seront faites directement sur le code déployé, puis une MR sera ouverte pour la source. |

## Décisions prises
1. **Attendre Loan** si besoin, mais démarrer la réunion sans lui.
2. **Nettoyer le tableau Kanban** :
   - Déplacer les tickets de *Redis/Dawn* vers *In‑Progress* ou *Ready* selon leur état.
   - Créer une colonne **« À trier »** pour les tickets non classés.
3. **Adopter le workflow de branches** décrit ci‑dessus (feature → main → production).
4. **Standardiser les notes de release** :
   - Titre du ticket + lien.
   - Indiquer les changements de base et de configuration.
   - Ajouter l’ID de migration.
5. **Créer un ticket “Release X.Y.Z”** dans le Kanban qui regroupe toutes les informations de la version (tickets, configs, migrations).
6. **Documentation** : le speaker met à jour le guide et la vidéo de démonstration, puis les partage avec l’équipe.

## Questions en suspens
| Question | Responsable / Prochaine action |
|----------|--------------------------------|
| Comment harmoniser définitivement les colonnes *Redis* et *Dawn* ? | Mickaël (discussion avec Benoît) |
| Format exact des notes de release (niveau de détail) ? | Confirmation avec Benoît et l’équipe produit |
| Processus à suivre pour des modifications de texte urgentes (ex. affichage de texte) ? | Benoît (définir si une release rapide ou MR directe) |
| Validation finale du workflow de branche avant le prochain déploiement ? | Tous les développeurs (revue lors du prochain sprint) |

## Tâches à effectuer
| Tâche | Responsable | Échéance |
|-------|-------------|----------|
| Nettoyer le tableau Kanban (déplacer tickets, créer colonne « À trier ») | **Mickaël** | Prochaine réunion |
| Mettre à jour la documentation et la vidéo de démonstration | **Speaker** | 2 jours |
| Ajouter les identifiants de migration dans les tickets de release | **Sébastien** | Avant la prochaine release |
| Vérifier que chaque ticket possède un lien et un titre clair dans les notes de release | **Benjamin** | Avant le prochain tag |
| Créer le ticket “Release 1.3.0” avec toutes les infos (tickets, configs, migrations) | **Speaker** | Avant le merge main → production |
| Confirmer le format final des notes de release avec Benoît | **Speaker + Benoît** | Avant la prochaine release |

## Prochaine rencontre
- **Date / Heure** : à définir (proposition : début de la prochaine itération, soit le **5 mai 2026**).
- **Objectif** : Faire le point sur le nettoyage du Kanban, valider le nouveau format de release notes et préparer la prochaine mise en production.

---

*Ce compte rendu a été rédigé à partir de la transcription de la réunion et synthétise les points essentiels pour le suivi du projet.*
