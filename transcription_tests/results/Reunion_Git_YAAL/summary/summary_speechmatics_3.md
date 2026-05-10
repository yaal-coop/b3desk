# Compte rendu de réunion

**Date** : 5 mai 2026
**Durée estimée** : ~1 h (début de la réunion, pause, puis reprise)

---

## Participants
| Nom | Rôle / Fonction |
|-----|-----------------|
| **Loan** | Développeur (présence incertaine) |
| **Laurent** | Expert produit & processus |
| **Benoît** | Responsable du Kanban / backlog |
| **Benjamin** | Développeur, suivi des migrations |
| **Michael** | (mentionné, rôle non précisé) |
| **Sébastien** | Développeur (intervention sur les migrations) |
| **Marine** | (mentionnée, rôle non précisé) |
| **Speaker** (animatrice) | Coordination, documentation, tests de release |
| **Autres** (participants non nommés) | Observateurs / contributeurs |

---

## Objet de la réunion
Passer en revue le **processus de déploiement** (branches, merge‑requests, tags, releases) et **nettoyer le tableau Kanban** (colonnes *Backlog*, *Ready*, *Down*).
Mettre à jour la documentation et définir les bonnes pratiques pour les futures releases (notes, migrations, configuration).

---

## Sujets abordés

| Sujet | Points clés |
|-------|--------------|
| **Présence de Loan** | Attente de Loan ; décision de commencer ou d’attendre selon le ressenti du groupe. |
| **Partage d’écran & documentation** | La doc de déploiement a été ouverte, partage d’écran pour vérifier les étapes. |
| **Kanban – colonne *Down*** | - Accumulation de tickets anciens et non triés.<br>- Problème de visibilité des releases associées.<br>- Proposition de créer une colonne « À trier » ou de vider la colonne après tri. |
| **Flux de travail (Backlog → Ready → In‑Progress)** | Clarification du rôle de chaque colonne ; discussion sur la redondance entre *Ready* et *In‑Progress*. |
| **Branches Git** | - `main` : branche de développement.<br>- `production` : branche de release.<br>- Processus de création de branche, merge, résolution de conflits. |
| **Merge‑requests & tags** | - Validation des MR avant merge.<br>- Création de tags (`v1.3`, etc.) pour les releases.<br>- Utilisation de l’option *follow‑tag* lors du push. |
| **Notes de release** | - Inclure les tickets (titre + lien) et les modifications de configuration.<br>- Ajouter l’identifiant de migration lorsqu’il y en a.<br>- Décider du niveau de détail (titre suffisant, lien pour le détail). |
| **Migrations DB** | - IDs générés par une librairie, ordre d’exécution important.<br>- Chaque fonctionnalité distincte possède son propre fichier de migration.<br>- Besoin d’ajouter les IDs de migration dans les notes de release. |
| **Responsabilités** | - Développeurs : création/merge des MR, tags, releases.<br>- Ops / testeurs : récupérer la livraison, tester, valider.<br>- Aucun intervenant ne doit modifier le code en production sans coordination. |
| **Documentation & formation** | - Vidéo de démonstration du processus de release réalisée.<br>- Mise à jour de la documentation avec les nouvelles bonnes pratiques. |
| **Prochaine réunion** | Planifiée dans deux semaines (point de suivi). |

---

## Décisions prises
| Décision | Responsable(s) |
|----------|----------------|
| Attendre Loan avant de commencer le travail de nettoyage du Kanban (si possible). | Tous |
| Nettoyer la colonne *Down* ; créer éventuellement une colonne « À trier » pour les tickets anciens. | Speaker (avec l’aide de Benoît) |
| Inclure dans les notes de release : <br>• Titre + lien du ticket <br>• Modifications de configuration <br>• ID de migration (le cas‑échéant). | Speaker (mise à jour) |
| Utiliser `main` comme branche de développement et `production` pour les releases, avec tags versionnés. | Tous (processus standard) |
| Ne pas intervenir directement sur le code en production sans accord préalable. | Tous |
| Ajouter un ticket récapitulatif dans le Kanban pour chaque release (contient config/base + migrations). | Speaker |
| Partager la vidéo de démonstration du processus de release avec l’équipe. | Speaker |

---

## Questions en suspens
| Question | Responsable(s) | Commentaire |
|----------|----------------|-------------|
| Pourquoi la colonne *Ready* apparaît‑elle avant *In‑Progress* dans le tableau actuel ? | Benoît (ou celui qui a configuré le tableau) | À clarifier pour éviter la redondance. |
| Quels seront les critères exacts pour décider d’ajouter une colonne « À trier » vs simplement vider *Down* ? | Speaker + Benoît | Décision à prendre lors du prochain nettoyage. |
| Comment automatiser l’inclusion des IDs de migration dans les notes de release ? | Benjamin (et équipe dev) | Possibilité d’un script ou d’une étape manuelle. |
| Existe‑t‑il des changements de configuration prévus pour la prochaine version ? | Tous (revue des tickets) | À vérifier avant la prochaine release. |

---

## Tâches à effectuer
| Tâche | Responsable | Échéance |
|-------|-------------|----------|
| Nettoyer la colonne *Down* et réaffecter les tickets aux bonnes colonnes (ou créer « À trier »). | Speaker (avec Benoît) | Avant la prochaine réunion (dans 2 semaines) |
| Mettre à jour la documentation de déploiement avec les nouvelles étapes et le processus de release. | Speaker | 1 semaine |
| Ajouter les titres + liens des tickets et les IDs de migration dans les notes de chaque release. | Speaker | À chaque release |
| Créer un ticket récapitulatif dans le Kanban pour chaque release (config, base, migrations). | Speaker | À chaque release |
| Vérifier et, si besoin, corriger les IDs de migration dans les scripts de migration. | Benjamin | Avant la prochaine release |
| Partager la vidéo de démonstration du processus de release avec l’équipe. | Speaker | Immédiatement |
| Demander à Benoît des précisions sur la configuration du tableau Kanban (colonnes). | Speaker | Avant la prochaine réunion |
| Préparer le point de suivi à envoyer dans deux semaines. | Speaker | Dans 2 semaines |

---

## Prochaine rencontre
- **Date** : dans **2 semaines** (date exacte à confirmer).
- **Objet** : suivi du nettoyage du Kanban, validation des nouvelles notes de release, revue des migrations et des configurations pour la prochaine version.

---

*Fin du compte rendu.*
