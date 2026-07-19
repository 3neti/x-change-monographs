# Appendix E — Deployment Architecture

Deployment architecture defines where institutional control remains and where providers may act under delegated authority. The governing question is not simply where the software runs. It is whether the institution retains control over its environment, data, credentials, providers, releases, evidence, and production decisions.

This appendix explains those responsibility boundaries. It is not an infrastructure specification, security design, public authority, procurement instrument, or production authorization.

```text
Government program and institution-approved channels
        ↓
Depository-institution-controlled x-change deployment
        ↓
emi-core
        ↓
Institution-specific 3neti/emi-{institution} driver
        ↓
Institution-approved APIs and credentials
        ↓
Institution settlement account
        ↓
Approved settlement arrangement
```

## Institution-Controlled Boundary

The depository institution owns or controls the approved production boundary. That control includes its hosting account, domains, deployment, databases, institutional data, encryption and access configuration, production credentials, provider accounts, monitoring, logs, backups, recovery, release approvals, and audit trail.

A managed-service provider may operate components only under delegated authority. Delegation changes who performs the work; it does not transfer institutional ownership or production accountability.

Separate institution deployments remain the default. Common licensed software does not require shared application tenancy, databases, credentials, government records, customer records, production authority, or audit trails.

## Maintained Software Boundary

ODTI maintains x-change, `emi-core`, supported components, documentation, reference architecture, and testing capability within agreed scope. The institution-specific driver is discovered, implemented, certified, and maintained under its approved scope.

Maintenance does not create pooled funds, common credentials, shared customer or beneficiary balances, or a common institutional operation.

## Integration Boundary

`3neti/emi-{institution}` implements the common contract for the institution's approved API behavior. Credentials and environment configuration remain separate from maintained source packages. Changes to authentication, certificates, endpoints, messages, statuses, reconciliation evidence, or API versions remain subject to institutional change governance.

## Government-System Boundary

Government portals, program systems, participant records, approvals, accounting systems, and reporting platforms remain under the authority of the responsible public institution. Integration must preserve that boundary across data minimization, identity, access, records, correction, support, and reconciliation. x-change does not become the source of public authority.

## Settlement Boundary

The depository institution owns or establishes the settlement account, participation, provider relationship, limits, credentials, and execution authority. No exclusive settlement institution is presumed. Shared settlement infrastructure does not require shared software tenancy.

## Production Boundary

Driver certification, provider certification, and successful demonstration provide evidence. They do not authorize production. Production requires the applicable public, banking, legal, risk, security, operational, accounting, reconciliation, continuity, and governance decisions.

The supporting [Program Architecture](../../../government-depository-digital-banking-program/annexes/program-architecture-map.md) explains ownership, licensing, operational, settlement, and infrastructure boundaries in full.
