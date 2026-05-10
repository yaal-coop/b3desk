# Compte‑rendu de réunion

**Date** : 4 mai 2026
**Heure** : non précisée (durée estimée non communiquée)

---

## Participants
| Nom | Rôle / Fonction |
|-----|-----------------|
| **Benjamin** | Développeur B3desk (tests WebDAV) |
| **Benoît** | Responsable tests navigateur / suivi devis |
| **Mickaël** | Contact projet SIP Media Gateway |
| **[Non nommés]** | Équipe messagerie, Renataire, représentants du MTE, DGFIC, etc. |

---

## Objet de la réunion
1. **Investigation des lenteurs / instabilités** entre B3desk et le service *nuages* (Nextcloud, WebDAV).
2. **Suivi du devis et du budget** pour l’API de messagerie nationale et le lancement du « salon silencieux ».
3. **Mise en place du projet SIP Media Gateway** (connecteur SIP pour BBB) et coordination avec les parties prenantes (Renataire, DGFIC, ministère de la Transition écologique).

---

## Sujets abordés
| N° | Thème | Points clés |
|----|-------|-------------|
| 1 | **Connexion B3desk ↔ Nuages** | - Le token (validité 30 jours) permet d’appeler directement le service nuages, le portail Apps n’est plus utilisé. <br> - Problème : requêtes WebDAV parfois lentes ou instables. <br> - Hypothèses : surcharge du nuage, bibliothèque Python WebDAV obsolète, plugins du navigateur de Benoît. |
| 2 | **Tests & Reproductions** | - Capture de trafic (tram) montre la cinématique correcte lorsqu’elle fonctionne. <br> - Nécessité de reproduire le dysfonctionnement pour identifier le point de rupture. |
| 3 | **Version Nextcloud** | - Des montées de version récentes pourraient impacter le comportement. |
| 4 | **Token applicatif** | - Durée actuelle : 30 jours. Possibilité d’allonger pour la production afin de réduire les sollicitations du portail Apps. |
| 5 | **Devis API messagerie nationale** | - Devis transmis à l’équipe messagerie, validation financière obtenue. <br> - Le « salon silencieux » peut être lancé immédiatement. |
| 6 | **Budget 2025 – Besprades** | - Un budget dédié au développement de Besprades est disponible, il faut identifier le support juridique et le vecteur de financement. |
| 7 | **Projet SIP Media Gateway** | - Financement prévu par la DGFIC. <br> - Nécessite du développement côté B3desk (génération/reprise SIP). <br> - Renataire assure les développements internes ; nous jouons le rôle de fournisseur de service. <br> - Discussion sur les fonctionnalités supplémentaires demandées et la capacité d’adaptation de la brique existante. |
| 8 | **Organisation de réunions futures** | - Besoin d’une réunion technique dédiée au SIP Media Gateway pour définir périmètre, spécifications et plan d’action. |

---

## Décisions prises
| Décision | Responsable / Commentaire |
|----------|----------------------------|
| **Poursuivre les tests** pour reproduire le problème de connexion WebDAV. | Benjamin (lead) |
| **Conserver l’action** de reproduction du problème jusqu’à obtention de résultats concluants. | Équipe B3desk |
| **Valider le devis** de l’API messagerie nationale et lancer le salon silencieux. | Benoît (transfert à l’équipe messagerie) |
| **Ne pas bloquer** le lancement du projet tant que le devis est validé ; attendre uniquement les retours financiers éventuels. | Tous les participants |
| **Planifier une réunion technique** sur le projet SIP Media Gateway afin de préciser les spécifications et les limites de la brique existante. | Mickaël (organisation) |
| **Étudier l’allongement** de la durée du token applicatif (au‑delà de 30 jours) pour la mise en production. | Responsable produit (non nommé) |
| **Identifier le support juridique et le vecteur financier** pour le budget 2025 dédié à Besprades. | Responsable financier (non nommé) |

---

## Questions en suspens
1. **Quelle est la cause exacte** de la lenteur/instabilité des requêtes WebDAV ? (surcharge nuage, bibliothèque Python, plugins navigateur, version Nextcloud…)
2. **Comment reproduire de façon fiable** le dysfonctionnement observé ?
3. **La version actuelle de Nextcloud** est‑elle compatible avec notre implémentation ? Faut‑il mettre à jour ou rétrograder ?
4. **Le token de 30 jours** est‑il suffisant en production ? Quels impacts sur le portail Apps ?
5. **Quel est le cadre juridique** et le mécanisme de financement exacts pour le budget Besprades 2025 ?
6. **Quelles fonctionnalités SIP supplémentaires** sont attendues par Renataire ? Sont‑elles réalisables avec la brique existante ou nécessitent‑elles un développement dédié ?

---

## Tâches à effectuer
| Action | Responsable | Échéance |
|--------|-------------|----------|
| Refaire les captures de trafic (tram) et tenter de reproduire le problème de connexion. | **Benjamin** | Prochaine semaine |
| Vérifier la version de la bibliothèque Python WebDAV et la mettre à jour si besoin. | **Benjamin** | 10 mai 2026 |
| Effectuer des tests avec le navigateur de **Benoît** (désactiver plugins) et rapporter les résultats. | **Benoît** | 8 mai 2026 |
| Confirmer la version de Nextcloud déployée et tester avec la dernière version stable. | **Équipe technique** | 12 mai 2026 |
| Proposer une durée de token plus longue (ex. 60 jours) et évaluer les impacts. | **Produit / Sécurité** | 15 mai 2026 |
| Informer l’équipe messagerie du statut du devis et lancer le salon silencieux. | **Benoît** | Immédiat |
| Identifier le support juridique et le financement pour le budget 2025 Besprades. | **Responsable financier** | 20 mai 2026 |
| Organiser une réunion technique sur le SIP Media Gateway (agenda, participants, date). | **Mickaël** | Avant fin mai 2026 |
| Préparer un document de spécifications fonctionnelles SIP (exigences Renataire). | **Mickaël / Renataire** | 30 mai 2026 |

---

## Prochaine rencontre
- **Objet** : Réunion technique sur le projet SIP Media Gateway (définition du périmètre, capacités de la brique existante, plan de développement).
- **Date / Heure** : à fixer (proposition avant le **31 mai 2026**).
- **Participants attendus** : Mickaël, représentants de Renataire, équipe B3desk, éventuellement un représentant DGFIC.

---

*Fin du compte‑rendu.*
