# Thrift Bank Digital Banking Program Guide

## AllBank Edition

### Executive Edition

Version 1.0

## Foreword

AllBank has served the Philippine market in different institutional forms for more than six decades. Today, it operates as a thrift bank with visible relationships across working households, employers, entrepreneurs, merchants, corporations, and small and medium-sized enterprises.

Its banking proposition already extends across deposits, consumer and commercial lending, payroll, corporate banking, merchant acceptance, collections, remittance, housing finance, mobile banking, online account opening, and corporate Internet banking. AllBank also participates in the country's principal retail-payment arrangements.

This is therefore not a guide to becoming digital for the first time.

It is a guide to a different institutional question: whether AllBank should establish one reusable governed operating Capability beneath its existing channels, products, payment connectivity, and customer relationships so that additional banking services may be introduced without rebuilding their operating foundations independently.

The Program does not replace AllBank's authority, channels, systems, providers, or settlement relationships. It begins with them. AllBank remains the bank, the customer institution, and the production authority throughout.

This Executive Edition applies the canonical Thrift Bank Digital Banking Program Guide to AllBank's institutional context. It supports an executive conversation about one enduring operating Capability. It is not a deployment proposal, a statement of AllBank approval, or a conclusion about operational readiness.

## Executive Summary

AllBank has already established substantial digital banking capability. Its services span retail and corporate banking, digital onboarding, mobile access, payroll, bulk payments, merchant acceptance, collections, remittance, housing, and other lending relationships. It participates in InstaPay, PESONet, QR Ph, and Bills Pay PH and has repeatedly extended payment reach through institutional partnerships.

The question is not whether AllBank should become digital. It is whether the institution can organize more of its banking responsibilities through one reusable governed operating foundation.

Settlement connectivity is necessary, but it is not a banking service. A rail can move funds and an API can transmit an instruction. Neither defines what the customer requested, establishes purpose, applies policy, recognizes and reserves resources, gathers evidence, manages exceptions, communicates status, or reconciles the completed service. Those remain responsibilities of the bank.

The **Program** is the institution-specific initiative through which AllBank would evaluate and, if approved, establish that foundation. The enduring result is the **Capability**: a maintained operating foundation through which customer requests become authorized, observable, executable, and reconcilable banking activity.

AllBank remains the protagonist. It retains its banking authority, products, customer and deposit relationships, channels, infrastructure, data, policies, credentials, production authority, and settlement relationships. x-change supplies the operating grammar beneath those arrangements. `emi-core` provides the common execution contract, and an AllBank-specific driver—represented conceptually as `3neti/emi-allbank`—would map that contract to the institution's approved API behavior.

The bank brings the authority and the rails. x-change brings the operating grammar. The bank-specific driver connects them.

The driver is institution-specific engineering, not an automatically available connector. It would require institutional discovery, API mapping, implementation, certification, and continuing maintenance. Certification would establish technical behavior under tested conditions. It would not establish operational readiness. Readiness would remain an AllBank judgment based on the complete banking ceremony.

Remittance makes the model visible. A customer asks the bank to make funds available to another person. The bank recognizes the funds, applies policy, reserves the required capacity, defines the conditions, issues a Pay Code credential, coordinates execution through its approved settlement relationship, preserves evidence, and reconciles the result.

The customer requested a banking outcome. The bank arranged it.

The same Capability could support services already relevant to AllBank. Payroll connects employers and employees. Merchant services connect commerce, settlement, reporting, and business relationships. Collections connect payer information with attribution and reconciliation. Housing and commercial lending may require governed releases against purpose and evidence. Their commercial meaning, participants, policies, and customer journeys differ. The operating grammar remains stable.

The priority among these services, and the operating model supporting them, can be determined only with AllBank. That is the purpose of institutional dialogue.

The appropriate next step is therefore not immediate implementation. It is a structured executive discussion about whether one governed Capability merits formal evaluation, which banking ceremony would best demonstrate it, and what evidence AllBank would require before considering controlled production.

## Section 1 — Why This Program?

> **Executive question:** Why should AllBank examine this Program?

> **Key message:** AllBank already has authority, relationships, channels, digital services, and payment connectivity. The opportunity is to determine whether one governed operating foundation could support more banking services over time.

> **Executive decision:** I understand the institutional question and can decide whether a reusable governed operating Capability merits formal evaluation.

AllBank's history, customer relationships, and regulated authority are institutional assets. Modernization should strengthen them rather than replace them.

The institution already serves consumer and business needs through branches, mobile banking, digital onboarding, AllConnect corporate Internet banking, merchant services, payment participation, and partner relationships. Its visible services include payroll, bulk sending, collections, merchant acceptance, remittance, housing, and commercial lending.

A bank can accumulate functioning channels and integrations without acquiring one reusable operating foundation beneath them. Each new service may bring a different financial-state model, approval process, provider integration, evidence requirement, exception path, and reconciliation practice.

That pattern creates repeated work. It can also make institutional responsibility harder to observe across products and channels. A customer sees a payroll credit, merchant payment, collection reference, transfer, remittance, or loan release. AllBank must see the complete obligation: purpose, authority, funds, conditions, evidence, execution, exceptions, support, and reconciliation.

The Program addresses that operating question. It does not confer banking authority, create customer relationships, or supply settlement access. It organizes authority and connectivity that AllBank already possesses or establishes through approved relationships.

The timing is practical. Maintained software, modern deployment practices, API-based integration, automated testing, observability, and regulated payment infrastructure now allow an institution to establish a reusable foundation without rebuilding every component for every service.

The opportunity is not technology for its own sake. It is to preserve AllBank's institutional choice while reducing repeated operating and engineering work.

One foundation would not make every AllBank service alike. It would give the bank a consistent way to govern their differences. The next question is what AllBank would establish through the Program.

## Section 2 — What Is the Program?

> **Executive question:** What exactly would AllBank be invited to establish?

> **Key message:** The Program is an AllBank-specific modernization initiative. Its intended result is a maintained operating Capability under AllBank's authority and control.

> **Executive decision:** I understand the Program, the Capability it is intended to establish, the participating roles, and the boundaries that remain subject to AllBank approval.

The Thrift Bank Digital Banking Program brings together licensed x-change software, institution-specific integration, controlled deployment, observability, testing, documentation, maintenance, and operating governance. The resulting Capability coordinates the progression from recognized funds and authorized purpose to conditions, credential, execution, evidence, and reconciliation.

The Program is the initiative. The Capability is the enduring operational result. The terms are not interchangeable. The Program can be evaluated, approved, governed, implemented, and reviewed. The Capability is what AllBank would continue to operate and evolve.

AllBank would be the program sponsor and banking authority. Its Board and Management would establish purpose, risk appetite, scope, accountability, and approval boundaries. Business, Operations, Treasury, Technology, Risk, Compliance, Legal, Information Security, Internal Audit, Finance, and other responsible functions would continue to perform their established roles.

Open Disbursement Technologies, Inc. (ODTI) licenses and maintains x-change, `emi-core`, supported components, documentation, reference architecture, testing capability, and an institution-specific driver within agreed scope. ODTI would not become the bank, the customer owner, the custodian, the settlement institution, or the production authority.

A DevOps or managed-service provider may perform delegated provisioning, deployment, monitoring, backup, recovery, release support, and incident-response work. The provider would act within AllBank's approved environment and delegated authority. It would not own the environment, data, credentials, billing relationships, or release decision.

AllBank's settlement institutions and payment providers would continue to perform supported financial movement under their agreements with the bank. The Program does not prescribe an exclusive settlement institution. AllBank would own or establish the relevant accounts, participation, credentials, limits, and execution authority.

The precise operating model supporting AllBank's current services is naturally unique to the institution. Any Program design would therefore begin with AllBank's approved architecture and relationships rather than assume a generic deployment.

Common software would not create a common bank. It would provide a maintained operating foundation within AllBank's own institutional boundaries.

Governance follows responsibility. The Board would authorize institutional purpose. Management would own implementation and operating accountability. Responsible functions would validate the complete service. Providers would supply only the capabilities assigned to them. Production could begin only through AllBank's approval process.

The Program should be judged by whether it establishes the Capability under institutional control—not by the quantity of software installed. Its value therefore begins with what the Capability enables AllBank to do.

## Section 3 — Why Should AllBank Proceed?

> **Executive question:** What could AllBank gain by proceeding?

> **Key message:** AllBank could gain a reusable governed foundation through which it may introduce and evolve banking services while preserving its authority, relationships, channels, and operating sovereignty.

> **Executive decision:** I understand the prospective institutional benefit and can decide whether it warrants commercial and implementation evaluation.

The principal benefit is operating leverage. A maintained grammar for authority, financial state, conditions, credentials, execution, and evidence can reduce the amount of foundational work repeated for each service. AllBank would still perform product design, policy, governance, integration review, training, customer treatment, and support. What changes is the starting point.

Existing channels remain valuable. AllBank Mobile, electronic onboarding, branches, AllConnect, the merchant portal, partner journeys, and approved APIs may initiate, present, or report activity. x-change would coordinate the governed ceremony beneath them. AllBank could improve a customer journey without redefining the financial state of the service, and it could add a channel without creating another independent settlement model.

Operating sovereignty would remain intact. AllBank would own or control its approved environment, deployment, data, domains, provider accounts, credentials, monitoring, backups, security configuration, releases, and audit trail. It would retain its customer and deposit relationships and its direct settlement relationships.

The same foundation could support services with different institutional purposes.

Payroll can connect employers, employees, deposits, payments, and continuing retail relationships. Merchant services can connect acceptance, settlement, reporting, liquidity, and business banking. Collections can connect payer information with matching, exceptions, and corporate reconciliation. Housing and commercial lending can connect approved finance with governed releases and continuing records. Remittance can serve a familiar immediate need while opening a broader household relationship.

These possibilities are not automatic returns or statements of AllBank priority. They become valuable only when the institution selects relevant services and operates them well. The credible benefit is the capacity to introduce, govern, and evolve services whose institutional and commercial value AllBank has independently established.

The Program also changes where scarce attention is spent. Rather than repeatedly rebuilding common orchestration machinery, AllBank can concentrate more management and engineering effort on customer relationships, product judgment, risk appetite, service quality, and chosen markets.

AllBank modernizes without becoming less itself. The operating model preserves that institutional boundary by design.

## Section 4 — How Does the Program Work?

> **Executive question:** How would the operating model work within AllBank?

> **Key message:** AllBank retains custody and authority. x-change coordinates the banking ceremony, and an AllBank-specific driver connects that ceremony to the institution's approved settlement capability.

> **Executive decision:** I understand where authority, funds, software, integration, execution, evidence, and reconciliation would reside.

The conceptual institutional stack is:

```text
AllBank Customer
          ↓
AllBank Products and Channels
          ↓
AllBank Banking Service
          ↓
x-change
          ↓
emi-core
          ↓
3neti/emi-allbank
          ↓
Approved AllBank API
          ↓
AllBank Settlement Arrangement
          ↓
InstaPay / PESONet / other approved rail or provider
```

The customer channel presents an experience. The banking service expresses AllBank's customer proposition, policy, terms, and responsibility. x-change coordinates the governed banking ceremony. `emi-core` defines the common execution contract. `3neti/emi-allbank` represents the institution-specific engineering that would translate that contract into AllBank's approved API behavior.

No production driver is assumed. Its feasibility and design would depend on discovery of AllBank's approved systems, interfaces, credentials, status models, controls, settlement arrangements, evidence, and reconciliation responsibilities.

The operating grammar keeps distinct responsibilities from being mistaken for one another.

A **Funding Event** records the external financial event through which Settlement Resources enter or become recognized by Treasury. It records institutional recognition; it does not create the underlying value.

**Treasury** maintains the operational state of Settlement Resources supporting the bank's activities. A **Lien** reserves capacity for an authorized purpose while an instruction remains outstanding.

A **Facility** gives the banking activity its purpose, participants, policies, commercial rules, and institutional responsibility. Commercial meaning belongs to the Facility.

A **Settlement Envelope** defines the evidence and conditions that must be satisfied before an instruction may proceed. Identity, approval, limits, documents, signatures, one-time passwords, beneficiary information, and other AllBank-defined requirements belong here.

A **Pay Code** represents an authorized instruction in a form that can be communicated, presented, validated, and executed. It is a credential—not money, a deposit, a wallet balance, or the banking service itself.

The banking service is the product. The Pay Code is the credential.

**Execution** coordinates the progression from authorized instruction to the outcome defined by the Facility. The execution engine and institution-specific driver address AllBank's approved API. Provider and institutional references, status, exceptions, and evidence return to the operating record for reconciliation.

Custody would not move into x-change. The underlying funds would remain within AllBank's regulated relationships. Treasury provides an operational view; it does not replace the bank account or determine the legal character of funds.

Technical completion remains narrower than readiness. A certified driver may perform agreed API behavior under tested conditions. AllBank must still decide whether the complete service can be authorized, operated, supervised, secured, settled, reconciled, supported, and governed.

## Section 5 — Banking in Action

> **Executive question:** How could the Capability apply to banking services relevant to AllBank?

> **Key message:** One operating grammar can support different AllBank services because purpose and policy may change while the responsibilities beneath them remain governed consistently.

> **Executive decision:** I can recognize how the operating model applies to a familiar ceremony and how the same foundation could support other AllBank-approved services.

Remittance remains the canonical explanatory ceremony because it makes the complete discipline visible within one familiar request. It forms part of AllBank's service portfolio, while the institution's operating journey can be understood only with AllBank.

A customer asks the bank to make funds available to another person. The bank receives or recognizes the funds, confirms authority, applies policy, records the remittance purpose, and identifies the recipient and permitted conditions.

Treasury recognizes the supporting Settlement Resources. A Lien reserves the required amount. The remittance Facility defines participants, limits, commercial rules, customer communication, and service responsibility. The Settlement Envelope records evidence and conditions. Once authorized, a Pay Code permits the instruction to be communicated and presented through an approved journey.

The recipient presents the Pay Code and satisfies the conditions. Execution coordinates the instruction through the bank's approved relationship. The institution-specific driver translates the common execution contract into approved API behavior. The financial movement occurs. x-change records the result, updates operational state, resolves the Lien, preserves evidence, and supports reconciliation and customer communication.

The customer requested a banking outcome. The bank arranged it.

AllBank's service portfolio brings several other ceremonies into view:

| Banking service | AllBank relevance | What remains governed |
| --- | --- | --- |
| Payroll | Employer instructions, employee attribution, recurring deposits, bulk release | Funding, authority, reservation, timing, exceptions, evidence, reconciliation |
| Merchant services | QR Ph acceptance, merchant relationships, settlement and reporting | Onboarding, conditions, execution, disputes, evidence, reconciliation |
| Collections | Bills payment, account sweeping, PDC warehousing, deposit services | Payer reference, purpose, matching, exceptions, reporting, evidence |
| Housing and commercial releases | Existing lending relationships and approved disbursement purposes | Documentary conditions, payees, stages, authority, execution, continuing records |
| Remittance | A familiar customer outcome and potential continuing household relationship | Funding, recipient conditions, credential, execution, evidence, reconciliation |

The table identifies relevance, not priority. AllBank should begin—if it chooses to proceed—with the ceremony that best combines institutional importance, bounded scope, operating familiarity, and readiness to learn.

One ceremony makes the grammar visible. Many services make the Capability useful.

## Section 6 — The Institutional Case

> **Executive question:** What kind of institution could the Program help AllBank become?

> **Key message:** The Capability could deepen relationships, preserve institutional choice, and lower repeated innovation cost while commercial value remains dependent on disciplined service selection and operation.

> **Executive decision:** I understand the institutional and commercial case and can decide whether it merits detailed evaluation under AllBank's strategy and financial authority.

A bank can retain an account while losing the practical center of a customer relationship. Salary may arrive elsewhere. Business collections may move through another provider. Merchant activity may be separated from deposits and credit. Household payments may migrate while the formal banking relationship remains.

The reverse can also occur. Payroll can connect an employer and employees to AllBank. Collections can connect the bank to the rhythm of an enterprise. Merchant services can connect commerce with liquidity and lending. Housing can sustain a long relationship. Remittance can become a recurring family relationship.

AllBank's service portfolio already touches many of these relationships. The institutional question is whether selected services can reinforce one another through repeated usefulness.

Over time, financial activity is more likely to return to an institution that remains useful across recurring needs.

This tendency is **Transaction Gravity**.

Transaction Gravity is not transaction volume alone and creates no entitlement to customer relevance. Service, pricing, channels, support, and fair exception handling still determine whether customers return. Its value is relational: the bank becomes a more natural place for income, deposits, payments, collections, obligations, and financial decisions to meet.

The Capability supports adaptability. Resilience allows AllBank to continue through difficulty; adaptability allows it to assume new responsibilities through an established foundation. The institution cannot predict every service required over the next decade. It can preserve the ability to evaluate new services without rebuilding its operating foundation each time.

The commercial case remains disciplined. Costs may include licensing, institution-specific implementation, driver engineering and maintenance, bank infrastructure, managed operations, internal governance and operations, settlement-provider charges, and continuing support. Economic value may arise through service income, stronger deposits, deeper employer and merchant relationships, reduced duplicated engineering, and the ability to introduce relevant services more efficiently. None is automatic.

Detailed economics require AllBank information and separate commercial analysis. A client-facing Program Guide should not invent prices, volumes, savings, or returns before the institution has defined the service and supplied the evidence required to evaluate them.

The Board would be deciding more than whether to acquire software. It would be deciding whether AllBank should establish a reusable Capability through which its authority and relationships may support more services over time.

## Section 7 — Launching the Program

> **Executive question:** What would happen if AllBank later authorized the Program?

> **Key message:** The next step is institutional discovery around one bounded banking ceremony—not an immediate production decision.

> **Executive decision:** I understand the institutional journey and the questions AllBank would need to resolve before authorizing implementation or controlled production.

The appropriate first step is to understand the institution directly.

AllBank would identify the customer need, product context, authority, source and destination of funds, policies, approvals, evidence, channels, systems, accounting, reconciliation, support, exceptions, settlement arrangements, and institutional owners relevant to one candidate ceremony.

The bank would then determine which ceremony best combines strategic importance, bounded scope, operating familiarity, and readiness to learn. Payroll, merchant services, collections, housing-related release, and remittance each offer a different institutional lens. The choice belongs to AllBank.

The customer journey would be defined as part of the banking service, not as a separate design exercise. The ceremony would identify what AllBank agrees to do, what evidence is required, how customers are informed, how exceptions are handled, and what completion means.

Driver discovery would examine approved API behavior, authentication, certificates, request and response structures, references, idempotency, webhooks, status, limits, exceptions, reversals, reconciliation evidence, test environments, and change processes. Only after this work could the feasibility and scope of `3neti/emi-allbank` be established.

If AllBank later authorized implementation, certification would remain a technical gate. Operational readiness would remain a separate institutional gate. Bank personnel would need to validate initiation, approvals, Funding Events, Treasury state, Liens, Facility rules, Settlement Envelope conditions, Pay Code presentation, execution, provider behavior, accounting, evidence, support, reconciliation, failure, delay, duplication, reversal, and uncertain outcomes as one banking operation.

Readiness is an institutional judgment. It exists only when AllBank has sufficient evidence that the ceremony can be authorized, operated, supervised, secured, settled, reconciled, supported, and governed under its authority.

No such conclusion is requested by this Executive Edition.

The immediate invitation is narrower: confirm whether the institutional question is relevant, identify the banking responsibility through which it should be examined, and establish what AllBank would need to know before considering any further decision.

The next step is a disciplined institutional dialogue: whether this Capability belongs within AllBank's future, and which banking responsibility should test that judgment first.

## Annexes

The annexes preserve the canonical operating, governance, and Treasury distinctions required to evaluate the Program. They provide institutional reference without converting this Executive Edition into an implementation specification.

- Annex A — Canonical Operating Model
- Annex B — Banking Ceremonies
- Annex C — Bank Driver Architecture
- Annex D — Governance Principles
- Annex E — Treasury and Settlement Grammar
- Annex F — Institutional Readiness Framework
- Annex G — Glossary
- Annex H — Applying This Program Guide to AllBank

## Annex A — Canonical Operating Model

The Program separates the customer proposition, governed banking ceremony, common execution contract, institution-specific integration, and regulated financial movement.

```text
AllBank Customer Channel
          ↓
AllBank Banking Service
          ↓
x-change
          ↓
emi-core
          ↓
3neti/emi-allbank
          ↓
Approved AllBank API
          ↓
AllBank Settlement Arrangement
          ↓
InstaPay / PESONet / other approved rail or provider
```

This model is conceptual. It describes institutional responsibilities and integration boundaries, not a production topology.

**The AllBank customer** requests a banking outcome through an institution-approved journey.

**AllBank products and channels** initiate, present, or report banking activity. They may include branches, mobile and Internet banking, corporate channels, merchant journeys, partner journeys, and approved APIs.

**The AllBank banking service** defines the customer outcome, participants, terms, policy, commercial meaning, service responsibility, and customer treatment. The banking service remains the product.

**x-change** coordinates the governed banking ceremony: recognized resources, purpose, authority, conditions, credential, execution, evidence, exceptions, and reconciliation.

**`emi-core`** provides the maintained common execution contract. It allows the operating grammar to address an institution-specific execution capability without making provider behavior part of the banking service.

**`3neti/emi-allbank`** represents the AllBank-specific driver. It would translate the common contract into the institution's approved authentication, request, response, reference, status, webhook, exception, reversal, security, and reconciliation behavior.

**The approved AllBank API and settlement arrangement** remain governed by AllBank and its providers. Financial movement occurs through the bank's regulated relationships. The software neither creates settlement access nor assumes custody.

The model preserves three boundaries:

1. AllBank defines and owns the banking service.
2. The operating grammar coordinates the service without replacing institutional authority.
3. Execution reaches approved financial infrastructure only through bank-governed integration.

Common software does not create a common bank. AllBank retains its own policies, environment, data, credentials, customer relationships, settlement relationships, production decisions, and audit trail.

## Annex B — Banking Ceremonies

A governed banking ceremony is the complete progression through which a customer request becomes authorized, executable, evidenced, and reconciled banking activity. The ceremonies below illustrate how one operating grammar can support different institutional purposes. They do not establish AllBank priorities or implementation scope.

### Payroll

An employer submits an authorized payroll instruction and provides or identifies the supporting funds. AllBank validates authority, timing, employee attribution, limits, exceptions, and required evidence. Treasury recognizes the Settlement Resources and reserves the required capacity. The payroll Facility defines the service and its commercial rules. Settlement Envelopes establish the conditions for release. Execution proceeds through the bank's approved capability, and the resulting institutional and provider evidence supports reporting, exception handling, and reconciliation.

Payroll may connect employer banking, employee deposits, payments, and continuing retail relationships. Its value depends on AllBank's service design and operation; the operating grammar does not determine the commercial proposition.

### Merchant Settlement

A merchant accepts customer payments through an AllBank-approved channel or arrangement. The merchant Facility defines participation, settlement terms, fees, timing, exceptions, and reporting. Treasury distinguishes recognized resources from amounts reserved or unresolved. Settlement Envelopes carry the conditions and evidence required before settlement. Execution coordinates approved movement, while the operating record supports merchant reporting, disputes, exceptions, and reconciliation.

The ceremony connects acceptance to a governed merchant relationship. QR or payment connectivity alone does not define the complete service.

### Collections

A payer submits funds for a defined obligation. AllBank captures the payer, biller, purpose, reference, amount, channel, and applicable conditions. The collections Facility defines matching and exception rules. The Settlement Envelope preserves required evidence. Execution coordinates the approved financial outcome. The completed record supports attribution, posting, exception resolution, biller reporting, and reconciliation.

The ceremony is valuable because it connects financial movement with institutional meaning. A successful transfer without reliable attribution may still leave the collection unresolved.

### Housing Finance

An approved housing-finance obligation may require release to a borrower, seller, developer, contractor, or other authorized recipient after defined conditions are satisfied. The Facility carries the financing purpose, participants, policies, stages, limits, and service responsibility. The Settlement Envelope records documentary and approval conditions. Treasury reserves the authorized resources. A Pay Code may represent the instruction where the approved journey requires one. Execution proceeds only after the bank's conditions are satisfied, with evidence retained for the continuing financing record and reconciliation.

The ceremony does not replace credit approval, legal review, collateral administration, or the bank's lending systems. It governs an authorized release within the wider banking relationship.

### Remittance

A customer asks AllBank to make funds available to another person. The bank receives or recognizes the funds, applies policy, identifies the recipient, defines the service conditions, and accepts responsibility for the outcome. Treasury recognizes and reserves the required resources. The remittance Facility carries purpose and service rules. The Settlement Envelope records evidence and conditions. A Pay Code represents the authorized instruction. The recipient satisfies the conditions, and execution coordinates the financial movement through AllBank's approved relationship. The operating record preserves status, evidence, exceptions, and reconciliation.

The customer requested a banking outcome. The bank arranged it.

### Government Disbursement

A government institution may authorize funds for a defined beneficiary, public purpose, program, or obligation. A participating bank would recognize the funding event and the governing authority, apply program and institutional rules, identify recipients, reserve resources, gather required evidence, and coordinate approved execution. The operating record would support attribution, exceptions, reporting, audit, and reconciliation.

This is an illustrative future ceremony, not a statement that AllBank currently provides or should prioritize the service. Any application would require the relevant public authority, legal arrangements, procurement, controls, and institutional approval.

Across these ceremonies, purpose and policy change. The responsibilities remain recognizable: funds, authority, conditions, credential where required, execution, evidence, exception handling, and reconciliation.

## Annex C — Bank Driver Architecture

The bank-specific driver connects the common execution contract to AllBank's approved API behavior.

```text
x-change
    ↓
emi-core
    ↓
emi-allbank
    ↓
Approved AllBank APIs and settlement capability
```

`emi-allbank` is the concise institutional label used in this annex. Within the canonical component grammar, the driver is represented conceptually as `3neti/emi-allbank`.

The driver adapts technology. It does not provide banking authority, settlement participation, custody, product definition, policy, or production approval. AllBank brings the authority and the rails. x-change brings the operating grammar. The bank-specific driver connects them.

No production driver is assumed to exist. Institution-specific engineering would require:

1. **Institutional discovery** — establish the approved systems, interfaces, environments, settlement arrangements, credentials, controls, owners, evidence, and reconciliation responsibilities relevant to the selected ceremony.
2. **API mapping** — map `emi-core` operations to AllBank-approved authentication, certificates, requests, responses, references, idempotency, statuses, webhooks, limits, exceptions, reversals, and provider behavior.
3. **Implementation** — create the maintained driver within approved architecture, security, coding, testing, release, and documentation practices.
4. **Certification** — demonstrate agreed technical behavior under controlled conditions, including success, failure, delay, duplication, uncertain status, and recovery paths.
5. **Continuing maintenance** — manage API changes, certificates, security updates, provider changes, test evidence, observability, defects, releases, and compatibility with the maintained common contract.

The driver should expose a stable execution contract to the operating grammar while preserving provider-specific detail at the institutional boundary. It should return references, status, evidence, and exceptions required by the complete banking ceremony rather than reduce execution to a successful API response.

Driver certification is necessary where the integration is used, but it is not operational readiness. AllBank must still judge whether the banking service can be authorized, operated, supervised, secured, settled, reconciled, supported, and governed.

## Annex D — Governance Principles

Governance follows institutional responsibility. No provider approval substitutes for AllBank approval.

| Participant | Principal responsibility | Institutional boundary |
| --- | --- | --- |
| Board of Directors | Approves institutional purpose, risk appetite, scope, accountability, and material progression | Fiduciary responsibility is not delegated to a technology provider |
| President, CEO, and Management | Own Program sponsorship, resources, accountability, and management decisions | Board approval does not constitute production readiness |
| Business and Product | Define the banking service, customer responsibility, policy, terms, and economic case | Technical credentials do not carry commercial meaning |
| Operations | Define supervision, support, escalation, exception handling, evidence, and reconciliation practice | Technical completion is not an operating decision |
| Treasury | Governs the operational view of Settlement Resources, reservations, and unresolved obligations | Software state does not replace the bank account or determine legal fund character |
| Technology | Governs architecture, integration, environments, identity, observability, resilience, service management, and release | External engineering extends rather than displaces institutional capability |
| Risk and Compliance | Review risks, controls, obligations, monitoring, and customer treatment within authority | Accountability does not transfer to certification artifacts |
| Legal | Reviews agreements, authority, customer terms, data treatment, and legal characterization | This Guide is not a legal agreement or legal opinion |
| Information Security | Governs access, credentials, certificates, testing, monitoring, incident response, and change | Production secrets remain under approved institutional control |
| Finance and Accounting | Define accounting, financial reporting, provider-charge treatment, and reconciliation requirements | Commercial estimates require separate financial approval |
| Internal Audit | Provides independent assurance according to its mandate | Internal Audit does not become an implementation owner |
| ODTI | Licenses and maintains x-change, `emi-core`, supported components, documentation, testing capability, and the bank-specific driver within scope | ODTI does not provide banking authority, custody, settlement access, or production approval |
| DevOps or managed-service provider | Performs delegated provisioning, deployment, monitoring, backup, recovery, release support, and incident work | The provider does not own AllBank's environment, data, credentials, billing, or release authority |
| Settlement institution or payment provider | Performs supported financial movement and provides records under its agreement with AllBank | The provider does not define AllBank's customer product or complete ceremony |

The principal decision gates are:

1. **Program authorization** — the Board or delegated authority permits Management to evaluate and establish the Program.
2. **Service definition** — AllBank approves the first banking ceremony and its accountable owners.
3. **Architecture and security approval** — responsible functions approve the intended environment and integration boundary.
4. **Driver certification** — agreed technical behavior is evidenced under controlled conditions.
5. **Operational readiness** — AllBank judges the complete ceremony ready for bounded production.
6. **Pilot decision** — the institution authorizes a limited production scope.
7. **Evidence review** — the institution decides to Proceed, Correct, Extend, or Pause.

The Program preserves operating sovereignty. AllBank retains control over authority, customer relationships, policy, infrastructure, data, credentials, production decisions, settlement relationships, and its institutional audit trail.

AllBank's approved banking, accounting, customer, and settlement systems remain institutional systems of record. x-change coordinates the governed ceremony and preserves its operating evidence; it does not replace those systems or redefine their authority.

## Annex E — Treasury and Settlement Grammar

Treasury provides the operational financial-state grammar supporting a governed banking ceremony.

### Canonical progression

```text
External financial event
        ↓
Funding Event
        ↓
Settlement Resources recognized by Treasury
        ↓
Lien reserves resources for an authorized purpose
        ↓
Facility gives the activity banking and commercial meaning
        ↓
Settlement Envelope establishes evidence and conditions
        ↓
Pay Code represents the authorized instruction
        ↓
Execution coordinates the approved outcome
        ↓
Evidence, state resolution, and reconciliation
```

### Governing distinctions

- A Funding Event records an external event; it does not manufacture funds.
- Treasury represents operational state; it is not the bank account or general ledger.
- Settlement Resources remain subject to their actual custody, ownership, legal character, and institutional controls.
- A Lien reserves capacity; it does not transfer custody.
- A Facility carries banking and commercial meaning; a Pay Code does not.
- A Settlement Envelope carries conditions and evidence; it does not perform settlement.
- A Pay Code is a credential; it is not money, a deposit, stored value, or the service itself.
- Execution coordinates the authorized outcome through AllBank's approved capability.
- Reconciliation compares operating state with institutional and provider evidence and resolves differences through approved procedures.

The underlying funds remain within AllBank's regulated relationships throughout. Treasury gives the ceremony an operational view of what is recognized, reserved, available, or unresolved. It neither assumes custody nor changes the legal character of funds.

Commercial meaning belongs to the Facility. The Facility identifies why the activity exists, who participates, what rules and limits apply, and what responsibility AllBank accepts. The Settlement Envelope then establishes what must be true before the instruction proceeds. This separation allows evidence and conditions to evolve without confusing them with the banking product.

Execution completes neither the institutional record nor the bank's responsibility by itself. Provider references, statuses, exceptions, and evidence must return to the operating record. Treasury state, Liens, accounting, customer communication, exception handling, and reconciliation must then be resolved according to approved procedures.

## Annex F — Institutional Readiness Framework

Readiness is AllBank's judgment that sufficient evidence exists to authorize, operate, supervise, secure, settle, reconcile, support, and govern a banking ceremony.

The judgment should address the complete institution, not only software behavior.

| Readiness dimension | Evidence required before bounded production |
| --- | --- |
| Governance | Approved purpose, accountable owners, decision rights, escalation, pilot authority, and review criteria |
| Banking service | Defined customer outcome, participants, policy, terms, limits, channels, communications, and fair treatment |
| Operations | Documented initiation, approval, supervision, support, exceptions, recovery, evidence, reconciliation, and end-of-day responsibilities |
| Treasury and settlement | Confirmed Funding Events, Settlement Resources, Liens, accounts, limits, liquidity, references, statuses, unresolved-state treatment, and settlement responsibilities |
| Risk, Compliance, and Legal | Reviewed regulatory obligations, risks, controls, customer terms, agreements, data treatment, and legal characterization |
| Technology and architecture | Approved environments, interfaces, identities, observability, capacity, resilience, backup, recovery, service management, and change processes |
| Information security | Approved access, credentials, certificates, secrets, testing, monitoring, incident response, vulnerability management, and production controls |
| Finance and accounting | Defined entries, fees, provider charges, reporting, reconciliation, exception treatment, and financial-control ownership |
| Customer experience | Tested initiation, evidence gathering, disclosures, status communication, assistance, failure treatment, and completion experience |
| People and providers | Trained personnel, operating procedures, support coverage, provider obligations, service levels, escalation paths, and continuity arrangements |
| Evidence and assurance | Test results, driver certification, operating rehearsals, control evidence, unresolved findings, approvals, and independent review where required |

Certification demonstrates that the AllBank-specific driver performs agreed technical behavior under tested conditions. It does not decide whether the product is suitable, the policy is approved, the staff are prepared, the settlement model is sufficient, the accounting is correct, customers can be supported, or exceptions can be governed.

Operational readiness therefore follows certification; it is not produced by certification. AllBank may authorize a limited pilot only when responsible functions have evaluated the complete ceremony and accepted the bounded production conditions.

Pilot evidence should be reviewed through the institutional choices **Proceed**, **Correct**, **Extend**, or **Pause**. A successful technical transaction is evidence within that review, not the review itself.

## Annex G — Glossary

These definitions apply to the Thrift Bank Digital Banking Program Guide and remain subordinate to the canonical x-change and Treasury grammar.

**Capability** — The enduring, maintained operating foundation established through the Program. It allows AllBank to turn customer requests into governed banking activity.

**Program** — The institution-specific initiative through which AllBank evaluates, establishes, governs, and introduces the Capability.

**Funding Event** — The record of an external financial event through which Settlement Resources enter or become recognized by Treasury. It records recognition; it does not create the underlying value.

**Treasury** — The operational view of Settlement Resources supporting the bank's activities, including what is recognized, reserved, available, or unresolved. It is not the bank account itself.

**Settlement Resources** — The resources recognized by Treasury as supporting an activity. Their custody and legal character remain within AllBank's regulated arrangements.

**Lien** — An operational reservation of Settlement Resources for an authorized purpose while an instruction remains outstanding.

**Facility** — The governed definition of a banking service. It carries purpose, participants, policies, commercial rules, limits, and institutional responsibility.

**Settlement Envelope** — The evidence and conditions that must be satisfied before an instruction may proceed.

**Pay Code** — A credential representing an authorized instruction in a form that can be communicated, presented, validated, and executed. It is not money, a deposit, stored value, or the banking product.

**Execution** — The coordination of an authorized instruction toward the banking outcome defined by the Facility through AllBank's approved execution capability.

**Execution Engine** — The component that coordinates the supported execution progression and invokes the applicable driver.

**`emi-core`** — The maintained common contract through which the operating grammar addresses institution-specific execution capability.

**Driver / `3neti/emi-allbank`** — The maintained institution-specific implementation of `emi-core` for AllBank's approved API, authentication, status, webhook, security, exception, and reconciliation behavior.

**Governed Banking Ceremony** — The complete progression from customer request and recognized funds through policy, authority, conditions, execution, evidence, exception handling, and reconciliation.

**Readiness** — AllBank's institutional judgment that sufficient evidence exists to authorize, operate, supervise, secure, settle, reconcile, support, and govern a ceremony.

**Certification** — Evidence that the AllBank-specific driver performs agreed technical behavior under tested conditions. Certification is not operational readiness.

**Transaction Gravity** — The tendency for financial activity to return to an institution that remains useful across recurring customer and enterprise needs.

**Operating sovereignty** — AllBank's continuing control over its banking authority, customer relationships, policies, infrastructure, data, credentials, production decisions, settlement relationships, and institutional audit trail.

## Annex H — Applying This Program Guide to AllBank

This AllBank Edition applies the canonical Thrift Bank Digital Banking Program Guide to an institution that already possesses banking authority, established customer relationships, digital channels, payment participation, lending activities, and service relationships across households and enterprises.

AllBank's published banking services informed the selection of institutional examples. Payroll, bulk payments, merchant acceptance, collections, remittance, housing finance, commercial lending, mobile banking, digital onboarding, and corporate Internet banking make the Program's operating question concrete without determining the institution's priorities.

The Guide identifies where one governed operating Capability may align with those responsibilities. It preserves the boundary between AllBank's banking service and the software supporting it; between AllBank's settlement authority and the driver connecting approved APIs; and between technical certification and institutional readiness.

This application does not assert how AllBank currently performs each ceremony, recommend a production design, select an initial service, establish commercial terms, or conclude that the institution is ready to proceed. Those decisions require direct institutional knowledge and AllBank authority.

The Guide is therefore a basis for executive dialogue. If the institutional question is relevant, AllBank can select one bounded banking responsibility, examine its complete ceremony, and determine what evidence would be required before any further decision.
