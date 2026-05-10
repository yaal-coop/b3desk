# Compte rendu de réunion
**Date** : 30 avril 2026
**Durée** : *non précisée* (environ 1 h)

---

## Participants
| Nom | Rôle / Fonction |
|-----|-----------------|
| **Hugo** | Chef de projet – coordination technique |
| **Manon** | Responsable produit / animation des ateliers |
| **Nicolas** | Responsable infrastructure (déploiement transcription) |
| **Développeurs** (2) | Équipe de développement (Dijon) |
| **Représentants ADRA Grand Est** | Partenaires thématiques |
| **Intervenants Framasoft** | Contributeurs au cœur de PeerTube |
| **Équipe Rancher** | Support technique (Rancher‑Crepe‑Rode) |
| **Autres** (développeurs, éditeur Tramasoft) | Participants ponctuels |

---

## Objet de la réunion
Faire le point sur l’état d’avancement des différents projets liés au **Portail Apps** et à la plateforme **Tube** : statistiques d’usage, nouvelles fonctionnalités (URL shortener, micro‑applications), architecture technique (Rancher, micro‑services), refonte graphique des « tubes », transcription vidéo et sécurité des assets.

---

## Sujets abordés

| N° | Sujet | Points clés |
|----|-------|-------------|
| 1 | **Statistiques Portail Apps** | - 80 000 vidéos (pré‑vacances) <br> - 221 000 comptes créés (hors comptes directs sur l’app) <br> - 73 000 comptes ré‑activés depuis décembre (≈ 1/3 des utilisateurs sur 5 mois) |
| 2 | **Matomo** | Installation terminée ; premières données de parcours utilisateurs disponibles (sources, terminaux, etc.). |
| 3 | **Version 6.4.1 du portail** | Mise en prod récente ; ajout du cycle de vie des utilisateurs et petites améliorations. |
| 4 | **Raccourcisseur d’URL** | - Deux devs en charge (visite de Hugo à Dijon). <br> - Livraison prévue fin de semaine / début de semaine prochaine. <br> - API réutilisable par d’autres services. |
| 5 | **Architecture micro‑applications** | - Chaque service sera appelé via une micro‑app sécurisée (tokens). <br> - Exemple : micro‑app « Kertubes » gère destruction de comptes, transfert de vidéos, etc. |
| 6 | **Rancher‑Crepe‑Rode** | - Livré il y a 2 semaines, pas encore fonctionnel. <br> - Documentation incomplète, besoin d’éclaircissements sur le déploiement d’applications. |
| 7 | **Thématique / identité graphique des tubes** | - Thème initial (DRAP Grand Est) obsolète depuis la version 7.1.1 (faille sécurité). <br> - Nouvelle approche : parler de *thèmes* plutôt que d’*instances*. <br> - Déploiement prévu au **rentrée prochaine** (3‑4 mois). |
| 8 | **Transcription vidéo** | - Fonctionnelle en environnement test (version 7). <br> - Besoin d’un deuxième serveur et de la configuration de tous les serveurs tubes. <br> - Objectif : externaliser transcription & transcodage pour alléger les serveurs tubes. |
| 9 | **Asset 1.1 – sécurité** | - Correctifs de failles en cours. <br> - Discussion avec Tramasoft et développeurs sur la répartition des développements. |
|10| **Plugin vidéo expiration** | - Core PeerTube (Framasoft) : durée de vie standard des vidéos. <br> - Plugin spécifique ministère : suppression automatique des vidéos contenant des mineurs après 1 an. |

---

## Décisions prises
| Décision | Responsable | Échéance |
|----------|--------------|----------|
| **Finaliser le raccourcisseur d’URL** et le rendre disponible via l’API. | Hugo (suivi des devs) | Fin de semaine / début semaine prochaine |
| **Adopter l’architecture micro‑applications** pour le cycle de vie des comptes et la gestion des tubes. | Équipe technique (Hugo) | Déploiement progressif dès le prochain sprint |
| **Reporter la refonte graphique des tubes** à la rentrée (3‑4 mois). | Manon (coordination avec ADRA Grand Est) | Rentrée prochaine |
| **Déployer la transcription** sur un second serveur et paramétrer tous les serveurs tubes. | Nicolas | Avant fin mai |
| **Séparer les développements** : <br>• Core PeerTube – expiration vidéo (Framasoft) <br>• Plugin spécifique ministère – gestion des vidéos contenant des mineurs. | Framasoft (core) / Équipe interne (plugin) | Préparer devis d’ici fin juin |
| **Poursuivre les investigations sur Rancher** pour rendre la plateforme opérationnelle. | Équipe Rancher | À définir (prochaine itération) |

---

## Questions en suspens
1. **Rancher** : Quand la documentation sera‑telle complète et le déploiement d’applications possible ?
2. **Thèmes des tubes** : Quels seront les livrables exacts (maquettes, guidelines) avant le lancement à la rentrée ?
3. **Sécurité Asset 1.1** : Quels sont les points restants à corriger avant la mise en production finale ?
4. **Calendrier de mise à jour du portail (6.4.1)** : Quels changements seront inclus dans la prochaine release (post‑vacances) ?

---

## Tâches à effectuer

| Tâche | Responsable | Délai |
|-------|-------------|-------|
| Suivi du **développement du raccourcisseur d’URL** (tests, documentation API). | Hugo | Fin de semaine |
| **Déploiement du deuxième serveur de transcription** et configuration globale. | Nicolas | 31 mai |
| **Organisation d’une réunion de cadrage** avec ADRA Grand Est pour finaliser le nouveau thème. | Manon | 15 juin |
| **Rédaction de la documentation Rancher** (procédures d’installation, usage). | Équipe Rancher | 30 juin |
| **Préparer le devis** pour le développement du plugin « vidéo mineur ». | Équipe produit | 10 juin |
| **Coordonner avec Framasoft** la mise à jour du core PeerTube (expiration vidéo). | Hugo | 20 juin |
| **Planifier les tests de sécurité** sur Asset 1.1 après correctifs. | Responsable sécurité (non nommé) | 15 juin |
| **Mise à jour des statistiques Matomo** : créer les premiers rapports d’usage. | Analyste data | 5 mai |

---

## Prochaine rencontre
**Date proposée** : **15 mai 2026** (même créneau horaire)
**Objectif** : Faire le point sur le raccourcisseur d’URL, la transcription, et les avancées Rancher.

---

*Fin du compte rendu.*
