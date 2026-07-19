# Appendix G — Canonical Diagrams

These Mermaid diagrams apply approved canonical concepts to the Government Depository Program. They describe responsibility and sequence, not production topology, public authority, procurement status, or legal fund characterization.

## Program Participants

```mermaid
flowchart LR
    Board["Board and Management"] --> Bank["Government Depository Institution"]
    Agency["Government Entity"] --> Bank
    Bank --> ODTI["ODTI"]
    Bank --> DevOps["DevOps Provider"]
    Bank --> Settlement["Settlement Provider"]
    Bank --> Participant["Payers, Personnel, Beneficiaries, and Suppliers"]
    Oversight["Regulator / Auditor"] -.-> Bank
    Oversight -.-> Agency
```

## Institutional Boundaries

```mermaid
flowchart TB
    Agency["Government Entity: public purpose, authority, participants, accountability"]
    Bank["Depository Institution: banking authority, custody, production, settlement"]
    X["x-change: operating grammar"]
    Driver["Institution-Specific Driver: approved API translation"]
    Provider["Provider: supported financial movement"]
    Agency --> Bank --> X --> Driver --> Provider
```

## Banking Operating Model

```mermaid
flowchart TB
    Program["Government Program and Authorized Instruction"] --> Service["Depository Banking Service"] --> X["Institution-Controlled x-change"] --> Core["emi-core"] --> Driver["3neti/emi-{institution}"] --> API["Institution API"] --> Account["Institution Settlement Account"] --> Rail["Approved Settlement Arrangement"]
```

## Operating Grammar

```mermaid
flowchart LR
    FE["Funding Event"] --> T["Treasury"] --> L["Lien"] --> F["Facility"] --> SE["Settlement Envelope"] --> PC["Pay Code"] --> E["Execution"] --> R["Evidence and Reconciliation"]
```

## Funding Event

```mermaid
flowchart LR
    External["External Financial Event"] --> FE["Funding Event Records Recognition"] --> Treasury["Treasury Operational State"]
```

## Treasury

```mermaid
flowchart LR
    Recognized["Recognized Settlement Resources"] --> Available["Available"]
    Recognized --> Reserved["Lien: Reserved"]
    Reserved --> Outstanding["Outstanding Instruction"] --> Resolved["Resolved Outcome"]
    Outstanding --> Unresolved["Unresolved / Exception"] --> Resolved
```

## Deposit Flow

```mermaid
flowchart LR
    PublicEntity["Authorized Public Entity"] --> Bank["Depository Institution Accepts Funds Under Its Authority"] --> Account["Institution Account and Records"] --> FE["Funding Event Records Recognition"] --> Treasury["Treasury Operational View"]
```

## Driver Architecture

```mermaid
flowchart LR
    X["x-change"] --> Core["emi-core"] --> Driver["3neti/emi-{institution}"] --> API["Approved Institution API"]
```

## Program Lifecycle

```mermaid
flowchart LR
    Approval["Program Authorization"] --> Authority["Authority and Suitability"] --> Ceremony["First Ceremony"] --> Driver["Driver Discovery and Mapping"] --> Implement["Implementation"] --> Certify["Certification"] --> Ready["Institutional Readiness"] --> Pilot["Controlled Pilot"] --> Review["Proceed / Correct / Extend / Pause"]
```

## Readiness

```mermaid
flowchart TB
    Technical["Driver Certification"] --> Evidence["Complete-Ceremony Evidence"]
    Public["Public Authority and Program Readiness"] --> Evidence
    Operations["Operations, Support, Accounting, Reconciliation"] --> Evidence
    Controls["Risk, Compliance, Security, Governance, Audit"] --> Evidence
    Evidence --> Decision["Institutional Readiness Decisions"]
```

## LGU Assistance Flow

```mermaid
flowchart LR
    LGU["LGU Authority and Approved Funding"] --> Facility["Assistance Facility"] --> Conditions["Recipient and Evidence Conditions"] --> Bank["Depository-Institution-Authorized Execution"] --> Recipient["Recipient Outcome"] --> Reconcile["Evidence and Reconciliation"]
```

## Payroll Flow

```mermaid
flowchart LR
    Employer["Government Employer Authority and Funding"] --> Payroll["Payroll Facility"] --> Conditions["Approvals and Personnel Attribution"] --> Execute["Institution-Authorized Execution"] --> Personnel["Personnel Outcomes"] --> Reconcile["Evidence and Reconciliation"]
```

## Pension and Benefit Flow

```mermaid
flowchart LR
    Authority["Benefit Authority and Funding"] --> Facility["Pension or Benefit Facility"] --> Conditions["Eligibility and Recipient Conditions"] --> Execute["Institution-Authorized Execution"] --> Recipient["Recipient Outcome"] --> Reconcile["Evidence and Reconciliation"]
```

## Merchant Flow

```mermaid
flowchart LR
    Payment["Accepted Payment"] --> Merchant["Merchant Facility"] --> Settlement["Institution-Approved Settlement"] --> Deposit["Merchant Deposit and Liquidity Relationship"] --> Reconcile["Evidence and Reconciliation"]
```

## Government Collection Flow

```mermaid
flowchart LR
    Payer["Payer and Public Obligation"] --> Channel["Approved Collection Channel"] --> Bank["Depository Institution"] --> Attribution["Agency, Account, and Obligation Attribution"] --> Reconcile["Evidence and Reconciliation"]
```

## Government Disbursement Flow

```mermaid
flowchart LR
    Agency["Authorized Public Institution"] --> Facility["Disbursement Facility"] --> Conditions["Beneficiary and Evidence Conditions"] --> Bank["Depository-Institution-Authorized Execution"] --> Beneficiary["Beneficiary Outcome"] --> Reconcile["Evidence and Reconciliation"]
```

## Commercial Waterfall

```mermaid
flowchart TB
    Service["Approved Public-Finance Service Economics"] --> Public["Public-Program and Accountability Obligations"] --> Provider["Settlement and Third-Party Obligations"] --> Operating["License, Integration, Operations, Support, Maintenance"] --> Institution["Institution Evaluates Residual Financial and Public Value"]
```

## Public-Finance Relationship Expansion

```mermaid
flowchart LR
    First["One Accountable Public-Finance Service"] --> Evidence["Trusted Execution and Evidence"] --> Relationships["Stronger Institutional Relationships"] --> Next["Institution Evaluates the Next Responsibility"] --> First
```

## Deployment Architecture

```mermaid
flowchart TB
    Channels["Government and Institution-Approved Channels"] --> Deployment["Depository-Institution-Controlled x-change Deployment"] --> Core["emi-core"] --> Driver["Institution-Specific Driver"] --> APIs["Institution APIs and Credentials"] --> Settlement["Institution Settlement Account and Approved Arrangement"]
```
