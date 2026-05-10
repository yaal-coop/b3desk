```markdown
# Compte rendu de réunion

## Objet de la réunion
Point projet sur l'avancement des différents programmes et outils numériques (DLE, Tribu, Nuage, VisioAgent, etc.).

## Participants
- Animateur (non nommé)
- Didier
- Hugo
- Benoît
- Simon
- Johan
- Frédéric
- Nicolas
- Joanne
- Samir
- Olivier
- Autres intervenants (Audran, Charly, Benjamin, Mickaël, etc.)

---

## Sujets abordés

### 1. Budget et jalons projets
- **Réduction du budget DLE** : Confirmation attendue sur les montants impactant le programme. Risque de coupes sur certains produits.
- **Suivi des jalons** : Besoin d’améliorer la précision des dates de livraison et de mise en production pour les nouvelles fonctionnalités. Problématique de visibilité avec les prestataires et éditeurs (ex. : décalages fréquents, manque de roadmaps claires).

### 2. Relations avec les prestataires et éditeurs
- **Manque de fiabilité** :
  - Exemples : Collaborat (aucune visibilité sur la roadmap), BBB (décalages permanents), Nextcloud (modifications unilatérales en version 31).
  - Problème récurrent de décalages entre engagements et livraisons (ex. : commandes BVB non livrées depuis un an).
- **Pistes d’amélioration** :
  - Exiger des engagements plus réalistes pour les développements financés.
  - Travailler sur la maîtrise des roadmaps éditeurs (ex. : Nextcloud, BBB).
  - Développer des plugins externes pour des fonctionnalités spécifiques (ex. : BBB).

### 3. Projets spécifiques

#### Tribu
- **Refonte graphique (UX8)** :
  - Chiffrage en cours avec les prestataires (3 lots : accueil/tableaux de bord, outils/recherche, administration).
  - Planning : Spécifications en cours, développement à lancer après validation du chiffrage.
  - Objectif : Mise en production fin 2025 (novembre/décembre).
- **Environnements** : Préparation de pré-prod et dev pour travailler en parallèle.

#### Nuage (Nextcloud)
- **Problème version 31** :
  - Modifications fonctionnelles unilatérales (liens de partage) rendant la mise à jour impossible sans correctif.
  - Report de la migration en attendant une solution de l’éditeur.
- **Migration académique** :
  - Script de migration testé avec Nantes (correctifs en attente).
  - Audit BDD : Augmentation de la RAM (de 8 Go à 12 Go) pour stabiliser les serveurs.
- **Global Scale** : Prérequis non rempli (version 31 nécessaire).

#### VisioAgent
- **Version 1.3** :
  - Livraison du frontal avec nouvelles fonctionnalités (bandeau d’informations, tri des salons, favoris).
  - Commande de 35 jours de développement validée pour poursuivre les évolutions.
- **Demandes du CNET** :
  - Délégation de salles (complexe à mettre en œuvre).
  - Besoin de clarifier les priorités et financements.

#### Portail Apps
- **Statistiques** :
  - 221 000 comptes ouverts (dont 73 000 actifs depuis décembre).
  - 80 000 vidéos sur PodÉdu.
- **Évolutions** :
  - Installation de Matomo pour des stats précises.
  - Raccourcisseur d’URL en développement (livraison prévue avant l’été).
  - Architecture en micro-applications pour le cycle de vie des comptes.

#### Messagerie (Aetna)
- **Déploiement en Corse** :
  - Premier pilote en conditions réelles (académie entière basculée en one shot).
  - Bilan mitigé : 99% des comptes migrés sans problème, mais difficultés sur certains usages (ex. : FGRA, exports EML).
  - Besoin d’améliorer l’accompagnement au changement.
- **Prochains déploiements** :
  - Accélération prévue (Nantes, Poitiers, PACA, Reims, Île-de-France).
  - Réunion des référents pour valider le plan de déploiement.

#### Autres projets
- **BNA** : Report de la campagne du 16 au 27/28 juin (éviter les sollicitations simultanées).
- **Communication unifiée** : Réflexion sur les outils (Cisco Webex, solutions libres) dans le cadre du déménagement à Gentilly.
- **Tube** :
  - Travaux sur les thèmes pour différencier les instances.
  - Transcription des vidéos opérationnelle sur test (généralisation prévue).
  - Automatisation des déploiements en attente de tests.

---

## Décisions prises
1. **Amélioration de la précision des jalons** :
   - Travailler avec les prestataires pour obtenir des dates plus fiables.
   - Communiquer des plages temporelles réalistes à la direction (ex. : "septembre/octobre" au lieu de "T4").

2. **Gestion des éditeurs** :
   - Exiger des engagements clairs pour les développements financés.
   - Prioriser la maîtrise des roadmaps éditeurs (ex. : Nextcloud, BBB).

3. **Report de la migration Nextcloud 31** :
   - Attendre un correctif de l’éditeur pour les liens de partage avant mise en production.

4. **Déploiement de Tribu** :
   - Valider le chiffrage et lancer les développements pour une MEP fin 2025.

5. **Accompagnement au changement** :
   - Renforcer la proximité avec les utilisateurs (VIP et terrain) pour les projets futurs (Nuage, Tribu, VisioAgent).

---

## Questions en suspens
- **Plugin Thunderbird** : Faut-il le diffuser largement ou le réserver au webmail pour inciter à son utilisation ?
- **Délégation de salles dans VisioAgent** : Comment prioriser et financer cette demande du CNET ?
- **Roadmap Collaborat** : Comment obtenir plus de visibilité de la part de l’éditeur ?

---

## Tâches à effectuer
| Tâche | Responsable |
|-------|-------------|
| Finaliser le chiffrage de la refonte Tribu | Simon |
| Organiser un retour d’expérience Squash avec Tribu | Simon |
| Préparer les slides pour le comité des référents (mardi prochain) | Équipe projet |
| Contacter l’UNISA pour recaler un point sur le Réseau de l’Aînés | Non précisé |
| Déployer la transcription des vidéos sur Tube | Nicolas |
| Valider les devis pour le cycle de vie des comptes/vidéos sur Tube | Équipe projet |
| Tester l’usine d’apport des contacts/archives pour la messagerie | Équipe Aetna |
| Envoyer le questionnaire Wi-Fi aux académies d’Île-de-France | Olivier |

---

## Prochaine rencontre
- **Comité des référents** : Mardi prochain (en distanciel).
- **Réunion de lancement pour l’Île-de-France** : Semaine prochaine.
- **Prochaine réunion projet** : Non précisée (à planifier).
```
