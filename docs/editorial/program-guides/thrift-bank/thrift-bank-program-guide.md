# Thrift Bank Digital Banking Program Guide

## A Canonical Implementation Guide for Philippine Thrift Banks

## Executive Summary

Philippine thrift banks already possess the authority, relationships, technology organizations, channels, and settlement arrangements required to conduct banking. The institutional question is not whether they can reach a payment rail. It is whether one bank can turn those foundations into a wider range of governed banking services without constructing a separate operating model for every product and channel.

Settlement connectivity is necessary, but it is not a banking service. A rail can move funds and an API can transmit an instruction. Neither defines the customer's request, establishes purpose, applies policy, recognizes and reserves resources, gathers evidence, manages exceptions, communicates status, or reconciles the completed service. Those remain banking responsibilities.

The **Program** is the institution-specific initiative through which a thrift bank establishes one reusable governed operating foundation. The enduring result is the **Capability**: a maintained foundation through which customer requests become authorized, observable, executable, and reconcilable banking activity.

The bank remains the protagonist. It retains its license, products, customer and deposit relationships, channels, infrastructure, data, policies, credentials, production authority, and settlement relationships. x-change supplies the operating grammar beneath those arrangements. `emi-core` provides the common execution contract, and a maintained bank-specific driver—represented as `3neti/emi-{bank}`—maps that contract to the institution's approved API behavior.

The bank brings the authority and the rails. x-change brings the operating grammar. The bank-specific driver connects them.

The driver is institution-specific engineering, not an automatically available connector. It requires institutional discovery, API mapping, implementation, certification, and continuing maintenance. Certification establishes technical capability under tested conditions. It does not establish operational readiness. Readiness remains an institutional judgment based on the complete banking ceremony.

Remittance makes the model visible. A customer asks the bank to make funds available to another person. The bank recognizes the funds, applies policy, reserves the required capacity, defines the conditions, issues a Pay Code credential, coordinates execution through its approved settlement relationship, preserves evidence, and reconciles the result.

The customer requested a banking outcome. The bank arranged it.

The same Capability can support payroll, collections, merchant services, SME disbursement, housing-related workflows, and other services approved by the bank. Their commercial meaning, participants, policies, evidence, and customer journeys differ. The operating grammar remains stable.

The Program begins with one bounded ceremony. Management defines the service, the bank-specific driver is discovered and certified, the complete operation is tested, personnel are prepared, and the institution decides whether evidence supports controlled production. Expansion follows only when the bank is prepared to assume the next responsibility.

The decision before the Board is whether the institution should establish one reusable governed operating Capability and authorize Management to define the first ceremony, complete the required institutional work, and return with evidence sufficient for a controlled production decision.

## Section 1 — Why This Program?

> **Executive question:** Why should our institution establish this Program?

> **Key message:** The bank already has authority, relationships, channels, technology, and settlement capability. The opportunity is to organize them through one governed operating foundation that can support more banking services over time.

> **Executive decision:** I understand the institutional problem and can decide whether establishing a reusable governed operating Capability merits formal evaluation.

Thrift banks serve households, employers, entrepreneurs, housing markets, and small and medium-sized enterprises through regulated authority and relationships built over time. Modernization should strengthen those institutional qualities rather than replace them.

Many thrift banks already operate core banking systems, Internet banking, mobile banking, corporate services, settlement accounts, payment integrations, cybersecurity controls, and professional technology organizations. Yet a bank can accumulate functioning channels without acquiring a reusable operating foundation beneath them. Each new service may bring its own financial-state logic, approval model, provider integration, exception process, evidence, and reconciliation practice.

That pattern creates repeated work. It also makes institutional responsibility harder to observe across channels and services. A customer sees a transfer, payroll release, collection reference, merchant payment, or disbursement. The bank must see the complete obligation: purpose, authority, funds, conditions, evidence, execution, exceptions, support, and reconciliation.

The Program addresses that operating problem. It does not confer banking authority or settlement access. It organizes authority and connectivity the bank already possesses or establishes through approved relationships.

The timing is practical. Maintained software, modern deployment practices, API-based integration, automated testing, observability, and regulated payment infrastructure now allow a bank to establish a reusable foundation without rebuilding every component for every service. The opportunity is not to adopt technology for its own sake. It is to preserve institutional choice while reducing repeated engineering.

One foundation will not make every service alike. It will give the bank a consistent way to govern their differences.

## Section 2 — What Is the Program?

> **Executive question:** What exactly is the institution being invited to establish?

> **Key message:** The Program is an institution-specific modernization initiative. Its result is a maintained operating Capability under the bank's authority and control.

> **Executive decision:** I understand the Program, the Capability it is intended to establish, the participating roles, and the boundaries that remain subject to institutional approval.

The Thrift Bank Digital Banking Program brings together licensed x-change software, institution-specific integration, controlled deployment, observability, testing, documentation, maintenance, and operating governance. The resulting Capability coordinates the progression from recognized funds and authorized purpose to conditions, credential, execution, evidence, and reconciliation.

The Program is the initiative. The Capability is the enduring operational result. The terms are not interchangeable: the Program can be approved, governed, implemented, and reviewed; the Capability is what the bank continues to operate and evolve.

The participating institution is the program sponsor and banking authority. Its Board and Management establish purpose, risk appetite, scope, accountability, and approval boundaries. Business, Operations, Treasury, Technology, Risk, Compliance, Legal, Information Security, Internal Audit, Finance, and other responsible functions perform their established roles.

Open Disbursement Technologies, Inc. (ODTI) licenses and maintains x-change, `emi-core`, supported components, documentation, reference architecture, testing capability, and the bank-specific driver within agreed scope. ODTI does not become the bank, customer owner, custodian, settlement institution, or production authority.

A DevOps or managed-service provider may perform delegated provisioning, deployment, monitoring, backup, recovery, release support, and incident-response work. The provider acts within the bank's approved environment and delegated authority. It does not own the environment, data, credentials, billing relationships, or release decision.

The bank's settlement institution or payment provider performs supported financial movement under its agreement with the bank. The Program does not prescribe NetBank or any other exclusive settlement institution. The bank owns or establishes the relevant account, participation, credentials, limits, and execution authority.

Licensing and participation remain institution-specific. The bank licenses the maintained software and approves the services and providers required for its deployment. Commercial agreements must identify the license, implementation, bank-specific driver, maintenance, managed operations, support, and third-party provider responsibilities without confusing any of them with banking authority.

Governance follows responsibility. The Board authorizes institutional purpose. Management owns implementation and operating accountability. Responsible functions validate the complete service. Providers supply only the capabilities assigned to them. Production begins only through the bank's approval process.

The Program should be judged by whether it establishes the Capability under institutional control—not by the quantity of software installed.

## Section 3 — Why Should the Institution Proceed?

> **Executive question:** What does the institution gain by proceeding?

> **Key message:** The bank gains a reusable governed foundation through which it can introduce and evolve banking services while preserving its authority, relationships, channels, and operating sovereignty.

> **Executive decision:** I understand the prospective institutional benefit and can decide whether it warrants commercial and implementation evaluation.

The principal benefit is operating leverage. A maintained grammar for authority, financial state, conditions, credentials, execution, and evidence reduces the amount of foundational work repeated for each service. The institution still performs product design, policy, governance, integration review, training, customer treatment, and support. What changes is the starting point.

Existing channels remain valuable. Internet banking, mobile banking, branches, corporate portals, and partner APIs may initiate, present, or report activity. x-change coordinates the governed ceremony beneath them. The bank can improve a customer experience without redefining the financial state of the service, and it can add a channel without creating another independent settlement model.

Operating sovereignty remains intact. The bank owns or controls its approved environment, deployment, data, domains, provider accounts, credentials, monitoring, backups, security configuration, releases, and audit trail. It retains its customer and deposit relationships and its direct settlement relationships.

The same foundation can support services with different institutional purposes. Payroll connects employers and employees. Collections connect the bank to SME operating activity. Merchant services connect commerce to deposits, liquidity, and credit. Housing workflows can govern documentary conditions and staged releases. Remittance can begin a continuing household relationship.

These opportunities are not automatic returns. They become valuable only when the institution selects relevant services and operates them well. The credible benefit is the capacity to introduce, govern, and evolve services whose institutional and commercial value the bank has independently established.

The Program also changes where scarce attention is spent. Rather than repeatedly rebuilding common orchestration machinery, the bank can concentrate more management and engineering effort on customer relationships, product judgment, risk appetite, service quality, and chosen markets.

The bank modernizes without becoming less itself.

## Section 4 — How Does the Program Work?

> **Executive question:** How does the operating model work?

> **Key message:** The bank retains custody and authority. x-change coordinates the banking ceremony, and the bank-specific driver connects that ceremony to the institution's approved settlement capability.

> **Executive decision:** I understand where authority, funds, software, integration, execution, evidence, and reconciliation reside.

The institutional stack is:

```text
Customer Channel
       ↓
Bank Product
       ↓
x-change
       ↓
emi-core
       ↓
3neti/emi-{bank}
       ↓
Bank API
       ↓
Bank Settlement Account
       ↓
InstaPay / PESONet / approved settlement arrangement
```

The customer channel presents an experience. The bank product expresses the customer proposition, policy, terms, and responsibility. x-change coordinates the governed banking ceremony. `emi-core` defines the common execution contract. `3neti/emi-{bank}` translates that contract into the institution's approved API behavior. The bank API and settlement account remain subject to institutional authority. The applicable rail or provider performs the supported financial movement.

The operating grammar keeps distinct responsibilities from being mistaken for one another.

A **Funding Event** records the external financial event through which Settlement Resources enter or become recognized by Treasury. It records institutional recognition; it does not create the underlying value.

**Treasury** maintains the operational state of Settlement Resources supporting the bank's activities. A **Lien** reserves capacity for an authorized purpose while an instruction remains outstanding.

A **Facility** gives the banking activity its purpose, participants, policies, commercial rules, and institutional responsibility. Commercial meaning belongs to the Facility.

A **Settlement Envelope** defines the evidence and conditions that must be satisfied before an instruction may proceed. Identity, approval, limits, documents, signatures, one-time passwords, beneficiary information, and other bank-defined requirements belong here.

A **Pay Code** represents an authorized instruction in a form that can be communicated, presented, validated, and executed. It is a credential—not money, a deposit, a wallet balance, or the banking service itself.

**Execution** coordinates the progression from authorized instruction to the outcome defined by the Facility. The execution engine and bank-specific driver address the bank's approved API. Provider and institutional references, status, exceptions, and evidence return to the operating record for reconciliation.

The driver is necessary because bank APIs differ. Authentication, certificates, signatures, request formats, idempotency, webhooks, status models, limits, errors, reversals, reconciliation evidence, and versioning must be discovered and mapped. ODTI implements and maintains the driver within scope; the bank governs credentials, review, certification, release, and change.

Custody does not move into x-change. The underlying funds remain within the bank's regulated relationships. Treasury provides an operational view; it does not replace the bank account or determine the legal character of funds.

Technical completion remains narrower than readiness. A certified driver may perform the agreed API behavior under tested conditions. The bank must still decide whether the complete service can be authorized, operated, supervised, secured, settled, reconciled, supported, and governed.

Further detail appears in [Treasury Grammar](appendices/treasury-grammar.md) and [Deployment Architecture](appendices/deployment-architecture.md).

## Section 5 — Banking in Action

> **Executive question:** Show me how the Capability works in practice.

> **Key message:** One operating grammar supports different banking services because purpose and policy may change while the responsibilities beneath them remain governed consistently.

> **Executive decision:** I can recognize how the operating model applies to a familiar ceremony and how the same foundation can support other institution-approved services.

Remittance is the canonical explanatory ceremony because it makes the complete discipline visible within one familiar request.

A customer asks the bank to make funds available to another person. The bank receives or recognizes the funds, confirms authority, applies policy, records the remittance purpose, and identifies the recipient and permitted conditions.

Treasury recognizes the supporting Settlement Resources. A Lien reserves the required amount. The remittance Facility defines participants, limits, commercial rules, customer communication, and service responsibility. The Settlement Envelope records evidence and conditions. Once authorized, a Pay Code permits the instruction to be communicated and presented through an approved journey.

The recipient presents the Pay Code and satisfies the conditions. Execution coordinates the instruction through the bank's approved relationship. The bank-specific driver translates the common execution contract into the bank's API behavior. The financial movement occurs. x-change records the result, updates operational state, resolves the Lien, preserves evidence, and supports reconciliation and customer communication.

The customer requested a banking outcome. The bank arranged it.

The same grammar applies elsewhere:

| Banking service | What changes | What remains governed |
| --- | --- | --- |
| Payroll | Employer authority, employee attribution, scale, timing, release | Funding, reservation, conditions, execution, evidence, reconciliation |
| Collections | Direction of value, payer reference, invoice or obligation attribution | Recognition, purpose, status, exceptions, evidence |
| Merchant services | Merchant rules, accepted instruments, settlement timing | Authority, financial state, execution, reconciliation |
| SME disbursement | Enterprise mandate, approvals, purpose, beneficiary | Conditions, reservation, instruction, evidence |
| Housing workflows | Documentary conditions, payees, release stages | Purpose, authority, readiness, execution, continuing records |

Remittance need not be the first production service. The bank should begin with the ceremony that best combines institutional importance, bounded scope, operating familiarity, and readiness to learn.

One ceremony makes the grammar visible. Many services make the Capability useful.

## Section 6 — The Institutional Case

> **Executive question:** What kind of institution can the Program help the bank become?

> **Key message:** The Capability can deepen relationships, preserve institutional choice, and lower repeated innovation cost while commercial value remains dependent on disciplined service selection and operation.

> **Executive decision:** I understand the institutional and commercial case and can decide whether it merits detailed evaluation under the bank's strategy and financial authority.

A bank can retain an account while losing the practical center of a customer relationship. Salary may arrive elsewhere. SME collections may move through another provider. Merchant activity may be separated from deposits and credit. Household payments may migrate while the formal banking relationship remains.

The reverse can also occur. Payroll can connect an employer and employees to the institution. Collections can connect the bank to the rhythm of an enterprise. Merchant services can connect commerce with liquidity and lending. Housing can sustain a long relationship. Remittance can become a recurring family relationship.

These services create opportunities for repeated usefulness. Over time, financial activity is more likely to return to an institution that remains useful across recurring needs.

This tendency is **Transaction Gravity**.

Transaction Gravity is not transaction volume alone and creates no entitlement to customer relevance. Service, pricing, channels, support, and fair exception handling still determine whether customers return. Its value is relational: the bank becomes a more natural place for income, deposits, payments, collections, obligations, and financial decisions to meet.

The Capability supports adaptability. Resilience allows the bank to continue through difficulty; adaptability allows it to assume new responsibilities through an established foundation. The institution cannot predict every service required over the next decade. It can preserve the ability to evaluate new services without rebuilding its operating foundation each time.

The commercial case remains disciplined. Costs may include licensing, institution-specific implementation, driver engineering and maintenance, bank infrastructure, managed operations, internal governance and operations, settlement-provider charges, and continuing support. Economic value may arise through service income, stronger deposits, deeper employer and merchant relationships, reduced duplicated engineering, and the ability to introduce relevant services more efficiently. None is automatic.

The Commercial Waterfall identifies the economic path without inventing prices: customer or institutional service economics flow into the bank's product model; provider and operating obligations are recognized; license, integration, operations, settlement, support, and maintenance responsibilities are allocated; the bank evaluates the residual institutional value. Detailed amounts require separate commercial agreements and financial analysis.

Commercial sustainability exists when the model funds dependable operation, maintenance, provider responsibilities, and institutional participation without obscuring who earns, pays, bears risk, or remains accountable.

The Board is deciding more than whether to acquire software. It is deciding whether the institution should establish a reusable Capability through which its authority and relationships can support more services over time.

## Section 7 — Launching the Program

> **Executive question:** What happens after approval?

> **Key message:** Approval begins a controlled institutional journey from discovery to one bounded production ceremony. It does not place the bank into production.

> **Executive decision:** I understand the sequence, evidence, governance gates, and next decision required to begin controlled implementation.

Board approval establishes purpose, scope, accountability, and the authority for Management to proceed. Management names responsible leaders and confirms the governance through which Business, Operations, Treasury, Technology, Risk, Compliance, Security, Legal, Finance, Audit, and providers will participate.

Implementation begins by understanding the institution. The bank explains the customer need, product context, authority, source and destination of funds, policies, approvals, evidence, channels, systems, accounting, reconciliation, support, exceptions, settlement arrangements, and institutional owners.

The bank then defines the first ceremony. The customer journey is part of the banking service, not a separate design exercise. The ceremony identifies what the bank agrees to do, what evidence is required, how customers are informed, how exceptions are handled, and what completion means.

Driver discovery proceeds in parallel. ODTI and the bank examine approved API behavior, authentication, certificates, request and response structures, references, idempotency, webhooks, status, limits, exceptions, reversals, reconciliation evidence, test environments, and change processes. The behavior is mapped to `emi-core`, implemented in `3neti/emi-{bank}`, tested, and certified.

Certification is a technical gate. Operational readiness is a separate institutional gate. Bank personnel validate initiation, approvals, Funding Events, Treasury state, Liens, Facility rules, Settlement Envelope conditions, Pay Code presentation, execution, provider behavior, accounting, evidence, support, reconciliation, failure, delay, duplication, reversal, and uncertain outcomes as one banking operation.

Readiness is an institutional judgment. It exists when the bank has sufficient evidence that the ceremony can be authorized, operated, supervised, secured, settled, reconciled, supported, and governed under its authority.

Controlled production should be deliberately narrow. The bank may limit customers, branches, employers, merchants, values, operating windows, or duration. Success measures are agreed before the pilot and may address correct authorization, execution outcomes, reconciliation completeness and timeliness, exception resolution, service availability, customer evidence, support performance, security, and control effectiveness. Volume alone is not evidence of readiness.

The institution reviews the evidence and decides whether to **Proceed**, **Correct**, **Extend**, or **Pause**.

Expansion is phased, not automatic. A bank may extend the same Facility, introduce another channel, add a customer group, increase approved limits, or define a new ceremony. Each step repeats the disciplines of authority, conditions, readiness, controlled operation, and evidence.

The first approval authorizes institutional learning. Each later approval determines whether the bank is prepared to carry a larger responsibility.

## Appendices

- [Appendix A — Glossary](appendices/glossary.md)
- [Appendix B — Governance](appendices/governance.md)
- [Appendix C — Commercial Waterfall](appendices/commercial-waterfall.md)
- [Appendix D — Treasury Grammar](appendices/treasury-grammar.md)
- [Appendix E — Deployment Architecture](appendices/deployment-architecture.md)
- [Appendix F — Frequently Asked Questions](appendices/faq.md)
- [Appendix G — Canonical Diagrams](appendices/diagrams.md)
