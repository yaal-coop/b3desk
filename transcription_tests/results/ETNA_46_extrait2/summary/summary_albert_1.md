# Compte rendu de réunion

**Date** : (non précisée)
**Durée estimée** : non indiquée

---

## Participants
| Nom | Rôle / Fonction |
|-----|-----------------|
| Hugo | Responsable fonctionnel / coordinateur technique |
| Manon | Chargée de projet (thématiques tubes) |
| Valera (Grand Est) | Représentant DRAP du Grand Est |
| Nicolas | Responsable déploiement transcription vidéo |
| Développeurs (2) | Développement du raccourcisseur d’URL et du RL |
| Autres intervenants | Équipe portail Apps, équipe infrastructure, éditeur Framasoft |

---

## Objet de la réunion
Faire le point sur l’état d’avancement du **portail Apps**, du **raccourcisseur d’URL**, de l’**architecture du cycle de vie**, du **Rancher en pré‑production**, des **thématiques des tubes** et du **déploiement de la transcription / transcodage vidéo**.

---

## Sujets abordés

| Sujet | Points clés |
|-------|-------------|
| **Statistiques du portail Apps** | 81 000 – 82 000 vidéos, 221 000 comptes (hors comptes créés directement sur les applis). 73 000 comptes actifs depuis décembre. |
| **Matomo** | Installé depuis 3 semaines → premières analyses de parcours utilisateurs disponibles. |
| **Portail 6.4.1** | Mis en production (nouveau cycle de vie, petites améliorations). |
| **Raccourcisseur d’URL (RL)** | Deux devs travaillent dessus, échange avec l’équipe de Dijon, démonstration attendue la semaine prochaine, mise à disposition via API (URL + QR‑code). |
| **Architecture du cycle de vie** | Passage à des micro‑applications sécurisées (token) pour chaque service (ex. gestion des comptes sur les « tubes »). |
| **Rancher (pré‑prod)** | Livré il y a 2 semaines, encore non fonctionnel (problèmes de certificats, procédure de déploiement). |
| **Thématiques des tubes** | Refondre l’affichage : passer d’« instances » à « thèmes » pour une meilleure lisibilité. Travail en cours, mise en production prévue à la rentrée. |
| **Transcription vidéo** | Fonctionnelle en environnement test, prête à être généralisée sur la version 7.1.1. Nécessite déploiement sur tous les serveurs tubes (action de Nicolas). |
| **Transcodage externalisé** | Projet d’externaliser le transcodage (et la transcription) sur des machines dédiées (DINUM, Constellation, etc.) afin de soulager les serveurs tubes. |
| **Sécurité version 7.1.1** | Priorité au déploiement de la 7.1.1 pour corriger une faille de sécurité. |
| **Gestion du cycle de vie des vidéos** | Discussion avec Framasoft (règles de durée de vie) et besoin d’un plugin spécifique pour le ministère (détection de mineurs, suppression après 1 an). |
| **Devis et marché** | En attente de devis pour les développements/plugins. |

---

## Décisions prises
| Décision | Responsable(s) | Délai / Commentaire |
|----------|----------------|---------------------|
| Lancer une démonstration du raccourcisseur d’URL la semaine prochaine. | Hugo (coordination) | À préparer d’ici fin de semaine. |
| Prioriser le déploiement de la version **7.1.1** du portail (sécurité). | Équipe technique | Déploiement immédiat. |
| Passer à une approche **thématique** pour les tubes (masquer les instances). | Manon & Valera (GR‑Est) | Mise en production prévue à la rentrée (3‑4 mois). |
| Externaliser transcription & transcodage sur des serveurs dédiés. | Nicolas (déploiement) + équipes infra | Phase de test en cours, déploiement progressif. |
| Répartir les développements : <br>• Règles de durée de vie → **Framasoft** <br>• Gestion spécifique (mineurs) → **Plugin interne** | Équipe produit | En attente de devis. |
| Continuer les investigations sur le **Rancher** (certificats, procédure de déploiement). | Équipe infrastructure | À résoudre avant fin du mois. |

---

## Questions en suspens
| Question | Responsable(s) | État |
|----------|----------------|------|
| Quand le **Rancher** sera‑t‑il pleinement opérationnel (déploiement d’applications) ? | Équipe infra | En cours d’investigation (certificats, droits de déploiement). |
| Quels sont les **devis** exacts pour les plugins vidéo (durée de vie, gestion des mineurs) ? | Équipe produit / éditeur | En attente de réponses des fournisseurs. |
| Date précise de mise à disposition du **raccourcisseur d’URL** en production. | Hugo | Démonstration prévue, date de mise en prod à confirmer. |
| Validation du **plan de transcodage externalisé** (capacités des machines DINUM/Constellation). | Nicolas & équipes infra | Étude en cours. |
| Gestion des **certificats** pour le Rancher en pré‑prod. | Équipe infra | Demande de clarification en cours. |

---

## Tâches à effectuer

| Tâche | Responsable | Échéance |
|-------|-------------|----------|
| Préparer la démonstration du raccourcisseur d’URL (scénarios, UI). | Hugo | Semaine prochaine |
| Déployer la version 7.1.1 du portail (mise à jour sécurité). | Équipe technique | Immédiat |
| Finaliser la documentation et les scripts de déploiement du **Rancher** (certificats, droits). | Équipe infra | Fin du mois |
| Paramétrer et déployer la **transcription** sur tous les serveurs tubes (version 7). | Nicolas | Avant la fin du trimestre |
| Élaborer le **plan de transcodage externalisé** (dimensionnement, contrats). | Nicolas + équipes infra | Q2 2026 |
| Rédiger et envoyer les **devis** pour les plugins vidéo (Framasoft + interne). | Équipe produit | 15 mai 2026 |
| Concevoir les maquettes des **thématiques tubes** et préparer le guide utilisateur. | Manon & Valera | Rentrée scolaire (septembre 2026) |
| Suivre les retours de la démonstration du raccourcisseur d’URL et planifier la mise en production. | Hugo | Après la démonstration |

---

## Prochaine rencontre
*Pas de date fixée lors de cette réunion.*
Il est recommandé de programmer une nouvelle réunion **dans 3 à 4 semaines** pour faire le point sur le raccourcisseur d’URL, le Rancher et l’avancement des thématiques tubes.

---

*Compte rendu rédigé par l’assistant spécialisé en comptes rendus de réunion.*
