**Compte rendu de la réunion (46ᵉ session)**

---

### Participants
- **Didier**
- **Hugo**
- **Benoît**
- **Audran** (comité de domaine)
- **Simon** (organisation du Squash / Tribu)
- **Frédéric** (intégration DBV, suivi licences)
- **Nicolas** (formation, suivi Nuage)
- **Maxime Leherici** (support éditeur Nextcloud)
- **Johan**, **François**, **Sophie**, **Valérie** (interventions ponctuelles)

*(d’autres intervenants sont cités sans être présents physiquement : Audran, les prestataires Collabora, Nextcloud, BGB, etc.)*

---

### Objet de la réunion
Faire le point sur l’avancement des projets du **programme DLE** : budget, jalons de livraison, relations avec les prestataires, licences, campagnes de communication, refonte d’applications (Tribu, Portail Apps, Nuage, BNA, etc.) et préparer les prochains comités de suivi.

---

### Sujets abordés
| Thème | Points clés |
|-------|-------------|
| **Budget DLE** | Réduction globale du budget confirmée ; attendue la validation des montants. |
| **Suivi des jalons / dates de livraison** | Difficulté à fournir des dates précises ; besoin d’une meilleure visibilité (ex. : « avant/pendant/après l’été »). |
| **Relation avec les prestataires** | Manque de fiabilité des plannings (Collabora, Nextcloud, BGB, etc.) ; besoin d’engagements plus réalistes. |
| **Licences IES Microsoft** | Renouvellement effectué la semaine précédente pour 30 000 agents. |
| **Squash avec Tribu** | À organiser, Simon en charge de la planification. |
| **Comité des référents** | Réunion prévue mardi ; slides à préparer et diffuser. |
| **Dotation** | Étude des besoins en profils à remettre à Frédéric. |
| **BNA (campagne d’enquête)** | Décalage d’un mois : du 16 juin au 27‑28 juin. |
| **Communication unifiée** | Choix entre outil privé vs. libre (Cisco, Webex, etc.) en cours d’étude. |
| **Refonte graphique Tribu (UX8)** | Chiffrage en cours ; 3 lots (accueil, recherche, admin) → ≈ 200 jrs. MEP prévue fin 2025 (début 2026). |
| **Nextcloud / version 31** | Régression fonctionnelle non prévue ; besoin d’un correctif avant mise en prod. |
| **RAM PostgreSQL** | +4 Go obtenus via ateliers Optimus Green (passage de 8 → 12 Go). |
| **Portail Apps** | 221 000 comptes, 80 000 vidéos, Matomo installé, raccourcisseur d’URL en cours de développement. |
| **Rancher (pré‑prod)** | Livré mais pas encore opérationnel ; besoin de documentation et de droits d’exploitation. |
| **Tube (thématisation, transcription, transcodage)** | Travail sur thèmes UI, transcription testée, plan d’externalisation du transcodage. |
| **Accompagnement terrain** | Nécessité d’être plus proche des utilisateurs finaux (VIP, académies, etc.). |
| **Déploiements académiques** | Pilotage en Corse, plan d’accélération (Nantes, Poitiers, PACA, etc.) et préparation du grand déploiement Q3‑Q4. |

---

### Décisions prises
- **Budget** : accepter la réduction globale du budget DLE (attente des chiffres définitifs).
- **Dates de livraison** : instaurer un suivi plus précis et communiquer des fourchettes (ex. : « avant l’été ») aux directions.
- **BNA** : reporter la campagne du 16 juin au 27‑28 juin pour éviter le chevauchement avec la DELCOM.
- **Intégration DBV** : validation du développement ; démarrage du projet avec l’éditeur.
- **Tribu** : ne pas couper le service pendant la mise en prod ; déploiement transparent.
- **Nextcloud** : ne pas pousser la version 31 en production tant que le correctif de régression n’est pas disponible.
- **RAM PostgreSQL** : augmentation validée et mise en production via Optimus Green.
- **Squash** : Simon organise la session avec Tribu.

---

### Questions en suspens
1. **Quand les éditeurs (Collabora, Nextcloud, BGB…) pourront‑t‑ils fournir des dates de livraison fiables ?**
2. **Quel sera le périmètre exact de la refonte graphique Tribu (lots à valider, date de mise en prod précise) ?**
3. **Correctif Nextcloud 31 : date de disponibilité et procédure de mise à jour parallèle.**
4. **Script de migration Nextcloud académique : délai de livraison du correctif par l’équipe de Nantes.**
5. **Choix final de l’outil de communication unifiée (privé vs. libre) et architecture SIP/BBB.**
6. **Déploiement du Rancher : quels droits et quelles procédures sont nécessaires pour le rendre opérationnel ?**
7. **Plan détaillé de l’accompagnement terrain (formation, support) pour les académies pilotes.**

---

### Tâches à effectuer
| Action | Responsable | Échéance / Commentaire |
|--------|-------------|------------------------|
| Confirmer les montants exacts du nouveau budget DLE | **Didier** | Dès réception des chiffres officiels |
| Produire un tableau de suivi des jalons avec fourchettes de dates | **Audran** | Avant le prochain comité référent |
| Organiser le **Squash** avec Tribu | **Simon** | À planifier (date à définir) |
| Préparer et diffuser les slides du comité référent (mardi) | **Frédéric** | Slides à envoyer d’ici fin de semaine |
| Finaliser le chiffrage de la refonte Tribu et valider le planning | **Équipe de développement Tribu** | Dès que les estimations seront actées |
| Obtenir le correctif de régression de Nextcloud 31 et planifier le test en pré‑prod | **Maxime Leherici** (support éditeur) | Avant toute mise en prod prévue |
| Suivre le correctif du script de migration (Nantes) | **Benoît** | Attente du correctif « ce week‑end » |
| Mettre à jour la RAM PostgreSQL sur tous les serveurs BDD | **Equipe Infra** | Déjà réalisé ; monitorer la stabilité |
| Déployer le raccourcisseur d’URL (RL) et le QR‑code pour le Portail Apps | **Hugo** + **Développeurs** | Démo attendue la semaine prochaine |
| Finaliser la documentation et les droits d’accès au Rancher | **Equipe Exploitation** | Priorité haute, avant le prochain déploiement |
| Planifier les formations support pour les académies (BNA, Tube, etc.) | **Frédéric** + **Responsable formation** | Avant le lancement des campagnes (juin) |
| Valider le choix de l’outil de visioconférence unifiée (Cisco/BBB) | **Paul Fouad** + **Direction** | Décision attendue avant le prochain trimestre |

---

### Prochaine rencontre
- **Comité des référents** – mardi prochain (date exacte à confirmer).
- Une réunion de suivi **Squash / Tribu** sera planifiée par Simon.
- Le **point de suivi des jalons** sera présenté lors du prochain comité de pilotage (date à définir).

---

*Fin du compte rendu.*
