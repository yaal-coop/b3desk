# Compte rendu de réunion
**Date** : 30 avril 2026
**Durée estimée** : ~ 2 h (initialement prévue 1 h)

---

## Participants
| Nom | Rôle / Fonction |
|-----|-----------------|
| **Johan** | Animateur de la réunion |
| **Benjamin** | Développeur B3Desk |
| **Michael** | Développeur / Responsable configuration |
| **Benoît** | Responsable tests & suivi financier |
| **Sébastien** | Responsable release |
| **Priscila** | Mentionnée (utilisatrice) |
| **Autres** | Participants ponctuels (ex. : Mickaël) |

---

## Objet de la réunion
Suivi du projet **B3Desk** : points techniques (configuration BBB/ScaleLight, code unique, ticket 166), organisation des réunions de suivi, état des livrables, investigations sur l’intégration Nextcloud/Nuage, budget et planning des développements (salon silencieux, SIP Media Gateway, backlog).

---

## Sujets abordés
1. **Mise en place d’un point de suivi bi‑hebdomadaire**
2. **Revue de la PR « code unique »**
   - Modifications de configuration (ScaleLight / BBB) à préciser.
   - Scénario de test à fournir.
3. **Ticket 166 – Erreur 500 sur les salons**
   - Résolution côté Arawa, conservation du log.
4. **Investigations Nextcloud / Nuage**
   - Capture de trames, stabilité du WebDAV, version de la bibliothèque Python.
5. **Budget / devis pour le salon silencieux**
   - Validation du devis, besoin de support juridique.
6. **Projet SIP Media Gateway** (intégration connecteur SIP à BBB)
7. **Backlog & chiffrage**
   - Utilisation de tags (large, medium, …) et tableau d’estimation.
8. **Plan de release**
   - Release 1.3 (sans numéro d’appel / code unique) → 1.3.1 ultérieurement.
9. **Organisation de la prochaine réunion**

---

## Décisions prises
| Décision | Responsable | Commentaire |
|----------|-------------|--------------|
| Instaurer un point de suivi toutes les 2 semaines, le **mercredi à 11h30**. | **Johan** (organisation) | Planning à diffuser lundi. |
| Ajouter dans la PR la description du paramètre à modifier (ScaleLight/BBB) et le reporter dans la release. | **Michael** | Garantir traçabilité. |
| Conserver la remontée de log du ticket 166 dans la prochaine release. | **Benjamin** | Aucun changement de code requis. |
| Le **salon silencieux** peut être lancé dès que le devis est validé (déjà validé). | **Benoît** (finance) | Attente du support juridique uniquement. |
| **Release 1.3** sera créée (sans numéro d’appel / code unique). **Release 1.3.1** intégrera ces fonctionnalités plus tard. | **Sébastien** | À réaliser cet après‑midi. |
| Prioriser dans la prochaine release :
  - Classement alphabétique / favoris des salles de visio.
  - Fonctionnalité salon silencieux. | **Équipe dev** | Le numéro d’appel et le code unique seront testés ultérieurement. |
| Reproduire les problèmes de connexion Nuage/Nextcloud et documenter les captures de trames. | **Benjamin** | Envoi des résultats dès que possible. |
| Benoît effectuera des tests complémentaires (navigateurs, charge serveur). | **Benoît** | Retour prévu avant la prochaine réunion. |
| Fournir, d’ici la fin de journée, un tableau de correspondance **tags ↔ estimation (jours/heures)**. | **Michael** | Utilisé pour le chiffrage du backlog. |
| Planifier une réunion avec **Renater** pour le projet SIP Media Gateway (définir périmètre et financement). | **Johan** | À organiser dès que possible. |

---

## Questions en suspens
| Question | Responsable(s) | État |
|----------|----------------|------|
| Intégration du **code unique** dans quelle release ? (1.3 ou 1.3.1) | **Benoît** (validation) | En attente de décision finale. |
| Validation du **support juridique** pour le salon silencieux. | **Benoît** / équipe juridique | En cours. |
| Stabilisation de la connexion **Nuage ↔ B3Desk** (WebDAV) – cause exacte du problème. | **Benjamin**, **Benoît** | Investigations en cours. |
| Besoin de **mise à jour de la bibliothèque Python WebDAV** (version, compatibilité). | **Benjamin** | À vérifier lors des tests. |
| Définir le **budget 2025** pour le développement de B3Desk et le projet SIP Media Gateway. | **Benoît**, **Direction financière** | En cours de finalisation. |

---

## Tâches à effectuer
| Tâche | Responsable | Délai |
|-------|-------------|-------|
| Diffuser le planning du point bi‑hebdomadaire (mercredi 11h30). | **Johan** (ou Benjamin) | Lundi prochain |
| Préciser le paramètre de configuration à modifier dans la PR. | **Michael** | Avant la prochaine release |
| Réaliser la capture de trames et reproduire le problème Nextcloud/Nuage. | **Benjamin** | Au plus tard **vendredi** |
| Effectuer des tests supplémentaires (navigateurs, charge serveur). | **Benoît** | Avant la prochaine réunion |
| Créer la **release 1.3** (tags, commits, branche). | **Sébastien** | Cet après‑midi |
| Envoyer le tableau **tags ↔ estimation** (jours/heure). | **Michael** | Fin de journée |
| Valider le devis du salon silencieux et obtenir le support juridique. | **Benoît** | ASAP |
| Organiser une réunion avec **Renater** (SIP Media Gateway). | **Johan** | À planifier (semaine prochaine) |
| Mettre à jour le backlog avec les tags d’estimation. | **Équipe dev** | Après réception du tableau de Michael |
| Planifier la **prochaine réunion de suivi** (date à définir). | **Johan** | À fixer (probablement la semaine suivante) |

---

## Prochaine rencontre
Une nouvelle réunion de suivi sera planifiée **la semaine prochaine** (date et heure à confirmer). Elle portera sur l’avancement des actions listées ci‑dessus, la validation du budget et les premiers résultats des investigations Nextcloud/Nuage.

---

*Rédigé par l’assistant de rédaction de comptes rendus.*
