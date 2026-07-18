# Appendix G — Canonical Diagrams

These Mermaid diagrams express the governed concepts in the Guide. They describe responsibility and sequence, not production topology or legal fund characterization.

## Program Participants

```mermaid
flowchart LR
    Board["Board and Management"] --> Bank["Thrift Bank"]
    Bank --> ODTI["ODTI"]
    Bank --> DevOps["DevOps Provider"]
    Bank --> Settlement["Settlement Institution"]
    Bank --> Customer["Customers and Enterprises"]
```

## Institutional Boundaries

```mermaid
flowchart TB
    Bank["Bank: authority, customers, custody, production, settlement"]
    X["x-change: operating grammar"]
    Driver["Bank-specific driver: approved API translation"]
    Provider["Provider: supported financial movement"]
    Bank --> X --> Driver --> Provider
```

## Banking Operating Model

```mermaid
flowchart TB
    Channel["Customer Channel"] --> Product["Bank Product"] --> X["x-change"] --> Core["emi-core"] --> Driver["3neti/emi-{bank}"] --> API["Bank API"] --> Account["Bank Settlement Account"] --> Rail["Approved Settlement Arrangement"]
```

## Operating Grammar

```mermaid
flowchart LR
    FE["Funding Event"] --> T["Treasury"] --> L["Lien"] --> F["Facility"] --> SE["Settlement Envelope"] --> PC["Pay Code"] --> E["Execution"] --> R["Evidence and Reconciliation"]
```

## Funding Event and Treasury

```mermaid
flowchart LR
    External["External Financial Event"] --> FE["Funding Event"] --> Recognized["Settlement Resources Recognized"] --> Reserved["Lien: Reserved"] --> Outcome["Resolved Outcome"]
```

## Deposit Flow

```mermaid
flowchart LR
    Customer["Customer"] --> Bank["Bank Accepts Deposit Under Its Authority"] --> Account["Bank Account and Records"] --> FE["Funding Event Records Recognition"] --> Treasury["Treasury Operational View"]
```

## Driver Architecture

```mermaid
flowchart LR
    X["x-change"] --> Core["emi-core"] --> Driver["3neti/emi-{bank}"] --> API["Approved Bank API"]
```

## Program Lifecycle

```mermaid
flowchart LR
    Approval["Program Approval"] --> Discovery["Institutional Discovery"] --> Ceremony["First Ceremony"] --> Driver["Driver Discovery and Mapping"] --> Implement["Implementation"] --> Certify["Certification"] --> Ready["Operational Readiness"] --> Pilot["Controlled Pilot"] --> Review["Proceed / Correct / Extend / Pause"]
```

## Readiness

```mermaid
flowchart TB
    Technical["Driver Certification"] --> Evidence["Complete-Ceremony Evidence"]
    Operations["Operations, Support, Reconciliation"] --> Evidence
    Controls["Risk, Compliance, Security, Governance"] --> Evidence
    Evidence --> Decision["Institutional Readiness Decision"]
```

## Remittance Flow

```mermaid
flowchart LR
    Sender["Sender Request and Funds"] --> Bank["Bank Applies Policy and Authority"] --> Credential["Pay Code Credential"] --> Recipient["Recipient Satisfies Conditions"] --> Execute["Execution Through Bank Relationship"] --> Reconcile["Evidence and Reconciliation"]
```

## Payroll Flow

```mermaid
flowchart LR
    Employer["Employer Authority and Funding"] --> Payroll["Payroll Facility"] --> Conditions["Approvals and Attribution"] --> Execute["Bank-Authorized Execution"] --> Employees["Employee Outcomes"] --> Reconcile["Evidence and Reconciliation"]
```

## Merchant Flow

```mermaid
flowchart LR
    Payment["Accepted Payment"] --> Merchant["Merchant Facility"] --> Settlement["Bank-Approved Settlement"] --> Deposit["Merchant Deposit and Liquidity Relationship"] --> Reconcile["Evidence and Reconciliation"]
```

## Government Disbursement Flow

```mermaid
flowchart LR
    Agency["Authorized Public Institution"] --> Facility["Disbursement Facility"] --> Conditions["Beneficiary and Evidence Conditions"] --> Bank["Bank-Authorized Execution"] --> Beneficiary["Beneficiary Outcome"] --> Reconcile["Evidence and Reconciliation"]
```

## Commercial Waterfall

```mermaid
flowchart TB
    Service["Approved Banking-Service Economics"] --> Provider["Settlement and Third-Party Obligations"] --> Operating["License, Integration, Operations, Support, Maintenance"] --> Bank["Bank Evaluates Residual Financial and Institutional Value"]
```

## Transaction Gravity and Service Expansion

```mermaid
flowchart LR
    First["One Useful Banking Service"] --> Return["Repeated Institutional Usefulness"] --> Relationships["Deeper Customer and Enterprise Relationships"] --> Next["Institution Evaluates the Next Service"] --> First
```

## Deployment Architecture

```mermaid
flowchart TB
    Channels["Bank Channels"] --> Deployment["Bank-Controlled x-change Deployment"] --> Core["emi-core"] --> Driver["Bank-Specific Driver"] --> APIs["Bank APIs and Credentials"] --> Settlement["Bank Settlement Account and Approved Arrangement"]
```

