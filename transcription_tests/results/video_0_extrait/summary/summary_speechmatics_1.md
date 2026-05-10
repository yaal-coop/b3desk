# Compte rendu de réunion

**Date** : 30 avril 2026
**Durée estimée** : ~1 heure (prévue 1 h, la réunion a débordé légèrement)

---

## Participants
| Nom | Rôle / Fonction |
|-----|-----------------|
| **Benjamin** | Responsable des tests de capture de trames (Nextcloud) |
| **Benoît** | Testeur (navigation, WebDAV) |
| **Renata** | Responsable montées en charge / adaptation |
| **Michael** | Contact technique (définition de l’offre) |
| **Reynaert** | Développeur interne (team) |
| **Intervenant(e) non nommé(e)** | Animateur·trice de la réunion, suivi projets & budgets |

---

## Objet de la réunion
1. **Analyse des performances et de la stabilité du flux WebDAV entre B3D et le cloud Nextcloud** (token, durée de validité, latence).
2. **État d’avancement du projet d’API messagerie nationale** (lancement, devis, financement).
3. **Budget 2025 pour le développement « bêtes froides »** et validation du devis.
4. **Projet Media Gateway / connecteur SIP** (financement DGFIP, besoins fonctionnels, adaptation technique).
5. **Organisation et planification des actions à venir**.

---

## Sujets abordés & décisions prises

| Sujet | Points clés | Décision |
|-------|-------------|----------|
| **1. Performances WebDAV (Nextcloud)** | - Les requêtes passent uniquement par le cloud une fois le token obtenu.<br>- Le token est valide 30 jours.<br>- Latence observée : possible surcharge du cloud ou bibliothèque Python WebDAV obsolète.<br>- Nécessité de reproduire le problème (capturer les trames au moment de l’échec). | - **Action** : poursuivre les tests jusqu’à reproduction du dysfonctionnement.<br>- **Report** : analyse détaillée sera faite lors d’une prochaine réunion. |
| **2. API messagerie nationale** | - Aucun retour pour le moment, projet en stand‑by.<br>- Le devis a été transféré à l’équipe messagerie, financement confirmé. | - Le « salon silencieux » reste en attente de retours.<br>- L’animateur(e) enverra un message sur CHAP dès que le lancement sera envisagé. |
| **3. Devis & budget** | - Devis validé, aucune contrainte budgétaire immédiate.<br>- Besoin de support juridique identifié. | - Lancement des commandes possible dès que le support juridique sera trouvé.<br>- Le budget 2025 pour les « bêtes froides » doit être attribué (recherche de financement en cours). |
| **4. Projet Media Gateway / SIP** | - Financement par la DGFIP.<br>- Nécessité d’ajouter des fonctionnalités supplémentaires (SIP A/B, arborescence via API).<br>- Risque d’un gros chantier si on doit ré‑implémenter la logique d’affichage. | - Démarrer le projet avec les briques existantes, puis envisager des évolutions selon les besoins et le financement.<br>- Organiser une réunion technique avec Michael pour clarifier l’offre actuelle. |
| **5. Coordination interne** | - Renata doit être consultée sur les montées en charge et les adaptations nécessaires.<br>- Reynaert assure les développements internes. | - Planifier une réunion de suivi avec Renata et Reynaert. |

---

## Questions en suspens
1. **Quelle est la cause exacte de la lenteur WebDAV ?**
   - Surcharge du cloud ? Obsolescence de la bibliothèque Python ?
2. **Le token applicatif peut‑il être prolongé au‑delà de 30 jours ?**
3. **Quel est le statut exact du support juridique nécessaire au lancement du devis ?**
4. **Version de Nextcloud utilisée : est‑elle suffisamment récente pour éviter les bugs connus ?**
5. **Quelles spécifications exactes attendues pour le connecteur SIP du projet Media Gateway ?**

---

## Tâches à effectuer

| Action | Responsable | Échéance |
|--------|-------------|----------|
| Refaire la capture de trames et reproduire le problème WebDAV | **Benjamin** | Dès que possible |
| Exécuter de nouveaux tests WebDAV (navigation, plugins) | **Benoît** | Dès que possible |
| Vérifier que la bibliothèque Python WebDAV est à jour et compatible | **Équipe technique** | Prochaine semaine |
| Rédiger un message sur CHAP pour informer du lancement éventuel de l’API messagerie | **Animateur·trice** | Avant la prochaine réunion |
| Identifier le support juridique et le valider | **Responsable juridique (non nommé)** | Au plus tard fin mai 2026 |
| Rechercher le financement du budget 2025 « bêtes froides » | **Intervenant(e) budget** | Juin 2026 |
| Organiser une réunion technique avec Michael pour définir l’offre actuelle | **Animateur·trice** | Semaine du 12 mai 2026 |
| Planifier une réunion de suivi avec Renata (montées en charge) et Reynaert (développements) | **Animateur·trice** | Avant fin mai 2026 |

---

## Prochaine rencontre
- **Objet** : Suivi des investigations WebDAV, état du projet API messagerie, validation du budget 2025 et avancement du Media Gateway.
- **Date proposée** : *à définir* (idéalement la première semaine de mai 2026).
- **Durée prévue** : 1 heure.

---

*Fin du compte rendu.*
