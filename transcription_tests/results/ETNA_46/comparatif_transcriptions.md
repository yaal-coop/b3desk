# Comparatif des transcriptions — ETNA 46

Comparaison de 6 outils de transcription sur le même fichier audio (`ETNA_46.mp3`).
Les résumés ont tous été générés par le **même LLM**, à partir de transcriptions produites par des outils différents. Les différences entre résumés révèlent donc ce que chaque transcription a capté ou raté.

---

## Outils comparés

| Outil | Fichier transcription | Fichier résumé |
|-------|-----------------------|----------------|
| Albert | `transcription_albert.txt` | `summary_albert.md` |
| AssemblyAI | `transcription_assemblyai.txt` | `summary_assemblyai.md` |
| Deepgram | `transcription_deepgram.txt` | `summary_deepgram.md` |
| Gladia | `transcription_gladia.txt` | `summary_gladia.md` |
| Groq | `transcription_groq.txt` | `summary_groq.md` |
| Pyannote | `transcription_pyannote.txt` | `summary_pyannote.md` |

---

## Erreurs de transcription confirmées

Vérifiées dans les fichiers de transcription bruts.

| Outil | Erreur dans le résumé | Ce que dit la transcription brute | Verdict |
|-------|-----------------------|-----------------------------------|---------|
| **AssemblyAI** | Participant : "Olivier" | *"Donc Olivier, Hugo, Benoît..."* — "Didier" mal entendu | Erreur de transcription |
| **AssemblyAI** | Enquête "BELCOM" | Transcription : "BELCOM" | Erreur — les 5 autres donnent **DELCOM** |
| **AssemblyAI** | Campagne "BMA" | Les occurrences de "bma" dans la transcription sont toutes à l'intérieur du mot **"webmail"** | Faux positif — le LLM a inféré "BMA" à partir des fragments de "webmail". Le terme correct est **BNA** (dit explicitement dans toutes les transcriptions) |
| **Deepgram** | Nom de réunion : "comité de **marge**" | Tous les autres : "comité de suivi / de domaine" | Erreur de transcription |
| **Albert** | Programme "**DLE**" (vs "DNE" partout ailleurs) | Albert capture le mot exact du locuteur ("DLE" dit une fois) | Albert est **correct** — c'est les autres qui ont normalisé |

---

## Hallucinations LLM dans les résumés

Cas où la transcription brute est correcte mais le LLM a produit une information fausse dans le résumé.

| Outil | Erreur dans le résumé | Ce que dit la transcription brute |
|-------|-----------------------|-----------------------------------|
| **Deepgram** | Portail Apps : **121 000 comptes** | *"deux-cent-vingt-et-un-mille comptes"* — transcription correcte à 221 000 |
| **Groq** | Portail Apps : "73k actifs depuis **déc. 2022**" | *"depuis décembre"* — sans année. Le LLM a inventé 2022 |

---

## Ce qui semblait être une erreur mais ne l'est pas

| Point | Outils concernés | Explication |
|-------|-----------------|-------------|
| **"fin 2025"** pour la MEP Tribu | Gladia, Groq, Pyannote | Le locuteur a dit explicitement *"la mise en prod qu'on souhaite faire pour la fin 2025"*. Ces résumés sont **plus précis** qu'Albert et Deepgram qui omettent l'année. |

---

## Informations présentes dans un seul résumé

Ces informations ont été captées par un seul outil — potentiellement manquées ou mal transcrites ailleurs.

### Pyannote — liste de participants la plus exhaustive
Seul outil à mentionner : Irina (pôle Paris), Mickaël (BBB 3.0), Benjamin, Manon, Christophe Sisko, Sœur Terreso, Bruno (communication unifiée), Joël.

### Pyannote — détails techniques uniques
- Prérequis éditeurs : Kubernetes, Kafka, Terraform
- Ticket d'incident avec **Onissa**
- Comité référents avec **DRAZI/SGRA**
- Fonctionnalités disparues dans **BBB 3.0** (question ouverte, assignée à Mickaël)
- Squash Tribu "hors Simon"
- Environnements Tribu : **pré-prod / iso-prod / AQT**
- Point C4 (formation équipes support)
- Formation **Microsoft Office & SBM**
- Plugin VisioAgent 1.3, responsable **Yal**
- Intégration BVV dans CHAP : **35 j dev** (seul à donner ce chiffre)

### AssemblyAI — déploiements académiques
- Pilotes nommés : **Nantes, Poitiers, Tacan**
- Plan d'accélération **Île-de-France** (oct-nov)
- Mise à jour **CPT** pendant les vacances d'été
- Tickets incidents **Omniface**

### Deepgram — informations chiffrées uniques
- Montant licences Microsoft : **~50 000 €**
- RAM : objectif **16 Go** (pas seulement 12 Go) avec atelier Optimus Green
- Participants : **Michael, Benjamin** (développeurs BBB), **JFR** (animateur)
- Collabora : versions **3.0, 3.1 et 4.0** listées explicitement

### Albert
- Tube : travaux avec la **DRAME du Grand Est**
- **YAL** mentionné (plugin délégation de salles VisioAgent)

### Gladia
- **Portail intranet** : reprise du projet (unique à ce résumé)
- Migration **comptes mineurs (Nuage)**
- **Messagerie Thunderbird/Webmail** : analyse des usages

---

## Synthèse qualitative

| Outil | Fiabilité transcription | Richesse des détails | Hallucinations LLM | Note globale |
|-------|------------------------|----------------------|---------------------|--------------|
| **Albert** | ✅ Bonne | Moyenne | Aucune constatée | Fiable et sobre |
| **AssemblyAI** | ⚠️ 3 erreurs (Olivier, BELCOM, BMA) | Bonne (déploiements académiques) | Aucune constatée | Enrichissant mais peu fiable sur les noms propres |
| **Deepgram** | ⚠️ Nom de réunion erroné | Moyenne | 121k comptes (grave) | Transcription dégradée sur les noms, LLM instable sur les chiffres |
| **Gladia** | ✅ Bonne | Bonne (portail intranet, messagerie) | Aucune constatée | Bon équilibre |
| **Groq** | ✅ Bonne | Moyenne | Date 2022 inventée | Fiable en transcription, LLM instable sur les dates |
| **Pyannote** | ✅ Bonne | ⭐ Excellente (participants, détails techniques) | Aucune constatée | Meilleure couverture des détails fins |

**Conclusion** : Pyannote capture le plus de détails (noms propres, acronymes, chiffres techniques). AssemblyAI est le plus sujet aux erreurs de transcription sur les noms propres. Deepgram et Groq ont les LLM de résumé les moins stables (hallucinations numériques et de dates). Albert et Gladia offrent le meilleur compromis fiabilité/richesse.
