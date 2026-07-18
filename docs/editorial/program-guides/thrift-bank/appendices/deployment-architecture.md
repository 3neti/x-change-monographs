# Appendix E — Deployment Architecture

This appendix describes responsibility and deployment boundaries. It is not an infrastructure specification, security design, or production authorization.

```text
Bank channels and products
        ↓
Bank-controlled x-change deployment
        ↓
emi-core
        ↓
Bank-specific 3neti/emi-{bank} driver
        ↓
Bank-approved APIs and credentials
        ↓
Bank settlement account
        ↓
InstaPay / PESONet / approved settlement arrangement
```

## Bank-Controlled Boundary

The bank owns or controls its approved hosting account, domains, deployment, databases, institutional data, encryption and access configuration, production credentials, provider accounts, monitoring, logs, backups, recovery, release approvals, and audit trail. A managed-service provider may operate components only under delegated authority.

## Maintained Software Boundary

ODTI maintains x-change, `emi-core`, supported components, documentation, reference architecture, testing capability, and the bank-specific driver within agreed scope. Maintained common software does not create shared production tenancy, pooled funds, common credentials, shared customer balances, or a common institutional audit trail.

## Integration Boundary

`3neti/emi-{bank}` implements the common contract for the institution's approved API behavior. Credentials and environment configuration remain separate from maintained source packages. Changes to authentication, certificates, endpoints, messages, statuses, reconciliation evidence, or API versions pass through institutional change governance.

## Settlement Boundary

The bank owns or establishes the settlement account, participation, provider relationship, limits, credentials, and execution authority. No NetBank dependency is presumed. The route used for a Facility remains subject to the bank's approvals and provider arrangements.

