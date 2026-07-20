# Philippine Veterans Bank — Digital Capability and Technology Signals

## Scope

This note separates visible channels, disclosed initiatives, payment participation, and material technology Unknowns. It does not infer a production architecture from public signals.

## Facts

### Digital banking channels

- **Observed.** Retail Digital Banking launched in February 2025; institutional Digital Banking launched in June 2025. [CLM-016]
- **Observed.** Publicly described functions include balance and account viewing, bills payment, transfers within PVB, transfers to other banks, e-wallet cash-in, statements and transaction history, alerts, limits, and stop-payment requests. [CLM-014–CLM-015]
- **Observed.** PVB announced that checking-account statements would move to online delivery from 1 February 2026, with printed copies available on request. [CLM-038]
- **Observed.** Public terms describe both self-registration and branch-assisted enrollment and refer to identity validation, multi-factor authentication, credentials, limits, and compromise reporting. [CLM-015, CLM-036]

### Payment and channel participation

- **Observed.** PVB discloses BancNet, PESONet, InstaPay, Bills Pay PH, card, POS, kiosk, and payment-gateway capabilities. [CLM-017]
- **Observed.** ECPay and Paynamics are named in relation to the kiosk and payment-gateway services. [CLM-018]
- **Observed.** The annual report states that InstaPay Sender and Bills Pay PH P2B Receiving were implemented in 2025, with CEPALCO as the Bills Pay PH pilot biller. [SRC-004]

### Disclosed systems and initiatives

| Area | Observed signal | Evidence boundary |
| --- | --- | --- |
| Fraud | Fraud Management System capable of real-time detection was disclosed | Does not establish coverage, tuning, assurance, or incident performance [CLM-040] |
| AML | AML system integration, workflow, monitoring, and dashboard upgrades were disclosed | Does not establish control effectiveness or supervisory outcome [CLM-040] |
| Treasury | Guava Treasury Management System was disclosed across front, middle, and back office | Does not establish interfaces, reconciliation, data lineage, or resilience [CLM-040] |
| Data | Enterprise Data Office was established as a data-governance hub | Does not establish enterprise data architecture or quality [CLM-040] |
| File exchange | Secure File Transfer Services were implemented for clients | Does not establish API capability or end-to-end automation [CLM-040] |
| Cards | Instant card issuance was piloted in selected branches | Does not establish full rollout or operating performance [CLM-040] |
| Regulatory applications | Advanced EPFS and OPS-MAL application work was disclosed | Does not establish final approval [CLM-041] |

### Activity signals

- **Observed.** The 2025 annual report disclosed 32% growth in digital-channel gross revenue, 40% growth in total digital-channel transactions, and 13% growth in transactions by PVB clients. [SRC-004]
- **Unknown.** Absolute users, transaction counts and values, comparable definitions, fraud and dispute rates, channel uptime, success rates, and segment adoption were not disclosed in the cited section. [CLM-049]

## Technology signal register

| Domain | Observed | Inferred | Unknown |
| --- | --- | --- | --- |
| Customer channels | Retail and institutional web/mobile services launched | PVB is broadening service beyond branch access | Architecture, ownership, vendor, capacity, active adoption |
| Payments | Multiple rails and providers disclosed | PVB has integration experience across distinct payment surfaces | Settlement accounts, provider contracts, API behavior, exceptions, reversals |
| Security | Customer security terms, fraud system, AML upgrade | Formal attention to fraud and compliance is visible | Effectiveness, assurance, SOC, incident history, privileged access |
| Data | Enterprise Data Office disclosed | Data governance is an explicit transformation theme | Data domains, lineage, ownership, quality, retention, analytics controls |
| Treasury | Named end-to-end Treasury platform | Treasury modernization is a current operating initiative | Integration with core, GL, settlement, risk, and reporting systems |
| Integration | Secure file transfer and payment-provider connections | File and third-party integration experience exists | API management, eventing, sandbox, test data, certification, observability |
| Delivery | Multiple 2025 launches and pilots | PVB can deliver change under some conditions | DevOps model, CI/CD, release governance, environments, support ownership |
| Resilience | Public terms acknowledge maintenance and service interruption | Availability risk is recognized | RTO/RPO, backup, DR tests, capacity, vendor concentration, incident command |

## Architecture boundary

**Unknown.** Public evidence does not establish:

- core banking platform and version;
- channel platform ownership or tenancy;
- cloud, data-center, network, and hosting arrangements;
- source-code, credential, secret, and data ownership;
- CI/CD, environment, and production-approval model;
- API gateway, catalog, authentication, idempotency, or rate limits;
- event and file-processing architecture;
- monitoring, logging, evidence retention, and observability;
- backup, disaster recovery, business continuity, RTO, or RPO;
- settlement-account, prefunding, limit, and liquidity structures;
- status, reversal, exception, dispute, and reconciliation interfaces;
- service-provider contracting and concentration; or
- feasibility or readiness of an institution-specific execution driver. [CLM-046]

## Observed implications

- **Inferred.** PVB has visible channel and integration activity sufficient to justify later technical discovery. It is not sufficient to support a technical-fit conclusion. [CLM-040, CLM-045–CLM-046]
- **Inferred.** Institutional and public-sector channel launches increase the importance of governance, evidence, reconciliation, and recovery across participant classes. The public record does not show how these are implemented. [CLM-016, CLM-019–CLM-022, CLM-049]
- **Inferred.** Named systems suggest modernization across customer, control, Treasury, and data domains rather than a single front-end project. The integration burden among those domains remains Unknown. [CLM-040]

## Outstanding questions

1. What systems of record support deposits, loans, cards, customers, Treasury, GL, AML, fraud, and channels?
2. Which components are owned, licensed, outsourced, hosted, or operated by third parties?
3. What production integration methods exist for inquiries, debits, credits, transfers, status, reversals, and reconciliation?
4. What environments, test data, certification, release, and rollback practices govern changes?
5. What security, privacy, access, logging, incident, continuity, and recovery controls are evidenced?
6. What channel-level operating measures exist by user class and workflow?
7. What current regulatory approvals or restrictions apply to digital and payment services?
8. What would an institution-specific execution-driver discovery require, and who could authorize it?
