# KPSI Master Plan — Ἡ Κοινὴ καθ᾿ αὑτὴν φωτιζομένη
## 50-Chapter Edition (revised 2026-06-18)

---

## Project overview

An LLPSI-style inductive graded reader for New Testament Koine Greek. Original continuous narrative in Greek — no translation — reader acquires vocabulary and grammar inductively, then transitions to real NT texts in the final act.

**Entry requirement:** Greek alphabet only. No prior grammar assumed.
**Target outcome:** A reader who completes the book can read most of the NT with a reader's edition, and the Johannine corpus, Mark, and 1 Corinthians without one.
**Model:** Hans Ørberg's *Lingua Latina per se Illustrata* (LLPSI) and Seumas MacDonald's *Linguae Graecae per se Illustrata* (LGPSI).
**Setting:** Corinth, 51 AD. Protagonist: Χρύσιππος, a Greek freedman merchant. The story intersects with the historical Pauline community — Aquila, Priscilla, Crispus, Sosthenes, Stephanas — figures named in Acts 18 and 1 Corinthians.

---

## Governing principles

### 1. Zero-prior-Greek entry
Every word in glosses, marginalia, and αἱ λέξεις sections must use only vocabulary already seen in the main text, or be a meta-term introduced in that very note. The Ch 1 inline gloss is the governing template for the entire book:

> `[νῆσος]{.gloss title="γῆ μικρὰ ἐν τῇ θαλάσσῃ"}`

### 2. Three apparatus tiers

| Tier | Accessibility rule |
|---|---|
| **Inline glosses** (`.gloss` tooltips) | Only previously seen vocabulary. No exceptions. |
| **αἱ λέξεις sections** | Reader's current level + meta-terms introduced in that section. Written in the question-and-answer style of Ch 1. Complexity grows as grammar expands. |
| **Chapter heading labels** (παρατατικός, ἀόριστος, etc.) | May appear as names before Greek prose explanation is possible. The explanation follows only once the reader has the grammar to receive it. |

### 3. Aspect mastery is the primary verbal goal

All three aspect systems — imperfect / aorist / perfect — must be felt as a single framework, not three separate past tenses acquired at intervals. Greek's morphological density makes aspect the single greatest obstacle to generalisation for NT readers. Provisions:

- Aspect *concept* introduced Ch 11 (before the aorist) via narrative contrast, not prose explanation
- 1st aorist Ch 14; 2nd aorist dedicated chapter Ch 15; aorist passive Ch 16
- Aorist consolidation Ch 17: all three types interleaved with imperfect, no new grammar
- Perfect introduced Ch 18 immediately after aorist, as its aspectual partner — not deferred to Ch 21 as in the original plan
- Greek prose explanation of the three-way aspect system deferred to Ch 18, when participles become available to express it

### 4. NT texts throughout — *Ἐν ταῖς γραφαῖς*

Every chapter from Ch 1 onward includes authentic NT Greek in an end-of-chapter *Ἐν ταῖς γραφαῖς* section. Selection criteria:
- Every word in the passage is known from the main text, or glossed using only known vocabulary
- The passage exemplifies the grammar of the current chapter where possible
- Early passages are very short (1–3 verses); length grows with the reader's competence
- By Act V, the reader has encountered every major text at least in fragment — Act V produces recognition, not shock

### 5. Vocabulary ceiling: NT-750

The original plan used NT-500 (~90% of all NT word occurrences). Raised to NT-750. The additional 250 lemmas are distributed at 2–3 per chapter across Ch 12–28, targeting vocabulary clusters in James, Hebrews, and the Pastoral Epistles. The `scripts/nt500.txt` file needs extending to rank 750; the ceiling parameter in `scripts/vocab_check.py` needs updating accordingly.

### 6. Philemon complete mid-course (Ch 25)

First complete NT book read at Ch 25, not at the end. Philemon (25 verses) uses the grammar available by Ch 25 (ἵνα + subjunctive, imperatives, basic conditionals); its social world of slave, freedom, debt, and intercession directly mirrors the narrative world of Chrysippus for 24 chapters. The Pauline letter schema is introduced in the αἱ λέξεις of this same chapter, unlocking the opening and closing of all 13 Pauline letters for all subsequent reading.

### 7. Three LXX quotations seeded mid-course

| LXX text | Seeded at | NT books activated |
|---|---|---|
| Ps 110:1 LXX (*εἶπεν ὁ κύριος τῷ κυρίῳ μου*) | Ch 10 | Mark 12:36; Acts 2:34–35; Heb 1:13; Rom 8:34 |
| Isa 53:7–8 (*ὡς πρόβατον ἐπὶ σφαγὴν ἤχθη*) | Ch 20 | Acts 8:32–33; 1 Pet 2:22–24 |
| Ps 117:22 (*λίθον ὃν ἀπεδοκίμασαν οἱ οἰκοδομοῦντες*) | Ch 21 | Matt 21:42; Mark 12:10; Acts 4:11; 1 Pet 2:7 |

Each listed with its NT cross-references on first appearance. The reader recognises them when they arrive in Act V.

### 8. Bridge chapters (Ch 37–38)

Ch 37: three NT passages (Mark 1, Acts 18, 1 John 1) rewritten with KPSI vocabulary and grammar but NT word order and sentence density — register transition, not grammar transition.
Ch 38: the same passages in their authentic form, sub-750 vocabulary glossed. Student reads the same content twice. Recognition effect closes the register gap without a hard cut into Act V.

### 9. Act V as survey + depth

Act V covers 1 John (complete), Mark narratives, Acts 18 (complete), 1 Cor 13, a Pauline letter survey, James, Hebrews, 1 Peter, and John's Prologue. The reader finishes knowing the *feel* of every major NT book — not just three deep texts — and knowing specifically what register challenges each one presents.

---

## 50-Chapter Map

### Act I — Corinth / Nominal Core (Ch 1–13)

*Tone: comic, grounded, domestic.*
*Grammar arc: εἰμί → present active → dative/genitive → 3rd decl. consonant stems → 3rd decl. neuter/i-stems → deponents → relative pronoun → aspect framing → imperfect.*

| Ch | Greek title | Grammar introduced | Narrative | *Ἐν ταῖς γραφαῖς* |
|---|---|---|---|---|
| 1 | Ἡ οἰκουμένη | εἰμί all forms; nom; 1st/2nd decl; article; particles (καί, δέ, μέν, ἀλλά, γάρ, ναί, οὐχί, ἆρα, ποῦ, τί) | Geography → Roman empire → Corinth → Chrysippus (three sentences) | 1 John 1:5 (*ὁ θεὸς φῶς ἐστίν*); John 1:1 (ἦν glossed) |
| 2 | Ἡ ἀγορά | Accusative (1st/2nd decl); present act. 3rd sg/pl → all persons; ἔχω, βλέπω, φέρω, λαμβάνω, πωλέω; τίς/τί | Chrysippus's stall; the mystery jar sold cheaply; Nikon the sardine-seller | 1 John 4:8 (*ὁ θεὸς ἀγάπη ἐστίν*) |
| 3 | Ἡ οἰκία | Dative; indirect object; λέγω/λαλέω + dat; 1st/2nd person present; vocative | Household: Melitta, Xanthias, Lykos. First direct speech. Lykos eats something. | John 1:1 expanded; 1 Cor 1:1–3 fragment |
| 4 | Τὸ λιμάνιον | Genitive (1st/2nd decl): possession, source, separation; comparative + ἤ; πρός + acc | Lechaion harbour; wrong cargo; Xanthias translates badly; Lykos carries cloth instead of rope | Luke 2:1–4 (geography; all words known) |
| 5 | Ὁ χρεώστης | Personal pronouns all cases; οὗτος/ἐκεῖνος/αὐτός (emphatic) | Theophrastus arrives with wax tablet; Melitta agrees with Theophrastus about everything; Chrysippus feels betrayed | 1 Cor 1:1–3 complete |
| **6** | **Ἡ ἑορτή** | **CONSOLIDATION — no new grammar. Zero new lemmas.** | Festival day; agora shuttered; Chrysippus at leisure; Lykos eats a wreath. Pure recycling. | 1 John 1:5 + 4:8 together; John 1:1 revisited |
| **7** | **Ὁ ξένος** | 3rd decl. consonant stems: ἀνήρ, νύξ, χάρις, πατήρ, σάρξ, χείρ; πᾶς | Syrian merchant with cheaper oil; Chrysippus borrows from Damon; Damon's father disapproves | Acts 18:1–2 (Aquila in the actual source text — heavily glossed) |
| **8** | **Τὸ σῶμα καὶ ἡ ψυχή** | 3rd decl. neuter stems + i-stems: σῶμα, πνεῦμα, πρᾶγμα, ὄνομα, δύναμις, πίστις; gen. of price; meta-vocab: τὸ γένος, ἡ πτῶσις | Melitta sells cloth; meets Priscilla at the well; Chrysippus passes Aquila's workshop without entering | Acts 18:3–4 |
| 9 | Τὸ ἱμάτιον | Deponents: πορεύομαι, ἔρχομαι, γίνομαι, ἀποκρίνομαι, ἐρωτάω | Melitta sends Chrysippus for a barley loaf; he returns with an expensive wheat loaf | Luke 2:8–11 (πορεύεσθε; εἶπεν previewed and glossed as future Ch 15) |
| 10 | Ξανθίας | Relative pronoun ὅς/ἥ/ὅ all cases; embedded relative clauses | Xanthias found at Cenchreae watching a ship from Lydia; the lit house on the way home | Acts 18:5–6; **Ps 110:1 LXX (seed #1)** + NT cross-references |
| 11 | Ἡ νύξ ἐν τῷ καπηλείῳ | **Aspect framing.** τὸ παρατατικόν as label; minimal pair demonstrated (ἐπώλει vs. ἐπώλησεν); no Greek prose definition possible yet | Damon narrates his life history in imperfect; Chrysippus tries to interject quick aorist facts; the contrast is dramatic before it is labelled | Mark 1:14–15 (imperfect background + aorist event visible) |
| 12 | Ἡ συναγωγή | Imperfect indicative fully conjugated: ἐζήτει, ἐβλέπεν, ᾔδει, ἦγεν; narrative reconstruction | Chrysippus searches the synagogue district; sustained imperfect narration of ongoing action | Acts 18:7–8 (first half) |
| 13 | Οἱ ἀδελφοί | Relative pronoun recycling; Act I close | Chrysippus outside the door of the community; he hears but does not enter; Melitta says she wants to go | Acts 18:8 complete (*ἐπίστευσεν... σὺν ὅλῳ τῷ οἴκῳ αὐτοῦ*) |

---

### Act II — The Community / Aorist System (Ch 14–24)

*Tone: comic-serious. The Pauline community enters.*
*Grammar arc: 1st aorist → 2nd aorist (dedicated chapter) → aorist passive → aorist consolidation → perfect → future → present participle → aorist participle → participle consolidation × 2.*

| Ch | Greek title | Grammar introduced | Narrative | *Ἐν ταῖς γραφαῖς* |
|---|---|---|---|---|
| **14** | **Ἐν τῷ λιμένι** | **1st aorist** (sigmatic) act + mid. Aorist/imperfect contrast throughout. Required pairs: ἀκούω/ἤκουσα, ζητέω/ἐζήτησα, βλέπω/ἔβλεψα | Chrysippus at Cenchreae; meets Aquila; his aorist actions against imperfect background — the contrast is felt before it is labelled | Mark 1:9 (ἦλθεν glossed as preview of Ch 15) |
| **15** | **Ἡ ἀγγελία** | **2nd aorist — all 6 suppletive pairs in one chapter.** λέγω/εἶπεν, ἔρχομαι/ἦλθεν, ὁράω/εἶδεν, λαμβάνω/ἔλαβεν, βάλλω/ἔβαλεν, φέρω/ἤνεγκεν. Each glossed with present on first occurrence. | Chrysippus reports to Melitta everything that happened at the harbour; every high-frequency NT verb in aorist in one connected narrative | Mark 1:9–11 (ἦλθεν now familiar; ἐγένετο introduced) |
| **16** | **Ἡ κατάκρισις** | **Aorist passive (θη-aorist)** | Theophrastus confronts Chrysippus publicly in the agora; passive forms narratively appropriate (κατῃσχύνθη — publicly shamed) | Mark 1:4 (*ἐβαπτίσθη*); Acts 18:8 (*ἐβαπτίσθησαν*) |
| **17** | **Ἡ ὁμολογία** | **Aorist consolidation — no new grammar.** All three aorist types + imperfect interleaved throughout. | Chrysippus retells the entire harbour story to Melitta; all suppletive pairs recycled in sequence; sustained aorist/imperfect narrative | 1 Cor 15:3–4 (**aspect payoff**: ἀπέθανεν/ἐτάφη [aor.] → ἐγήγερται [perf., glossed as preview of Ch 18]) |
| **18** | **Μέλιττα καὶ Πρίσκιλλα** | **Perfect (τὸ παρακείμενον).** Minimal pair in αἱ λέξεις: ἐπίστευσεν (aorist, moment of decision) vs. πεπίστευκεν (perfect, current state). High-value seeds: γέγραπται, ἀκήκοα, οἶδα. Greek prose three-way aspect explanation now possible (participles available). | Melitta visits Priscilla and returns speaking differently; Chrysippus notices | 1 Cor 15:3–4 **revisited, unglossed**; Ps 110:1 LXX cross-reference activated |
| 19 | Ὁ Ἀκύλας | Future indicative; complementary infinitives | A ship from Ephesus with bad news: a debt Chrysippus forgot he had. Chrysippus is offered work by Aquila; declines. | Acts 18:9–10 (Paul's vision) |
| 20 | Ἡ ἐπιστολή | Present participle (attributive + predicative). Chapter structured so participial parsing is required for comprehension — who the people are cannot be understood without it. | Chrysippus at the community gathering for the first time — watching, not participating | **Isa 53:7–8 LXX (seed #2)** with NT cross-references listed |
| 21 | Ἡ μνήμη | Aorist active participle; present vs. aorist participle contrast in proximate context | Chrysippus leaves the gathering quickly but cannot stop remembering what was read; same verb as aorist ptcp (completed act) then as present ptcp (ongoing state) | **Ps 117:22 LXX (seed #3)** — Mark 12:10 cross-reference listed |
| **22** | **Ὁ Χρύσιππος μανθάνει** | **Participle consolidation A** — present + aorist active participles together, no new morphology. Same verb appears in both forms in adjacent sentences. | Chrysippus visits sick Damon; does not know what to say; both participle types woven through the narrative | Mark 1:40–42 (healing narrative — authentic aspect contrast in participial forms) |
| 23 | Ἡ ὕβρις | Substantival + articular participle; aorist passive participle | Sosthenes beaten before the governor (Acts 18:17); Chrysippus watches from the crowd | Acts 18:12–17 complete |
| **24** | **Ὁ λόγος τοῦ Παύλου** | **Participle consolidation B** — all types together: present/aorist/passive. Aspectual distinction in participial form now visible and practiced. | Paul arrives in Corinth; Chrysippus sees him in the agora; Melitta says to go back to the community | Acts 18:17; 2 John (complete — 13 verses, now accessible) |

---

### Act III — Conviction / Advanced Grammar (Ch 25–36)

*Tone: serious with comic relief. Chrysippus is being changed without fully consenting to it.*
*Grammar arc: subjunctive → imperatives → infinitives → conditionals (split into two chapters) → perfect M/P → genitive absolute → ὅτι discourse → periphrastic → pluperfect → optative.*

| Ch | Greek title | Grammar introduced | Narrative | *Ἐν ταῖς γραφαῖς* |
|---|---|---|---|---|
| 25 | Φιλήμων | ἵνα + subjunctive (introduced via the text itself); **Pauline letter schema in αἱ λέξεις** | Chloe's people arrive carrying a letter; Chrysippus reads it slowly, with help | **Philemon complete** (first full NT book mid-course) |
| 26 | Τὸ βάπτισμα | ἵνα + subj. continued; ὡς + subj. | Crispus's household baptised; Chrysippus is outside the door during it | 3 John (complete — 15 verses) |
| 27 | Ἡ κρίσις | Imperatives; negated imperatives (μή + present vs. μή + aorist aspect distinction) | Melitta tells Chrysippus to go back to the community; he argues; she wins | James 1:1–8 (diatribe register; NT-750 ceiling makes this accessible) |
| 28 | Ἡ ἀπόφασις | Articular infinitive; ὥστε + infinitive | Theophrastus's daughter falls ill; Chrysippus does not know what to do | Phil 2:5–11 (Christ hymn — grammar complete; rare vocabulary glossed) |
| **29** | **Εἰ... εἰ δέ...** | **Conditionals A: first + third class only.** Theophrastus proposes settlement terms; both conditional classes used by different speakers in the same scene. | Theophrastus negotiates; Chrysippus deliberates; the difference between εἰ + indicative and ἐάν + subjunctive is felt before it is labelled | 1 Cor 15:17 (*εἰ δὲ Χριστὸς οὐκ ἐγήγερται* — force now fully readable) |
| **30** | **Εἰ γὰρ ἦν...** | **Conditionals B: second + fourth class.** Contrary-to-fact conditionals as testimony. | Damon recovers; no one can explain why; characters speak of what would have been if Paul had not come | Rom 8:38–39 (doxology; all words now known) |
| 31 | Ἡ πεποίθησις | Perfect middle/passive; perfect participle | Chrysippus attends a full community gathering; hears Paul speak at length | Heb 1:1–4 (grammar complete; heavily glossed; literary register noted) |
| 32 | Ὁ οἶκος τοῦ Στεφανᾶ | Genitive absolute | Stephanas's household; Chrysippus hears testimony in the language of the community | 1 Pet 1:1–5 (diaspora address; Isa 53 LXX cross-reference active) |
| 33 | Ἡ μαρτυρία | ὅτι recitative + indirect discourse; Hebraistic parataxis | Paul teaches on love (1 Cor 13 in summary); Chrysippus reports to Melitta what he heard | Luke 15:11–24 (Prodigal Son first half — aorist narrative + imperfect background) |
| 34 | Ὁ Παῦλος λαλεῖ | Periphrastic constructions (ἦν + participle); pluperfect | Melitta decides; the household discussion through the night | Luke 15:25–32 (Prodigal Son complete) |
| 35 | Ἡ χλόη | Optative wishes: εἴη, μὴ γένοιτο | Chrysippus prays for the first time; the optative as the grammar of desire and uncertainty | Phil 4:4–7 (imperatives + peace formula) |
| 36 | Τὸ πλοῖον ἀπέρχεται | Potential optative; Act IV close | Paul leaves Corinth (Acts 18:18); Chrysippus watches the ship depart; the grammar is complete | Acts 18:18–22 |

---

### Bridge — Register Transition (Ch 37–38)

| Ch | Content |
|---|---|
| **37** | Three NT passages (Mark 1:1–15; Acts 18:1–17; 1 John 1:1–10) rewritten in KPSI narrative style — same vocabulary and grammar, NT word order and sentence density. No new grammar. Transition in register only. |
| **38** | The same three passages in their authentic form, with sub-750 vocabulary glossed. Student reads the same content twice across two chapters. Recognition effect closes the gap before Act V. |

---

### Act V — Real NT Texts (Ch 39–50)

| Ch | Text | Notes |
|---|---|---|
| 39–40 | **1 John complete** (split across 2 chapters) | Johannine vocabulary built throughout the course; the first sustained unadapted reading |
| 41 | **Mark**: 1:1–15; 2:1–12; 5:21–43 | Three complete pericopes; natural aorist/imperfect narrative prose |
| 42 | **Acts 18 complete** | Every named character is now a person the reader has followed for 36 chapters |
| 43 | **1 Corinthians 13** | The narrative destination; seeded since Ch 2 |
| 44–45 | **Pauline survey**: Romans, Galatians, Philippians, Colossians, 1 Thessalonians — openings + closings | Pauline schema active; reader navigates 5 letters in 2 chapters |
| 46 | **James 1–2** | NT-750 ceiling minimises reader's edition dependency |
| 47 | **Hebrews 1:1–4:13** | Most literary NT Greek; grammar complete; Ps 110:1 LXX seed pays off here |
| 48 | **1 Peter complete** | Isa 53 LXX seed pays off at 2:22–24 |
| 49–50 | **John 1:1–18 (Prologue)** — twice | Ch 49: full marginal notes. Ch 50: no notes. Ends where the book began: φῶς, λόγος, εἰμί. |

---

## Key design decisions

| Decision | Rationale |
|---|---|
| **NT-500 → NT-750** | Unlocks James, Hebrews, Pastorals. ~2–3 lemmas/ch across Ch 12–28. No new chapters needed. |
| **Perfect moved to Ch 18** (was Ch 21) | Taught as aspectual viewpoint alongside aorist, not as a 4th past tense arriving 10 chapters later. |
| **Dedicated 2nd aorist chapter (Ch 15)** | εἶπεν, ἦλθεν, εἶδεν, ἔλαβεν, ἔβαλεν, ἤνεγκεν are NT top-100 verb forms; opaque from their present stems without explicit pairing. |
| **Consolidation chapters** (6, 17, 22, 24) | Convert paradigm knowledge into fluency. No new grammar; maximum cross-type recycling density. |
| **Conditionals split** into Ch 29 + Ch 30 | Four conditional classes are four distinct constructions. Compressing them produces the same learning damage as compressing the aorist. |
| **Philemon at Ch 25** | First complete NT book mid-course; psychological milestone; clearest Pauline schema exemplar; thematically resonant with the narrative. |
| **Pauline letter schema at Ch 25** | One αἱ λέξεις section unlocks navigation of all 13 Pauline letter openings and closings. |
| **3 LXX quotations seeded** (Ps 110:1, Isa 53, Ps 117:22) | Each appears in 3–5 NT books. Force-multiplier for Acts, Hebrews, 1 Peter, Romans, and the Synoptics. |
| **Bridge chapters 37–38** | Same content twice: scaffolded then authentic. Prevents hard register drop at Act V entry. |
| **Act V as survey + depth** | Reader finishes knowing the feel of every major NT book, not just 3 deep texts. |
| **Aspect concept at Ch 11** (pre-aorist) | Demonstrated via narrative contrast before it is labelled; label before Greek prose definition is possible; prose definition deferred to Ch 18. |
| **Glosses vocabulary-controlled throughout** | Every apparatus word uses only previously seen vocabulary or meta-terms introduced in that note. Ch 1 model governs unconditionally. |

---

## Grammar sequencing checklist

| Feature | Chapter | Required narrative provision |
|---|---|---|
| Aspect concept (label only) | 11 | Imperfect/aorist minimal pair in narrative; no prose definition |
| Aspect concept (prose definition) | 18 | Three-way contrast expressed using participles the reader now has |
| 1st aorist + imperfect contrast | 14 | Same verb in both forms in proximate narrative context |
| 2nd aorist suppletive pairs | 15 | All 6 pairs in one connected narrative; present stem gloss on first occurrence |
| Aorist passive | 16 | Narrative context where passive voice is semantically appropriate (humiliation scene) |
| All aorist types combined | 17 | Consolidation narrative; no new vocabulary |
| Perfect as current state | 18 | Minimal pair: aorist (event, moment) vs. perfect (state, now) with same verb |
| Present vs. aorist participle contrast | 21, 22 | Same verb as present ptcp then aorist ptcp in proximate context |
| Conditionals first + third class | 29 | Two speakers using different classes in same conversation |
| Conditionals second + fourth class | 30 | Contrary-to-fact testimony; narrative makes the semantic force unmistakable |

---

## NT texts programme

| Stage | Primary source | Secondary |
|---|---|---|
| Ch 1–5 | 1 John 1:5; 4:8; John 1:1 fragments | 1 Cor 1:1–3 |
| Ch 6–10 | 1 John together; Acts 18:1–6; Ps 110:1 LXX | Luke 2:1–11 |
| Ch 11–16 | Mark 1:9–15; Acts 18:7–8; 1 Cor 15:3–4 (preview) | — |
| Ch 17–24 | 1 Cor 15:3–4 (payoff); Acts 18:9–17; Isa 53 + Ps 117:22 LXX | 2 John; Mark healing narratives |
| Ch 25–36 | Philemon; 3 John; James 1; 1 Cor 15:17; Heb 1:1–4; 1 Pet 1; Luke 15 | Phil 2:5–11; 4:4–7; Rom 8:38–39 |
| Ch 37–38 | Bridge: scaffolded → authentic (Mark 1; Acts 18; 1 John 1) | — |
| Ch 39–50 | 1 John; Mark; Acts 18; 1 Cor 13; Pauline survey; James; Heb; 1 Pet; John Prologue | — |

---

## Vocabulary tracking

- **Ceiling:** NT-750 lemmas by frequency
- **Recycling rule:** Every introduced lemma appears 5–8× in its introduction chapter, then every 2–3 chapters
- **Atrophy threshold:** Word absent for 4+ chapters = flagged by `vocab_check.py`
- **Tool:** `python3 scripts/vocab_check.py [--chapter N] [--atrophy-threshold 4]`
- **Action required:** Extend `scripts/nt500.txt` to NT-750 rank; update ceiling parameter in `vocab_check.py`
- **Non-NT vocab:** Permitted only when NT-750 vocab cannot carry the narrative. Must be glossed and noted in αἱ λέξεις with provenance; never at the expense of NT-750 recycling targets.

---

## Source files

| File | Purpose |
|---|---|
| `src/story_plan.md` | Detailed chapter-by-chapter narrative and grammar notes |
| `src/001.md` | Chapter 1 complete draft — model for αἱ λέξεις style and inline gloss format |
| `scripts/nt500.txt` | NT frequency list (needs extending to rank 750) |
| `scripts/vocab_check.py` | Vocabulary tracking and atrophy detection |
| `scripts/html.sh` / `pdf.sh` / `ebook.sh` | Build pipeline (HTML, PDF via XeLaTeX, EPUB) |
| `templates/default.html` | `.gloss` tooltip rendering |
| `templates/default.latex` | Marginal note rendering for PDF output |
