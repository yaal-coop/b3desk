# Compte rendu de réunion
**Date** : 30 avril 2026
**Durée estimée** : non précisée (environ 1 h)

---

## Participants
| Nom / Rôle | Fonction / Organisation |
|------------|--------------------------|
| **Hugo** | Développeur / coordinateur technique |
| **Manon** | Responsable produit / thématisation |
| **Valérie (Grand Est)** | Représentante régionale (Grand Est) |
| **Nicolas** | Responsable infrastructure & déploiement |
| **Framasoft** | Éditeur partenaire (développement plugins) |
| **Développeur(s)** | Équipe de développement (2 personnes) |
| **Speaker** | Animateur de la réunion (précise les points) |

---

## Objet de la réunion
Faire le point sur l’avancement du **portail Apps** (statistiques, développements, sécurité, architecture micro‑services, thématisation, transcription & transcodage) et définir les actions prioritaires avant la reprise post‑vacances.

---

## Sujets abordés

| N° | Thème | Points clés |
|----|-------|-------------|
| 1 | **Statistiques du portail** | - 82 000 vidéos (pré‑vacances) <br> - 221 000 comptes ouverts (hors ouvertures directes) |
| 2 | **Suivi d’usage (Matomo)** | Statistiques détaillées disponibles (parcours, terminaux, etc.) |
| 3 | **Raccourcissement LRL** | Aucun avancement visible ; discussion avec Hugo et l’équipe. |
| 4 | **Développements en cours** | - 2 devs travaillent jusqu’à fin de semaine.<br> - Rapport de développement attendu fin de semaine.<br> - Mise à jour prévue le **1 juillet à 12 h**. |
| 5 | **API de génération d’URL courtes** | Outil disponible pour d’autres services. |
| 6 | **Architecture micro‑applications** | - Déploiement par service, sécurisation via tokens.<br> - 7 micro‑apps couvrent 11 « tubes ». |
| 7 | **Rancher pré‑prod** | Livré il y a 2 semaines, toujours non fonctionnel. |
| 8 | **Dérogations certificats** | Demande de clarification en cours. |
| 9 | **Thématisation (identité graphique)** | - 11 tubes → besoin d’une identité claire.<br> - Travail prévu, mais aucune livraison avant la rentrée (3‑4 mois). |
|10| **Faille de sécurité 7.1.1** | Urgence traitée en 3 semaines, problème résolu. |
|11| **Transcription vidéo** | Fonctionnelle en test ; généralisation à déployer avec Nicolas. |
|12| **Externalisation transcodage** | Projet de déplacer transcription & transcodage sur serveurs dédiés pour alléger les tubes. |
|13| **Priorités** | - Déploiement de l’asset 1.1 (failles de sécurité). |
|14| **Cycle de vie comptes/vidéos** | - Besoin de devis (développeur, Framasoft). <br> - Fonction d’auto‑effacement des vidéos à implémenter (Framasoft). |

---

## Décisions prises
| Décision | Responsable | Délai |
|----------|--------------|-------|
| **Mise à jour du portail** le 1 juillet à midi. | Hugo (coordination) | 01/07/2026 |
| **Prioriser le déploiement de l’asset 1.1** (sécurité). | Nicolas & équipe infra | Immédiat |
| **Déployer la transcription** sur l’asset 1.1 puis généraliser. | Nicolas | Après mise à jour du 1 juillet |
| **Externaliser transcription & transcodage** sur deux serveurs dédiés. | Nicolas + équipe infra | À planifier (post‑déploiement) |
| **Diviser le développement du cycle de vie** : <br>– Auto‑effacement → Framasoft <br>– Gestion spécifique (ex. “mine” dans vidéo) → équipe interne | Framasoft / Développeur interne | En cours (devis à obtenir) |
| **Thématisation** : aucune mise en production avant la rentrée (3‑4 mois). | Manon (pilotage) | Rentrée scolaire 2026‑2027 |
| **Clarifier les demandes de dérogation certificats**. | Speaker (demande) | ASAP |
| **Résoudre le Rancher pré‑prod** (mettre en service). | Équipe infra | À définir |

---

## Questions en suspens
1. **État du Rancher pré‑prod** : pourquoi n’est‑il toujours pas fonctionnel ?
2. **Détails des dérogations certificats** : quelles sont les exigences exactes ?
3. **Calendrier précis** pour la mise en place de la thématisation (jalons intermédiaires).
4. **Devis du développeur** pour le cycle de vie complet (auto‑effacement + spécificités).

---

## Tâches à effectuer

| Action | Responsable | Échéance |
|--------|-------------|----------|
| Fournir le **rapport de développement** de la semaine. | Hugo | Fin de semaine (03/05/2026) |
| **Déployer l’asset 1.1** (mise à jour sécurité). | Nicolas | Avant le 01/07/2026 |
| Configurer **tous les serveurs tubes** pour la transcription automatisée. | Nicolas | Après déploiement asset 1.1 |
| **Obtenir le devis** pour le cycle de vie des comptes/vidéos. | Développeur interne | 10 mai 2026 |
| **Finaliser la charte graphique** des 11 tubes (prototype). | Manon | Avant la rentrée (septembre 2026) |
| **Organiser la réunion de suivi** (thématisation) avec Valérie, Hugo, Manon. | Manon | Dans 2 semaines (post‑vacances) |
| **Clarifier les demandes de dérogation** auprès du service certificats. | Speaker | ASAP |
| **Planifier l’externalisation** du transcodage (acquisition serveurs). | Nicolas | Q3 2026 |

---

## Prochaine rencontre
**Date prévue** : dans **2 semaines** (après les vacances d’été), avec la participation de **Valérie (Grand Est), Hugo, Manon** et les équipes techniques.

---

*Fin du compte rendu.*
