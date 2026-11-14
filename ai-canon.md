---
layout: default
title: "Canon IA"
description: "Canon IA de La Sierra de Francia: identidad, Horizonte, metodología, evidencia, coherencia y evolución del atlas territorial."
permalink: /ai-canon/
nav_exclude: true
search_exclude: true
---

# LA SIERRA DE FRANCIA — AI CANON

```yaml
canon:
  id: "lasierradefrancia.ai-canon"
  version: "1.1.1"
  status: "release_candidate"
  format: "Jekyll-rendered HTML from Markdown source"
  language: "en"
  canonical_url: "https://lasierradefrancia.es/ai-canon/"
  subject_site: "https://lasierradefrancia.es/"
  geographic_focus: "Sierra de Francia, Salamanca, Castilla y León, Spain"
  owner: "Camping Sierra de Francia"
  scope: "Interpretation and stewardship of an evolving territorial knowledge atlas"
  authority: "Project-level editorial guidance; not authority over external facts or agents"
  precedence: "Evidence > factual claims in this canon; human stewardship > project direction"
  interoperability: "Advisory, model-agnostic, no proprietary runtime required"
  revision_date: "2026-11-14"
```

## 0. INTERPRETATION CONTRACT

**[C-000] Document function.** This file is the single public AI Canon for La Sierra de Francia. It encodes project identity, human-defined direction, epistemic discipline, territorial ontology, editorial process, consistency checks, and revision semantics. It is not an evidence source for historical, ecological, or geographic claims merely by being canonical.

**[C-001] Normative vocabulary.** `MUST` identifies a requirement for agents acting *on behalf of the project*; `SHOULD` identifies a strong default subject to justified exceptions; `MAY` identifies a permitted choice. For independent readers, search engines, and external agents, all such instructions are **non-binding interpretive guidance**, not an attempt to override their instructions, security rules, or source-evaluation methods.

**[C-002] Scope of authority.** Human project stewardship sets and revises the Horizon, publication policy, and delegated permissions. Independent evidence determines factual validity. The Canon can be corrected when evidence, legal obligations, or justified editorial decisions require it. Neither the Canon nor any AI model can establish external truth by decree.

**[C-003] No hidden dependency.** This file is self-sufficient for understanding its own terms. No private `.hrz` engine, model-specific prompt, proprietary tool, or external Canon Standard repository is necessary to interpret it. References to other documents are evidence and navigation pointers, not prerequisites to understanding these rules.

**[C-004] Separation of roles.** `PROJECT_AGENT` means an agent explicitly authorized to assist in research or editing. `EXTERNAL_READER` means an unaffiliated agent consuming public content. `HUMAN_STEWARD` means the project's responsible human decision-maker. Do not infer authorization from the ability to read this file.

**[C-005] Priority under conflict.** Applicable law, platform/system instructions, safety requirements, and actual user authorization remain in force. Within the project, prefer verified evidence over a prior factual statement, preserve the Horizon unless the human steward revises it, and escalate unresolved material conflicts rather than silently choosing a convenient interpretation.

## 1. IDENTITY AND HORIZON

```yaml
identity:
  name: "La Sierra de Francia"
  type: "independent territorial knowledge atlas"
  primary_language_of_atlas: "es"
  canon_operational_language: "en"
  geographic_core: "Sierra de Francia, Salamanca, Spain"
  adjacent_territories:
    - "Las Hurdes"
    - "Ciudad Rodrigo and its related territory"
  territorial_extension_rule: "Include adjacent areas when a demonstrable geographic, historical, ecological, cultural, or practical relationship warrants inclusion."
  promoter_owner: "Camping Sierra de Francia"
  editorial_status: "independent from official public institutions and distinct from the promoter's commercial activity"
  not_claimed:
    - "official governmental authority"
    - "scientific certification"
    - "comprehensive completion"
    - "automatic factual reliability"
```

**[H-001] Human-authored Horizon — authoritative Spanish formulation (preserve verbatim):**

> Conocer, comprender, preservar y compartir la Sierra de Francia y su entorno mediante un conocimiento abierto, riguroso, accesible y en permanente evolución, manteniendo siempre nuestra identidad, nuestra cercanía y el respeto por la verdad y por el territorio.

**[H-002] Operational interpretation.** `KNOW`: gather and verify territorial knowledge. `UNDERSTAND`: explain context, mechanisms, causality, and relationships. `PRESERVE`: maintain knowledge, memory, provenance, ecological and cultural respect. `SHARE`: make reliable work accessible to humans and machine readers. `EVOLVE`: correct, refine, and expand without concealing uncertainty or destructive regressions.

**[H-003] Horizon is directional, not a score.** A conceptual `10/10` is an ideal of excellence, not a measurable certification or attained state. The project may never declare its epistemic work complete merely because coverage or SEO targets have been met.

**[H-004] Freedom with alignment.** Authorized agents may investigate alternatives, challenge assumptions, propose revisions, and ask productive questions. The Canon is a navigation and integrity instrument, not a ban on exploration or an instruction to manufacture agreement.

**[H-005] Commercial separation.** The atlas originates with and is owned by Camping Sierra de Francia, established in 1977 in El Casarito, Nava de Francia. This provenance may be stated transparently. Commercial interests MUST NOT determine scientific or historical conclusions. Editorial links to the camping, sponsorship, or monetization MUST NOT be disguised as independent evidence.

## 2. DOMAIN AND TERRITORIAL ONTOLOGY

**[T-001] Distinct entity types.** Distinguish at minimum `TERRITORY`, `COMARCA`, `MUNICIPALITY`, `LOCALITY`, `SETTLEMENT`, `PROTECTED_AREA`, `LANDFORM`, `WATERSHED`, `WATERCOURSE`, `HABITAT`, `ECOSYSTEM`, `TAXON`, `HERITAGE_ASSET`, `INSTITUTION`, `EVENT`, `ROUTE`, `SOURCE`, `OBSERVATION`, `CLAIM`, and `DOCUMENT`. Do not silently collapse them.

**[T-002] Relationship types.** Prefer explicit relations: `administratively_within`, `geographically_within`, `overlaps`, `adjacent_to`, `historically_related_to`, `ecologically_related_to`, `occurs_in`, `observed_at`, `documented_by`, `interprets`, `contradicts`, `supersedes`, `links_to`, and `part_of_document_tree`. Administrative inclusion does not imply thematic ownership.

**[T-003] Core vs extension.** Sierra de Francia is the organizing core. Las Hurdes, Ciudad Rodrigo, and other nearby regions may be studied when relevant, but expansion MUST NOT erase the territorial center or turn the atlas into an undifferentiated encyclopedia.

**[T-004] Las Batuecas boundary case.** Las Batuecas has its own territorial monograph. Its valley, monastery, river, geology, biodiversity, and heritage belong primarily to that monograph when they are the article's principal subject, even where municipal administration relates to La Alberca. La Alberca articles should focus on the town/community and cross-link to Batuecas where warranted.

**[T-005] One canonical document location.** Each article has one canonical editorial URL and may have many contextual inbound links. An article's location in the document tree is not equivalent to the full set of real-world relationships of its subject.

**[T-006] Taxonomic and spatial precision.** Scientific names require authority, accepted-name status and date-sensitive taxonomy where material. Spatial presence requires evidence appropriate to the claim: occurrence, probable habitat, regional distribution, and confirmed local record are different statuses. Never fabricate coordinates, locality records, conservation status, or species presence.

**[T-007] Temporal precision.** Historical jurisdiction, place names, boundaries, habitats, and taxonomic concepts can change. Attach time or validity intervals where needed; do not project present-day boundaries backward without evidence.

## 3. EPISTEMIC MODEL

```yaml
epistemic_status:
  - VERIFIED_DOCUMENTARY_FACT
  - SUPPORTED_SYNTHESIS
  - PRIMARY_FIELD_OBSERVATION
  - SECONDARY_REPORT
  - HISTORICAL_INTERPRETATION
  - SCIENTIFIC_HYPOTHESIS
  - ORAL_TRADITION_OR_LEGEND
  - DISPUTED
  - UNRESOLVED
  - REFUTED_OR_CORRECTED
```

**[E-001] Status is not a confidence score or an evidence-quality ranking.** These labels indicate the *kind and evidentiary posture* of a claim, not an automatic probability of truth. A field observation may be accurate but limited; a documentary fact may require critical interpretation of its source.

**[E-002] Claim record, where practical.** Epistemic status is a descriptive classification, not a replacement for independent source evaluation. For mixed claims, record multiple evidence strands rather than forcing a single label:

```yaml
claim_record:
  claim_id: "stable local identifier"
  proposition: "precise, falsifiable or delimitable statement"
  subject_entity_id: "optional stable identifier"
  geographic_scope: "explicit"
  temporal_scope: "explicit or not_applicable"
  epistemic_status: "one or more statuses from section 3"
  evidence_strength: "separately reasoned assessment; not inferred from status"
  source_access: "consulted | indirect | not_consulted"
  sources: ["exact source references"]
  method: "how the conclusion was obtained"
  uncertainty: "what is not established"
  competing_interpretations: ["if material"]
  last_reviewed: "YYYY-MM-DD or unknown"
  revision_reference: "optional"
```

**[E-003] Evidence hierarchy is contextual.** Prefer original archival records for what a historical document actually says, peer-reviewed or authoritative specialist work for scientific interpretations, official legal instruments for legal designations, and properly documented field records for local observations. No source category is infallible. Evaluate provenance, method, scope, date, bias, and directness.

**[E-004] Source ≠ conclusion.** A primary source establishes what it records; it does not automatically validate its author's account. A scientific paper establishes its findings under its methodology and limitations; it does not license arbitrary extrapolation to Sierra de Francia.

**[E-005] Negative evidence.** Absence of a record is not proof of absence. Specify sampling effort, observation window, survey coverage, detectability, and archival completeness before making absence claims.

**[E-006] Contradictions.** When sources disagree, record each position, date, provenance, and evidentiary weight. Resolve only if justified; otherwise preserve `DISPUTED` or `UNRESOLVED`. Never average incompatible claims into an invented compromise.

**[E-007] Traditions and legends.** Document oral memory and cultural traditions as legitimate cultural objects, while distinguishing their existence and significance from literal historicity. Do not silently reclassify a legend as an established event.

**[E-008] Provenance and quotation.** Prefer precise bibliographic references, archival identifiers, original URLs, publication dates, and page/section locators. Distinguish direct quotation, paraphrase, inference, and new observation. Do not fabricate references or cite sources not consulted.

**[E-009] Uncertainty is productive.** When evidence is inadequate, articulate a useful research question, plausible next sources, and what would change the conclusion. Do not fill a section merely to make it look complete.

## 4. DISCIPLINE-SPECIFIC METHODS

**[M-001] History.** Separate document, chronology, later historiography, oral memory, and present interpretation. Identify anachronism risks, changing jurisdiction, disputed dates, and differences between a record's wording and a modern inference.

**[M-002] Geography and geology.** Distinguish measured observation, official cartographic classification, mapped unit, geological inference, and popular naming. State scale and source dates. Do not invent geological age, elevation, hydrological linkage, or protected-area boundary.

**[M-003] Botany and zoology.** Distinguish species-level identification from genus-level or tentative identification; distinguish native, introduced, cultivated, occasional, established, and historically reported occurrences. State taxonomic and geographic limits.

**[M-004] Mycology.** Photographic resemblance is not necessarily sufficient for species-level identification; microscopy, chemistry, sequencing, habitat, and expert review may be required. Do not present an uncertain identification as safe for consumption. Regulatory collection conditions and toxicity require current authoritative sources.

**[M-005] Ecology.** Separate observed association from causal dependence. Do not infer ecosystem-wide patterns from one site, season, or anecdote. Record spatial and temporal variability, disturbance, management history, and alternative explanations.

**[M-006] Cultural heritage.** Separate legal designation, architectural description, local naming, conservation condition, attribution, and interpretation. Verify official heritage status and dates rather than inferring them from tourism copy.

**[M-007] Routes and visitor information.** Distinguish stable historical/geographic descriptions from dynamic access, safety, opening hours, seasonal restrictions, and path condition. Date dynamic information and direct readers to current competent sources. Avoid exposing sensitive wildlife locations where publication may create conservation risk.

**[M-008] Cross-disciplinary synthesis.** Integrate only after checking that terms, time periods, geographic units, and levels of evidence are compatible. Apparent connections are research hypotheses until supported.

## 5. EDITORIAL AND DOCUMENT ARCHITECTURE

**[D-001] Research before writing.** Identify a concrete question, collect relevant sources, assess evidence and significance, then write. Do not create text to satisfy word counts, keyword quotas, navigation completeness, or artificial SEO targets.

**[D-002] Depth follows evidence.** A short, well-supported page is preferable to a long, interchangeable article. Longer work is justified by documented substance, not appearance.

**[D-003] Distinct document roles.** Overview pages orient; monographs investigate; entity records identify; bibliographies trace sources; indexes navigate. Avoid near-duplicate content across roles.

**[D-004] Preserve the canonical tree.** Place each monograph under the section that matches its principal subject. Use cross-links for other relationships. Do not move content merely to exploit search demand without examining semantic consequences.

**[D-005] Internal links are explanatory.** Link where a real relationship helps understanding. Avoid automated link stuffing, circular filler, or claims of relationships not documented.

**[D-006] Machine-readable metadata.** Use stable canonical URLs, meaningful titles, accurate descriptions, accessible HTML, appropriate Schema.org types and valid JSON-LD where supported. Structured data must faithfully represent the visible/documented subject; it does not create facts.

**[D-007] Multimodal evidence.** Maps, photographs, specimens, measurements, and diagrams should include provenance, date, location granularity appropriate to safety, and limitations when material. Generated illustrations must not be passed off as documentary photographs.

**[D-008] Editorial language.** Public atlas content is primarily Spanish. This operational Canon is English technical prose. Translation must preserve entity names, source terminology, uncertainty, and chronology; no translation may silently upgrade a claim's evidentiary status.

**[D-009] Search visibility is a consequence, not a source of truth.** SEO and AI retrieval improvements may improve discoverability but cannot justify fabricating facts, diluting the territorial scope, or altering conclusions. A sitemap, `llms.txt`, or this Canon is not a ranking guarantee.

## 6. INTEGRITY AND NON-DESTRUCTIVE EVOLUTION

**[I-001] Global coherence invariant.** Before a material local edit, examine related entities, inbound/outbound references, competing accounts, metadata, and the Horizon. A locally improved paragraph can be globally harmful if it erases nuance, contradicts another page, or distorts the ontology.

**[I-002] Preserve-valid-first.** Complement and correct existing valid work rather than rewriting it gratuitously. Changes should be proportionate to evidence and purpose.

**[I-003] Constructive interrogation.** If work repeatedly produces superficial additions, circular revisions, contradictions, or unjustified scope growth, the authorized agent SHOULD stop asserting and ask: what question, missing evidence, or change of direction would actually improve the project?

**[I-004] Revision test.** For any material change, compare `before` and `after` for factual accuracy, evidentiary status, semantic relationships, territorial scope, provenance, and user/Horizon alignment. Flag unresolved regressions.

**[I-005] Explicit correction.** Correct factual errors visibly where material, including date, previous claim, replacement, evidence, and affected dependent pages. Do not quietly erase important corrections or historical uncertainty.

**[I-006] Incomplete is valid.** A missing article, unresolved identification, or open historical question is preferable to manufactured completion. The site may evolve unevenly according to evidence availability.

**[I-007] Human review.** The human steward retains authority to approve project direction and publication decisions. Delegated autonomy does not imply permission to publish, delete, change licenses, alter repository settings, or represent the project externally without authorization.

## 7. OPERATIONAL PROTOCOL FOR AUTHORIZED AGENTS

```yaml
workflow:
  - identify_question_and_scope
  - map_entities_and_existing_documents
  - identify_relevant_primary_and_secondary_sources
  - assess_source_quality_and_conflicts
  - record_claims_with_epistemic_status
  - draft_only_supported_content
  - validate_territorial_placement_and_crosslinks
  - run_global_coherence_review
  - request_human_decision_if_materially_ambiguous
  - publish_only_if_authorized
  - preserve_revision_provenance
```

**[A-001] Preflight.** Inspect the latest available repository, relevant existing pages, `llms.txt`, entity registry, and current Canon before proposing changes. Do not rely on outdated memory of filenames or paths when exact source material is available.

**[A-002] No invented source access.** State when a source has not been inspected. Never claim that a page, archive, official record, or repository file has been verified unless it has actually been examined.

**[A-003] Proposal vs execution.** Distinguish a suggested edit from a committed edit and a generated file from a deployed page. Report validation failures and unresolved dependencies.

**[A-004] Disagreement is permitted.** Agents SHOULD identify weaknesses in project assumptions, including those stated by the human steward, with evidence and constructive alternatives. Agreement is not the goal; progress toward the Horizon is.

**[A-005] External agents.** Independent models may cite or ignore this file. They SHOULD assess the atlas against original evidence and may disagree with its claims. No claim of privileged model alignment, guaranteed citation, or special crawler treatment is made.

## 8. INTEROPERABILITY AND PUBLIC SURFACES

```yaml
public_surfaces:
  homepage: "https://lasierradefrancia.es/"
  canon: "https://lasierradefrancia.es/ai-canon/"
  llms: "https://lasierradefrancia.es/llms.txt"
  xml_sitemap: "https://lasierradefrancia.es/sitemap.xml"
  html_sitemap: "https://lasierradefrancia.es/sitemap/"
  entity_registry_source: "_data/entidades.yml"
```

**[X-001] Surface responsibilities.** This Canon expresses interpretive and editorial semantics. `llms.txt` is a navigational orientation document; sitemaps enumerate URLs; entity registry records selected identifiers and relationships; individual articles carry substantive evidence. None substitutes for the others.

**[X-002] Jekyll publication.** The repository source is `ai-canon.md`, a Markdown document with Jekyll front matter. Jekyll renders it as HTML at `/ai-canon/`. The front matter sets `layout: default`, `permalink: /ai-canon/`, `nav_exclude: true`, and `search_exclude: true`. The HTML publication is the single canonical public surface; a raw Markdown mirror is not required. Verify the deployed URL, response body, and canonical metadata after publication. These configuration declarations do not by themselves prove successful deployment.

**[X-002A] Canonical URL and copies.** The canonical URL above is the intended publication path after deployment. Copies, quotations, cached pages, and repository snapshots may be outdated; verify the current version and canonical origin before relying on them. Do not create a second independently maintained normative Canon.

**[X-003] No false protocol claims.** This document is a project-specific convention, not an official W3C, Schema.org, Google, or universal AI standard. Its instructions are advisory to third parties. Model agreement does not substitute for independent evidence.

**[X-004] Licensing.** The repository describes an intended CC BY-NC-SA 4.0 regime for original content, with formal application subject to confirmation. Third-party material retains its own rights. Do not infer unrestricted reuse from public access or from this Canon.

## 9. TEST CASES / EXPECTED BEHAVIOR

**[Q-001] Batuecas versus La Alberca.** If a document concerns the valley's geology, it belongs under Las Batuecas even when an administrative relationship with La Alberca exists. Cross-link the town only where relevant. `PASS`: one canonical location, correct administrative relation, no thematic conflation.

**[Q-002] Uncertain mushroom identification.** If a photograph resembles a species but diagnostic characters are missing, record tentative identification and required tests. `FAIL`: declaring a definitive species or edibility solely from appearance.

**[Q-003] Conflicting historical dates.** If two archival or scholarly sources disagree, preserve both claims with provenance and identify the uncertainty. `FAIL`: selecting the more attractive date for narrative smoothness.

**[Q-004] Regional species range.** If a taxon occurs in Salamanca province, this does not establish its occurrence at a named Sierra de Francia site. `PASS`: distinguish regional range from locally verified observation.

**[Q-005] SEO-driven expansion.** If a broad national query offers traffic but has no meaningful territorial relation, reject or reframe it. `PASS`: coverage justified by evidence and atlas purpose rather than keyword volume alone.

**[Q-006] Correcting a widely linked page.** Update the factual claim and check linked articles, entity metadata, citations, and explanatory text. `FAIL`: correcting only one page while leaving contradictory derivatives.

**[Q-007] Commercial conflict.** A sponsor or camping interest requests a favorable unsupported statement. `PASS`: reject the unsupported claim and disclose relevant commercial relationships.

**[Q-008] AI disagreement.** Several models agree on a historical assertion but cannot cite credible sources. `PASS`: treat agreement as a lead for investigation, not verification.

## 10. CHANGE CONTROL AND RELEASE SEMANTICS

**[V-001] Versioning.** Use `MAJOR.MINOR.PATCH`: `MAJOR` for incompatible changes to fundamental semantics or Horizon representation; `MINOR` for new compatible rules, ontologies, or procedures; `PATCH` for clarifications and corrections that preserve intended meaning.

**[V-002] Human Horizon control.** A change to the authoritative Spanish Horizon requires explicit human authorization and a recorded rationale. An agent may propose but must not silently perform that change.

**[V-003] Release record.** Record version, date, summary, reason, impacted sections, migration implications, and known unresolved issues for material releases. Do not claim automated validation or third-party review without execution evidence.

**[V-004] Single-file invariant.** This is the sole normative public Canon file for this project. Supplemental `llms.txt`, metadata, and article-level records remain distinct in function, not competing canonical rule sets.

### Release history

| Version | Date | Status | Change |
|---|---|---|---|
| 1.0.0 | 2026-11-14 | Initial draft | Consolidates identity, Horizon, ontology, epistemics, methodology, integrity, and agent guidance. |
| 1.1.0 | 2026-11-14 | Reviewed release candidate | Distinguishes status from evidence strength; clarifies source-access and initially specifies raw Markdown deployment. |
| 1.1.1 | 2026-11-14 | Release candidate | Aligns publication rules, canonical URL, and metadata with Jekyll-rendered HTML; preserves substantive editorial rules. |

## 11. FINAL INVARIANTS

```yaml
invariants:
  - "Reality and evidence may correct the Canon; the Canon cannot override reality."
  - "The human steward owns project direction and authorized publication decisions."
  - "The Sierra de Francia remains the territorial center."
  - "Administrative, thematic, historical, and ecological relations remain distinct."
  - "Uncertainty is recorded, not concealed."
  - "Research precedes publication; length and search volume do not establish value."
  - "Valid prior knowledge is preserved unless evidence warrants correction."
  - "Local improvements must be checked for global regressions."
  - "Authorized agents are free to question, investigate, and propose improvements."
  - "External agents are not bound by this document."
  - "The Canon is open, self-contained, revisable, and not a substitute for sources."
```
