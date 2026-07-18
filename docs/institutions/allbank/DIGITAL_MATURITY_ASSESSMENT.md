# Digital Maturity Assessment — AllBank

## Document record

- Status: Accepted for Analysis
- Version: 0.1
- Evidence cutoff: 18 July 2026
- Basis: Public evidence only
- Scoring: None

## Assessment method

This assessment describes evidenced capability, bounded maturity indications, and unknowns. It does not assign a numerical score or maturity grade. A public channel proves presence, not adoption, reliability, integration quality, or institutional readiness.

## Executive assessment

**Observed.** AllBank has visible digital capability across retail mobile banking, online onboarding, corporate internet banking, national payment rails, QR merchant acceptance, bills payment, and partner-led payment services. [CLM-011–CLM-016, CLM-022–CLM-025]

**Inferred.** The public record is consistent with a bank that has progressed beyond basic channel digitization into multichannel transaction services and external payment partnerships. [INF-001–INF-004]

**Unknown.** Public sources are insufficient to assess adoption, customer experience, internal reuse, automation, data quality, operational performance, cybersecurity assurance, API maturity, or production readiness. [UNK-004–UNK-010, UNK-015]

## Capability assessment

| Dimension | Existing public capability | Classification | Maturity indication | Unknowns requiring clarification |
| --- | --- | --- | --- | --- |
| Retail mobile banking | iOS and Android apps; annual reports describe account inquiry, transfers, QR, and payments. | Observed | Maintained mobile channel visible through Aug 2025 app updates. | Active users, feature parity, uptime, completion, disputes, release governance |
| Digital onboarding | Public e-KYC journey for selected account types. | Observed | Digital account-opening front end is present. | Approval rate, turnaround, manual review, exception handling, fraud controls, activation |
| Corporate digital banking | AllConnect login, terms, and enrollment; maker/authorizer controls and corporate functions. | Observed | More than inquiry-only capability is publicly described. | Client adoption, entitlement model, workflow depth, service levels, host integration |
| Retail payment rails | Sender/receiver participation in InstaPay, PESONet, QR Ph P2P/P2M, and Bills Pay PH. | Observed | Broad current network participation. | Volumes, limits, settlement-account design, providers, reconciliation, exception rates |
| Merchant acceptance | QRPh P2M, POS acquiring, merchant portal, and partner announcements. | Observed | Merchant-facing surfaces and partner distribution are visible. | Merchant count, onboarding, settlement terms, reporting, disputes, economics |
| Payroll and bulk payments | Payroll products and corporate functions including payroll and bulk transfer. | Observed | Employer-oriented transaction capability is publicly listed. | Employers, employees, funding model, cut-offs, exceptions, lending linkage, priority |
| Collections and cash management | Bills payment, PDC warehousing, deposit pick-up, night depository, account sweeping. | Observed | Multiple business-collection and cash-management services are disclosed. | Digitization level, straight-through processing, reconciliation, product status, volumes |
| Partner ecosystem | Named QR/payment partnerships in 2023, 2024, and 2026 sources. | Observed | Repeated partnership-led expansion signal. | Common integration pattern, governance, partner performance, economics, current status |
| Standards orientation | Historical ISO 20022 statement. | Observed — historical | Awareness or adoption of a payments-message standard was disclosed. | Current scope, version, systems, production use, governance |
| Security posture | Institution-issued guidance names several technical controls and transaction notifications. | Observed | Public evidence of stated security practices. | Independent certification, testing, control effectiveness, incident and recovery evidence |
| API and integration capability | Public corporate bulk sending was described as available via API in the 2023 report. | Observed | At least one public API reference exists. | API catalog, ownership, access, authentication, idempotency, webhooks, errors, versioning |
| Reusable operating model | No direct public evidence. | Unknown | Cannot be assessed. | Whether services share governed purpose, evidence, exception, settlement, and reconciliation grammar |
| Data and analytics | No sufficient public evidence. | Unknown | Cannot be assessed. | Data platform, reporting, decisioning, customer analytics, model governance |
| Cloud and DevOps | No sufficient public evidence. | Unknown | Cannot be assessed. | Hosting, CI/CD, observability, credentials, segregation, change and release governance |
| Operational readiness | No ceremony-level evidence available. | Unknown | Cannot be assessed from channel presence or partner announcements. | Policy, people, controls, support, settlement, evidence, reconciliation, failure handling |

## Customer-journey maturity

### Retail onboarding

**Observed.** A customer can enter a public digital onboarding journey and select among published account types. [CLM-012]

**Unknown.** The public surface does not show the complete journey from application through screening, approval, initial funding, credential activation, support, and exception resolution. [UNK-009–UNK-010]

### Corporate banking

**Observed.** AllConnect materials distinguish corporate account ownership and authorized-user functions, including maker/authorizer controls. [CLM-013–CLM-014]

**Inferred.** Public control language suggests that the corporate channel is designed around institutional authorization rather than simple consumer-style access. It does not establish end-to-end operating maturity. [INF-002]

### Merchant payments

**Observed.** AllBank has public merchant and partner surfaces for QRPh payment acceptance. [CLM-015, CLM-022–CLM-025]

**Unknown.** Merchant onboarding, settlement evidence, dispute handling, reconciliation, support, and partner accountability are not public. [UNK-008–UNK-010]

## Principal maturity findings

### Highest-confidence observations

1. AllBank maintains multiple active public digital surfaces rather than a single isolated app.
2. It participates as sender/receiver across major retail-payment systems.
3. Its corporate channel publicly expresses authorization controls and business functions.
4. QR and partner distribution recur across several years of public evidence.
5. Public evidence is materially stronger for channel and network presence than for internal architecture or operating performance.

### Evidence gaps

The assessment cannot responsibly determine:

- digital adoption by segment;
- customer-journey quality;
- straight-through-processing rates;
- service availability and operational resilience;
- API and integration maturity;
- commonality across services;
- security effectiveness;
- reconciliation maturity;
- technology ownership and deployment model; or
- readiness for any proposed ceremony.

## Assessment conclusion

**Inferred.** AllBank demonstrates meaningful public digital breadth. The next analytical question is not whether digital channels exist. It is how the institution governs the complete banking responsibilities beneath those channels and whether one reusable operating capability could support them without disturbing authority, custody, settlement, or channel ownership.

That question requires institution-provided discovery. This assessment does not answer it through public-source inference.
