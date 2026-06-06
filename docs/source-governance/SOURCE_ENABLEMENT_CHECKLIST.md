# Source Enablement Checklist (Disabled-Ready Sources)

This checklist is for enablement planning only. It does not auto-enable any source.

Current verified counts:

- total_sources: 26
- machine_ingest_sources: 8
- runnable_now: 7
- enable_ready: 0
- deprecated: 3
- machine_ready_disabled: 0
- adapter_missing: 16

All machine-ingest sources are now enabled. This checklist is retained for reference and future source onboarding.

## Global Preconditions (Required For Any Enablement)

- Confirm legal terms of use permit machine ingestion and local evidence retention.
- Confirm source endpoint availability and stable fetch behavior over multiple runs.
- Run adapter contract tests and source-specific replay/fixture tests.
- Run one non-publishing dry ingestion via `POST /api/admin/sources/{source_key}/dry-run`.
- Confirm dry-run indicates expected evidence snapshot behavior before any real run.
- Verify review queue payload quality and citation/evidence binding quality.
- Regenerate proof artifacts and verify source registry truth table consistency.
- Obtain documented approval from release/security/governance owners.
- Enable exactly one source at a time, never as a bulk toggle.

## Source-Specific Checklist (Complete)

All machine-ingest sources are now enabled. No sources remain in the enable-ready queue.

Enabled sources:
- `justice_canada_laws_xml`
- `saskatoon_open_data_public_safety`
- `sk_courts_qb_decisions`
- `sk_courts_ca_decisions`
- `federal_court_canada`
- `scc_decisions`
- `sk_legislature_hansard`

## Non-Goals (Alpha Integrity)

- No production-readiness claim is implied by this checklist.
- No source is enabled automatically.
- Evidence, review, and publication guardrails remain unchanged.
