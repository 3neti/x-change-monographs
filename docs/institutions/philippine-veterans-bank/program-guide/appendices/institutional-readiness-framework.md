# Annex F — Institutional Readiness Framework

Readiness is PVB's judgment, together with the responsible public authority where applicable, that sufficient evidence exists to authorize, operate, supervise, secure, settle, reconcile, support, evidence, and govern a public-finance ceremony.

The judgment should address the complete institutional setting, not only software behavior.

| Readiness dimension | Evidence required before bounded production |
| --- | --- |
| Public and institutional governance | Approved purpose, authority, accountable owners, decision rights, escalation, controlled-production authority, and review criteria |
| Banking service | Defined outcome, participants, policy, terms, limits, channels, communications, and fair treatment |
| Operations | Documented initiation, approval, supervision, support, exceptions, recovery, evidence, reconciliation, and end-of-day responsibilities |
| Treasury and settlement | Confirmed Funding Events, Settlement Resources, Liens, accounts, limits, liquidity, references, statuses, unresolved-state treatment, and settlement responsibilities |
| Risk, Compliance, Legal, and Privacy | Reviewed public authority, regulatory obligations, risks, controls, participant terms, agreements, data treatment, and legal characterization |
| Technology and architecture | Approved environments, interfaces, identities, observability, capacity, resilience, backup, recovery, service management, and change processes |
| Information security | Approved access, credentials, certificates, secrets, testing, monitoring, incident response, vulnerability management, and production controls |
| Finance and accounting | Defined entries, fees, provider charges, reporting, reconciliation, exception treatment, and financial-control ownership |
| Participant experience | Tested initiation, evidence gathering, disclosures, status communication, assistance, failure treatment, and completion experience |
| People and providers | Trained personnel, operating procedures, support coverage, provider obligations, service levels, escalation paths, and continuity arrangements |
| Evidence and assurance | Test results, technical validation, operating rehearsals, control evidence, unresolved findings, approvals, and independent review where required |

Technical validation demonstrates that PVB-specific integration performs agreed behavior under tested conditions. It does not decide whether the public program is authorized, the banking service is suitable, policy is approved, personnel are prepared, settlement is sufficient, accounting is correct, participants can be supported, or exceptions can be governed.

Operational readiness therefore follows technical validation; it is not produced by technical validation. PVB and the responsible public institution may authorize bounded production only when responsible functions have evaluated the complete ceremony and accepted the operating conditions.

Evidence should be reviewed through the institutional choices **Proceed**, **Correct**, **Extend**, or **Pause**. A successful technical transaction is evidence within that review, not the review itself.

```mermaid
flowchart LR
    Dialogue["Institutional Dialogue"] --> Definition["Ceremony Definition"]
    Definition --> Discovery["Integration Discovery"]
    Discovery --> Technical["Technical Validation"]
    Technical --> Operational["Operational Readiness"]
    Operational --> Controlled["Controlled Production Decision"]
    Controlled --> Review["Proceed · Correct · Extend · Pause"]
```

No arrow makes the next state automatic. Each transition requires the authority and evidence appropriate to the responsibility being considered.
