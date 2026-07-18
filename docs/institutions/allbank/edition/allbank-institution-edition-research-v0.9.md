# Thrift Bank Digital Banking Program

## AllBank Institution Edition

### Research Edition

Prepared from Publicly Available Information

Version 0.9

18 July 2026

---

## Publication Status

This publication has been prepared from publicly available information together with the canonical x-change editorial framework.

Observed facts are distinguished from bounded inferences and recommendations.

Where public evidence is insufficient, this publication identifies those areas transparently rather than substituting unsupported conclusions.

The purpose of this Research Edition is to facilitate executive discussion. It is expected to evolve into a Confirmed Edition following institutional engagement.

This is not an AllBank-approved publication, a commercial proposal, an implementation plan, or a statement that AllBank has selected or adopted the Program.

### Evidence classification

**Observed** — directly supported by an identified public source.

**Inferred** — a bounded interpretation of identified observations.

**Recommended** — a matter proposed for discussion or editorial treatment, not an AllBank intention.

**Unknown** — not established by the public evidence reviewed.

Claim identifiers refer to the governed [AllBank Evidence Register](../EVIDENCE_REGISTER.md). The complete public record appears in the [Public Source Register](../PUBLIC_SOURCE_REGISTER.md). The evidence cutoff is 18 July 2026.

---

## Foreword

An institution-specific publication should begin with the institution.

AllBank is not being approached as a generic thrift bank waiting to become digital. The public record describes a long-established regulated institution with deposits, loans, branches, mobile banking, electronic onboarding, corporate internet banking, merchant services, payroll functions, collection services, remittance relationships, and participation in major Philippine payment systems. [CLM-001–CLM-016, CLM-029–CLM-031]

Those observations establish a meaningful starting point. They do not disclose how AllBank organizes its internal operating responsibilities, which services matter most to management, how current integrations behave, or where the institution sees its next opportunity. [UNK-004–UNK-015]

This Research Edition therefore has a limited purpose. It brings the canonical Thrift Bank Digital Banking Program into AllBank's evidenced context so that management may confirm what is accurate, correct what is incomplete, and identify what deserves further examination.

The canonical Program Guide remains the source of doctrine. It holds that a bank brings its authority and settlement relationships; x-change brings a reusable operating grammar; and an institution-specific driver connects that grammar to the bank's approved systems. It also distinguishes a Program—the institutional initiative—from the Capability that may endure after the initiative has been completed.

This edition does not change those propositions. It tests their possible relevance against public evidence about AllBank. Where the evidence ends, the publication asks a question.

That boundary is intentional. Institutional dialogue should begin with a responsible account of what is known, not with the appearance of certainty.

---

## Executive Summary

AllBank already possesses the foundation of a modern thrift bank. It has banking authority, customer and deposit relationships, consumer and commercial products, physical and digital channels, and participation in InstaPay, PESONet, QR Ph P2P, QR Ph P2M, and Bills Pay PH. Its public services include payroll, corporate bulk sending, merchant acceptance, collections, housing finance, consumer lending, and remittance. [CLM-005–CLM-016, CLM-029–CLM-031]

The question raised by this Research Edition is therefore not whether AllBank should become digital. Public evidence shows that it already operates across digital and physical channels. [INF-001]

The question is whether one reusable, governed operating capability could help the institution organize additional banking services across those channels and relationships without diminishing AllBank's authority, control, or institutional identity.

Under the canonical Program, AllBank would remain the bank. It would continue to own its customer relationships, define its products, approve its policies, control its infrastructure and credentials, establish its settlement relationships, and decide when a banking service is operationally ready. Common operating software would not create a common bank. Settlement connectivity would not itself constitute a banking service.

The Program would be the initiative through which the institution evaluates and, if approved, establishes the Capability. That Capability would provide a consistent grammar for expressing the purpose of a banking service, the participants and conditions governing it, the resources available to it, the credential through which a customer may invoke it, and the evidence produced when the bank executes it.

Public evidence suggests several places where such an inquiry may be relevant. Payroll connects employers, employees, deposits, payments, and potentially other financial relationships. Merchant acceptance connects business onboarding, payment instructions, settlement, evidence, and reconciliation. Collections connect payer identity, reference information, matching, exceptions, and business reporting. Housing and SME banking may require governed releases against purpose and evidence. Remittance remains the canonical explanatory ceremony because it reveals the complete operating model through one familiar customer request. [CLM-009–CLM-016, CLM-029–CLM-031; INF-006]

None of these has been selected as an AllBank priority. Public product presence does not establish management intent, transaction volume, operating difficulty, economics, or readiness. [UNK-004–UNK-012, UNK-016]

The institutional possibility is broader than any one service. When a bank remains useful across recurring customer, employer, merchant, borrower, depositor, and business needs, those relationships may reinforce one another. The canonical Program describes this tendency as Transaction Gravity. Public evidence establishes that AllBank serves several of the relevant relationships. It does not establish that Transaction Gravity is already occurring, nor does it guarantee a commercial result. [CLM-006, CLM-008–CLM-016, CLM-029–CLM-031; INF-002]

An institution-specific integration would also be required. In canonical terms, that prospective driver is identified conceptually as `3neti/emi-allbank`. No production integration bearing that identity is known to exist. Any such driver would require institutional discovery, API mapping, implementation, certification, release governance, and continuing maintenance. Certification would demonstrate defined technical behavior; it would not decide whether AllBank is operationally ready.

The immediate decision is therefore not an implementation decision. It is whether the following questions merit structured executive discussion:

- Which banking relationships matter most to AllBank's strategy?
- Which existing service would best reveal the value—or limits—of a reusable operating capability?
- How are authority, settlement, evidence, exceptions, reconciliation, and customer responsibility governed today?
- What institution-specific integration would be feasible within AllBank's approved architecture?
- What evidence would management and the Board require before any controlled production activity?

This Research Edition offers a disciplined starting point for that conversation. It is designed to be corrected. A Confirmed Edition should be prepared only after AllBank has supplied or validated the institutional evidence required to replace public inference with institutional understanding.

---

# Chapter 1 — Understanding AllBank

## An established thrift-bank institution

**Observed.** AllBank's institutional history extends to 1961, when the institution was registered as a domestic thrift bank. BSP authorization and commercial operations followed in 1963. The bank later changed its name from Optimum Development Bank, Inc. to AllBank (A Thrift Bank), Inc., with recorded approvals in 2017, and became the surviving entity in a 2019 merger with Rural Bank of Plaridel, Inc. [CLM-001–CLM-004]

PDIC listed AllBank as an insured thrift bank with its head office in Mandaluyong in October 2025. [CLM-005]

These facts matter because the institution-specific inquiry begins from existing banking authority and history. The Program would not create a bank, confer authority, or replace the governance through which AllBank exercises its responsibilities.

## The public customer proposition

**Observed.** AllBank publicly describes its focus as specialized financing and banking services for working-class Filipinos, business owners, corporations, micro, small, and medium enterprises, and entrepreneurs. [CLM-006]

Its published deposit products include savings, checking, payroll, time, and foreign-currency accounts. Published lending products include salary, auto, housing, and commercial loans. Public business services include payroll, corporate bulk sending, PDC warehousing, deposit pick-up, night depository, POS acquiring, and corporate internet banking. [CLM-008–CLM-010]

**Inferred.** The public proposition spans household finance and business transaction services. It presents AllBank as an institution serving more than a single product, segment, or transaction type. [INF-002]

**Unknown.** The public record does not establish the current customer mix, product profitability, active-account counts, deposit concentration, portfolio priority, or which published services remain strategic in 2026. [UNK-003–UNK-005, UNK-011–UNK-012, UNK-016]

## Physical and digital presence

**Observed.** AllBank's 2023 annual report named 16 branches across Metro Manila and selected Luzon provinces. Current branch and ATM counts are not established. [CLM-007, UNK-002]

The institution also maintains mobile-banking applications, a public electronic onboarding journey, the AllConnect corporate internet-banking service, and a merchant portal. Public AllConnect materials describe maker and authorizer controls and functions that include account inquiry, transfers, payroll, bulk sending, account sweeping, bills payment, loan viewing, and checkbook re-order. [CLM-011–CLM-015]

**Inferred.** AllBank presents as a multichannel institution rather than a branch-only or digital-only bank. Its public footprint suggests a hybrid physical-digital service model concentrated in Metro Manila and Luzon. [INF-001, INF-007]

This is a description of visible channels, not a maturity judgment. Public presence does not reveal active use, reliability, customer completion, operational effort, or whether service responsibilities are organized consistently beneath those channels. [UNK-004, UNK-006, UNK-009–UNK-010]

## Public financial context

**Observed.** BSP reported AllBank total assets of ₱9.903 billion, deposit liabilities of ₱7.366 billion, and net loans and receivables of ₱2.679 billion as of 31 March 2026. BSP reported a 29.14 percent return on equity for the year ended 31 December 2025. [CLM-017–CLM-020]

These are point-in-time or period measures from published regulatory tables. They establish institutional scale and selected balance-sheet facts. They do not establish causation, future performance, strategic priorities, liquidity policy, or the economics of any candidate banking ceremony.

**Unknown.** Current CASA composition, deposit concentration, loan mix, non-performing-loan measures, capital measures, revenue mix, and service-level economics require institution-provided evidence. [UNK-003, UNK-012]

## Public strategic signals

**Observed.** Public records describe multiple payment and QR partnerships, including relationships announced with UMI Technologies, Dragonpay, PearlPay, JustPayTo, Salmon, SAFC, and Manny Pay. The 2023 annual report framed digital partnerships as a means of extending customer and merchant reach. [CLM-022–CLM-025]

**Inferred.** Partnership-led extension of payment reach is a recurring public pattern. [INF-003]

That pattern does not show the scale, status, economics, technical architecture, or strategic importance of each relationship. It does, however, support a serious inquiry into how AllBank governs services that span its own channels, external partners, payment rails, merchants, businesses, and customers.

## What remains to be understood

The public record establishes a regulated, multichannel thrift bank with visible breadth. It leaves the most important institution-specific questions open:

- Which relationships does management intend to deepen?
- Which services are growing, stable, being redesigned, or no longer central?
- Where does repeated operating work occur across products and partners?
- Which responsibilities are owned by business, Operations, Treasury, Technology, Risk, Compliance, and service providers?
- What would AllBank regard as a meaningful institutional outcome?

These are not omissions to be covered with generic prose. They are the beginning of the executive discussion.

---

# Chapter 2 — Current Digital Banking Position

## Digital capability is already visible

**Observed.** AllBank has public retail and corporate digital surfaces. Its mobile applications were updated in August 2025. Its public e-KYC journey offers several account-opening choices. AllConnect supports corporate access and published maker-authorizer controls. A P2M merchant portal and QRPh merchant service are also visible. [CLM-011–CLM-015]

**Observed.** BSP participant lists dated 31 March 2026 identify AllBank as a sender and receiver for InstaPay, PESONet, QR Ph P2P, QR Ph P2M, and Bills Pay PH. [CLM-016]

These observations answer one question clearly: this is not an institution with no digital capability or payment connectivity.

They leave another question unanswered: whether the bank has one reusable operating model beneath those channels and connections.

## Internet and corporate banking

**Observed.** AllConnect is a live corporate internet-banking surface. Published materials describe inquiry, transfer, payroll, bulk-send, sweeping, bills-payment, loan-viewing, and checkbook functions, with maker and authorizer controls. [CLM-013–CLM-014]

This shows that AllBank already recognizes institutional authorization and corporate operating needs. It does not establish how those functions are implemented, how service-specific policies are expressed, how exceptions are handled, or whether the same operating grammar is reused outside AllConnect.

## Mobile banking and onboarding

**Observed.** Public app-store listings confirm AllBank Mobile on iOS and Android. The public e-KYC journey shows account-opening choices, while one virtual-card option was marked as forthcoming when accessed. [CLM-011–CLM-012]

**Unknown.** Active users, successful onboarding, abandonment, response times, support events, and the distribution of customer activity across mobile and branch channels are not public. [UNK-004, UNK-009–UNK-010]

A channel can be visible without disclosing the institutional work beneath it. A Research Edition should not convert an interface into an assumption about the complete banking service.

## Payments and settlement connectivity

**Observed.** AllBank's participation across five BSP-listed payment arrangements establishes significant payment connectivity. [CLM-016]

**Inferred.** This connectivity creates a plausible foundation on which governed banking ceremonies may operate. It does not establish a reusable operating grammar, an institution-specific driver, or readiness for any new service. [INF-004]

Settlement connectivity and banking service must remain separate ideas. A rail can carry an instruction. The bank must still define the service, authorize the participants and conditions, govern funds and credentials, handle uncertain outcomes, reconcile activity, produce evidence, and remain accountable to the customer.

**Unknown.** The public record does not identify AllBank's settlement accounts, service providers, credentials, limits, release controls, attribution rules, internal ledgers, exception ownership, or reconciliation responsibilities. [UNK-008, UNK-014]

## Merchant, payroll, and collection services

**Observed.** Public materials describe QRPh P2M merchant acceptance and real-time merchant crediting. Corporate materials include payroll and bulk sending. The product set includes PDC warehousing, deposit pick-up, bills payment, and night depository services relevant to business collections and cash management. [CLM-010, CLM-014–CLM-015, CLM-030–CLM-031]

These are distinct banking services, but they share institutional concerns: customer authority, purpose, approved participants, funding, execution, evidence, exceptions, reconciliation, and support.

**Inferred.** There may be repeated work across these services. Public evidence does not establish its extent, cost, or whether AllBank already operates a common orchestration layer.

## Technology signals and limits

**Observed.** Historical public disclosures include adoption of ISO 20022 and an API reference for corporate bulk sending. AllConnect security guidance describes controls including encryption, firewalls, intrusion detection, backup, endpoint security, authentication, and transaction notifications. [CLM-010, CLM-026–CLM-027]

These are useful signals. They are not a current architecture inventory, API contract, independent security assurance, or integration-readiness assessment.

**Unknown.** Core banking, cloud, payment integration, identity, fraud, security, observability, API behavior, testing environments, recovery evidence, and change-control arrangements require direct institutional discovery. [UNK-006–UNK-007, UNK-015]

## Position at the beginning of discussion

**Inferred.** AllBank appears digitally established but operationally undisclosed. The public record is strong enough to show channels, products, rails, and partnerships. It is not strong enough to determine whether a reusable governed capability would solve a material institutional problem.

The appropriate response is not to assume a gap. It is to test for one.

---

# Chapter 3 — Where the Canonical Program Aligns

## The Program and the Capability

The canonical Program is an institutional initiative. Its intended result is a reusable governed operating Capability.

That distinction is important for AllBank. The Program would be bounded work undertaken through AllBank's governance. The Capability, if approved and established, would remain available beneath approved channels to support more than one banking service.

The Program would not turn x-change into a bank, a payment switch, a settlement provider, or a customer channel. AllBank would continue to bring the authority and the rails. x-change would bring the operating grammar. A bank-specific driver would connect them.

## Alignment with what AllBank already possesses

**Observed.** AllBank already has the institutional assets from which the canonical model begins:

- banking authority and insured-bank status; [CLM-005]
- customer and deposit relationships; [CLM-006, CLM-008, CLM-018]
- lending and transaction services; [CLM-009–CLM-010]
- branch, mobile, onboarding, corporate, and merchant channels; [CLM-007, CLM-011–CLM-015]
- payment-network participation; [CLM-016]
- employer, merchant, business, household, and partner touchpoints. [CLM-006, CLM-010, CLM-015, CLM-022–CLM-025, CLM-029–CLM-031]

The potential alignment is therefore not based on replacing absent infrastructure. It is based on asking whether these institutional assets could be made more reusable across banking responsibilities.

## Consumer banking

**Observed.** AllBank publicly offers deposits, salary loans, auto loans, housing loans, mobile banking, electronic onboarding, transfers, bills payment, and remittance. [CLM-008–CLM-009, CLM-011–CLM-012, CLM-014, CLM-016, CLM-029]

**Inferred.** These services create multiple points at which a customer may ask the bank to arrange a governed financial outcome.

**Recommended.** Executive discussion should examine whether the operating work behind those outcomes is currently service-specific or whether selected responsibilities could be expressed through one common grammar.

The recommendation concerns discovery, not product redesign.

## Merchant services

**Observed.** AllBank has public evidence of merchant acceptance, QR Ph P2M participation, a merchant portal, and partnerships intended to extend payment reach. [CLM-015–CLM-016, CLM-022–CLM-025]

The canonical model may be relevant where merchant onboarding, payment purpose, settlement, evidence, notification, exceptions, and reconciliation must be governed as one banking responsibility.

**Unknown.** Current merchant counts, volumes, onboarding policy, settlement practice, dispute handling, pricing, partner roles, and strategic priority are not established. [UNK-002, UNK-004, UNK-009–UNK-012]

## Payroll

**Observed.** Payroll appears in AllBank's public deposit and corporate-service materials. AllConnect materials include payroll and bulk-send functions. [CLM-008, CLM-010, CLM-014, CLM-030]

Payroll is a strong candidate for executive examination because it can connect an employer's instruction, bank-held funding, employee credits, evidence, exceptions, and reconciliation through a recurring ceremony.

**Unknown.** Public sources do not establish client count, scale, funding method, cut-offs, exception rates, account-opening relationships, lending linkage, or management priority.

## Housing and SME banking

**Observed.** AllBank publicly offers housing and commercial lending and identifies MSMEs and entrepreneurs among its intended constituencies. [CLM-006, CLM-009]

The canonical grammar may be relevant when an approved lending responsibility requires releases to defined payees against evidence and conditions. That is a conceptual alignment. It is not a description of AllBank's current housing or commercial-loan process.

**Unknown.** Portfolio scale, release stages, documentary controls, approved payees, servicing model, and strategic priority are not public. [UNK-003, UNK-005, UNK-010–UNK-011]

## Collections and business cash management

**Observed.** Corporate bulk sending, account sweeping, bills payment, PDC warehousing, deposit pick-up, and night depository services are visible in AllBank's public materials. [CLM-010, CLM-014, CLM-031]

Collections become institutionally significant when the bank must do more than receive value. It must identify the payer, attribute the payment, apply reference rules, resolve unmatched activity, report to the business customer, and preserve evidence.

**Recommended.** Management should test whether collection workflows provide a useful example of banking capability exceeding payment connectivity.

## Where alignment is not yet established

The public record does not establish:

- that AllBank experiences material duplication across services;
- that a common operating layer is absent;
- that approved APIs can support the canonical model;
- that a particular ceremony has executive priority;
- that an institution-specific driver is feasible;
- that a business case exists; or
- that the institution is ready for implementation.

These are decisive matters. The Research Edition does not answer them on AllBank's behalf.

---

# Chapter 4 — Potential Banking Ceremonies

## Why begin with a ceremony

A banking ceremony is the complete, observable sequence through which a customer asks the bank to arrange an outcome and the bank assumes responsibility for doing so.

The ceremony is useful because it keeps the institution—not the software—at the center of the discussion. It allows management to examine purpose, authority, funding, evidence, execution, exception handling, reconciliation, and customer responsibility through one bounded service.

The candidates below arise from public evidence. None is prescribed.

## Payroll

**Observed.** AllBank publicly lists payroll services, payroll accounts, corporate bulk sending, and corporate maker-authorizer controls. [CLM-008, CLM-010, CLM-014, CLM-030]

**Inferred.** Payroll could reveal how a recurring employer instruction becomes multiple governed employee outcomes while preserving funding controls, release authority, status, exceptions, and reconciliation.

**Recommended.** Management should consider payroll as a possible lead ceremony if it is strategically important, operationally familiar, sufficiently bounded, and supported by evidence.

Questions include who funds the activity, who authorizes release, how employee eligibility is established, what cut-offs apply, and how incomplete or rejected credits are resolved.

## Merchant payments

**Observed.** AllBank publicly supports QRPh merchant acceptance and is listed for QR Ph P2M participation. Public partnerships also show recurring attention to merchant and payment reach. [CLM-015–CLM-016, CLM-022–CLM-025]

**Inferred.** Merchant payments could demonstrate how onboarding, merchant authority, payer instruction, settlement, evidence, notification, disputes, and reconciliation come together as a banking service.

**Recommended.** This ceremony should be evaluated if management wishes to examine recurring merchant and consumer relationships rather than a single payment transaction.

Public evidence does not establish AllBank's current merchant journey, economics, service levels, or partner responsibilities.

## Collections

**Observed.** AllBank publishes services relevant to recurring business collections and cash management. [CLM-010, CLM-014, CLM-031]

**Inferred.** Collections could demonstrate that receipt of funds is only one part of the banking outcome. Payer identity, reference information, matching, exception handling, client reporting, and reconciliation may be equally important.

**Recommended.** Management should examine collections where current business customers experience material reconciliation or evidence requirements.

The existence, extent, and cost of any such difficulty remain Unknown.

## Housing-related release

**Observed.** Housing loans appear in AllBank's published lending portfolio. [CLM-009]

**Inferred.** A housing-related ceremony could illustrate governed release to a seller, developer, contractor, or other approved payee after defined documentary or institutional conditions have been met.

This treatment is conceptual. It does not describe AllBank's lending policy, approved release process, portfolio emphasis, or current systems.

**Recommended.** Housing should be considered only if management confirms its strategic relevance and identifies a bounded release ceremony suitable for discussion.

## Customer-directed settlement

Customer-directed settlement is a general category in which a customer asks the bank to apply available resources toward a permitted outcome under the bank's policy.

**Observed.** AllBank offers transfers, bills payment, corporate bulk sending, merchant payments, and payment-network connectivity that may contain customer-directed instructions. [CLM-010, CLM-014–CLM-016]

**Inferred.** A carefully selected example could help distinguish the customer-facing request, the banking service, the credential used to invoke it, and the settlement rail used to execute it.

**Unknown.** The public record does not establish a single AllBank service that should bear this label, nor the authority, funding, evidence, settlement, and exception rules that would govern it.

**Recommended.** Use this category only after management selects a specific existing banking responsibility. It should not become an abstract substitute for a real customer journey.

## Remittance

**Observed.** AllBank's 2023 public product list included Western Union remittance delivered with identified partners. Current service availability and operating practice require confirmation. [CLM-029, UNK-016]

Remittance remains the canonical explanatory ceremony because the customer request is familiar: the customer wants value made available to an intended recipient. The customer does not ask for an API, a rail, or an orchestration layer. The customer asks the bank to arrange an outcome.

The ceremony exposes the complete operating grammar without making the architecture the subject. Funding must be recognized. The permitted service and participants must be established. Conditions and evidence must be satisfied. A credential may allow the intended recipient to invoke the outcome. The bank remains responsible for execution, exceptions, and evidence.

**Recommended.** Retain remittance as the explanatory default unless AllBank management confirms that payroll, merchant payments, collections, housing, or another service would better represent the institution's current priorities. [REC-002]

This recommendation concerns the narrative. It does not recommend remittance as the first production service.

## Selecting the right ceremony

The strongest ceremony is not necessarily the newest or largest. It is the one that makes institutional responsibility visible within a bounded scope.

Management would need to consider:

- strategic importance;
- customer and institutional relevance;
- familiarity of the underlying banking service;
- clarity of authority and funding;
- availability of evidence;
- manageable exceptions;
- integration feasibility; and
- the institution's ability to judge readiness.

Until that evidence is available, the Research Edition preserves the candidates without selecting among them.

---

# Chapter 5 — Potential Transaction Gravity

## The observed relationships

**Observed.** AllBank's public services touch depositors, borrowers, employers, employees, corporate account holders, merchants, billers, remittance users, and payment partners. [CLM-006, CLM-008–CLM-016, CLM-022–CLM-025, CLM-029–CLM-031]

These relationships are more consequential than isolated transactions. An employer may need payroll and cash management. An employee may receive salary, hold deposits, transfer funds, pay bills, remit value, or later borrow. A merchant may accept payments, manage collections, maintain deposits, pay suppliers, or seek financing. A housing borrower may require disbursement, payment, account, and servicing relationships over many years.

The public record establishes that AllBank offers services relevant to those patterns. It does not establish that individual customers use them together.

## The bounded inference

**Inferred.** When the institution remains useful across more of a customer's or business's recurring financial needs, activity may be more likely to return to the institution. Employer, merchant, collection, remittance, deposit, and lending relationships may therefore reinforce one another. [INF-002, INF-006]

The canonical Program calls this tendency **Transaction Gravity**.

Transaction Gravity is not a claim that transactions automatically create deposits, loyalty, lending demand, or profitability. It is a way of asking whether repeated institutional usefulness gives customers and enterprises more reasons to continue a banking relationship.

## The possible institutional significance

A reusable operating capability may matter because it could allow the bank to introduce additional governed services without rebuilding every operating foundation independently. If that proved true in AllBank's environment, adaptability—not a single feature—would be the institutional result.

The relevance could appear in several relationship paths:

**Employer to employee.** Payroll may connect employer operating needs with employee accounts and continuing retail-bank usefulness.

**Merchant to business banking.** Payment acceptance may connect transaction activity with settlement, reporting, deposits, cash management, and financing relationships.

**Collections to institutional deposits.** Better attribution and reconciliation may make the bank more useful to corporate customers managing recurring receivables.

**Remittance sender to recipient.** A familiar transfer outcome may introduce or reinforce a relationship with one or both parties.

**Borrower to long-term service.** Housing or business finance may create recurring needs for release, payment, evidence, deposits, and servicing.

These are possible relationship patterns, not observations about AllBank customer behavior.

## What must be measured

**Unknown.** Public evidence does not reveal active customer counts, recurring balances, cross-service use, employer activity, merchant activity, retention, transaction completion, acquisition cost, unit economics, or relationship profitability. [UNK-004, UNK-009, UNK-012]

Without those measures, Transaction Gravity remains an analytical possibility.

**Recommended.** If management considers the concept relevant, discovery should begin with relationship evidence rather than transaction volume alone. Useful questions may include:

- Do payroll relationships lead to durable employee deposits or wider service use?
- Do merchant and collection relationships deepen operating balances or business engagement?
- Which services cause customers to return, and which remain isolated transactions?
- What evidence distinguishes customer usefulness from mere throughput?
- What operating cost is incurred each time a new service is added or changed?

The purpose is not to prove the thesis in advance. It is to determine whether the institution sees the same pattern in its own evidence.

## Institutional strength before commercial conclusion

The first question is whether one governed capability could make AllBank more adaptable while preserving its authority and control. The second is whether that adaptability improves service, evidence, operating consistency, or relationship depth. Only then can a commercial case be assessed.

The Research Edition does not contain that business case. Public information cannot establish it.

---

# Chapter 6 — Institution-Specific Driver

## A conceptual integration boundary

The canonical Program describes the institution-specific integration conceptually as:

```text
3neti/emi-allbank
```

This is a prospective identifier for discussion. No production integration bearing this identity is known to exist. The notation does not assert that AllBank has approved x-change, exposed suitable APIs, selected a technology design, or begun implementation.

## What the driver would do

In canonical architecture, the driver connects the common operating grammar to the bank's approved systems and settlement relationships.

The bank brings the authority and the rails. x-change brings the operating grammar. The bank-specific driver connects them.

That connection is not a generic adapter installed without institutional work. It must respect the bank's actual interfaces, credentials, status models, limits, evidence, failure behavior, security requirements, release controls, and reconciliation arrangements.

The driver would not provide banking authority or settlement access. It would not own the customer relationship, hold customer funds, decide product policy, or determine readiness.

## Required development sequence

Any `3neti/emi-allbank` driver would require:

```text
Institutional discovery
        ↓
API mapping
        ↓
Implementation
        ↓
Certification
        ↓
Continuing maintenance
```

### Institutional discovery

AllBank and the relevant providers would need to identify the approved systems, owners, interfaces, credentials, settlement arrangements, control boundaries, evidence, exceptions, reconciliation, and support responsibilities relevant to a selected ceremony.

### API mapping

The institution would need to establish what interfaces actually exist and how they behave. Relevant matters may include authentication, certificates, signatures, idempotency, instruction submission, balances, status, webhooks, time-outs, errors, reversals, limits, transaction history, and reconciliation evidence.

### Implementation

Only after mapping could the driver be implemented against approved contracts and environments. Implementation would translate canonical execution responsibilities into institution-specific calls and responses without redefining the banking service.

### Certification

Certification would test the driver's defined technical behavior, including predictable outcomes under expected success, failure, duplicate, delayed, partial, and uncertain conditions.

Driver certification would not establish operational readiness.

### Continuing maintenance

Interfaces, certificates, security requirements, provider behavior, limits, and versioned contracts change. The driver would require governed release, monitoring, regression testing, incident response, and continuing maintenance throughout its useful life.

## What public evidence establishes

**Observed.** Public materials refer to corporate bulk sending via API, and BSP records establish payment-system participation. [CLM-010, CLM-016]

**Unknown.** The public record does not identify the relevant API catalog, owners, access authority, authentication, idempotency, webhook behavior, status and error models, testing environments, versioning, settlement evidence, or reconciliation design. [UNK-006–UNK-008]

**Recommended.** Treat existing rail participation as an institutional asset while keeping driver feasibility entirely subject to discovery. [REC-003]

## Readiness remains an institutional judgment

A technically certified driver is one part of a complete banking service. AllBank would still need to determine whether product policy, customer journeys, operating procedures, Treasury, settlement, risk, compliance, security, support, recovery, evidence, and governance are ready for controlled production.

That decision belongs to the institution.

The Research Edition does not make it.

---

# Chapter 7 — Questions for Executive Discussion

The purpose of executive discussion is not to defend the Research Edition. It is to replace incomplete public understanding with institution-provided evidence.

The questions below are an agenda, not a questionnaire to be answered at once. Each answer should record its provider, authority, date, approval status, permitted use, distribution restrictions, and supporting evidence.

## Strategy

1. What are AllBank's most important institutional priorities for the next three years?
2. How does management rank deposit growth, consumer lending, housing, SME and corporate banking, payroll, merchant services, collections, remittance, and partner distribution?
3. Which customer, employer, merchant, borrower, depositor, and business relationships matter most?
4. Which services are being expanded, maintained, redesigned, limited, or retired?
5. What institutional outcome would justify examining one reusable governed operating capability?

## Operations

6. Who is accountable for the complete banking outcome in each candidate ceremony?
7. Where do initiation, approval, evidence, notification, exception handling, reconciliation, and support differ across services?
8. Where do customers leave a digital journey and require branch or operations assistance?
9. Which repeated operating work creates delay, risk, inconsistency, or cost?
10. What failure, duplicate, reversal, delay, partial-result, and uncertain-outcome procedures are already governed?

## Treasury

11. How does Treasury recognize resources available to a service, reservations, releases, returns, and uncertain outcomes?
12. Which external events would constitute Funding Events for the candidate ceremony?
13. What operational and financial evidence must remain aligned throughout execution?
14. Who controls liquidity, release authority, limits, and end-of-day reconciliation?

## Technology

15. Which core-banking, payment, integration, identity, fraud, channel, and reconciliation systems support the candidate services?
16. Which environments and systems are owned or controlled by AllBank, and which are provider-managed?
17. What approved APIs exist for validation, instruction, status, balance, history, reversal, and reconciliation?
18. Who owns API change control, test environments, certification, production release, observability, and maintenance?
19. Does AllBank already use a common orchestration or workflow layer across services?

## Settlement

20. Which accounts, ACH arrangements, service-provider relationships, credentials, limits, and internal ledgers support the candidate ceremonies?
21. How are instructions attributed to the correct customer, employer, merchant, service, and partner?
22. Who owns settlement confirmation, exceptions, returns, uncertain outcomes, and reconciliation?
23. Which settlement responsibilities must remain bank-controlled, and which may be performed by approved providers?

## Products

24. Which existing service best combines strategic importance, bounded scope, operating familiarity, and readiness to learn?
25. Should remittance remain the explanatory ceremony, or would payroll, merchant payments, collections, housing, or another service better represent AllBank?
26. What policy, participants, funding, conditions, evidence, exceptions, and customer responsibilities define that service?
27. Which product measures demonstrate institutional usefulness rather than transaction volume alone?

## Governance

28. Which Board and management authorities would approve discovery, implementation, controlled production, and wider use?
29. What evidence must Operations, Treasury, Technology, Risk, Compliance, Information Security, Internal Audit, and business owners review?
30. Who decides that the complete service—not only the driver or rail—is operationally ready?
31. What would cause management to proceed, correct, extend, or pause a bounded pilot?

## Customer experience

32. What outcome does the customer believe the bank has agreed to arrange?
33. Which channel should initiate the service, communicate conditions, and present evidence?
34. How should the bank communicate when an outcome is delayed, rejected, duplicated, reversed, or uncertain?
35. Which completion, turnaround, complaint, dispute, abandonment, and satisfaction measures matter?
36. How should the customer experience be defined as part of the banking service rather than as a separate design exercise?

## From discussion to evidence

An answer should not automatically become publication fact. It must first be classified as institution-provided evidence, checked for authority and permitted use, and reconciled with the existing evidence register.

If an answer remains unavailable, the matter remains Unknown.

---

# Conclusion

Based on publicly available information, AllBank appears to possess many of the institutional assets from which a reusable governed operating capability could be examined: banking authority, deposit and customer relationships, physical and digital channels, broad payment participation, business services, consumer products, and visible employer, merchant, collection, lending, remittance, and partner relationships.

That evidence supports an inquiry. It does not support an implementation conclusion.

The public record cannot establish AllBank's current strategic priorities, internal architecture, approved APIs, settlement operating model, cross-service duplication, service economics, customer behavior, driver feasibility, or readiness. Those are institution-specific matters. They should be learned from the institution.

The next step is therefore not immediate implementation.

It is institutional dialogue.

Through that dialogue, observations may be confirmed, inaccuracies corrected, inferences tested, and priorities understood. A suitable banking ceremony may then be selected. The responsibilities of the institution, its providers, its settlement relationships, and any prospective driver may be mapped with evidence.

Only after that work should a Confirmed Edition be prepared.

The standard is simple: where this Research Edition knows, it records. Where it infers, it qualifies. Where it does not know, it asks.

That is how an institution-specific engagement should begin.

---

## Research Record

- Institution Intelligence: [AllBank Institution Intelligence Report](../INSTITUTION_INTELLIGENCE_REPORT.md)
- Source record: [Public Source Register](../PUBLIC_SOURCE_REGISTER.md)
- Claim record: [Evidence Register](../EVIDENCE_REGISTER.md)
- Digital maturity: [Digital Maturity Assessment](../DIGITAL_MATURITY_ASSESSMENT.md)
- Institutional analysis: [Strategic Gap Analysis](../STRATEGIC_GAP_ANALYSIS.md)
- Editorial adaptation: [Editorial Mapping](../EDITORIAL_MAPPING.md)
- Discovery agenda: [Questions for Management](../QUESTIONS_FOR_MANAGEMENT.md)
- Edition authority and lifecycle: [Edition Relationship](EDITION_RELATIONSHIP.md)
