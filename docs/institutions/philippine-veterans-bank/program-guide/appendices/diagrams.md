# Appendix G — Program Diagrams

These diagrams provide conceptual views of the PVB Program. They preserve the canonical operating distinctions and do not prescribe implementation.

## Institutional Identity

```mermaid
flowchart LR
    Commercial["Private Commercial Bank"] --> PVB["Philippine Veterans Bank"]
    Veterans["Statutory Veterans Institution"] --> PVB
    Depository["Official Government Depository"] --> PVB
    PVB --> Capability["Trusted Public-Finance Capability"]
```

## Program Participants

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

## Banking Operating Model

```mermaid
flowchart TD
    Public["Authorized Public Program"] --> Service["PVB Depository Banking Service"]
    Service --> Grammar["Governed Operating Capability"]
    Grammar --> Integration["PVB-Specific Integration"]
    Integration --> Settlement["PVB-Approved Execution and Settlement"]
    Settlement --> Evidence["Status, Evidence, Exceptions, and Reconciliation"]
```

## Operating Grammar

```mermaid
flowchart LR
    Funding["Funding Event"] --> Treasury["Treasury"]
    Treasury --> Lien["Lien"]
    Lien --> Facility["Facility"]
    Facility --> Envelope["Settlement Envelope"]
    Envelope --> PayCode["Pay Code"]
    PayCode --> Execution["Execution"]
    Execution --> Evidence["Evidence and Reconciliation"]
```

## Bounded Public-Assistance Ceremony

```mermaid
flowchart TD
    Authority["Public Purpose and Authorized Participants"] --> Funding["Approved Funding and PVB Recognition"]
    Funding --> Service["PVB Banking Service"]
    Service --> Conditions["Conditions and Evidence"]
    Conditions --> Credential["Pay Code or Approved Presentation"]
    Credential --> Execution["PVB-Authorized Execution"]
    Execution --> Outcome["Participant Outcome"]
    Outcome --> Reconcile["Evidence, Exceptions, and Reconciliation"]
```

## Candidate Ceremony Sequence

```mermaid
flowchart TD
    Assistance["1. Bounded Public Assistance<br/>Primary Discovery Candidate"] --> Collections["2. Public Collections<br/>Secondary Candidate"]
    Collections --> Identity["3. Veterans' Benefits and Government or Military Payroll<br/>Strategic Later Candidates"]
    Identity --> Later["4. Treasury and GOCC Services<br/>Later Evaluation"]
    Later --> Deferred["5. Procurement Settlement<br/>Deferred Pending Evidence"]
```

## Readiness Progression

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
