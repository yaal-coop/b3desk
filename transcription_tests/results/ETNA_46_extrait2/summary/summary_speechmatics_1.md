# Compte rendu de réunion
**Date** : 30 avril 2026
**Durée** : non précisée (environ 1 h)

---

## Participants
| Nom | Fonction / Rôle |
|-----|-----------------|
| **Hugo** | Responsable technique / coordinateur des développements |
| **Manon** | Chargée de projet (thématiques PeerTube) |
| **Nicolas** | Responsable infrastructure (serveurs de transcription) |
| **Développeurs** (2) | Travaux sur le raccourcisseur d’URL |
| **Équipe Framasoft** | Partenaire pour le plugin de cycle de vie |
| **Équipe ATS / Portail AP** | Présente les statistiques et l’évolution du portail |
| **Autres participants** | Membres de la DRAC du Grand Est & Grand Ouest, équipe de production |

---

## Objet de la réunion
Faire le point sur l’état d’avancement des différents projets liés au **portail AP / ATS**, aux **services vidéo (VOD, PeerTube)** et aux **infrastructures associées** (rancher, micro‑applications, transcription, raccourcisseur d’URL).

---

## Sujets abordés

| Sujet | Points clés |
|-------|-------------|
| **Statistiques du portail** | - 81 000 → ≈ 82 000 vidéos VOD.<br>- 221 000 comptes ouverts (hors comptes créés directement sur le cloud).<br>- 73 000 comptes réactivés depuis décembre (≈ 1/3 des utilisateurs actifs sur 5 mois). |
| **Installation de Matomo** | - Permet d’obtenir des stats précises sur le parcours utilisateur (origine, terminal, etc.).<br>- Données fiables dès le 3ᵉ semaine d’utilisation. |
| **Mise en production 6.4 du portail** | - Fonctionnalités de cycle de vie utilisateur ajoutées.<br>- Travaux en cours sur le raccourcisseur d’URL. |
| **Raccourcisseur d’URL** | - Deux développeurs mobilisés.<br>- Collaboration avec l’équipe de Dijon (échange d’une matinée).<br>- Livraison prévue **8 juillet 2024 à 12 h**. |
| **Architecture micro‑applications** | - Chaque service (ex. PeerTube) sera appelé via une micro‑application sécurisée (token).<br>- Centralisation de la logique métier dans la micro‑app, pas dans le portail. |
| **Rancher (pré‑prod)** | - Livré, mais toujours non fonctionnel.<br>- Problèmes de déploiement (logiciel libre vs exploitant) et de certificats. |
| **Thématiques / identité graphique des PeerTube** | - 11 instances PeerTube, besoin d’une identité visuelle unifiée.<br>- Version 7.1.1 ne supporte plus les évolutions graphiques introduites depuis la 5.0 → 6.4.<br>- Travail collaboratif (DRAC Grand Est, Grand Ouest, Hugo, Manon) : nouvelle approche « thèmes » au lieu d’« instances ».<br>- Déploiement prévu **au plus tard à la rentrée prochaine** (3‑4 mois). |
| **Transcription & transcodage vidéo** | - Fonctionnalité opérationnelle en test sur la version 7.<br>- Besoin d’un second serveur de transcription pour comparaison.<br>- Objectif : externaliser transcription & transcodage sur deux grosses machines afin de réduire la charge des serveurs de diffusion. |
| **Cycle de vie des comptes & vidéos** | - Plugin Framasoft : durée de vie maximale d’une vidéo (auto‑effacement).<br>- Plugin spécifique (minors) : suppression d’une vidéo contenant des mineurs après 1 an (développement interne). |
| **Sécurité** | - Mise à jour urgente 7.1.0 pour corriger une faille. |

---

## Décisions prises
| Décision | Responsable / Commentaire |
|----------|---------------------------|
| **Déploiement du raccourcisseur d’URL** le 8 juillet 2024 à 12 h. | Hugo (coordination) |
| **Adoption de l’architecture micro‑applications** pour tous les services (PeerTube, tubes, etc.). | Équipe technique (portail) |
| **Prioriser le déploiement de la transcription** sur un second serveur avant de généraliser. | Nicolas |
| **Passer à une communication « thèmes »** plutôt qu’« instances » pour les PeerTube. | Manon & Hugo (pilotage) |
| **Externaliser transcription & transcodage** sur deux machines dédiées. | Nicolas & équipe infra |
| **Développer le plugin de suppression des vidéos contenant des mineurs** (déploiement sous forme de plugin, pas dans le cœur PeerTube). | Équipe interne + Framasoft (partenariat) |

---

## Questions en suspens
| Question | Responsable / Prochaine action |
|----------|--------------------------------|
| **Rancher pré‑prod** : pourquoi le déploiement échoue‑t‑il ? (logiciel libre vs exploitant, certificats). | Équipe infra – demander clarification supplémentaire au support Rancher. |
| **Calendrier exact** pour la refonte graphique des PeerTube (thèmes). | Manon – fournir un planning détaillé d’ici la fin mai. |
| **Modalités de mise à disposition du raccourcisseur d’URL via API** pour d’autres services. | Hugo – rédiger la documentation API avant le 15 juillet. |
| **Devis et marché** pour le plugin de cycle de vie (Framasoft). | Responsable projet – finaliser le cahier des charges et lancer appel d’offres. |

---

## Tâches à effectuer

| Tâche | Responsable | Échéance |
|-------|-------------|----------|
| Finaliser le développement du raccourcisseur d’URL et préparer le déploiement. | Deux développeurs (équipe Dijon) | 8 juillet 2024 |
| Déployer le deuxième serveur de transcription et réaliser les tests de comparaison. | Nicolas | 15 mai 2024 |
| Rédiger la documentation API du raccourcisseur d’URL. | Hugo | 15 juillet 2024 |
| Clarifier les exigences de certificat et le processus de déploiement sur Rancher. | Équipe infra | 10 mai 2024 |
| Élaborer le planning détaillé de la refonte des thèmes PeerTube. | Manon | 31 mai 2024 |
| Produire le cahier des charges et lancer le marché pour le plugin de suppression des vidéos mineurs. | Responsable projet (non nommé) | 30 mai 2024 |
| Coordination avec Framasoft pour l’intégration du plugin de durée de vie vidéo. | Hugo / Framasoft | 15 juin 2024 |

---

## Prochaine rencontre
**Date proposée** : 15 mai 2024
**Objet** : Suivi des actions (rancher, transcription, raccourcisseur d’URL) et validation du planning de refonte des thèmes PeerTube.

---

*Fin du compte rendu.*
