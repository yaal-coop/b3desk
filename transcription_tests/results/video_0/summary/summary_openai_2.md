# Compte rendu de réunion

**Date** : 4 mai 2026
**Durée estimée** : ~1 h

---

## Participants
| Nom | Rôle / Fonction |
|-----|-----------------|
| **Mickaël** | Animateur / Responsable produit |
| **Benjamin** | Développeur backend |
| **Sébastien** | Responsable release |
| **Benoît** | Responsable financier / suivi devis |
| **Miguel** | Responsable configuration (ARAWA) |
| **Renata** | Développeuse SIP (partenaire) |
| **Michael** | Contact projet SIP Media Gateway |
| **Arawa** (représenté par Miguel) | Équipe intégration |
| **Autres** (participants ponctuels) | – |

---

## Objet de la réunion
1. Mettre en place un point de suivi bi‑hebdomadaire.
2. Faire le point sur les livrables récents (code génétique, configuration ScaleLite/BBB, ticket 166).
3. Discuter des tests et scénarios de validation (B3desk, PIN, dial‑number).
4. Analyser les problèmes de performance entre B3desk et le service Nuage/Nextcloud.
5. Faire le point sur les projets en cours (Salon silencieux, SIP Media Gateway, backlog).
6. Planifier la prochaine release (v1.3) et les actions associées.

---

## Sujets abordés & Décisions prises

| Sujet | Décision / Conclusion |
|-------|-----------------------|
| **Point bi‑hebdomadaire** | Réunion fixée chaque **mercredi à 11 h 30**. Mickaël enverra l’invitation. |
| **Livraison du code génétique** | Aucun développement supplémentaire n’est nécessaire côté BBB, uniquement une **modification de configuration** (ScaleLite/BBB). |
| **Configuration ScaleLite** | La variable à modifier sera précisée dans la PR et incluse dans l’APR & la release. |
| **Scénario de test B3desk** | - Activer la nouvelle option (`ON`). <br> - Mettre à jour le `dial_number` (BBB) dans la config B3desk. <br> - Vérifier que le PIN affiché correspond à la configuration. |
| **Ticket 166 (erreur 500 salons)** | Le problème a été résolu côté ARAWA (suppression d’un champ). La **remontée de logs** sera conservée dans la prochaine release. |
| **Performance Nuage / Nextcloud** | - Investigation en cours : reproduire le problème, capturer les traces. <br> - Vérifier la version des bibliothèques WebDAV et les mettre à jour si besoin. |
| **Salon silencieux** | Le devis est validé, le lancement peut démarrer dès que le support juridique sera trouvé. |
| **Projet SIP Media Gateway** | Projet en phase de lancement, financement BGF confirmé. Une réunion dédiée sera planifiée avec Renata & Michael. |
| **Backlog & estimation** | Adoption d’un système de **tags (XS, S, M, L)** avec correspondance temps. Mickaël préparera un tableau de mapping. |
| **Release 1.3** | - Session de création de la release prévue **aujourd’hui à 14 h** (Sébastien). <br> - La version 1.3 contiendra le classement des salles et les améliorations testées. <br> - Le code unique et le numéro d’appel seront intégrés dans une **release 1.3.1** après validation. |
| **Planification future** | Le point bi‑hebdomadaire servira à suivre l’avancement des actions ci‑dessus. |

---

## Questions en suspens
| Question | Responsable / Suivi |
|----------|---------------------|
| Nom exact de la variable à modifier dans ScaleLite (paramètre à préciser). | Benjamin (à ajouter dans la PR). |
| Calendrier précis pour l’intégration du **code unique** et du **numéro d’appel** (release 1.3.1). | Mickaël (définir avec l’équipe produit). |
| Délai de mise en place du support juridique pour le salon silencieux. | Benoît (validation budget). |
| Confirmation du **tag → estimation** (heures/jours) à communiquer. | Mickaël (tableau à livrer d’ici fin de journée). |
| Résolution définitive du problème de lenteur/instabilité Nuage‑WebDAV. | Benjamin (reproduire le bug, analyser les logs). |

---

## Tâches à effectuer

| Action | Responsable | Échéance |
|--------|-------------|----------|
| Envoyer l’invitation du point bi‑hebdomadaire (mercredi 11 h 30). | Mickaël | 5 mai 2026 |
| Mettre à jour la PR avec la description précise du paramètre ScaleLite à modifier. | Benjamin | 5 mai 2026 |
| Fournir le scénario de test complet pour B3desk (activation option, dial‑number, vérif PIN). | Benjamin | 6 mai 2026 |
| Intégrer les changements de configuration (ON flag, dial‑number) dans l’APR et la release. | Miguel | 6 mai 2026 |
| Conserver la remontée de logs du ticket 166 dans la prochaine release. | Mickaël / équipe | 6 mai 2026 |
| Reproduire le problème de performance Nuage, capturer les traces et vérifier les versions des bibliothèques WebDAV. | Benjamin | 12 mai 2026 |
| Mettre à jour les bibliothèques WebDAV si besoin. | Benjamin | 12 mai 2026 |
| Préparer le tableau de correspondance **tags ↔ estimation (jours/heure)** et le partager. | Mickaël | 5 mai 2026 (fin de journée) |
| Conduire la session de création de la release 1.3 (git, tags, tests). | Sébastien (avec Benjamin) | 4 mai 2026 – 14 h |
| Valider le support juridique et lancer le **salon silencieux**. | Benoît | Dès validation (prévu avant 15 mai 2026) |
| Organiser une réunion dédiée au projet **SIP Media Gateway** (participants Renata, Michael, etc.). | Mickaël | À planifier (semaine du 15 mai) |
| Définir le planning de la release 1.3.1 (code unique, numéro d’appel). | Mickaël | À définir (avant fin juin) |

---

## Prochaine rencontre
- **Réunion bi‑hebdomadaire** : **Mercredi 11 mai 2026 à 11 h 30** (lien Teams/Zoom à venir).
- **Session release 1.3** : Aujourd’hui, **14 h** (Sébastien & Benjamin).

---

*Document rédigé par l’assistant IA, basé sur la transcription de la réunion.*
