# Compte rendu de réunion

**Date** : 5 mai 2026
**Durée estimée** : ~1 h 30 (la réunion a duré plus longtemps que la durée prévue d’une heure)

---

## Participants
- **Johan**
- **Bastien**
- **Benjamin**
- **Mickaël**
- **Benoît**
- **Michael**
- **Sébastien**

---

## Objet de la réunion
- Mettre en place un point de suivi bi‑hebdomadaire.
- Faire le point sur les livraisons récentes (code unique, migrations, tickets) et les configurations associées.
- Discuter des problèmes de performance avec Nextcloud/Nuage (WebDAV).
- Avancer sur les projets *Salon silencieux* et *Media‑Gateway SIP connector*.
- Planifier les releases (notamment la version 1.3) et définir les estimations de charge du backlog.

---

## Sujets abordés & décisions prises

| # | Sujet | Décision / Conclusion |
|---|-------|-----------------------|
| 1 | **Planning du point bi‑hebdomadaire** | Réunion fixée chaque **mercredi à 11 h 30**. |
| 2 | **Livraison du “code unique”** | - Ajouter dans la PR la description de la configuration à changer (paramètre BVB ping). <br> - Documenter le paramètre dans la release. |
| 3 | **Scénario de test B3 Desk** | Benjamin doit fournir un scénario de test détaillé. |
| 4 | **Migrations** | - La migration actuelle dépend de la migration de *classement des salons* (non encore en prod). <br> - Toutes les migrations seront incluses dans la release et s’exécuteront dans l’ordre. |
| 5 | **Ticket 166 – erreur 500 sur les salons** | Le bug est corrigé côté Arawa. La remontée de logs sera conservée dans la prochaine release. |
| 6 | **Performance Nextcloud / Nuage (WebDAV)** | - Investigation en cours : reproduire le problème, capturer les traces, vérifier la version de la bibliothèque Python WebDAV. <br> - Action à poursuivre jusqu’à identification de la cause. |
| 7 | **Projet “Salon silencieux”** | - Devis validé, financement assuré par l’équipe messagerie. <br> - Lancement des commandes dès que possible. |
| 8 | **Media‑Gateway – connecteur SIP** | - Projet validé, financement DGFIP. <br> - Nécessité de suivre les évolutions et de prévoir une réunion de cadrage technique. |
| 9 | **Backlog & estimation** | Michael doit fournir, d’ici la fin de journée, un tableau de correspondance **tags → estimation (heures / jours)**. |
|10| **Création de la release 1.3** | Sébastien (avec le support de Benjamin) réalisera la release **à 14 h** le même jour. |
|11| **API messagerie nationale** | Une réunion dédiée sera planifiée (responsable : Michael) pour préciser besoins et priorités. |

---

## Questions en suspens
1. **Scénario de test B3 Desk** – détails attendus de Benjamin.
2. **Nom exact de la variable de configuration** (dial number / BB number) – clarification requise.
3. **Intégration du “code unique”** – doit‑il être inclus dans la release 1.3 ou attendre une version ultérieure ? (à confirmer avec Benoît).
4. **État de la bibliothèque WebDAV** – version actuelle et besoin éventuel de mise à jour.
5. **Impact de la procédure de création de release** sur le guide/documentation – à vérifier.

---

## Tâches à effectuer

| Tâche | Responsable | Échéance |
|-------|-------------|----------|
| Planifier le point bi‑hebdomadaire (calendrier partagé) | Johan | Immédiat |
| Mettre à jour la PR avec les changements de configuration (BVB ping, dial number) | Benjamin | Avant la prochaine release |
| Fournir le scénario de test B3 Desk | Benjamin | 12 mai 2026 |
| Vérifier que la migration de classement des salons est bien appliquée en prod | Michael | Avant la release 1.3 |
| Conserver la remontée de logs du ticket 166 dans la prochaine release | Benoît | Release 1.3 |
| Reproduire le problème de performance WebDAV et capturer les traces | Benjamin | Au plus tard 19 mai 2026 |
| Vérifier et, si besoin, mettre à jour la bibliothèque Python WebDAV | Michael | 19 mai 2026 |
| Envoyer le tableau de correspondance tags → estimation (heures/jours) | Michael | 5 mai 2026 (fin de journée) |
| Créer la release 1.3 (inclure les migrations, logs, etc.) | Sébastien (assistance Benjamin) | 5 mai 2026 à 14 h |
| Organiser une réunion technique sur l’API messagerie nationale | Michael | À planifier (prochaine semaine) |
| Lancer les commandes pour le projet “Salon silencieux” | Benoît | Dès validation du budget |
| Coordonner le projet Media‑Gateway SIP connector (définir spécifications) | Michael & Benjamin | À définir (suite à réunion de cadrage) |

---

## Prochaine rencontre
- **Réunion bi‑hebdomadaire** : **mercredi 12 mai 2026 à 11 h 30** (et chaque mercredi suivant).
- Une réunion spécifique sur l’**API messagerie nationale** sera planifiée d’ici la semaine prochaine (date à confirmer).

---

*Fin du compte rendu.*
