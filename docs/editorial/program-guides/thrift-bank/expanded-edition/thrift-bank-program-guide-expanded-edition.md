# Thrift Bank Digital Banking Program Guide

## Expanded Edition

### A Canonical Implementation Guide for Philippine Thrift Banks

## Executive Summary

Philippine thrift banks occupy a distinctive institutional position. They serve households, employers, merchants, property buyers, developers, entrepreneurs, and small and medium-sized enterprises through banking relationships that often extend across many years. Their relevance has never depended on transaction processing alone. It rests on the ability to understand a customer, accept deposits, extend credit, support enterprise activity, finance homes, and remain present as financial needs change.

The environment surrounding those relationships has changed. Customers now encounter real-time payments, mobile access, digital wallets, embedded payment experiences, and continuously available services in many parts of daily life. They reasonably expect their bank to be accessible and responsive. Yet adding another channel or payment connection does not by itself give an institution a coherent way to define, authorize, operate, evidence, support, and reconcile a growing range of banking services.

That distinction matters. Settlement connectivity can carry an instruction. It cannot determine why the instruction exists, whether the customer is entitled to request it, what funds or capacity support it, which conditions must be met, what evidence must be retained, how an uncertain outcome should be handled, or when the service is complete. Those are institutional responsibilities. They belong to the bank.

The Thrift Bank Digital Banking Program is an institution-specific modernization initiative through which a bank establishes one reusable governed operating foundation beneath its chosen products and channels. The **Program** is the time-bounded initiative that the Board authorizes and Management governs. Its enduring result is the **Capability**: a maintained institutional ability to turn recognized funds and authorized customer purpose into observable, executable, supportable, and reconcilable banking activity.

The bank remains the protagonist. It retains its banking authority, products, customer and deposit relationships, channels, infrastructure, data, policies, credentials, release decisions, production accountability, and settlement relationships. x-change supplies the operating grammar used to coordinate the banking ceremony. `emi-core` provides a common execution contract. A maintained bank-specific driver—represented as `3neti/emi-{bank}`—maps that contract to the institution's approved API behavior.

The bank brings the authority and the rails. x-change brings the operating grammar. The bank-specific driver connects them.

This arrangement does not make x-change another bank channel, settlement provider, or source of banking authority. It allows existing and future channels to rely on a consistent operating foundation. A branch, mobile application, corporate portal, partner interface, or assisted service may present a different customer experience while the bank governs financial state, conditions, execution, evidence, and reconciliation through one grammar.

The grammar begins when an external financial event is recognized through a **Funding Event**. **Treasury** maintains the operational state of the Settlement Resources supporting approved activity. A **Lien** reserves capacity for an authorized purpose. A **Facility** defines the banking service, its participants, policies, and commercial meaning. A **Settlement Envelope** records the evidence and conditions that must be satisfied. A **Pay Code** represents an authorized instruction as a credential that can be communicated, presented, validated, and executed. **Execution** coordinates the approved outcome through the bank's settlement relationship and returns evidence for support and reconciliation.

These concepts do not transfer custody away from the bank or create a second ledger of legal ownership. They make the operational responsibilities surrounding a banking service explicit. Funds remain within the bank's regulated arrangements. The bank decides what the service means, who may use it, when it may proceed, and what constitutes completion.

Remittance provides the clearest first view of the Capability. A customer asks the bank to make funds available to another person. The bank recognizes the supporting funds, applies policy, reserves the required capacity, records the purpose and conditions, issues a Pay Code credential, coordinates execution through its approved relationship, preserves evidence, and reconciles the result.

The customer requested a banking outcome. The bank arranged it.

The same operating grammar can support other institution-approved services. Payroll changes the mandate, scale, timing, and attribution. Collections change the direction of value and the obligation being satisfied. Merchant services connect payments to an enterprise relationship. SME disbursement applies enterprise authority and beneficiary controls. Housing-related workflows may require documentary conditions and staged releases. Customer-directed settlement can allow an authorized customer to select an approved destination without changing the bank's custody, policy, or execution responsibilities.

The institutional value is not the number of services listed. It is the ability to introduce and govern relevant services without reconstructing the same foundations each time. That can reduce duplicated engineering, improve observability, preserve institutional choice, and allow Management to focus scarce attention on customer relevance, service quality, risk, operations, and chosen markets.

Over time, useful services may also deepen recurring relationships. Salary can connect an employer and employees to the bank. Collections can reveal the operating rhythm of an enterprise. Merchant activity can connect deposits, liquidity, and credit. Housing can sustain a long relationship. Remittance can become a repeated family interaction. Financial activity is more likely to return to an institution that remains useful across more of these needs. This tendency is **Transaction Gravity**. It is not guaranteed volume or an entitlement to deposits. It is the relational effect of sustained institutional usefulness.

The Program begins with one bounded banking ceremony. Institutional discovery establishes the customer need, banking responsibility, funds flow, approvals, evidence, systems, support, and settlement arrangement. Driver discovery and API mapping identify how the common execution contract will address the bank's approved interface. Implementation and certification establish technical behavior under tested conditions. They do not establish operational readiness.

Readiness is an institutional judgment. The bank must decide whether the complete ceremony can be authorized, operated, supervised, secured, settled, reconciled, supported, and governed. Controlled production begins only when the evidence supports that decision. The institution then reviews the result and decides whether to proceed, correct, extend, or pause.

The decision before the Board is therefore more than whether technology may be useful. It is whether the institution should establish one reusable governed operating Capability; authorize Management to define and prepare the first banking ceremony; and require Management to return with evidence sufficient for a controlled production decision.

## Section 1 — Why This Program?

> **Executive question:** Why should our institution establish this Program?

> **Key message:** The bank already has authority, relationships, channels, technology, and settlement capability. The opportunity is to organize them through one governed operating foundation that can support more banking services over time.

> **Executive decision:** I understand the institutional problem and can decide whether establishing a reusable governed operating Capability merits formal evaluation.

### The Institutional Question

Thrift banks have evolved by carrying responsibilities that are both transactional and relational. They receive deposits and move funds, but they also finance homes, support employers, understand enterprises, and serve households through changing stages of financial life. Their strength lies in regulated authority joined to institutional memory: the bank knows why the relationship exists, how it has developed, and which responsibilities it is prepared to accept.

Modernization should extend that strength. It should not reduce the institution to a collection of payment connections or require it to surrender the relationships through which banking value is created. The relevant question is not whether a thrift bank can add another digital feature. It is whether the bank can make its established authority useful through more services, more channels, and more moments in the customer's financial life without creating a separate operating institution behind each one.

### How Banking Has Evolved

Customers no longer experience banking only through a branch or a single account. An employee may receive salary through one institution, pay through a wallet, borrow elsewhere, and use another provider for remittance. An SME may maintain deposits with a bank while directing collections, merchant receipts, payroll, and supplier payments through several platforms. A household may preserve a housing loan relationship while conducting most daily financial activity outside the lender.

This fragmentation does not mean the bank has become unnecessary. It means the practical center of the relationship can move even while the formal account remains. The institution may retain customer records and balances yet lose repeated visibility into income, payments, enterprise activity, and changing needs. Conversely, a bank that remains useful across those activities may deepen its understanding and relevance without becoming the exclusive provider of every financial service.

### Why Channels Are Not Enough

Most thrift banks are not beginning from an absence of technology. They may already operate core banking, branches, automated teller machines, mobile and Internet banking, corporate portals, payment connections, cybersecurity controls, data platforms, and professional technology organizations. These assets are essential. Their presence, however, does not guarantee a reusable operating model beneath them.

A channel presents an experience and carries a request. It does not necessarily establish how the bank will recognize supporting funds, reserve capacity, evaluate conditions, assign responsibility, instruct a provider, handle delay, preserve evidence, reverse or correct an outcome, and reconcile the service. If each product or channel implements those duties separately, the bank can appear digitally capable while remaining operationally fragmented.

The result is not merely duplicated software. It is duplicated institutional interpretation. Business, Operations, Treasury, Technology, Finance, Risk, Compliance, Security, and Support may each need to rediscover how a new service works and where responsibility rests. The work returns whenever the bank adds a channel, changes a provider, modifies a process, or introduces another banking ceremony.

### The Cost of Fragmentation

Fragmentation accumulates quietly. One service may use its own approval state; another may apply a different reference model; a third may reconcile against provider reports; a fourth may depend on manual exception handling known to a small operating team. Each can function. Together they make the institution harder to observe, change, and govern.

This complexity affects more than Technology. Operations must interpret inconsistent statuses. Treasury must understand how capacity is recognized and reserved. Finance must establish how results reach accounting. Support must explain uncertain outcomes to customers. Risk and Compliance must determine whether controls remain effective across variations. Management must decide whether apparently similar services are in fact governed by comparable standards.

The Program does not promise to eliminate institutional complexity. Banking services differ for good reasons. It seeks to separate necessary differences—customer purpose, product policy, participants, evidence, commercial rules—from foundational responsibilities that can be governed consistently.

### Customer Expectations and Institutional Responsibility

Customers experience immediacy as a service expectation. They also expect the bank to remain responsible when an outcome is delayed, declined, duplicated, or unclear. A fast interface does not reduce that expectation. It often increases it, because the customer assumes that an institution capable of accepting a request can also explain what happened.

The bank therefore requires more than an instruction that reaches a rail. It requires an operating record that connects the request to authority, purpose, funds, conditions, execution, evidence, customer communication, support, and reconciliation. That record allows the institution to respond as a bank rather than as an observer of a provider's status.

### Recurring Relationships

Thrift banking becomes more valuable when it participates in recurring activity. Payroll creates repeated contact with employers and employees. Collections and merchant services connect the bank to enterprise cash flow. Housing creates a long-duration relationship with a household and a network of counterparties. Remittance can connect family needs across locations. SME disbursement can place the bank within the operating cycle of a business.

No single ceremony guarantees a broader relationship. The opportunity arises because recurring usefulness gives the institution more occasions to serve well, understand needs, and earn the next interaction. A bank can become more relevant without attempting to hold every activity inside one product.

### Institutional Continuity

Technology changes faster than banking responsibility. Providers, interfaces, security methods, and payment arrangements will continue to evolve. The institution needs a way to accommodate those changes without allowing each one to redefine the banking service.

A governed operating foundation preserves continuity between what the customer requests and what the bank accepts responsibility to perform. Channels and providers may change around it. Product policies and services may evolve within it. The bank's authority, evidence, and accountability remain visible.

That continuity is the reason for the Program. The objective is not technology adoption in the abstract. It is an enduring institutional ability to govern more banking activity through a foundation the bank controls.

### Section Summary

The bank already possesses the essential institutional foundations of banking. The present limitation is that channels, products, and integrations can grow faster than the common operating discipline beneath them. The Program merits evaluation because it offers a way to make modernization reusable while preserving the authority, relationships, and judgment that distinguish the institution.

## Section 2 — What Is the Program?

> **Executive question:** What exactly is the institution being invited to establish?

> **Key message:** The Program is an institution-specific modernization initiative. Its result is a maintained operating Capability under the bank's authority and control.

> **Executive decision:** I understand the Program, the Capability it is intended to establish, the participating roles, and the boundaries that remain subject to institutional approval.

### Program and Capability

The **Program** is the institutional initiative. It has a sponsor, scope, governance, budget, sequence, participants, decisions, and evidence. It can be approved, implemented, reviewed, extended, or stopped. Its work includes institutional discovery, service definition, integration, deployment, testing, preparation, controlled production, and learning.

The **Capability** is the enduring operational result. It is the maintained ability to receive or recognize a customer request, connect that request to authority and purpose, represent the supporting financial state, apply conditions, coordinate execution through the bank's approved relationship, preserve evidence, support the customer, and reconcile the result.

The distinction prevents a familiar implementation error. Software can be installed and a project can be declared complete while the institution remains unable to operate the service dependably. Conversely, a Capability continues after the implementation project ends. It must be governed, maintained, observed, supported, and adapted as the bank's services and providers change.

### One Reusable Operating Capability

The Program does not make every banking service identical. Payroll is not remittance. Merchant acquiring is not an SME disbursement. A housing release has different parties, evidence, timing, and risk from a customer transfer. The value of the Capability is that these differences can be expressed within a stable set of institutional responsibilities.

The bank defines the banking product and Facility. It determines participants, policies, commercial terms, limits, evidence, approvals, customer treatment, and the meaning of completion. The operating grammar supplies a consistent way to recognize funding, reserve capacity, record conditions, issue an authorized credential, execute through approved arrangements, and preserve results.

Reuse therefore occurs beneath product meaning. It reduces repeated foundational work without flattening legitimate differences between services.

### The Participating Institution

The thrift bank is the Program sponsor, banking authority, customer institution, infrastructure owner or controller, production authority, and settlement principal. Its Board establishes the institutional purpose and boundaries. Management accepts implementation and operating accountability. Responsible functions apply the bank's existing governance to the new Capability.

Business defines the customer proposition and service obligations. Operations defines how the ceremony is performed and supported. Treasury governs liquidity and settlement capacity. Technology governs architecture, integration, credentials, deployment, observability, and change. Risk, Compliance, Legal, and Information Security evaluate the applicable duties and controls. Finance and Accounting define recognition and reconciliation. Internal Audit retains its independent role. The exact allocation follows the bank's organization; the responsibilities do not disappear because a provider performs technical work.

### ODTI and the Licensed Software

Open Disbursement Technologies, Inc. (ODTI) licenses and maintains x-change, `emi-core`, supported components, documentation, reference architecture, testing capability, and the bank-specific driver within agreed scope. It contributes the common operating grammar and the engineering necessary to connect that grammar to the institution's approved interface.

ODTI does not provide the bank's license, banking authority, customer relationship, deposit relationship, settlement participation, custody, risk appetite, or production decision. It does not become the operator of the banking service merely because its software helps coordinate the ceremony. Those boundaries are essential to a credible institutional model.

### The Bank-Specific Driver

The driver represented as `3neti/emi-{bank}` is institution-specific engineering. It is not assumed to exist because the bank has an API, and it is not a generic promise of compatibility. The work begins with discovery of the approved interface and the institutional meaning attached to its behavior.

Authentication, certificates, signatures, request formats, references, idempotency, status models, webhooks, limits, errors, reversals, timeouts, reconciliation evidence, test environments, versioning, and change notices must be understood. That behavior is mapped to the common `emi-core` contract, implemented, tested, reviewed, and certified. Continuing maintenance is required when the bank or provider changes the interface.

Driver certification establishes that agreed technical behavior works under tested conditions. It does not establish that the banking product, Operations, Treasury, Support, Finance, controls, or governance are ready for production.

### DevOps and Managed Operations

A DevOps or managed-service provider may perform delegated provisioning, deployment, monitoring, backup, recovery, release support, incident response, and other approved operational work. Delegation makes responsibilities executable; it does not transfer institutional ownership.

The provider acts within the bank's approved environment and access model. The bank owns or controls the environment, domains, provider accounts, credentials, data, security configuration, monitoring expectations, backup policy, and release authority. The provider must produce evidence sufficient for the bank to supervise the delegated work.

This model enables professional operational support while preserving operating sovereignty. The bank remains capable of determining what runs, where it runs, who may change it, and how its operation is evidenced.

### Settlement Relationships

The bank brings or establishes its own approved settlement relationships. A settlement institution or payment provider moves funds under its agreement with the bank and within the supported arrangement. The Program does not confer access to a rail and does not prescribe NetBank or any other exclusive settlement institution.

The bank owns or controls the relevant account, participation, credentials, limits, funding arrangements, and execution authority. x-change coordinates an approved instruction; the driver translates it; the provider performs the supported financial movement. This separation allows provider connectivity to change without silently changing who owns the customer relationship or who remains responsible for the banking service.

### Existing Channels and Banking Systems

The Capability is not a replacement for core banking, general ledger, customer records, fraud controls, channels, data platforms, or enterprise systems. It must coexist with the bank's architecture and address each system according to its institutional role.

Branches, mobile applications, Internet banking, corporate portals, partner channels, and assisted services may initiate or present activity. Core and accounting systems remain authoritative for the records assigned to them. x-change coordinates the governed ceremony and maintains the operational evidence required for that purpose. Integration design must identify which system owns each decision, record, status, and reconciliation responsibility.

This is why institutional discovery precedes implementation. A technically convenient connection is not sufficient if it obscures the bank's recordkeeping, control, or customer responsibilities.

### Governance Model

Governance follows responsibility. The Board authorizes institutional purpose, risk boundaries, sponsorship, and the basis on which Management may proceed. Management appoints accountable leaders and establishes the decision forums through which scope, design, readiness, controlled production, and expansion are approved.

Providers participate within assigned responsibilities. They may present evidence and recommendations, but they do not decide that the institution is operationally ready. The bank decides when a service may enter production, which customers may use it, what limits apply, how performance is reviewed, and whether expansion is justified.

The Program should use existing governance wherever it is fit for purpose. It should not create a parallel authority structure around software. Where existing committees or controls do not address a new responsibility, Management should make the gap explicit and approve the required treatment.

### Licensing and Commercial Boundaries

The bank licenses maintained software and separately approves the services required for its deployment and operation. Agreements should distinguish software licensing, institution-specific implementation, driver engineering and maintenance, managed operations, support, settlement-provider obligations, and internal bank costs.

These are different economic and accountability relationships. Combining them into one undifferentiated technology price would make it harder for the institution to understand what it is buying, what it continues to own, and which responsibilities survive a provider change.

The Program Guide does not set institution-specific prices or replace negotiated agreements. It establishes the categories that a sound commercial evaluation must address.

### What the Program Is Not

The Program is not a new bank, a shared bank, a payment switch, a settlement network, a wallet, or a transfer of banking authority to x-change. It is not merely an API project, because connectivity does not define the complete service. It is not merely a channel project, because the same ceremony may appear through several channels. It is not completed by driver certification, because technical capability is narrower than institutional readiness.

These exclusions are not defensive qualifications. They identify the operating boundaries that allow the Program to strengthen the bank without confusing software, providers, and institutional authority.

### Section Summary

The Program is an institution-specific path to one reusable Capability. The bank remains responsible for banking; ODTI supplies and maintains the operating grammar and agreed integration; operational providers act under delegated authority; settlement providers move funds under the bank's relationship. The Program succeeds when the bank can govern and operate the resulting Capability—not when software has merely been installed.

## Section 3 — Why Should the Institution Proceed?

> **Executive question:** What does the institution gain by proceeding?

> **Key message:** The bank gains a reusable governed foundation through which it can introduce and evolve banking services while preserving its authority, relationships, channels, and operating sovereignty.

> **Executive decision:** I understand the prospective institutional benefit and can decide whether it warrants commercial and implementation evaluation.

### Operating Leverage

The first institutional benefit is operating leverage. A maintained grammar for authority, funding recognition, reservation, conditions, credentials, execution, evidence, and reconciliation reduces the foundational work repeated for each banking service.

The bank still performs product design, risk assessment, governance, integration review, training, customer treatment, support, and financial evaluation. Reuse does not remove institutional work. It gives that work a more stable foundation and allows teams to begin with responsibilities already understood rather than reconstructing them from separate channel and provider implementations.

### Customer Retention and Relevance

Customer retention is not secured by an account alone. A customer may maintain a deposit or loan while directing daily activity elsewhere. The bank preserves relevance when it remains useful across recurring needs and responds dependably when those needs create exceptions.

The Capability gives the institution a way to add relevant services without allowing each service to become its own operating island. That can make it easier to connect new experiences to an established relationship and to preserve a coherent record of how the bank has served the customer.

### CASA and Recurring Activity

Current and savings account relationships can become stronger when recurring financial activity passes through the institution. Payroll, collections, merchant receipts, household payments, and remittance may create reasons for customers to retain and use balances. The Program does not guarantee CASA growth, and no service should be approved on that assumption alone.

The institutional opportunity is more disciplined: useful services may increase the number of legitimate occasions on which the bank participates in a customer's financial life. Management can then evaluate whether the resulting activity supports deposits, liquidity, service income, credit relationships, or customer retention under the bank's own strategy.

### Employers, Merchants, and SMEs

Payroll is more than a batch payment. It connects the bank to an employer's authority, funding, schedule, employee attribution, exceptions, and evidence. When operated well, it can also introduce employees to deposit, payment, remittance, savings, and credit relationships.

Merchant services and collections place the bank closer to enterprise operating activity. They can improve visibility into the timing and character of receipts while giving the enterprise a more coherent relationship between transactions, deposits, liquidity, and financing. SME disbursement can apply enterprise mandates and approval structures to supplier or beneficiary payments through the same governed foundation.

These relationships retain their own commercial and risk logic. The Capability does not make an unsuitable product suitable. It allows the bank to evaluate and operate suitable products without rebuilding the operating grammar beneath each one.

### Housing and Long-Duration Relationships

Housing finance demonstrates why a thrift bank requires more than payment capability. The relationship may involve borrowers, sellers, developers, brokers, insurers, appraisers, documentary conditions, scheduled obligations, and staged releases. The banking value lies in governing the relationship over time, not merely sending a final transfer.

A reusable Capability can support approved housing-related ceremonies while the bank's lending, legal, documentary, and credit systems retain their authority. Conditions and evidence can be associated with an authorized purpose; execution can occur only when the bank's requirements are met; the resulting record can support operations and reconciliation.

### Institutional Optionality

The bank cannot know every service, channel, or provider it will require during the next decade. Institutional optionality is the ability to respond to those changes without surrendering authority or rebuilding the same foundations repeatedly.

Optionality does not mean pursuing every opportunity. It means preserving the practical capacity to evaluate one. A bank with a maintained operating Capability can decide that a proposed service is strategically irrelevant, commercially unsound, or operationally premature. That ability to say no from a position of capability is as valuable as the ability to proceed.

### Technology Investment

Technology investment becomes more durable when it creates a reusable institutional asset rather than a single product integration. The bank's investment includes software, driver engineering, deployment, control design, observability, documentation, training, and operating knowledge. These elements should remain useful as the institution adds approved ceremonies or changes channels and providers.

The relevant comparison is therefore not simply the price of one integration against the price of one license. It is the long-term cost of repeatedly creating separate operating arrangements compared with establishing and maintaining one governed foundation. That comparison must include internal effort, provider dependence, control duplication, support complexity, change cost, and the value of institutional learning.

### Long-Term Economics

The Program's economics should be evaluated without invented projections. Costs may include licensing, implementation, bank-specific driver work, infrastructure, managed operations, cybersecurity, internal governance, support, settlement-provider charges, maintenance, and continuing improvement.

Value may arise through service income, stronger deposit relationships, deeper employer and merchant relationships, reduced duplicated engineering, improved operational visibility, better exception handling, and faster introduction of services the bank has independently determined to be worthwhile. Each source of value requires evidence and remains subject to the bank's product, financial, risk, and accounting judgments.

The enduring proposition is not that every service will succeed. It is that the institution can make those decisions through a reusable Capability rather than through repeated foundational reinvention.

### Section Summary

The Program can improve operating leverage, preserve customer relevance, connect the bank to recurring household and enterprise activity, and create a more durable basis for technology investment. Its benefits remain conditional on disciplined service selection and operation. The institution proceeds because it values the capacity to govern and evolve banking services—not because software alone promises a commercial result.

## Section 4 — How Does the Program Work?

> **Executive question:** How does the operating model work?

> **Key message:** The bank retains custody and authority. x-change coordinates the banking ceremony, and the bank-specific driver connects that ceremony to the institution's approved settlement capability.

> **Executive decision:** I understand where authority, funds, software, integration, execution, evidence, and reconciliation reside.

### Banking Before Technology

The operating model begins with a banking responsibility. A customer or authorized institution asks the bank to produce an outcome. The bank decides whether the request belongs to an approved product, whether the person or institution has authority, what resources support it, which conditions apply, how execution may occur, what evidence must remain, and what the bank will communicate if the outcome is delayed or uncertain.

Technology makes these responsibilities observable and repeatable. It does not create them. The architecture should therefore be read from the customer request downward, not from a software component upward.

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

The channel presents the experience. The product defines the bank's proposition and responsibility. x-change coordinates the ceremony. `emi-core` supplies the common execution contract. The bank-specific driver translates that contract into approved API behavior. The bank's API, account, and settlement arrangement remain under institutional authority.

### Funding Event

A banking ceremony needs an explicit point at which the institution recognizes the external financial event supporting it. That point is the **Funding Event**. It may record a confirmed deposit, approved funding instruction, account movement, or other event the bank has determined is sufficient for Treasury to recognize Settlement Resources.

The Funding Event does not create money and does not determine legal ownership. It records that the institution has recognized an external event according to approved rules. The source evidence, time, amount, reference, account relationship, and status allow Operations, Treasury, Finance, and Support to understand why operational capacity appears.

For the customer, this recognition connects funds to the requested service. For Operations, it establishes an observable entry into the ceremony. For Treasury, it changes the operational state it is responsible to monitor. For settlement, it does not move funds by itself; it establishes the bank's basis for later instructions.

### Treasury

**Treasury** maintains the operational state of Settlement Resources supporting approved banking activity. It answers practical questions: what resources have been recognized, what amount remains available for authorized use, what has been reserved, what is in execution, and what has been resolved or requires attention.

This operational view does not replace the bank account, core banking record, general ledger, or legal characterization of funds. It allows the ceremony to coordinate financial responsibility without pretending to become the bank's accounting system. Reconciliation connects the operational view back to the authoritative institutional and provider records.

Treasury is therefore both a control and a shared language. Business can understand whether a service has supporting capacity. Operations can see why an instruction may or may not proceed. Technology can implement consistent state transitions. Finance can trace those transitions to accounting and settlement evidence. Management can observe exposure and unresolved activity.

### Lien

Recognition alone is insufficient when several instructions may rely on the same capacity. A **Lien** reserves Settlement Resources for an authorized purpose while the instruction remains outstanding. It prevents the institution from treating committed capacity as freely available for another ceremony.

The Lien is not a transfer to the customer, a deposit product, or a change in legal ownership. It is an operational reservation. Its lifecycle must be tied to the authorized instruction and resolved according to the outcome: consumed, released, expired, reversed, or escalated under bank-defined rules.

For a customer, the Lien may appear only through service status or the availability of the request. For Treasury and Operations, it explains why capacity is unavailable and which obligation it supports. For reconciliation, it provides the link between recognition, reservation, execution, and final resolution.

### Facility

A **Facility** gives the ceremony its banking meaning. It identifies the service, participants, authorities, policies, limits, commercial rules, customer treatment, and institutional owner. Remittance, payroll, merchant services, collections, SME disbursement, and housing-related releases differ because their Facilities express different responsibilities.

Commercial semantics belong to the Facility. A Pay Code does not decide what a service costs, who earns a fee, or which customer relationship is being served. Treasury does not decide the product purpose. The Facility places those decisions where the bank can govern them as part of a banking service.

The Facility also protects reuse. The same operating grammar can support different services because each Facility preserves the differences that matter. A new service should not require a new definition of funding, reservation, execution, or evidence merely to express a different banking purpose.

### Settlement Envelope

An authorized purpose must still satisfy conditions before execution. The **Settlement Envelope** records the evidence and requirements attached to the instruction. Those may include identity, beneficiary information, approvals, limits, documents, signatures, one-time passwords, account status, purpose, timing, or other bank-defined controls.

The Envelope is not a document folder added after the transaction. It is the governed expression of what the bank requires before it is prepared to execute. Conditions may be satisfied through a channel, branch process, enterprise mandate, bank review, or another approved source. The institution decides which evidence is authoritative and how exceptions are handled.

For the customer, the Envelope becomes the requirements of the service. For Operations, it provides an observable readiness state. For Risk and Compliance, it locates relevant controls within the ceremony. For Technology, it prevents a provider success response from being mistaken for authorization that the bank never established.

### Pay Code

Once purpose, authority, funding, and conditions are governed, the bank may represent the authorized instruction through a **Pay Code**. The Pay Code is a credential. It can be communicated, presented, validated, and used to request execution according to the Facility and Settlement Envelope.

It is not money, a wallet balance, a deposit, stored value, a settlement account, or the banking service itself. The customer purchases or requests a banking outcome. The Pay Code is the credential through which the approved instruction can be completed.

This distinction makes the credential useful across channels without allowing the channel to redefine the service. A Pay Code might be presented by a recipient, communicated to an employee, associated with a merchant or obligation, or used in another bank-approved journey. Its meaning always comes from the Facility and the governed instruction behind it.

### Execution

**Execution** coordinates the transition from an authorized instruction to the outcome defined by the Facility. The execution engine applies the common contract. The bank-specific driver translates that contract into the bank's approved API behavior. The provider or settlement arrangement performs the supported financial movement.

Execution must address more than the happy path. Requests may time out, return uncertain status, be declined, duplicate a previous reference, exceed a limit, encounter an unavailable provider, or require reversal or investigation. The operating model must preserve enough state and evidence for the bank to determine what it knows, what it does not yet know, and which action is permitted.

The software does not independently decide the bank's policy for those circumstances. It implements the approved progression and exposes the evidence needed for responsible handling.

### Evidence and Reconciliation

Every ceremony produces institutional evidence: the original request, authority, funding recognition, reservations, conditions, approvals, execution attempts, provider references, status changes, customer notifications, exceptions, interventions, and resolution. This record allows the bank to support customers, supervise providers, investigate incidents, and demonstrate how an outcome occurred.

Reconciliation compares the operational record with the bank's authoritative accounts, provider records, and applicable accounting treatment. It is not a final administrative step added after execution. It is part of the definition of a complete banking service.

An instruction that appears successful to a customer but cannot be reconciled remains an institutional concern. An instruction that appears uncertain in a channel may already have settled and must not be repeated casually. Evidence and reconciliation allow the bank to distinguish these states and respond consistently.

### Custody and Authority

At no point does the operating grammar transfer custody to x-change. Funds remain within the bank's regulated relationships and move only through arrangements the bank has approved. The bank controls the accounts, credentials, limits, product rules, and authority by which execution occurs.

The same principle applies to institutional judgment. Software may evaluate configured conditions and providers may report technical outcomes. The bank remains responsible for determining what those outcomes mean within the banking service, how customers are treated, and whether production should continue.

### The Bank-Specific Driver in Operation

The driver connects a stable banking execution contract to interface behavior that is specific to the institution. It may translate authentication, message structure, references, status, errors, callbacks, and reconciliation evidence. It should isolate provider-specific or bank-specific change from the product meaning expressed elsewhere in the ceremony.

Isolation does not make the driver trivial. A change in authentication, certificate policy, API version, field meaning, idempotency behavior, or status interpretation can affect execution. The bank and ODTI must therefore govern discovery, implementation, testing, certification, release, monitoring, and maintenance as a continuing lifecycle.

### Operational Readiness

Technical certification demonstrates that agreed software behavior works under tested conditions. Operational readiness answers a wider question: can the bank safely accept responsibility for the complete service in production?

That judgment requires evidence from Business, Operations, Treasury, Technology, Finance, Support, Risk, Compliance, Security, Legal, and other responsible functions. It includes normal activity and exceptions; customer communication and internal escalation; settlement and reconciliation; access, monitoring, backup, recovery, and change; and the authority to pause when evidence becomes insufficient.

Readiness is an institutional judgment, not a technical declaration.

### Section Summary

The operating model keeps purpose, funds, conditions, credential, execution, and evidence distinct while connecting them through one ceremony. Each component exists because the bank has a responsibility that must remain observable. The architecture supports the institution precisely by allowing that architecture to recede behind a banking service the customer can understand.

## Section 5 — Banking in Action

> **Executive question:** Show me how the Capability works in practice.

> **Key message:** One operating grammar supports different banking services because purpose and policy may change while the responsibilities beneath them remain governed consistently.

> **Executive decision:** I can recognize how the operating model applies to a familiar ceremony and how the same foundation can support other institution-approved services.

### An Ordinary Banking Request

A customer enters a branch and asks, “Can I send money to my daughter?”

The teller does not begin by describing Treasury, Settlement Envelopes, drivers, or APIs. The teller explains the service: the information required, the amount and charges, how the daughter will receive or claim the funds, how long the instruction remains valid, and what the customer should retain.

The customer provides the funds and required information. The bank accepts responsibility for arranging the requested outcome under its approved remittance service. The daughter later presents the credential, satisfies the conditions, and receives the outcome through the bank's approved arrangement.

### What Did the Customer Purchase?

The customer purchased a funded banking outcome delivered through a governed banking service. The customer did not purchase an API call, access to a payment rail, or a piece of software. The bank accepted the request, applied its authority, and arranged the result.

This is familiar banking behavior. A customer who requests a manager's check does not usually describe the instrument through its legal and settlement mechanics. The customer understands that the bank has accepted responsibility to complete a defined payment. The banker and the customer may describe the same service differently because the institution must govern details the customer should not be required to master.

The Pay Code occupies a similarly restrained place in the remittance ceremony. It is the credential through which the approved instruction can be presented and executed. It is not the value and not the service.

The customer requested a banking outcome. The bank arranged it.

### The Customer Perspective

The sender experiences a request, disclosed terms, payment or funding, a credential, status, and evidence. The recipient experiences presentation, validation, fulfillment, and confirmation. Both should understand what the bank has promised and what they must do without needing to understand the operating grammar beneath the service.

When something does not proceed normally, the customer needs the bank to explain whether the instruction is pending, declined, expired, completed, or under investigation. The quality of the operating record becomes part of the customer experience because it determines whether the institution can answer with confidence.

### The Operations Perspective

Operations sees a complete ceremony. The request belongs to a remittance Facility. The bank has recognized supporting funds through a Funding Event. Treasury shows the corresponding capacity and Lien. The Settlement Envelope records identity, recipient information, approvals, limits, and other conditions. The Pay Code is issued only within that governed state.

Operations also sees the exceptions. A recipient may present incomplete information. A credential may expire. A provider may return an uncertain result. A customer may dispute completion. Each case requires an approved path, an accountable role, and sufficient evidence to act without creating a second unintended outcome.

### The Treasury Perspective

Treasury sees why capacity exists, what amount has been reserved, which instruction relies on it, what has entered execution, and how the result should resolve the Lien. This prevents an attractive customer experience from depending on invisible or duplicated settlement capacity.

Treasury does not need to adopt the customer's language, but its operational state must remain traceable to the customer obligation. When a reservation remains unresolved, the institution should be able to identify the service, instruction, provider status, and required action.

### The Technology Perspective

Technology sees channel initiation, product and Facility configuration, identity and authorization sources, x-change state, the `emi-core` contract, driver behavior, API credentials, provider responses, observability, and evidence. Its responsibility is not merely to make a request succeed. It must make normal and exceptional behavior supportable within the bank's architecture and control environment.

The bank-specific driver isolates approved API behavior, but Technology still governs release, certificates, secrets, monitoring, capacity, backup, recovery, incident handling, and change. A technically correct driver becomes useful only as part of a complete institutional operation.

### The Settlement Perspective

The settlement institution or payment provider receives an instruction through the bank's approved relationship and performs the supported financial movement. It may validate credentials, apply its own limits and controls, return references, and report status under the applicable agreement.

That provider does not define the remittance product or own the bank's customer obligation. Its evidence becomes part of the bank's operating record and reconciliation. If provider status is uncertain, the bank must use the agreed inquiry and exception process rather than assume that no movement occurred.

### The Management Perspective

Management sees whether the bank is delivering the service it approved. It considers customer treatment, service performance, unresolved items, reconciliation, control effectiveness, provider dependence, cost, and relationship value. It also decides whether evidence supports expansion, correction, or pause.

The Capability gives Management a consistent basis for comparing ceremonies without pretending that their commercial purpose is the same. A rise in transaction count is informative, but it is not by itself proof of institutional value or readiness for broader scope.

### The Support Perspective

Support sees the customer at the moment when the ceremony is least abstract. The customer wants to know what happened and what the bank will do next. Support therefore requires clear statuses, customer-safe explanations, provider references, escalation paths, and authority for permitted remedies.

A governed ceremony reduces dependence on informal interpretation. It allows the institution to answer from an evidence trail connected to the banking obligation rather than from disconnected channel and provider screens.

### Payroll

Payroll reuses the same grammar but changes the banking purpose. An employer authorizes a payroll obligation and provides funding according to the bank's approved arrangement. The Facility defines the employer, employee attribution, schedule, limits, approvals, charges, notifications, exceptions, and service responsibility.

Treasury recognizes and reserves capacity. Settlement Envelopes record enterprise authority and required evidence. Pay Code credentials or equivalent authorized instructions represent employee outcomes. Execution coordinates approved release and preserves evidence for the employer, employees, bank, and reconciliation.

The value is not a remittance flow multiplied by many recipients. It is a governed employer relationship that can connect recurring income, deposits, service, and future banking needs.

### Collections

Collections reverse the direction of attention. The bank must identify the payer, obligation, enterprise, reference, amount, timing, and exceptions so that received value is attributed correctly. A successful payment that cannot be associated with the intended obligation is not a complete collection service.

The Facility defines the collection purpose and parties. Funding Events record recognized receipts. The operating record connects customer or payer evidence to enterprise reporting and bank reconciliation. The same grammar supports a different institutional promise: not merely to receive funds, but to identify what the payment satisfied.

### Merchant Services

Merchant services connect accepted payments to a broader enterprise relationship. The bank governs merchant eligibility, instruments, settlement timing, fees, reserves where applicable, exceptions, and evidence. Treasury and reconciliation connect accepted activity to settlement and the merchant's deposit relationship.

The Capability does not replace acquiring rules or provider obligations. It gives the bank a consistent way to express and observe the service around them. That visibility can help Management understand the relationship between transaction activity, deposits, liquidity, service quality, and credit opportunity.

### SME Disbursement

An SME disbursement begins with enterprise authority. The bank must understand who may instruct, which approvals apply, what purpose and beneficiary information are required, how funding is recognized, what limits govern release, and which evidence the enterprise needs.

The Facility expresses those mandates and policies. The Settlement Envelope records the conditions. Treasury reserves capacity. Execution addresses the approved destination through the bank's relationship. Evidence supports the enterprise, the bank, and reconciliation. The ceremony helps the bank remain within the operating rhythm of the SME rather than appearing only at the moment of borrowing.

### Housing-Related Ceremonies

Housing may require controlled releases to sellers, developers, contractors, insurers, or other approved parties. Documentary conditions, milestones, loan authority, borrower obligations, and payee validation can matter as much as the final movement of funds.

The operating grammar allows those conditions to be made explicit without replacing the loan system, credit decision, collateral records, or legal process. The Facility defines the approved banking purpose. The Settlement Envelope records required evidence. Execution occurs only through the bank's authority and preserves a traceable result.

### Customer-Directed Settlement

Some services may allow an authorized customer to select an approved recipient or destination at the time of use. Customer direction does not transfer custody or product authority away from the bank. The Facility defines the permitted choices, the Settlement Envelope records the conditions, and the bank controls how execution occurs.

This distinction allows flexibility at the edge of the service while maintaining institutional control beneath it. The customer can direct an approved outcome; the customer does not redefine the bank's settlement relationship or operating responsibilities.

### One Ceremony, Many Services

The ceremonies differ in participants, purpose, policy, timing, evidence, and commercial meaning. They remain comparable because the same institutional questions recur: what funds or capacity support the request, who has authority, which conditions must be met, how execution may occur, what evidence remains, and how the result is reconciled.

The Program does not replace familiar banking services. It organizes them through one consistent operating model.

The Program begins with one familiar banking ceremony. From that ceremony, the institution may progressively modernize others without changing the operating foundation beneath them.

## Section 6 — The Institutional Case

> **Executive question:** What kind of institution can the Program help the bank become?

> **Key message:** The Capability can deepen relationships, preserve institutional choice, and lower repeated innovation cost while commercial value remains dependent on disciplined service selection and operation.

> **Executive decision:** I understand the institutional and commercial case and can decide whether it merits detailed evaluation under the bank's strategy and financial authority.

### Relationships Before Transactions

A transaction can be completed without creating a relationship. Banking value develops when the institution remains useful before, during, and after the transaction: it understands the purpose, handles exceptions, connects the activity to other needs, and earns the customer's return.

This is why the institutional case cannot be reduced to payment volume. The same number of transactions can represent very different relationships. Payroll may be a file-processing service or the beginning of employee banking. Merchant settlement may be a provider pass-through or part of a broader deposit and credit relationship. The Capability gives the bank a foundation; strategy and service determine what the institution builds upon it.

### Transaction Gravity

A customer may keep an account with one bank while salary, payments, collections, merchant receipts, and remittance occur elsewhere. The formal relationship remains, but financial activity has found other centers. The reverse is possible when an institution becomes repeatedly useful across legitimate needs.

Payroll may bring income into the bank. Collections and merchant services may connect enterprise receipts. SME payments may connect supplier activity. Housing may connect a household over many years. Remittance may create recurring contact with a family. Over time, financial activity is more likely to return to an institution that remains useful across more of these needs.

This tendency is **Transaction Gravity**.

Transaction Gravity is not automatic deposit growth, customer lock-in, or a claim that every service should remain inside one bank. It describes the relational effect of usefulness. Customers and enterprises naturally return to institutions that help them complete important financial activity dependably and coherently.

### Resilience

Resilience is the ability to continue operating through disruption. The Program can support resilience by making responsibilities, states, evidence, provider boundaries, and exception paths more observable. A bank that knows which instructions are authorized, reserved, executing, uncertain, or reconciled is better positioned to respond when a channel or provider fails.

Resilience still depends on architecture, security, continuity planning, backups, recovery, personnel, provider arrangements, and tested procedures. The operating grammar does not replace those disciplines. It gives them a clear banking context: continuity exists to preserve the institution's accepted obligations and evidence.

### Adaptability

Adaptability is different. It is the ability to assume a new responsibility without rebuilding the institution beneath it. A bank may need to add a provider, change an interface, support a new customer journey, introduce another enterprise service, or respond to a new market expectation.

A maintained Capability allows the bank to preserve product meaning and institutional controls while changing selected channels, drivers, or settlement arrangements. It does not make change effortless. It makes the scope of change more intelligible and reduces the likelihood that a technical substitution silently rewrites the banking service.

### Institutional Capability

Capability includes software, but it also includes people, policy, governance, records, operating knowledge, provider management, and the evidence by which the institution decides. That is why the Program cannot be judged solely by deployment completion or interface certification.

An institution has established the Capability when it can define a ceremony, prepare responsible functions, operate and support normal and exceptional outcomes, reconcile the result, supervise providers, and decide responsibly whether to expand. The Capability belongs to the bank because the bank retains the authority and knowledge required to use it.

### Commercial Sustainability

Commercial sustainability requires the service model to support dependable operation over time. Costs may include license, implementation, driver engineering and maintenance, infrastructure, managed operations, internal staffing, security, support, settlement charges, and continuing improvement. These costs should be visible rather than hidden inside an undifferentiated promise of innovation.

Potential value may include service income, deeper deposits, employer and merchant relationships, improved retention, reduced duplicated engineering, better operational visibility, and the ability to introduce relevant services more efficiently. None should be assumed without institutional analysis.

The Commercial Waterfall identifies where customer or institutional service economics arise, which provider and operating obligations must be met, and what residual financial and institutional value the bank evaluates. It is a governance tool for clarity, not a substitute for pricing, forecasts, accounting treatment, or negotiated agreements.

### Collective Learning Without a Collective Bank

Thrift banks may benefit from common software, documented patterns, maintained components, and learning that improves the platform over time. That commonality does not create common banking authority, pooled customers, shared custody, or a common production environment.

Each institution evaluates and operates its own Program. Common engineering can lower repeated innovation cost while institutional decisions remain specific. The distinction allows the ecosystem to learn without asking the bank to become less independent.

### The Board's Institutional Decision

The Board is not being asked to approve a catalogue of possible products. It is being asked whether the bank should establish the governed capacity to evaluate, introduce, and operate relevant products through one maintained foundation.

That decision should reflect strategy, risk appetite, customer need, institutional capacity, commercial discipline, and the willingness to govern the Capability after implementation. Approval is justified only if Management can define a bounded first ceremony and return with evidence for the next decision.

### Section Summary

The institutional case joins relationships, adaptability, resilience, operating leverage, and commercial discipline. The Capability can make the bank more able to serve; it cannot decide where the bank should compete or guarantee that customers will return. Those outcomes remain the product of institutional judgment and dependable banking.

## Section 7 — Launching the Program

> **Executive question:** What happens after approval?

> **Key message:** Approval begins a controlled institutional journey from discovery to one bounded production ceremony. It does not place the bank into production.

> **Executive decision:** I understand the sequence, evidence, governance gates, and next decision required to begin controlled implementation.

### Establish Executive Sponsorship

Board approval establishes purpose, boundaries, accountable sponsorship, and the authority for Management to proceed with defined work. It should identify the institutional outcome being evaluated, the basis on which resources may be committed, and the evidence required before controlled production.

Management appoints an executive sponsor and responsible leaders. Business, Operations, Treasury, Technology, Finance, Risk, Compliance, Legal, Information Security, Internal Audit, Support, and providers participate according to the bank's governance. The Program should not be delegated to Technology as though it were an integration project.

Board approval begins the Program. It does not place the bank into production.

### Understand the Institution

Implementation begins with understanding the institution. The team examines the customer need, current product and channel, authority, source and destination of funds, policies, approvals, evidence, systems of record, accounting, reconciliation, support, exceptions, settlement arrangements, provider agreements, and institutional owners.

This discovery should describe current practice honestly, including manual work, local knowledge, unresolved ambiguity, and controls that exist outside formal systems. The purpose is not to automate every current step. It is to understand what responsibility the bank already carries and which treatment should govern the future ceremony.

### Select the First Service

The first service should be institutionally meaningful and operationally bounded. Remittance remains the canonical explanatory ceremony, but it need not be the first production choice. The bank may select payroll, collections, merchant services, an SME disbursement, or another approved ceremony if it offers a clearer need, manageable scope, accountable participants, and a realistic opportunity to learn.

Selection should consider customer value, operating familiarity, settlement readiness, data and evidence, provider dependencies, internal capacity, exception complexity, and the ability to limit exposure. A service is a poor pilot merely because it is technically easy if it teaches the institution little or carries no strategic relevance.

### Define the First Banking Ceremony

The bank defines what it agrees to do for the customer, who may request it, how funding is recognized, what conditions apply, how capacity is reserved, what the Pay Code or authorized instruction represents, how execution occurs, what evidence is retained, how exceptions are handled, and what completion means.

The customer journey is defined as part of the banking service, not as a separate design exercise. Disclosures, notifications, status, support, and remedies must correspond to the actual institutional states beneath the experience.

The resulting definition becomes the shared object of review. Business can confirm the proposition; Operations can confirm the ceremony; Treasury can confirm financial state; Technology can confirm systems and integration; control functions can confirm treatment; Finance can confirm records and reconciliation; Support can confirm customer handling.

### Conduct Driver Discovery

Driver discovery examines the bank's approved API and the institutional environment around it. The team identifies authentication, certificates, network controls, signatures, message structures, reference generation, idempotency, status, callbacks, limits, errors, timeouts, reversals, inquiries, reconciliation evidence, test data, environment access, versioning, support, and change notification.

Discovery also determines what the interface does not provide. A missing status, inconsistent reference, limited test environment, or unclear reversal path may require a bank process, provider clarification, interface change, or a narrower first ceremony. The gap should not be hidden inside driver code.

### Map and Implement the Driver

The discovered behavior is mapped to the common `emi-core` execution contract. The mapping identifies which bank or provider state corresponds to each common request, response, status, and exception. ODTI implements `3neti/emi-{bank}` within agreed scope and maintains traceability between the contract and approved interface behavior.

Implementation includes normal and exceptional paths. It must address duplicate requests, delayed responses, ambiguous outcomes, provider errors, credential rotation, logging, sensitive data, observability, and the evidence needed for inquiry and reconciliation. The bank governs access, review, environments, and release.

### Certify Technical Behavior

Certification demonstrates that the driver performs the agreed behavior under tested conditions. Tests should cover successful execution and the failures that could create operational uncertainty or financial exposure. Evidence should identify the interface version, environment, credentials or certificate context, test cases, results, known limitations, and approvals.

Certification is necessary but narrow. It does not demonstrate that staff are prepared, accounting is correct, support can respond, reconciliation closes, provider arrangements are adequate, or the complete service complies with bank policy.

Driver certification is not operational readiness.

### Test the Complete Ceremony

The bank tests the operation from request through final reconciliation. This includes channel behavior, product rules, authority, Funding Events, Treasury state, Liens, Facility policies, Settlement Envelope conditions, Pay Code presentation, execution, provider behavior, evidence, accounting, customer communication, support, and resolution.

Testing should include normal completion, rejection, expiry, duplication, insufficient capacity, failed conditions, timeout, uncertain provider status, delayed callback, reversal where supported, reconciliation difference, credential failure, and service interruption. The objective is not to prove that failure never occurs. It is to prove that the institution can recognize and govern it.

### Determine Operational Readiness

Responsible functions review the complete evidence and determine whether the bank can accept production responsibility. Readiness includes documented authority, trained personnel, approved procedures, service and support coverage, settlement and reconciliation, monitoring and alerting, access control, incident escalation, backup and recovery, provider contacts, change governance, customer communication, and the authority to pause.

Readiness is an institutional judgment, not a technical declaration. A project schedule cannot make the institution ready. Neither can a provider's assurance. The decision belongs to the bank and should identify any conditions or limits that continue into controlled production.

### Prepare the Institution

Preparation turns an approved design into an operation people can perform. Personnel rehearse ordinary and exceptional journeys. Support scripts and escalation paths reflect actual system states. Treasury and Finance agree how unresolved items and reconciliation differences are handled. Technology confirms monitoring, access, capacity, continuity, and release support. Management confirms decision rights during the pilot.

The institution also prepares customers and participating enterprises where required. Terms, instructions, notifications, service windows, limits, privacy treatment, and support routes should be understandable before the bank accepts the first production request.

### Begin Controlled Production

Controlled production is deliberately narrow. The bank may limit eligible customers, branches, employers, merchants, values, destinations, operating windows, transaction counts, or duration. These limits should reflect the risks and learning objectives of the ceremony, not an arbitrary desire to call the service a pilot.

Success measures are agreed in advance. They may include correct authorization, completion and decline behavior, reconciliation completeness and timeliness, unresolved instructions, exception resolution, support performance, customer evidence, security events, provider availability, and control effectiveness. Volume alone is not evidence of readiness or value.

### Review the Evidence

Management reviews operational and customer evidence against the agreed measures. The review should identify what worked, what required intervention, where evidence was insufficient, which assumptions proved incorrect, and what the institution learned about the service and its own operation.

The decision is to **Proceed**, **Correct**, **Extend**, or **Pause**. Proceed confirms that the bounded scope may continue. Correct requires remediation before continuation or expansion. Extend allows further observation within defined limits. Pause protects the institution and customers while evidence or capability is restored.

### Expand Deliberately

Expansion may add customers, branches, employers, merchants, value limits, operating windows, channels, providers, or another banking ceremony. Each change should identify which established evidence remains valid and which responsibilities must be reviewed again.

A new channel may preserve Facility and Treasury behavior while requiring customer, security, and support review. A provider change may preserve product meaning while requiring new driver discovery, certification, settlement, and exception testing. A new Facility may reuse the operating grammar while requiring full product, policy, commercial, and operational approval.

Expansion is therefore cumulative learning, not automatic rollout.

### Govern Lessons Learned

Experience should improve operations, documentation, tests, controls, support, and future service design. Institution-specific learning belongs in the bank's governance and implementation records. Improvements to shared engineering may enter maintained software through controlled change.

If field experience appears to challenge canonical doctrine, the issue should be evaluated explicitly. An institution-specific edition should not silently redesign the framework. A doctrinal change requires an Editorial Decision Record and the corresponding governance review.

### Section Summary

The Program moves from approval to discovery, one defined ceremony, institution-specific driver work, technical certification, complete-operation testing, readiness, controlled production, evidence, and deliberate expansion. Each gate answers a different question. The sequence protects the distinction between being able to connect and being prepared to bank.

## Appendices

The shared canonical appendices form part of this Expanded Edition. They remain unchanged and retain their existing governance status.

- [Appendix A — Glossary](../appendices/glossary.md)
- [Appendix B — Governance](../appendices/governance.md)
- [Appendix C — Commercial Waterfall](../appendices/commercial-waterfall.md)
- [Appendix D — Treasury Grammar](../appendices/treasury-grammar.md)
- [Appendix E — Deployment Architecture](../appendices/deployment-architecture.md)
- [Appendix F — Frequently Asked Questions](../appendices/faq.md)
- [Appendix G — Canonical Diagrams](../appendices/diagrams.md)
