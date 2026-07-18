# Thrift Bank Digital Banking Program Guide

## AllBank Edition

### Executive Edition

Version 0.9

## Foreword

AllBank has served the Philippine market in different institutional forms for more than six decades. Today, it operates as a thrift bank with visible relationships across working households, employers, entrepreneurs, merchants, corporations, and small and medium-sized enterprises.

Its public banking proposition already extends across deposits, consumer and commercial lending, payroll, corporate banking, merchant acceptance, collections, remittance, housing finance, mobile banking, online account opening, and corporate Internet banking. AllBank also participates in the country's principal retail-payment arrangements.

This is therefore not a guide to becoming digital for the first time.

It is a guide to a different institutional question: whether AllBank should establish one reusable governed operating Capability beneath its existing channels, products, payment connectivity, and customer relationships so that additional banking services may be introduced without rebuilding their operating foundations independently.

The Program does not replace AllBank's authority, channels, systems, providers, or settlement relationships. It begins with them. AllBank remains the bank, the customer institution, and the production authority throughout.

This Executive Edition adapts the canonical Thrift Bank Digital Banking Program Guide to AllBank's visible institutional context. It is intended to support an executive conversation about institutional capability. It is not a deployment proposal, a statement of AllBank approval, or a conclusion about operational readiness.

## Executive Summary

AllBank has already established substantial digital banking capability. Its public services span retail and corporate banking, digital onboarding, mobile access, payroll, bulk payments, merchant acceptance, collections, remittance, housing, and other lending relationships. It participates in InstaPay, PESONet, QR Ph, and Bills Pay PH and has repeatedly extended payment reach through institutional partnerships.

The question is not whether AllBank should become digital. It is whether the institution can organize more of its banking responsibilities through one reusable governed operating foundation.

Settlement connectivity is necessary, but it is not a banking service. A rail can move funds and an API can transmit an instruction. Neither defines what the customer requested, establishes purpose, applies policy, recognizes and reserves resources, gathers evidence, manages exceptions, communicates status, or reconciles the completed service. Those remain responsibilities of the bank.

The **Program** is the institution-specific initiative through which AllBank would evaluate and, if approved, establish that foundation. The enduring result is the **Capability**: a maintained operating foundation through which customer requests become authorized, observable, executable, and reconcilable banking activity.

AllBank remains the protagonist. It retains its banking authority, products, customer and deposit relationships, channels, infrastructure, data, policies, credentials, production authority, and settlement relationships. x-change supplies the operating grammar beneath those arrangements. `emi-core` provides the common execution contract, and an AllBank-specific driver—represented conceptually as `3neti/emi-allbank`—would map that contract to the institution's approved API behavior.

The bank brings the authority and the rails. x-change brings the operating grammar. The bank-specific driver connects them.

The driver is institution-specific engineering, not an automatically available connector. It would require institutional discovery, API mapping, implementation, certification, and continuing maintenance. Certification would establish technical behavior under tested conditions. It would not establish operational readiness. Readiness would remain an AllBank judgment based on the complete banking ceremony.

Remittance makes the model visible. A customer asks the bank to make funds available to another person. The bank recognizes the funds, applies policy, reserves the required capacity, defines the conditions, issues a Pay Code credential, coordinates execution through its approved settlement relationship, preserves evidence, and reconciles the result.

The customer requested a banking outcome. The bank arranged it.

The same Capability could support services already relevant to AllBank's visible business. Payroll connects employers and employees. Merchant services connect commerce, settlement, reporting, and business relationships. Collections connect payer information with attribution and reconciliation. Housing and commercial lending may require governed releases against purpose and evidence. Their commercial meaning, participants, policies, and customer journeys differ. The operating grammar remains stable.

Publicly available information cannot establish which of these services AllBank considers most strategically important or how the institution currently organizes the complete operating model supporting them. Those questions belong in institutional dialogue.

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

One foundation would not make every AllBank service alike. It would give the bank a consistent way to govern their differences.

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

The Program should be judged by whether it establishes the Capability under institutional control—not by the quantity of software installed.

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

AllBank modernizes without becoming less itself.

## Section 4 — How Does the Program Work?

> **Executive question:** How would the operating model work within AllBank?

> **Key message:** AllBank retains custody and authority. x-change coordinates the banking ceremony, and an AllBank-specific driver connects that ceremony to the institution's approved settlement capability.

> **Executive decision:** I understand where authority, funds, software, integration, execution, evidence, and reconciliation would reside.

The conceptual institutional stack is:

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

Remittance remains the canonical explanatory ceremony because it makes the complete discipline visible within one familiar request. AllBank has publicly presented remittance among its services, although the institution's current operating journey would need to be understood directly.

A customer asks the bank to make funds available to another person. The bank receives or recognizes the funds, confirms authority, applies policy, records the remittance purpose, and identifies the recipient and permitted conditions.

Treasury recognizes the supporting Settlement Resources. A Lien reserves the required amount. The remittance Facility defines participants, limits, commercial rules, customer communication, and service responsibility. The Settlement Envelope records evidence and conditions. Once authorized, a Pay Code permits the instruction to be communicated and presented through an approved journey.

The recipient presents the Pay Code and satisfies the conditions. Execution coordinates the instruction through the bank's approved relationship. The institution-specific driver translates the common execution contract into approved API behavior. The financial movement occurs. x-change records the result, updates operational state, resolves the Lien, preserves evidence, and supports reconciliation and customer communication.

The customer requested a banking outcome. The bank arranged it.

Publicly visible AllBank services suggest several other ceremonies worth executive consideration:

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

AllBank's public proposition already touches many of these relationships. The institutional question is whether selected services can reinforce one another through repeated usefulness.

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

The next step is dialogue.
