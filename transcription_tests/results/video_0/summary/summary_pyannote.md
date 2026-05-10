# Compte rendu de réunion

**Date** : 28 avril 2026
**Durée estimée** : ~1 heure

## Participants
- **Sébastien**
- **Benjamin**
- **Mickaël** (également mentionné sous le nom *Mickey*)
- **Benoît**
- (Références à **Arawa** pour la configuration téléphonique)

---

## Objet de la réunion
Suivi des développements B3Desk (code unique, PIN, migrations, tickets), état des intégrations (Nextcloud/Nuage, SIP Media Gateway), planification des releases et organisation du point de suivi bi‑hebdomadaire.

---

## Sujets abordés

| N° | Sujet | Points clés |
|----|-------|-------------|
| 1 | **Point de suivi bi‑hebdomadaire** | Décision de se réunir toutes les 2 semaines. |
| 2 | **Code unique & PIN** | - Ajouter le code unique dans la PR et la release.<br>- Configurer la nouvelle option *on* et le **dial‑number** (numéro de téléphone) dans B3Desk.<br>- Le PIN affiché sera celui du téléphone, généré aléatoirement, modifiable. |
| 3 | **Migrations** | - Vérifier que la migration actuelle s’exécute correctement.<br>- Respecter l’ordre des migrations (le tri des salons doit précéder la migration du code unique). |
| 4 | **Ticket 166 – Erreur 500 salon** | Problème résolu (cohérence de donnée). Aucun suivi supplémentaire requis. |
| 5 | **Connexion B3Desk ↔ Nuage (Nextcloud)** | - Lenteur observée sur les requêtes WebDAV.<br>- Hypothèses : surcharge du serveur, bibliothèque Python obsolète, token applicatif (30 jours).<br>- Nécessité de reproduire le problème et de collecter des métriques. |
| 6 | **Salon silencieux & budget** | - Devis validé, financement en cours via l’équipe messagerie.<br>- Lancement possible dès validation juridique. |
| 7 | **Projet SIP Media Gateway** | - Intégration d’un connecteur SIP à BBB.<br>- Dépendances côté B3Desk (génération/lien SIP). |
| 8 | **Estimation des tâches (tags)** | Besoin d’une correspondance *tag → estimation* (heures/jours) pour le backlog. |
| 9 | **Release 1.3** | - Contiendra le classement des salles et les améliorations testées.<br>- Le numéro d’appel et le code unique seront reportés à une release ultérieure. |
|10| **Création de la release** | Planifiée à 14 h cet après‑midi, avec accompagnement de Benjamin. |

---

## Décisions prises

1. **Point bi‑hebdomadaire** : mise en place d’une réunion toutes les deux semaines. Sébastien enverra l’invitation.
2. **Configuration téléphonique** : activer la nouvelle option et renseigner le `dial_number` fourni par Arawa.
3. **Migrations** : la séquence sera respectée ; la migration sera incluse dans la prochaine release.
4. **Ticket 166** : considéré comme résolu, aucune action supplémentaire.
5. **Salon silencieux** : lancement autorisé dès que le devis sera financé (déjà validé).
6. **Release 1.3** : sera publiée le même jour (14 h), sans le numéro d’appel ni le code unique.
7. **Estimation des tâches** : Mickaël (ou Benjamin) fournira un tableau de correspondance tags ↔ estimation d’ici la fin de journée.
8. **Connexion Nuage** : le problème reste en suspens et sera revu lors du prochain point.

---

## Questions en suspens

- **Intégration du code unique** : dans quelle release sera‑t‑il finalement intégré ? (À confirmer avec Benoît).
- **Numéro de téléphone** : Arawa doit confirmer le `dial_number` exact à utiliser.
- **Stabilité Nuage/Nextcloud** : comment reproduire le problème et quelles librairies mettre à jour ?
- **Support juridique** pour le salon silencieux : besoin d’une confirmation finale (apparente mais non formalisée).

---

## Tâches à effectuer

| Responsable | Action | Échéance |
|-------------|--------|----------|
| **Sébastien** | Envoyer l’invitation pour le point bi‑hebdomadaire. | Dès que possible |
| **Benjamin** | Vérifier le bon déroulement de la migration et remonter tout problème. | Avant la release 1.3 |
| **Mickaël** (ou **Benjamin**) | Fournir le tableau de correspondance *tag → estimation* (heures/jours). | Fin de journée |
| **Benjamin** | Réaliser la création de la release 1.3 à 14 h, avec assistance si besoin. | 14 h, 28 avril 2026 |
| **Benoît** | Décider de l’inclusion du code unique dans une future release. | Avant la prochaine release |
| **Arawa** | Communiquer le numéro de téléphone (`dial_number`) à configurer dans B3Desk. | Dès que possible |
| **Équipe B3Desk** | Investiguer la lenteur de la connexion Nuage : reproduire le problème, capturer les logs, vérifier les versions des bibliothèques WebDAV. | Prochaine itération (point bi‑hebdomadaire) |

---

## Prochaine rencontre

- **Réunion de suivi** : toutes les deux semaines (prochaine date proposée : **10 mai 2026**, 10 h).
- L’ordre du jour sera centré sur :
  1. Retour sur la release 1.3.
  2. Avancement de la connexion Nuage/Nextcloud.
  3. Validation du numéro de téléphone et du code unique.
  4. Mise à jour du backlog avec les tags/estimations.

---

*Fin du compte rendu.*
