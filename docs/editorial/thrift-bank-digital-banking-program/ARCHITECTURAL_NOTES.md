# Thrift Bank Digital Banking Program

## Architectural Notes

### Status

Canonical architecture companion — Phase 1

## Purpose

These notes explain the institutional architecture supporting the Phase 1 source manuscript. They are not an implementation guide, API specification, security design, certification instrument, or production authorization.

The architecture begins with banking responsibility and moves downward toward technical execution.

## Institutional Stack

```text
Customer Channel
       │
       ▼
Bank Product
       │
       ▼
x-change
       │
       ▼
emi-core
       │
       ▼
3neti/emi-{bank}
       │
       ▼
Bank API
       │
       ▼
Bank Settlement Account
       │
       ▼
InstaPay / PESONet / other supported arrangements
```

This sequence describes responsibility and integration. It does not imply that every service uses every rail, that every bank exposes the same API, or that the Program grants access to any settlement arrangement.

## Layer Responsibilities

### Customer Channel

The customer channel is the surface through which a customer, employee, merchant, enterprise, bank officer, or partner initiates, presents, reviews, or receives information about a banking activity.

Channels may include:

- a branch;
- Internet banking;
- mobile banking;
- a corporate portal;
- a merchant experience;
- a partner API;
- an assisted operating interface; or
- another channel approved by the bank.

The channel does not own the financial meaning of the service. It presents an experience through which the bank’s product and operating rules are applied.

### Bank Product

The bank product expresses the institution’s customer proposition and responsibility. It determines the service offered, the eligible participants, the applicable terms and policies, the customer journey, the commercial treatment, and the institutional owners.

The product remains the bank’s product. x-change does not acquire the customer relationship by supporting the activity.

### x-change

x-change coordinates the governed banking ceremony.

Its operating grammar distinguishes:

- the external financial event recognized as a Funding Event;
- the Treasury state of Settlement Resources;
- a Lien reserving resources for an authorized purpose;
- the Facility carrying banking and commercial meaning;
- the Settlement Envelope carrying evidence and readiness conditions;
- the Pay Code carrying an authorized instruction as a credential; and
- Execution coordinating the intended banking outcome.

x-change does not receive deposits, create stored value, become the settlement institution, or replace the bank’s channels and products.

### `emi-core`

`emi-core` is the maintained integration contract between the common operating grammar and institution-specific execution capability.

Conceptually, it defines the behavior required to:

- prepare an approved execution instruction;
- submit it through an authorized route;
- preserve institutional and provider references;
- receive synchronous and asynchronous status;
- distinguish supported outcome states;
- handle retries and idempotency according to the approved contract;
- surface exceptions without concealing ambiguity;
- obtain the evidence required for reconciliation; and
- support controlled evolution of the integration boundary.

`emi-core` should not contain the commercial meaning of payroll, collections, remittance, merchant services, or another Facility. It provides an execution contract, not a product catalogue.

### `3neti/emi-{bank}`

`3neti/emi-{bank}` is the maintained bank-specific integration driver.

It implements the `emi-core` contract for one institution’s approved API behavior. Its responsibilities may include translation of:

- authentication and credential use;
- certificate and signing requirements;
- endpoint and request structure;
- institutional transaction references;
- idempotency rules;
- synchronous responses;
- webhooks and asynchronous status;
- provider status and error models;
- timeout, retry, reversal, and uncertain-outcome behavior;
- limits and supported execution routes;
- reconciliation queries, records, or files; and
- interface version changes.

The package is institution-specific because the bank interface and operating relationship are institution-specific.

Illustrative package names such as `3neti/emi-allbank`, `3neti/emi-psbank`, and `3neti/emi-citysavings` explain the naming pattern only. They do not claim that the named institution has adopted, commissioned, approved, or certified a driver.

### Bank API

The Bank API is the institution’s approved technical interface for the supported activity. It remains subject to the bank’s architecture, security, identity and access, operating limits, service management, change procedures, and production controls.

The API may expose only part of the institution’s underlying capability. The driver must implement what the bank has actually approved, not what a generic payment interface is assumed to provide.

### Bank Settlement Account

The settlement account remains within the bank’s regulated relationship and under the applicable institutional authority. The Program does not convert the account into an x-change balance or common pooled resource.

Treasury may maintain an operational view of Settlement Resources, reservations, obligations, and outcomes. That view does not replace the bank account or determine the legal character of the underlying funds.

### Supported Settlement Arrangements

InstaPay, PESONet, and other supported arrangements perform or support financial movement according to their rules and the bank’s participation or provider relationship.

The Program does not presume that a particular rail is available, appropriate, or required for every Facility. The bank determines the supported route through its own authority, arrangements, risk decision, and product design.

## Canonical Boundary Statement

> The bank brings the authority and the rails.
>
> x-change brings the operating grammar.
>
> The bank-specific driver connects them.

The three parts must remain distinct.

The bank’s authority is not created by the driver. The operating grammar is not the settlement rail. The driver is not the banking service. The architecture works because each concern remains governed by the party responsible for it.

## Driver Lifecycle

```text
Discovery
    │
    ▼
Mapping
    │
    ▼
Implementation
    │
    ▼
Certification
    │
    ▼
Maintenance
    │
    ▼
Version Evolution
```

### Discovery

Discovery establishes what the bank interface actually does and under what authority it may be used.

The participants examine:

- the intended banking ceremony;
- applicable accounts and settlement arrangements;
- approved API services;
- authentication, certificates, and access controls;
- request and response behavior;
- references and idempotency;
- webhooks and status updates;
- limits and operating windows;
- errors, retries, reversals, and ambiguous outcomes;
- provider evidence and reconciliation;
- test environments and test data;
- security and architecture requirements;
- service management and incident paths; and
- interface change and notification procedures.

The bank’s technology and operating teams lead the explanation of the institutional boundary. ODTI records the behavior required for the supported driver. Discovery is complete when assumptions have been replaced by an agreed description of the interface and its operating context.

### Mapping

Mapping relates the discovered bank behavior to the `emi-core` contract.

The work identifies:

- which bank operation satisfies each required execution behavior;
- how canonical identifiers relate to institutional and provider references;
- how request fields are derived and validated;
- how provider states map to supported execution states;
- how synchronous and asynchronous evidence is combined;
- how uncertain outcomes are surfaced;
- how reconciliation confirms or corrects operating state;
- which behavior is unsupported or requires a design decision; and
- which controls remain outside the driver and within the bank’s service operation.

Mapping must not conceal a missing capability behind a convenient translation. A gap is recorded as a gap and returned for institutional or architectural decision.

### Implementation

ODTI implements the institution-specific driver within the agreed scope and maintained engineering standards.

Implementation should preserve separation among:

- canonical execution behavior;
- bank-specific translation;
- credentials and environment configuration;
- Facility and commercial semantics;
- customer-channel behavior; and
- operational policy.

Production credentials and institution-specific secrets do not become source-code defaults or shared package assets. The bank governs how they are provisioned, accessed, rotated, monitored, and revoked.

Implementation completion means that the agreed driver behavior is available for controlled validation. It does not authorize production banking activity.

### Certification

Certification establishes technical capability against an approved evidence set.

The evidence may address:

- authentication and secure connection;
- supported instruction preparation and submission;
- correct reference handling;
- idempotent and duplicate behavior;
- expected success, pending, rejection, failure, reversal, and timeout paths;
- webhook validation and status progression;
- reconciliation evidence;
- observability and diagnostic records;
- security requirements within the driver scope;
- compatibility with the approved x-change and `emi-core` versions; and
- repeatability in the designated controlled environment.

Certification does not establish that a bank product is legally approved, operationally ready, commercially acceptable, or authorized for production. It answers a narrower question: whether the bank-specific driver performs the agreed technical behavior under the tested conditions.

### Maintenance

The driver becomes a maintained institutional dependency.

Maintenance may include:

- defect correction;
- security remediation;
- compatibility with maintained x-change and `emi-core` releases;
- controlled response to bank API changes;
- test-suite maintenance;
- documentation updates;
- observability improvements;
- support for agreed provider behavior; and
- incident analysis within the driver’s scope.

The bank remains responsible for provider governance, production approval, credentials, operational supervision, and service continuity. ODTI remains responsible for the maintained driver within the agreed support boundary.

### Version Evolution

Bank APIs, security requirements, provider rules, and operating needs change.

Version evolution should be deliberate. A proposed change is discovered and mapped before implementation. Compatibility is assessed. The driver is tested against the new behavior. The bank reviews the institutional effect, including settlement, reconciliation, support, and rollback. Production release follows the bank’s change authority.

Where parallel API versions must coexist, the architecture should make the supported boundaries explicit. Version evolution must not silently alter the meaning of provider status, evidence, or execution outcome.

## Technical Capability and Institutional Readiness

The driver lifecycle produces technical evidence. The banking-service lifecycle produces institutional evidence.

These lifecycles meet, but they are not interchangeable.

A service may be technically connected while remaining institutionally unready because:

- product authority is incomplete;
- customer terms or communications are unresolved;
- operating ownership is unclear;
- exception paths are not supportable;
- settlement or reconciliation evidence is insufficient;
- accounting treatment is incomplete;
- personnel are unprepared;
- security or risk decisions remain open; or
- the bank has not authorized controlled production.

Conversely, an approved product proposition cannot enter production without a tested and supportable integration path.

Readiness requires both, followed by the bank’s institutional judgment.

## Shared Infrastructure Boundary

Within this architecture, shared infrastructure may include:

- x-change and maintained components;
- `emi-core`;
- reusable integration patterns;
- engineering standards;
- deployment automation;
- test frameworks;
- observability patterns;
- reference controls;
- documentation; and
- maintained releases.

It does not include:

- pooled funds;
- pooled settlement;
- shared banking authority;
- shared production accounts;
- shared customer balances;
- common production credentials;
- a common customer database; or
- a shared institutional audit trail.

Software commonality reduces repeated engineering. Operational sovereignty remains with the bank.

## Architecture Decision Boundary

These notes establish the Phase 1 conceptual model only.

They do not decide:

- the bank’s first production Facility;
- the applicable settlement route;
- detailed API schemas;
- hosting topology;
- security architecture;
- service-level commitments;
- certification test cases;
- pricing or commercial allocation;
- legal characterization;
- production limits; or
- release authorization.

Those decisions require institution-specific discovery, approved source material, and the responsible authority of the participating bank.
