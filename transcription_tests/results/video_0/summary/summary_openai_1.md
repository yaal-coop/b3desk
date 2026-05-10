# Compte rendu de réunion

**Date** : 4 mai 2026
**Heure** : 10 h – 12 h (environ)
**Durée estimée** : ~2 h

---

## Participants
| Nom | Rôle / Service |
|-----|----------------|
| **Benjamin** | Développeur B3Desk |
| **Mickaël** | Responsable technique |
| **Sébastien** | Lead release / Git |
| **Benoît** | Testeur / Support |
| **Miguel** | (mentionné) |
| **Arawa** | Équipe infra (ScaleLite / BBB) |
| **Renata** | Développeuse SIP |
| **Michael** | (mentionné) |
| **Autres** | Participants du projet messagerie nationale, SIP Media Gateway, etc. |

---

## Objet de la réunion
1. Organisation d’un point de suivi bi‑hebdomadaire.
2. Revue des livrables récents (code générique, PR, configuration).
3. Validation des scénarios de test et des migrations.
4. Suivi du ticket #166 (erreur 500 salons).
5. Investigation des lenteurs/instabilités entre B3Desk et le service **Nuage/Nextcloud**.
6. Avancement du budget et du devis pour la messagerie nationale et le projet **SIP Media Gateway**.
7. Estimation et chiffrage du backlog (tags = large/medium).
8. Planification de la **release 1.3**.

---

## Sujets abordés & décisions prises

| Sujet | Décision / Conclusion |
|-------|-----------------------|
| **Point bi‑hebdomadaire** | Réunion toutes les 2 semaines, le **mercredi à 11 h 30**. Invitation à envoyer. |
| **Livraison du code générique** | Aucun développement supplémentaire requis, seulement une **modification de configuration** (ScaleLite / BBB). La PR doit être mise à jour avec le paramètre exact. |
| **Scénario de test B3Desk** | - Activer la nouvelle option dans la config.<br>- Vérifier que le **PIN** (téléphone) s’affiche correctement.<br>- Tester la migration (ordre des migrations respecté). |
| **Ticket #166 – Erreur 500 salons** | Problème résolu côté **ARAWA** (suppression d’un champ). La remontée de log sera conservée dans la prochaine release. |
| **Instabilité Nuage ↔ B3Desk** | - Confirmation que les appels passent par le token applicatif (WebDAV).<br>- Besoin de reproduire le problème pour identifier la cause (charge serveur, lib Python, etc.).<br>- Benoît effectuera de nouveaux tests. |
| **Budget messagerie nationale** | Devis validé, financement assuré par l’équipe messagerie. Le **salon** passe en **mode silencieux** en attendant le lancement. |
| **Projet SIP Media Gateway** | Le projet est validé, financement BGF. Une réunion dédiée sera planifiée pour cadrer les fonctionnalités et les dépendances avec **Renata**. |
| **Chiffrage du backlog** | Mickaël doit fournir, d’ici la fin de journée, un tableau de correspondance **tags ↔ estimation (jours/heures)**. |
| **Release 1.3** | - Création prévue à **14 h** le même jour (Sébastien guide Benjamin).<br>- La release contiendra les nouvelles configurations, le classement des salles, mais **pas** le numéro d’appel ni le code unique (prévu pour 1.3.1). |
| **Prochaine étape** | Après la release, vérifier la migration, le classement des salles et lancer les tests de stabilité Nuage. |

---

## Questions en suspens
| Question | Responsable / Action |
|----------|----------------------|
| Nom exact du paramètre ScaleLite à modifier. | Benjamin (mise à jour PR). |
| Scénario complet de test B3Desk (exemple de flux). | Benjamin (fournir doc). |
| Confirmation du moment où le **salon silencieux** pourra être activé (validation juridique). | Mickaël (coordination avec le service juridique). |
| Décision finale sur l’inclusion du **code unique** et du **numéro d’appel** dans la release 1.3 ou 1.3.1. | Mickaël & Benjamin (à valider avant la release). |
| Résolution définitive de l’instabilité Nuage/Nextcloud. | Benoît (tests de reproduction). |
| Table de correspondance tags ↔ estimation. | Mickaël (à envoyer d’ici la fin de journée). |

---

## Tâches à effectuer

| Tâche | Responsable | Échéance |
|-------|-------------|----------|
| Envoyer l’invitation pour le point bi‑hebdomadaire (mercredi 11 h 30). | Mickaël | Avant le mercredi suivant |
| Mettre à jour la PR avec le paramètre de configuration ScaleLite/BBB. | Benjamin | Avant la release 1.3 |
| Ajouter la configuration (ON) et le **dial‑number** dans l’APR et la release. | Équipe dev (Benjamin) | Avant la release 1.3 |
| Rédiger le scénario de test B3Desk (activation PIN, création salon). | Benjamin | Avant la release 1.3 |
| Vérifier le bon ordre d’exécution des migrations (tri → nouvelle migration). | Benjamin | Avant la release 1.3 |
| Conserver la remontée de log du ticket #166 dans la prochaine release. | Équipe dev | Release 1.3 |
| Réaliser des tests de charge/instabilité entre B3Desk et Nuage. | Benoît | Au plus tard 2 semaines |
| Fournir le tableau de correspondance **tags ↔ estimation**. | Mickaël | Fin de journée (4 mai) |
| Accompagner Benjamin lors de la création de la release 1.3 (14 h). | Sébastien | 14 h le 4 mai |
| Planifier une réunion dédiée au projet **SIP Media Gateway** (cadrage fonctionnel). | Mickaël | Prochaine quinzaine |
| Suivi du support juridique pour le salon silencieux. | Mickaël | À définir |

---

## Prochaine rencontre
- **Réunion bi‑hebdomadaire** : chaque mercredi à **11 h 30** (prochaine le 9 mai 2026).
- **Suivi release 1.3** : aujourd’hui à **14 h** (débrief prévu lors du point bi‑hebdomadaire).
- **Réunion projet SIP Media Gateway** : à planifier (invitation à venir).

---

*Document rédigé par l’assistant de rédaction de comptes rendus.*
