# Compte rendu de réunion

**Date** : (non précisée)
**Durée estimée** : non indiquée

---

## Participants
- **Hugo** (développeur)
- **Manon** (responsable fonctionnelle)
- **Nicolas** (responsable technique)
- **Équipe Portail Apps** (présence implicite)
- **Développeur(s) externe(s)** (Pramasoft)
- **Éditeur** (logiciel de gestion vidéo)

---

## Objet de la réunion
Faire le point sur l’état d’avancement du **Portail Apps** (statistiques, version, nouvelles fonctionnalités) ainsi que sur les projets connexes : raccourcissement d’URL, architecture micro‑applications, refonte graphique (thèmes), transcription & transcodage des vidéos, et les aspects de sécurité et de conformité.

---

## Sujets abordés

| N° | Thème | Points clés |
|----|-------|-------------|
| 1 | **Statistiques du portail** | • ≈ 82 000 vidéos, 221 000 comptes ouverts (hors comptes directs sur l’app). <br>• 73 000 comptes ré‑activés depuis décembre. <br>• Matomo installé → premières données de parcours utilisateurs. |
| 2 | **Version 6.4.0** | Mise en production avant les vacances. Quelques travaux de cycle de vie restent à finaliser. |
| 3 | **Raccourcissement d’URL** | Développement en cours (2 développeurs). Hugo doit présenter les premiers prototypes début de semaine prochaine. |
| 4 | **Mise à jour sécuritaire 7.1.1** | Planifiée le **1 juillet à 12 h**. Priorité aux correctifs de failles. |
| 5 | **Architecture micro‑applications** | • Déploiement d’une micro‑app par service (ex. « pierres‑cubes »). <br>• Pré‑prod livrée il y a 2 semaines, mais non fonctionnelle (problèmes de Rancher, certificats). |
| 6 | **Thématique graphique** | Travail initié par le « RAT du Grand Est ». Nouvelle approche : parler de *thèmes* plutôt que d’*instances*. Aucun changement prévu avant la rentrée prochaine. |
| 7 | **Transcription & transcodage** | • Transcription fonctionnelle en test, à généraliser. <br>• Déploiement prévu avec Nicolas (serveur supplémentaire). <br>• Objectif : externaliser transcodage pour alléger les serveurs tubes. |
| 8 | **Gestion du cycle de vie des vidéos** | • Développement d’une règle « vidéo expirée après X temps » (pramasoft). <br>• Cas particulier : vidéos contenant des mineurs → suppression après 1 an (développé en interne). |
| 9 | **Devis & marché** | Attente de devis du développeur et de l’éditeur pour les plugins de gestion du cycle de vie. |

---

## Décisions prises
1. **Mise à jour 7.1.1** sera déployée le **1 juillet à midi**.
2. Le **raccourcissement d’URL** continue ; Hugo présentera les avancées la semaine prochaine.
3. La **refonte graphique (thèmes)** sera reportée à la rentrée prochaine ; aucune modification avant.
4. **Transcription** sera déployée sur l’ensemble des serveurs tubes dès que le deuxième serveur sera configuré (responsable : Nicolas).
5. **Externalisation du transcodage** sera planifiée après le déploiement complet de la transcription.
6. **Règle d’expiration des vidéos** : implémentation par Pramasoft (durée maximale) ; règle spécifique aux mineurs gérée en interne.

---

## Questions en suspens
- **Rancher / pré‑prod** : comment finaliser le déploiement des micro‑applications (certificats, droits d’exploitation) ?
- **Calendrier exact** de la mise en place du nouveau thème graphique.
- **Devis final** pour les plugins de gestion du cycle de vie (qui doit être validé, quel budget).
- **Capacité du serveur de transcription** : besoin d’un deuxième serveur, mais aucune date précise n’est fixée.

---

## Tâches à effectuer

| Tâche | Responsable | Échéance |
|-------|-------------|----------|
| Présenter les premiers prototypes de raccourcissement d’URL | **Hugo** | Début de semaine prochaine |
| Suivi du rapport RM et validation de la mise à jour 7.1.1 | **Équipe Portail Apps** | 1 juillet 12 h |
| Configurer le deuxième serveur de transcription et le paramétrer sur tous les serveurs tubes | **Nicolas** | Dès que le serveur sera disponible (prévu Q2) |
| Finaliser le déploiement des micro‑applications en pré‑prod (résolution des problèmes Rancher) | **Équipe Technique** | Avant fin juin |
| Élaborer le devis détaillé pour les plugins de gestion du cycle de vie (vidéo expiration) | **Développeur Pramasoft** + **Éditeur** | À réception du besoin, avant fin mai |
| Préparer la communication « Thème disparu, retour prochain » pour les utilisateurs | **Manon** | Avant la rentrée (septembre) |
| Suivi des certificats et des exigences de sécurité pour la version 7.1.1 | **Équipe Sécurité** | Avant le 1 juillet |

---

## Prochaine rencontre
*Pas de date fixée lors de cette réunion.*
Il est recommandé de programmer une nouvelle réunion **début juin** pour faire le point sur le déploiement de la version 7.1.1, la mise en production de la transcription et l’avancement du projet Rancher.
