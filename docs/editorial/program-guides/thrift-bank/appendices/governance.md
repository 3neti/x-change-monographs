# Appendix B — Governance

Governance follows institutional responsibility. No provider approval substitutes for the bank's approval.

| Participant | Principal responsibility | Boundary |
| --- | --- | --- |
| Board of Directors | Approves institutional purpose, risk appetite, scope, accountability, and material progression | Does not delegate fiduciary responsibility to a technology provider |
| President / CEO / Management | Owns Program sponsorship, resources, accountability, and management decisions | Does not treat Board approval as production readiness |
| Business / Product | Defines the banking service, customer responsibility, policy, terms, and economic case | Does not assign commercial meaning to technical credentials |
| Operations | Defines supervision, support, escalation, exception handling, evidence, and reconciliation practice | Does not rely on technical completion as an operating decision |
| Treasury | Governs the operational view of Settlement Resources, reservations, and unresolved obligations | Does not replace the bank account or determine legal fund character through software state |
| Technology | Governs architecture, integration, environments, identity, security, observability, resilience, service management, and release | External engineering extends rather than displaces institutional technology capability |
| Risk and Compliance | Reviews risks, controls, obligations, monitoring, and customer treatment within authority | Does not transfer accountability to certification artifacts |
| Legal | Reviews agreements, authority, customer terms, data treatment, and legal characterization | The Guide is not a legal agreement or legal opinion |
| Information Security | Governs access, credentials, certificates, testing, monitoring, incident response, and change | Production secrets remain under approved institutional control |
| Finance / Accounting | Defines accounting, financial reporting, provider-charge treatment, and reconciliation requirements | Commercial estimates require separate financial approval |
| Internal Audit | Provides independent assurance according to its mandate | Does not become an implementation owner |
| ODTI | Licenses and maintains x-change, `emi-core`, supported components, documentation, testing capability, and the bank-specific driver within scope | Does not provide banking authority, custody, settlement access, or production approval |
| DevOps / managed-service provider | Performs delegated provisioning, deployment, monitoring, backup, recovery, release support, and incident work | Does not own the bank's environment, data, credentials, billing, or release authority |
| Settlement institution / payment provider | Performs supported financial movement and provides records under its agreement with the bank | Does not define the bank's customer product or complete ceremony |

## Decision Gates

1. **Program authorization** — The Board or delegated authority permits Management to evaluate and establish the Program.
2. **Service definition** — The institution approves the first banking ceremony and its accountable owners.
3. **Architecture and security approval** — Responsible functions approve the intended environment and integration boundary.
4. **Driver certification** — Agreed technical behavior is evidenced under controlled conditions.
5. **Operational readiness** — The bank judges the complete ceremony ready for bounded production.
6. **Pilot decision** — The institution authorizes a limited production scope.
7. **Evidence review** — The institution decides to Proceed, Correct, Extend, or Pause.

