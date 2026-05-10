# Compte rendu de réunion

**Date** : 30 avril 2026
**Durée estimée** : ~2 h 30 (la réunion a dépassé le temps prévu)

---

## Participants
| Nom | Rôle / Fonction |
|-----|-----------------|
| **Benjamin** | Développeur / Responsable technique |
| **Benoît** | Testeur / Responsable des investigations Nuage |
| **Mickaël / Michael** | Chef de projet / Responsable du backlog |
| **Yael** | Contact finance / Support juridique |
| **Renata** | Développeuse interne (mentionnée) |
| **Autres** | Participants non nommés (présents via Tchap) |

---

## Objet de la réunion
Suivi des développements en cours (code unique, configuration BBB/ScaleLite, migrations, tickets), planification des points de suivi, validation de budgets et préparation des prochaines releases.

---

## Sujets abordés

| N° | Sujet | Points clés |
|----|-------|--------------|
| 1 | **Mise en place d’un point de suivi bi‑hebdomadaire** | Proposition : chaque mercredi à **11 h 30**. Tous les participants sont d’accord. |
| 2 | **Livraison du “code unique”** | - Questions sur la configuration nécessaire (ScaleLite / BBB). <br>- Nécessité d’ajouter le paramètre `DialNumber` dans la PR et la release. |
| 3 | **Scénario de test B3desk** | - Changer la configuration pour activer la nouvelle option. <br>- Vérifier que le PIN affiché dans B3desk correspond à celui présent dans la visioconférence. |
| 4 | **Migrations de base de données** | - Ordre des migrations (tri des salons → code unique). <br>- La release exécutera les migrations dans l’ordre, pas de problème prévu. |
| 5 | **Ticket 166 – Erreur 500 sur les salons** | - Problème résolu par Arawa (suppression d’un champ). <br>- Conservation de la remontée de logs dans la prochaine release. |
| 6 | **Performance de la connexion Nuage / Nextcloud** | - Le token applicatif (validité 30 jours) est utilisé directement entre B3desk et Nuage. <br>- Problèmes de lenteur/instabilité observés, plusieurs hypothèses (surcharge serveur, bibliothèque WebDAV obsolète, plugins navigateur). |
| 7 | **Salon « silencieux »** | - Devis validé, financement en cours de finalisation. <br>- Possibilité de lancer le développement rapidement. |
| 8 | **Projet SIP Media Gateway** | - Intégration d’un connecteur SIP à BBB, financé par la DG Philips. <br>- Nécessité de clarifier les spécifications et le support juridique. |
| 9 | **Backlog & planification des releases** | - Priorité : release **1.3** (sans numéro d’appel & code unique). <br>- Release **1.3.1** prévue pour intégrer ces fonctionnalités. <br>- Classement des salons (favoris) prêt à être déployé. |
|10| **Estimation des tâches (tags)** | - Besoin d’un tableau de correspondance *tag → durée* (jours/heure). |
|11| **Procédure de création de release** | - Benjamin doit réaliser la release 1.3 à **14 h** le même jour, assistance possible. |

---

## Décisions prises

| Décision | Responsable | Délai |
|----------|-------------|-------|
| Instaurer le point de suivi toutes les 2 semaines, le mercredi à 11 h 30. | **Organisateur** (envoi d’invitation) | Immédiat |
| Ajouter le paramètre `DialNumber` dans la PR et le documenter pour la release. | **Benjamin** (ou équipe dev) | Avant la release 1.3 |
| Conserver la remontée de logs du ticket 166 dans la prochaine release. | **Équipe** | Release 1.3 |
| Lancer le développement du salon silencieux dès que le financement sera confirmé. | **Speaker / Yael** | Dès validation financière |
| Effectuer la release **1.3** (sans numéro d’appel & code unique) le **30 avril 2026 à 14 h**. | **Benjamin** (avec assistance) | 14 h le même jour |
| Benoît réalise des tests de performance sur Nuage et rapporte les résultats. | **Benoît** | Prochaine réunion |
| Produire un tableau de correspondance *tag → durée* et le diffuser. | **Michael** | Avant la prochaine réunion |
| Planifier une réunion dédiée au projet SIP Media Gateway (spécifications, financement). | **Speaker** | À définir |

---

## Questions en suspens

1. **Scénario de test complet** – Quels sont les cas exacts à couvrir pour valider le nouveau PIN dans B3desk ?
2. **Intégration du code unique & du numéro d’appel** – Dans quelle release (1.3 ou 1.3.1) seront-ils finalement déployés ?
3. **Cause précise de l’instabilité Nuage** – S’agit‑il d’une surcharge serveur, d’une bibliothèque WebDAV obsolète ou d’un problème côté navigateur ?
4. **Financement du projet SIP Media Gateway** – Qui assure le support juridique et le budget final ?
5. **Correspondance tags ↔ temps** – Valeurs exactes à définir (ex. : *Medium* = 3 jours).

---

## Tâches à effectuer

| Tâche | Responsable | Échéance |
|-------|-------------|----------|
| Envoyer l’invitation du point bi‑hebdomadaire (mercredi 11 h 30). | Organisateur | Immédiat |
| Mettre à jour la PR avec le paramètre `DialNumber` et la description. | Benjamin / Équipe dev | Avant la release 1.3 |
| Fournir le scénario de test B3desk (activation de l’option, vérif du PIN). | Benjamin | Avant la prochaine réunion |
| Vérifier l’ordre des migrations et s’assurer qu’elles sont incluses dans la release. | Michael / Benjamin | Release 1.3 |
| Intégrer la remontée de logs du ticket 166 dans la release. | Équipe | Release 1.3 |
| Réaliser les tests de charge / latence sur Nuage (WebDAV). | Benoît | Avant la prochaine réunion |
| Préparer le tableau de correspondance *tag → durée* (ex. : Small = 1 j, Medium = 3 j, Large = 5 j). | Michael | Avant la prochaine réunion |
| Créer la release **1.3** à 14 h (commande Git, tags, commits). | Benjamin (avec assistance) | 30 avril 2026, 14 h |
| Confirmer le financement et le support juridique du projet SIP Media Gateway. | Speaker / Yael | À définir |
| Mettre à jour le backlog avec les tags d’estimation et prioriser les nouvelles tâches (messagerie nationale, SIP). | Michael | Après la prochaine réunion |

---

## Prochaine rencontre

- **Réunion bi‑hebdomadaire** : chaque **mercredi à 11 h 30** (prochaine le 7 mai 2026).
- Un point dédié au **SIP Media Gateway** sera planifié ultérieurement (date à confirmer).

---

*Document rédigé par l’assistant de rédaction de comptes rendus.*
