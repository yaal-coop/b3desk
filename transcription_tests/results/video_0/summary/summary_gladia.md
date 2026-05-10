# Compte rendu de réunion
**Date** : 28 avril 2026
**Durée estimée** : ~1 h 30 (conversation continue et points de suivi)

---

## Participants
| Nom | Rôle / Fonction |
|-----|-----------------|
| **Johan** | Animateur de la réunion |
| **Bastien** | Développeur, responsable de la PR |
| **Benjamin** | Développeur, tests & migrations |
| **Benoît** | Responsable tests (Nextcloud/Nuage) |
| **Mickaël** | Responsable backlog & chiffrage |
| **Autres** (présence ponctuelle) | Participants aux échanges (ex. “toi”, “je”) |

---

## Objet de la réunion
1. Organisation d’un point de suivi bi‑hebdomadaire.
2. Retour sur la livraison du **code unique** et les configurations associées (ScaleLight, BBB, B3Desk).
3. Gestion des migrations et du **ticket 166** (erreur 500 salons).
4. Problèmes de stabilité avec **Nextcloud/Nuage** (WebDAV).
5. Validation du **devis** et lancement du **salon silencieux** ainsi que du projet **SIP Media Gateway**.
6. Planification des releases (v1.3, v1.3.1) et estimation des tâches du backlog.

---

## Sujets abordés & Décisions prises

| Sujet | Décision / Action | Responsable(s) |
|-------|-------------------|----------------|
| **Point bi‑hebdomadaire** | Réunion fixée chaque **mercredi à 11 h 30**. | Johan (envoi de l’invitation) |
| **Configuration ScaleLight / BBB** | Ajouter la modification de paramètre dans la PR et la mentionner dans l’APR & la release. | Bastien (préciser le paramètre) |
| **Scénario de test B3Desk** | Fournir un scénario de test décrivant le nouveau PIN et le numéro de téléphone affiché. | Benjamin |
| **Migrations** | Respecter l’ordre : migration de tri des salons → migration du code unique. La release doit contenir les deux migrations dans le bon ordre. | Benjamin (vérifier) |
| **Ticket 166 (erreur 500 salons)** | Correction appliquée côté Arawa ; conserver la remontée de logs. | Équipe Arawa (maintien du log) |
| **Stabilité Nextcloud/Nuage** | - Reproduire le problème de lenteur WebDAV.<br>- Vérifier la version des bibliothèques Python utilisées.<br>- Envisager d’allonger la durée du token applicatif (30 j → plus). | Benoît (tests) + Benjamin (analyse) |
| **Devis & budget** | Devis validé, lancement du **salon silencieux** autorisé. | Tous (validation) |
| **Projet SIP Media Gateway** | Démarrer le développement côté B3Desk (génération lien SIP). Financement par la DGFIP confirmé. | Johan (coordination) |
| **Backlog & chiffrage** | Créer un tableau de correspondance **tags ↔ estimation (heures/jours)** et l’envoyer d’ici la fin de journée. | Mickaël |
| **Release 1.3** | Planifiée le **28 avril 2026 à 14 h** (sans le numéro d’appel ni le code unique). | Benjamin (exécution) |
| **Release 1.3.1** | Contiendra le numéro d’appel et le code unique après validation. | À définir (post‑release 1.3) |

---

## Questions en suspens

1. **Nom exact de la variable** à modifier dans la configuration ScaleLight/BBB.
2. **Intégration du code unique** : sera‑t‑il inclus dans la release 1.3 ou reporté à 1.3.1 ? (à confirmer avec Benoît).
3. **Stabilité WebDAV** : cause exacte (surcharge serveur, bibliothèque obsolète, version Nextcloud).
4. **Support juridique** pour l’API de messagerie nationale – besoin d’un interlocuteur dédié.
5. **Adaptation du connecteur SIP** aux spécifications de Renater : quelles extensions seront financées ?

---

## Tâches à effectuer

| Tâche | Responsable | Échéance |
|-------|-------------|----------|
| Envoyer l’invitation du point bi‑hebdomadaire (mercredi 11 h 30) | **Johan** | Immédiat |
| Préciser le paramètre de configuration dans la PR (ScaleLight/BBB) | **Bastien** | Avant la prochaine release |
| Fournir le scénario de test B3Desk (PIN & numéro) | **Benjamin** | Avant la release 1.3 |
| Vérifier l’ordre des migrations et les inclure dans la release | **Benjamin** | Avant 14 h (release 1.3) |
| Conserver la remontée de logs du ticket 166 dans la release | Équipe Arawa | Déjà fait |
| Reproduire le problème Nextcloud/Nuage et analyser la cause | **Benoît** | Au plus tard 5 mai 2026 |
| Mettre à jour les bibliothèques Python WebDAV si besoin | **Benjamin** | Après analyse Benoît |
| Prolonger la durée du token applicatif (si pertinent) | **Benjamin** | À définir |
| Rédiger et envoyer le tableau de correspondance tags ↔ estimation | **Mickaël** | Fin de journée (28 avril) |
| Exécuter la release 1.3 (création tags, commits, etc.) | **Benjamin** (avec l’aide de l’équipe) | 28 avril 2026, 14 h |
| Préparer la release 1.3.1 (numéro d’appel & code unique) | À définir | Après validation de 1.3 |
| Suivi du projet SIP Media Gateway (spécifications, financement) | **Johan** | En cours |

---

## Prochaine rencontre
- **Réunion bi‑hebdomadaire** : **Mercredi 11 h 30** (date à confirmer chaque semaine).
- **Suivi release 1.3** : Point de contrôle après la mise en production à 14 h le même jour.

---

*Fin du compte rendu.*
