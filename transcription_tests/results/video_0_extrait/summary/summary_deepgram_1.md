# Compte rendu de réunion

**Date** : 30 avril 2026
**Durée** : ~ 2 h 30 (la réunion était prévue 1 h)

---

## Participants
- **Benjamin**
- **Benoît**
- **Michael**
- **Équipe Betwardsk / Betfra‑Desk** (représentée par les intervenants)
- **Renater** (mentionnée)
- **DGFI** (financement du projet BBB)
- **MTE** (Ministère de la Transition Écologique)

---

## Objet de la réunion
Suivi des incidents de connexion entre l’application Betwardsk/Betfra‑Desk et le cloud Nextcloud, état d’avancement des projets :
1. Lancement des travaux pour la messagerie nationale (devis, budget, salon silencieux).
2. Développement du connecteur BBB financé par la DGFI.

---

## Sujets abordés

| N° | Sujet | Points clés |
|----|-------|-------------|
| 1 | **Instabilité de la connexion Nextcloud** | - Tests de capture de trames réalisés. <br>- Le token applicatif (validité 30 jours) est correctement transmis, mais la connexion au cloud est lente/instable. <br>- Hypothèses : surcharge du cloud, bibliothèque Python obsolète, version de Nextcloud, plugins du navigateur. |
| 2 | **Reproduction du problème** | - Nécessité de reproduire le dysfonctionnement de façon fiable. <br>- Benoît a un navigateur « particulier » avec de nombreux plugins. |
| 3 | **Mise à jour des librairies** | - Vérifier que les dépendances Python utilisées par Betwardsk sont à jour. |
| 4 | **Travaux messagerie nationale** | - Devis transféré à l’équipe messagerie, validé. <br>- Salon en mode silencieux en attente de retours. |
| 5 | **Budget développement Betfra‑Desk** | - 2 025 € alloués, besoin de définir le vecteur financier. |
| 6 | **Projet connecteur BBB** | - Financé par la DGFI, nécessite des développements supplémentaires avec Renater. <br>- Discussion sur les fonctionnalités à fournir, adaptation aux technologies de Renater. |
| 7 | **Organisation des prochaines réunions** | - Une réunion technique dédiée au connecteur BBB sera planifiée. <br>- Une réunion de suivi des tests Nextcloud sera également prévue. |

---

## Décisions prises

1. **Conserver l’action de reproduction** du problème de connexion avant toute modification majeure.
2. **Maintenir le salon en mode silencieux** jusqu’à réception des retours sur le devis.
3. Le **devis est validé** → les commandes peuvent être lancées dès que le support juridique sera confirmé.
4. **Mettre à jour** les librairies Python de Betwardsk.
5. **Poursuivre le projet BBB** : organiser une réunion dédiée pour cadrer les besoins fonctionnels et les développements avec Renater.
6. **Étudier l’extension** de la durée de validité du token applicatif (au‑delà de 30 jours) pour réduire la sollicitation du portail.

---

## Questions en suspens

- Quelle est la cause exacte de l’instabilité ? (surcharge du cloud, bibliothèque obsolète, version de Nextcloud, plugins navigateur)
- Comment reproduire de façon fiable le problème de connexion ?
- Le token applicatif doit‑il être prolongé ? Si oui, à quelle durée ?
- Quel support juridique est requis pour le lancement des travaux messagerie ?
- Détails du financement du budget Betfra‑Desk (qui porte le coût ?)
- Quels développements supplémentaires Renater devra‑t‑il fournir pour le connecteur BBB ?

---

## Tâches à effectuer

| Responsable | Action | Délai |
|-------------|--------|-------|
| **Benjamin** | Réaliser de nouveaux tests de connexion, capturer les trames, tenter de reproduire le problème. | 1 semaine |
| **Benoît** | Effectuer des tests avec son navigateur, désactiver les plugins éventuels. | 1 semaine |
| **Équipe Betwardsk** | Vérifier et mettre à jour les dépendances Python utilisées. | 3 jours |
| **Michael / Équipe messagerie** | Finaliser le support juridique et valider le financement du devis. | 2 semaines |
| **Organisateur (vous)** | Poster un message sur le canal CHAP pour informer du statut du salon silencieux et du lancement des travaux. | Immédiat |
| **Renater** | Fournir les spécifications techniques des développements internes nécessaires pour le connecteur BBB. | 2 semaines |
| **Organisateur** | Planifier la prochaine réunion technique sur le connecteur BBB et la réunion de suivi des tests Nextcloud. | À fixer (dans les 10 jours) |

---

## Prochaine rencontre

- **Objet** : Suivi des tests de connexion Nextcloud ; cadrage du projet connecteur BBB.
- **Date / Heure** : À définir (prévoir dans les deux prochaines semaines).
- **Durée prévue** : 1 h.

---

*Fin du compte rendu.*
