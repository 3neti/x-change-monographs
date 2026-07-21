# Appendix G — Program Diagrams

These diagrams specialize the approved Government Depository operating concepts for PVB without changing canonical definitions. They are editorial source diagrams, not implementation specifications.

## Institutional Identity

```mermaid
flowchart LR
    Veterans["Statutory Veterans Institution"] --> PVB["Philippine Veterans Bank"]
    Commercial["Private Commercial Bank"] --> PVB
    Depository["Official Government Depository"] --> PVB
    PVB --> Capability["Proposed Trusted Public-Finance Capability"]
```

## Program Lineage

```mermaid
flowchart TD
    Intelligence["Institution Intelligence"] --> Assessment["Strategic Assessment"]
    Assessment --> Gap["Gap Analysis"]
    Gap --> Program["Accepted Modernization Program"]
    Program --> Guide["PVB Digital Banking Program Guide"]
    Guide --> Validation["Management Validation"]
```

## Operating Model

```mermaid
flowchart TD
    Public["Authorized Public Program"] --> Service["PVB Depository Banking Service"]
    Service --> Grammar["Governed Operating Capability"]
    Grammar --> Integration["PVB-Specific Execution Capability"]
    Integration --> Settlement["PVB-Approved Settlement Arrangement"]
    Settlement --> Evidence["Status, Evidence, and Reconciliation"]
```

## Responsibility Boundaries

```mermaid
flowchart LR
    Government["Government Entity<br/>Purpose · Authority · Participants · Accountability"]
    PVB["PVB<br/>Banking Authority · Custody · Accounts · Readiness"]
    Xchange["x-change<br/>Operating Grammar"]
    Providers["Approved Providers<br/>Delegated Execution and Evidence"]
    Government --> PVB
    PVB --> Xchange
    Xchange --> Providers
    Providers --> PVB
```

## Bounded Public-Assistance Ceremony

```mermaid
flowchart TD
    Authority["Public Purpose and Authorized Participants"] --> Funding["Approved Funding and PVB Recognition"]
    Funding --> Facility["PVB Banking Service and Facility"]
    Facility --> Conditions["Settlement Envelope Conditions"]
    Conditions --> Credential["Pay Code or Approved Presentation"]
    Credential --> Execution["PVB-Authorized Execution"]
    Execution --> Outcome["Participant Outcome"]
    Outcome --> Reconcile["Evidence, Exceptions, and Reconciliation"]
```

## Readiness Progression

```mermaid
flowchart LR
    Program["Program Readiness"] --> Workflow["Workflow Readiness"]
    Workflow --> Implementation["Implementation Readiness"]
    Implementation --> Technical["Technical Readiness"]
    Technical --> Operational["Operational Readiness"]
    Operational --> Limited["Limited-Production Readiness"]
    Limited --> Production["Production Readiness"]
    Production --> Expansion["Expansion Readiness"]
```

No arrow makes the next state automatic. Each transition requires the evidence and authority appropriate to the responsibility being considered.

## Evidence Review

```mermaid
flowchart LR
    Operate["Bounded Operation"] --> Review["Institutional Evidence Review"]
    Review --> Proceed["Proceed"]
    Review --> Correct["Correct"]
    Review --> Extend["Extend"]
    Review --> Pause["Pause"]
```
