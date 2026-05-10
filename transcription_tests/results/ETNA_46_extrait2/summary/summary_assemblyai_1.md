# Compte‑rendu de réunion
**Date** : (non précisée)
**Durée estimée** : ≈ 1 h 30 (déduction basée sur le volume des points abordés)

---

## Participants
| Nom / Rôle | Fonction / Service |
|------------|--------------------|
| **Hugo** | Responsable technique / liaison avec les développeurs |
| **Manon** | Chargée de l’expérience utilisateur / thématisation des tubes |
| **Valra (du Grand Est)** | Représentant de la DRAM du Grand Est |
| **Nicolas** | Responsable infrastructure / serveurs tubes |
| **Développeurs** (2) | Équipe de développement (Dijon) |
| **Équipe Tradeprod** | Gestion du Rancher (environnement de production) |
| **Intervenants non nommés** | Participants aux échanges (ex. équipe Framasoft) |

---

## Objet de la réunion
Faire le point sur l’avancement des projets liés au **Portail Apps**, au **raccourcisseur d’URL**, à l’**architecture micro‑applications**, à la **mise en production du Rancher**, à la **thématisation des tubes** et à la **transcription / transcodage vidéo**.

---

## Sujets abordés

| Thème | Points clés |
|-------|-------------|
| **Statistiques Portail Apps** | - 221 000 comptes ouverts (hors accès direct via l’application). <br>- 73 000 comptes réactivés depuis décembre (≈ 1/3 des utilisateurs en 5 mois). <br>- Plus de 80 000 vidéos sur Apple Educ. |
| **Matomo** | Installation terminée ; premières données fiables sur parcours utilisateur (source, terminaux, etc.). |
| **Version 6.4.1 du portail** | Mise en production ; nouvelles fonctions de cycle de vie utilisateur. |
| **Raccourcisseur d’URL (RMS)** | - Deux développeurs dédiés (visite à Dijon). <br>- Développement prévu jusqu’à fin de semaine, démonstration attendue la semaine prochaine. <br>- Mise à jour planifiée le **1 juillet à 12 h**. |
| **Architecture micro‑applications** | Découpage du portail en appels à des micro‑services sécurisés (tokens). Exemple : gestion des *tiers‑tubes* (11) via micro‑app dédiée. |
| **Rancher (Tradeprod)** | Livré il y a ~2 semaines, mais non fonctionnel ; problème de documentation et de certificats. Demande de clarification en cours. |
| **Thématisation des tubes** | - Thème graphique ancien (DRAM Grand Est) non compatible avec la version 7.1.1 (faille sécurité). <br>- Proposition de masquer les *instances* au profit de *thèmes* (inspiré de Nestled). <br>- Aucun livrable avant la rentrée prochaine (prévision 3‑4 mois). |
| **Transcription vidéo** | Fonctionnelle en environnement de test (version 7). Nécessité de déployer sur tous les serveurs tubes (action avec Nicolas). |
| **Transcodage externalisé** | Projet d’utiliser deux machines dédiées (Dynium, France Numérique) pour le transcodage, afin de réduire la charge des serveurs tubes. |
| **Partenariat Framasoft** | Intégration d’une règle de durée de vie des vidéos (suppression automatique). |
| **Spécificités ministère** | Gestion des vidéos contenant des mineurs (suppression après 1 an) via un plugin dédié. |

---

## Décisions prises
| Décision | Responsable / Date |
|----------|--------------------|
| **Mise à jour du raccourcisseur d’URL** – déploiement le **1 juillet à 12 h**. | Hugo / Équipe dev |
| **Poursuivre le développement des micro‑applications** selon l’architecture décrite. | Équipe dev (Dijon) |
| **Masquage des instances au profit des thématiques** – implémentation différée à la rentrée (3‑4 mois). | Manon & équipe UX |
| **Déploiement de la transcription vidéo** sur l’ensemble des serveurs tubes. | Nicolas |
| **Externalisation du transcodage** sur deux machines dédiées (Dynium, France Numérique). | Équipe infrastructure |
| **Intégration de la règle de durée vidéo via Framasoft** dans le cœur de PeerTube. | Framasoft / équipe dev |
| **Développement du plugin “mineurs”** pour le ministère de l’Éducation nationale. | Équipe dev (plugin) |
| **Clarification et documentation du Rancher** – demande de dérogation et contacts gouvernementaux. | Responsable Rancher (Tradeprod) |

---

## Questions en suspens
| Question | Responsable / Suivi |
|----------|---------------------|
| **Quand la démonstration du raccourcisseur d’URL sera‑t‑elle disponible ?** | Hugo (prévu la semaine prochaine) |
| **Quand le Rancher sera‑t‑il pleinement opérationnel (déploiement d’applications) ?** | Responsable Rancher – dépend de la documentation et des certificats |
| **Calendrier exact de la refonte graphique des tubes (thèmes)** – aucune livraison avant la rentrée, mais besoin de préciser les jalons. | Manon / DRAM Grand Est |
| **Finalisation du devis et du marché pour les développements spécifiques (plugin mineurs, etc.)** | Responsable achats / chef de projet |
| **Plan de suivi des performances après mise en production du transcodage externalisé** | Nicolas / équipe infrastructure |

---

## Tâches à effectuer
| Action | Responsable | Échéance |
|--------|-------------|----------|
| Suivi du développement du raccourcisseur d’URL et organisation de la démonstration. | **Hugo** | Semaine prochaine |
| Finaliser le code du raccourcisseur et préparer le déploiement du 1 juillet. | Développeurs (Dijon) | 1 juillet |
| Déployer la transcription vidéo sur tous les serveurs tubes. | **Nicolas** | Dès que le serveur secondaire est configuré |
| Mettre en place le masquage des instances → affichage thématique. | **Manon** | Avant la rentrée (prévision 3‑4 mois) |
| Rédiger et valider la documentation du Rancher, obtenir les certificats nécessaires. | Responsable Rancher (Tradeprod) | À définir |
| Coordination avec Framasoft pour intégrer la règle de durée de vie des vidéos. | **Équipe dev** | Prochain sprint |
| Développer le plugin “mineurs” (détection & suppression après 1 an). | **Équipe dev** | À planifier (post‑déploiement) |
| Élaborer le devis et lancer l’appel d’offres pour les développements spécifiques. | Responsable achats | ASAP |
| Planifier la prochaine réunion de suivi. | **Organisateur** | Proposé : dans 3 semaines (date à confirmer) |

---

## Prochaine rencontre
- **Date / Heure** : à définir (suggestion : dans 3 semaines).
- **Objectif** : Faire le point sur le raccourcisseur d’URL, le Rancher, la thématisation des tubes et le déploiement de la transcription/transcodage.

---

*Fin du compte‑rendu.*
