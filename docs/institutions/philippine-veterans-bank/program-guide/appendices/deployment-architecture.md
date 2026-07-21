# Appendix E — Deployment Architecture

The proposed deployment model preserves PVB operating sovereignty. It describes the boundary to be validated; it does not state PVB's current production architecture.

```text
PVB Governance and Production Authority
        ↓
PVB-Owned or PVB-Controlled Operating Environment
        ↓
Licensed x-change Capability
        ↓
Maintained PVB-Specific Integration
        ↓
PVB-Approved Systems, Providers, Accounts, and Settlement Arrangements
```

## Institution-Controlled Boundary

PVB would own or control its approved domains, environment, databases, institutional data, encryption and access configuration, production credentials, provider accounts, monitoring, logs, backups, recovery, release approvals, records, and audit trail.

## Maintained Software Boundary

ODTI would license and maintain the agreed x-change operating capability, documentation, and validation support. Licensing would not confer banking authority, public authority, custody, settlement access, or production approval.

## Integration Boundary

Institution-specific integration would connect the operating grammar to PVB's approved systems and execution paths. It would require discovery, interface mapping, implementation, validation, certification, change control, and continuing maintenance. Its technical behavior would remain narrower than institutional readiness.

## Delegated-Service Boundary

An approved provider could perform technical or operating work within PVB's authority. Delegation would not transfer ownership of the environment, data, credentials, provider relationships, evidence, releases, or production decisions.

## Settlement Boundary

PVB would retain or establish its direct approved relationships with settlement and payment providers. Common provider use would not create shared software tenancy, pooled funds, shared credentials, or shared institutional authority.

## Current-State Unknowns

Public evidence does not establish PVB's core-system boundaries, cloud or hosting model, data and credential ownership, delivery pipeline, interface quality, provider contracts, observability, recovery posture, production approvals, or capacity for institution-specific integration. [CLM-046] These matters require institution-approved discovery.

