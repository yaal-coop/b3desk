# Compte rendu de réunion

**Date** : 28 avril 2026
**Durée** : ~ 2 h 30 (prévue 1 h, a duré 2 h 30)

---

## Participants
| Nom | Rôle / Fonction |
|-----|-----------------|
| **Benjamin** | Développeur B3desk |
| **Benoît** | Responsable technique / coordination |
| **Mickaël** | Chef de projet / animation réunion |
| **Renata** (mentionnée) | Développeuse interne (pas présente) |
| **Yael** (mentionnée) | Contact finance / juridique |
| **Sébastien** | Expert release |
| **Autres** (participants anonymes) | Présents aux échanges |

---

## Objet de la réunion
- Faire le point sur l’avancement des développements (code unique, configuration BBB/ScaleLite, migrations, tickets)
- Définir une cadence de suivi bi‑hebdomadaire
- Discuter des incidents de connexion Nuage/Nextcloud et du projet SIP Media Gateway
- Planifier les prochaines releases (1.3, 1.3.1) et les priorités du backlog

---

## Sujets abordés

| # | Sujet | Points clés |
|---|-------|-------------|
| 1 | **Récurrence des réunions** | Proposition d’un point toutes les 2 semaines, le **mercredi à 11 h 30**. Accord de tous. |
| 2 | **Livraison du “code unique”** | - Deux‑trois questions sur la PR. <br> - Nécessité d’une configuration supplémentaire (ScaleLite/BBB). <br> - Variable **DialNumber** à préciser dans la PR et dans la release. |
| 3 | **Scénario de test B3desk** | - Activer la nouvelle option dans la config (WebEnv). <br> - Vérifier que le PIN affiché dans B3desk correspond à celui présent dans la visioconférence. |
| 4 | **Migrations** | - La migration du code unique dépend de la migration de classement des salons. <br> - Toutes les migrations seront exécutées dans l’ordre dans la release. |
| 5 | **Ticket 166 – Erreur 500 salons** | - Résolu par Arawa (suppression d’un champ). <br> - Conservation de la remontée de logs dans la prochaine release. |
| 6 | **Problèmes de connexion Nuage / Nextcloud** | - Le token applicatif (validité 30 jours) est utilisé uniquement entre B3desk et Nuage. <br> - Instabilité possible du WebDAV (bibliothèque Python obsolète, surcharge du serveur). <br> - Nécessité de reproduire le problème et de capturer les traces. |
| 7 | **Salon « silencieux »** | - Devis validé, financement en cours via l’équipe Messagerie. <br> - Lancement possible dès que le support juridique sera confirmé. |
| 8 | **Projet SIP Media Gateway** | - Intégration d’un connecteur SIP à BBB. <br> - Financement par la DG Philips, besoin de clarifier les spécifications et les fonctionnalités supplémentaires. |
| 9 | **Backlog & prochaines releases** | - Priorité : classement des salles (favoris) → release 1.3. <br> - Code unique et numéro d’appel seront intégrés dans la release 1.3.1. |
|10| **Estimation des tâches (tags)** | - Utilisation de tags *large / medium* pour chiffrer les tâches (jours/hours). <br> - Besoin d’un tableau de correspondance à fournir. |
|11| **Procédure de création de release** | - Sébastien a présenté la procédure. <br> - Release 1.3 prévue à **14 h** le même jour, avec accompagnement de Benjamin. |

---

## Décisions prises
| Décision | Responsable / Commentaire |
|----------|---------------------------|
| Instaurer un point **bi‑hebdomadaire** le mercredi à **11 h 30**. | Mickaël (envoi de l’invitation). |
| Ajouter la description de la configuration **DialNumber** dans la PR et la release. | **Benjamin**. |
| Documenter le **scénario de test** (activation de l’option, vérif du PIN). | **Benjamin**. |
| Conserver la **remontée de logs** liée au ticket 166 dans la prochaine release. | Équipe dev (pas de responsable dédié). |
| Lancer le **salon silencieux** dès validation du support juridique. | Mickaël (suivi du dossier juridique). |
| Planifier la **release 1.3** (sans numéro d’appel / code unique) à **14 h** le même jour. | **Benjamin** (avec l’aide de Sébastien). |
| Préparer une **release 1.3.1** pour intégrer le numéro d’appel et le code unique. | Benoît (coordination). |
| Reproduire le problème de connexion **Nuage/WebDAV** et capturer les traces. | **Benjamin** (et Benoît pour les tests). |
| Vérifier et mettre à jour les **bibliothèques Python WebDAV** si besoin. | Équipe technique. |
| Fournir un **tableau de correspondance tags ↔ estimation** (jours/heure). | **Mickaël** (à envoyer d’ici la fin de journée). |
| Clarifier le périmètre et le financement du **SIP Media Gateway**. | Mickaël (avec Yael). |
| Définir le **budget 2025** pour le développement d’Espadès. | Mickaël. |

---

## Questions en suspens
1. **Intégration du code unique** : sera‑t‑il dans la release 1.3 ou 1.3.1 ? (Benoît doit confirmer avec Mickaël).
2. **Nom exact de la variable** de configuration DialNumber côté Arawa (à préciser dans la PR).
3. **Stabilité de la connexion Nuage** : quelles sont les causes exactes (surcharge serveur, bibliothèque obsolète, etc.) ?
4. **Support juridique** pour le salon silencieux : délai de validation.
5. **Spécifications détaillées** du projet SIP Media Gateway (fonctionnalités supplémentaires demandées).

---

## Tâches à effectuer

| Tâche | Responsable | Échéance |
|-------|-------------|----------|
| Envoyer l’invitation du point bi‑hebdomadaire (mercredi 11 h 30). | **Mickaël** | Immédiat |
| Ajouter la description de la configuration **DialNumber** dans la PR. | **Benjamin** | Avant la release 1.3 |
| Rédiger le **scénario de test** (activation option + vérif PIN). | **Benjamin** | Avant la release 1.3 |
| Vérifier l’ordre des migrations et les inclure dans la release. | **Benjamin** | Avant la release 1.3 |
| Conserver la remontée de logs du ticket 166 dans la release. | Équipe dev | Avant la release 1.3 |
| Lancer le **salon silencieux** dès validation juridique. | **Mickaël** | Dès que le support juridique est reçu |
| Créer la **release 1.3** (procédure à 14 h). | **Benjamin** (avec Sébastien) | Aujourd’hui, 14 h |
| Préparer la **release 1.3.1** (numéro d’appel + code unique). | **Benoît** | Après la release 1.3 |
| Reproduire le problème Nuage/WebDAV, capturer les traces. | **Benjamin** | Au plus tard 5 jours |
| Faire tester le problème Nuage par **Benoît** (avec différents navigateurs). | **Benoît** | Au plus tard 5 jours |
| Mettre à jour les bibliothèques Python WebDAV si nécessaire. | Équipe technique | Avant la prochaine release |
| Envoyer le **tableau de correspondance tags ↔ estimation**. | **Mickaël** | Fin de journée |
| Clarifier le périmètre et le financement du **SIP Media Gateway**. | **Mickaël** (avec Yael) | Prochaine semaine |
| Finaliser le **budget 2025** pour le développement d’Espadès. | **Mickaël** | Prochaine réunion |

---

## Prochaine rencontre
- **Date** : mercredi 5 mai 2026
- **Heure** : 11 h 30 (point bi‑hebdomadaire)
- **Ordre du jour prévisionnel** :
  1. Suivi des actions de la réunion du 28 avril.
  2. Retour sur les tests Nuage/WebDAV.
  3. Avancement du salon silencieux et du SIP Media Gateway.
  4. Validation du planning de release 1.3.1.

---

*Fin du compte rendu.*
