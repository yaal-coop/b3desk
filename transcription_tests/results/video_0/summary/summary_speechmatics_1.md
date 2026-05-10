# Compte rendu de réunion

**Date** : 4 mai 2026
**Durée estimée** : ~ 2 h 30 (la réunion a dépassé la durée prévue d’une heure)

---

## Participants
| Nom | Rôle / Fonction |
|-----|-----------------|
| **Benjamin** | Développeur / Responsable technique |
| **Benoît** | Responsable tests / Coordination |
| **Maryse** | Gestion de projet / Budgets |
| **Michael** | Gestion du backlog & estimation |
| **Sébastien** | Responsable release |
| **Autres** (participants non nommés) | Membres de l’équipe de développement et de support |

---

## Objet de la réunion
- Faire le point sur l’avancement des développements (code unique, configuration, migrations, etc.)
- Organiser la cadence des réunions de suivi
- Discuter des incidents récents (ticket 166, instabilité Nextcloud)
- Valider les étapes de release (v1.3) et les prochains livrables (salon silencieux, projet SIP)
- Définir les besoins d’estimation et de chiffrage du backlog

---

## Sujets abordés

| N° | Sujet | Points clés |
|----|-------|-------------|
| 1 | **Planification des points de suivi** | Proposition d’un point toutes les 2 semaines, le **mercredi à 11 h 30**. |
| 2 | **Livraison du “code unique”** | - Deux/ trois questions sur la configuration. <br>- Nécessité d’ajouter dans la PR la modification de configuration (paramètre à activer). |
| 3 | **Configuration BB Dial Number** | - Variable à définir côté “Arabic/Scale Lite”. <br>- Utilisation du même nom de paramètre que l’API ( `DialNumber` ). |
| 4 | **Migrations & ordre de release** | - Migration actuelle dépend de la migration de tri des salons (non encore en prod). <br>- Toutes les migrations seront exécutées dans l’ordre grâce au script de release. |
| 5 | **Ticket 166 – Erreur 500 salon** | - Problème de cohérence de données résolu côté Rawa (suppression d’un champ). <br>- Conservation des logs dans la prochaine release. |
| 6 | **Instabilité Nextcloud / Nuage** | - Problème de lenteur lors des appels WebDAV après obtention du token. <br>- Hypothèses : surcharge du serveur, bibliothèque Python obsolète. <br>- Action : reproduire le problème, capturer les traces, tester avec différents navigateurs. |
| 7 | **Salon silencieux** | - Devis validé, besoin de support juridique et de financement. <br>- Budget 2025 pour 2 jours de dev B3 DS à réserver. |
| 8 | **Projet Media‑Gateway (connecteur SIP)** | - Financement DGFIP, besoin de définir les fonctionnalités à livrer. |
| 9 | **Backlog & chiffrage** | - Utilisation de tags ( `medium` , etc.) pour estimer les tâches en jours/hours. <br>- Demande d’un tableau de correspondance tags ↔ estimation. |
|10| **Préparation de la release 1.3** | - Procédure de release à suivre (Sébastien). <br>- Réunion de préparation prévue l’après‑midi à 14 h. |

---

## Décisions prises

| Décision | Responsable | Commentaire |
|----------|-------------|--------------|
| Instaurer un point **bi‑hebdomadaire** le mercredi à 11 h 30. | **Benjamin** (envoi de l’invitation) | Calendrier partagé à créer. |
| Ajouter la modification de configuration (activation du nouveau paramètre) dans la PR et la note de release. | **Benjamin** | Garantir que le même changement sera appliqué en prod. |
| Conserver les logs du ticket 166 dans la prochaine release. | **Équipe dev** | Aucun changement de code requis. |
| Poursuivre l’investigation Nextcloud / Nuage jusqu’à reproduction du problème. | **Benjamin** (captures de trames) & **Benoît** (tests) | Rapport à fournir dès que possible. |
| Lancer le **salon silencieux** dès validation du devis et obtention du support juridique. | **Maryse** (budget & juridique) | Commande à passer rapidement. |
| Valider le **budget 2025** pour 2 jours de dev B3 DS. | **Maryse** | À inclure dans le plan financier. |
| Créer et diffuser un tableau de correspondance **tags ↔ estimation** (jours/heure). | **Michael** | À envoyer d’ici la fin de journée. |
| Effectuer la **release 1.3** après validation des tests du code unique et des nouvelles fonctionnalités. | **Sébastien** (lead release) & **Benjamin** (support) | Réunion de préparation à 14 h le même jour. |
| Organiser une réunion de suivi du **projet SIP** dès que les spécifications seront finalisées. | **À définir** (probablement Michael) | À planifier ultérieurement. |

---

## Questions en suspens

1. **Scénario de test** détaillé pour les changements B3 Desk (ping, code unique).
2. **Nom exact** de la variable de configuration à modifier (paramètre “lite”).
3. **Indice de configuration** du BB Dial Number côté “Arabic/Scale Lite”.
4. Confirmation que la migration de tri des salons sera bien incluse **avant** la migration du code unique.
5. Décision finale : inclure le **code unique** dans la release 1.3 ou le reporter à une version ultérieure.
6. Reproduction fiable du problème de **latence WebDAV** (Nextcloud).
7. Obtention du **support juridique** pour le salon silencieux.
8. Définition précise du périmètre fonctionnel du **connecteur SIP** (Media‑Gateway).

---

## Tâches à effectuer

| Tâche | Responsable | Échéance |
|-------|-------------|----------|
| Envoyer l’invitation du point bi‑hebdomadaire (mercredi 11 h 30). | **Benjamin** | Immédiate |
| Documenter la modification de configuration dans la PR et les notes de release. | **Benjamin** | Avant la release 1.3 |
| Vérifier et garantir l’ordre des migrations dans le script de release. | **Benjamin** | Avant la release 1.3 |
| Conserver les logs du ticket 166 dans la prochaine release. | **Équipe dev** | Avant la release 1.3 |
| Capturer les traces réseau et reproduire le problème Nextcloud. | **Benjamin** | Au plus tard 1 semaine |
| Effectuer des tests complémentaires sur Nextcloud avec différents navigateurs. | **Benoît** | Au plus tard 1 semaine |
| Finaliser le budget et le support juridique pour le salon silencieux. | **Maryse** | Avant la prochaine release |
| Réserver les 2 jours de dev B3 DS pour 2025. | **Maryse** | Avant fin du trimestre |
| Créer le tableau de correspondance **tags ↔ estimation** et le diffuser. | **Michael** | Fin de journée (aujourd’hui) |
| Préparer la release 1.3 (script, tags, tests). | **Sébastien** & **Benjamin** | Réunion de préparation 14 h, release après validation |
| Planifier une réunion de suivi du projet SIP (Media‑Gateway). | **À définir** | Prochaine quinzaine |
| Mettre à jour le backlog avec les tags d’estimation et les priorités. | **Michael** | Continu |

---

## Prochaine rencontre

- **Réunion bi‑hebdomadaire** : **Mercredi** à **11 h 30** (prochaine occurrence le 8 mai 2026).
- **Réunion de préparation de la release 1.3** : **Aujourd’hui** à **14 h** (déjà planifiée).

---

*Document rédigé par l’assistant de rédaction de comptes rendus.*
