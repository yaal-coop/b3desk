# Compte rendu de réunion

**Date** : 4 mai 2026
**Durée estimée** : ~1 h (début ≈ 09 h 30 – fin ≈ 10 h 30)

---

## Participants
| Nom | Rôle / Fonction |
|-----|-----------------|
| **Mickaël** | Responsable documentation & tests de livraison |
| **Benoît** | Responsable du tableau Kanban (backlog) |
| **Benjamin** | Développeur, gestion des migrations |
| **Sébastien** | Développeur (vérification des migrations) |
| **Lohan** *(absent ou en retard)* | Expert produit & process |
| **Autres** (participants non nommés) | Observateurs / contributeurs |

---

## Objet de la réunion
Passer en revue :

1. L’état de la documentation de déploiement.
2. Le tableau Kanban (colonnes *Don*, *Redis*, *Ready*, etc.).
3. Le processus de release (branches *Main* / *Production*, tags, notes de version).
4. La gestion des migrations de base de données.

---

## Sujets abordés

| Sujet | Points clés |
|-------|--------------|
| **Documentation** | - Traduction et clarification en cours.<br>- Mickaël propose de la rendre exploitable par des non‑experts.<br>- Besoin de Lohan pour valider les étapes. |
| **Kanban – colonne *Don*** | - Accumulation de tickets anciens et non triés.<br>- Origine : suppression des versions mineures par Benoît.<br>- Décision de créer une colonne **« A trier »** pour libérer la vue fonctionnelle.<br>- Question sur la colonne *Redis* (doublon avec *Don*). |
| **Processus de release** | - Branches : *Main* (développement) → *Production* (releases).<br>- Merge de *Main* dans *Production* crée des conflits (ex. `init`, `pyproject`).<br>- Utilisation de tags (`v1.3.0`, `v3.0`) pour déclencher les releases GitHub.<br>- Notes de version : inclure les tickets, les changements de base et de configuration, le lien vers les tickets, éventuellement le titre. |
| **Migrations** | - Identifiants générés par une librairie (hash).<br>- Chaque migration possède son propre fichier ; elles sont exécutées séquentiellement.<br>- Besoin d’ajouter l’ID de migration dans les notes de version.<br>- Exemple de migration : ajout de champs `updated_at`, `created_at`, `his_favorite` dans la table `meeting`. |
| **Responsabilités** | - Mickaël : tests de livraison, validation des releases, rédaction des notes de version.<br>- Benoît : gestion du tableau Kanban, décision sur la colonne *Redis*.<br>- Benjamin : suivi des migrations et de leurs IDs.<br>- Lohan : validation finale du process (présence souhaitée). |

---

## Décisions prises

| Décision | Responsable(s) | Commentaire |
|----------|----------------|-------------|
| Créer une colonne **« A trier »** dans le Kanban pour les tickets bloqués dans *Don*. | Mickaël | Permet de nettoyer la vue fonctionnelle. |
| Nettoyer la colonne *Don* (déplacer ou archiver les tickets). | Mickaël | À faire immédiatement. |
| Conserver la colonne *Redis* pour le moment, mais en discuter avec Benoît. | Benoît | Décision finale à venir. |
| Les notes de version devront contenir : <br>• Titre du ticket<br>• Lien vers le ticket<br>• Indication « modif base » / « modif config »<br>• ID de migration le cas échéant. | Mickaël (rédaction) <br>Benjamin (fournir les IDs) | Standardisation du format. |
| Utiliser les tags Git (`vX.Y.Z`) pour créer les releases GitHub. | Mickaël | Tagging automatisé avec `git push --follow-tags`. |
| Le processus de merge : <br>- Développeurs testent et valident les PR.<br>- Mickaël effectue le merge final dans *Main* puis *Production*. | Développeurs / Mickaël | Conformité au workflow actuel. |

---

## Questions en suspens

| Question | Responsable(s) | État |
|----------|----------------|------|
| Quelle est la fonction exacte de la colonne *Redis* et doit‑elle être supprimée ? | Benoît | En attente de clarification. |
| Tous les tickets présents dans *Don* ont‑ils déjà été inclus dans une release ? | Mickaël | À vérifier avant le nettoyage. |
| Y a‑t‑il des changements de configuration prévus pour la prochaine version ? | Mickaël / Benjamin | Aucun changement identifié pour la version 3.0, à confirmer. |
| Comment automatiser l’inclusion des IDs de migration dans les notes de version ? | Benjamin | À définir (script ou checklist). |

---

## Tâches à effectuer

| Tâche | Responsable | Échéance |
|-------|-------------|----------|
| Nettoyer la colonne *Don* et déplacer les tickets non traités vers **« A trier »**. | Mickaël | Avant la fin de journée. |
| Discuter avec Benoît du maintien ou de la suppression de la colonne *Redis*. | Benoît | Prochaine réunion. |
| Ajouter les IDs de migration aux notes de version de la release 3.0. | Benjamin (fournir IDs) <br> Mickaël (intégrer) | Avant la publication de la release. |
| Mettre à jour la documentation de déploiement avec le nouveau workflow (branches, tags, release notes). | Mickaël | D’ici 2 jours. |
| Vérifier les valeurs par défaut (`updated_at`, `created_at`, `his_favorite`) des nouvelles migrations et les consigner. | Sébastien | Avant la prochaine release. |
| Créer un ticket Kanban récapitulatif « Release 3.0 » contenant toutes les infos de configuration et de base. | Mickaël | Avant le merge final. |
| Enregistrer une courte vidéo de démonstration du processus de release pour les remplaçants. | Mickaël | Avant la fin de la semaine. |

---

## Prochaine rencontre

- **Date** : 11 mai 2026 (ou à convenir)
- **Objet** : Point d’avancement sur le nettoyage du Kanban, validation du format des notes de version et revue des migrations avant la release 3.1 Dev.

---

*Fin du compte rendu.*
