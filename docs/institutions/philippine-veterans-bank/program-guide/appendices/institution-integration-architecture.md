# Annex C — Institution Integration Architecture

Institution-specific integration connects the common operating grammar to PVB's approved execution behavior.

```text
x-change
    ↓
PVB-Specific Integration
    ↓
PVB-Approved Execution Interfaces and Capabilities
    ↓
PVB-Governed Settlement or Payment Arrangements
```

The integration adapts technology. It does not provide public authority, banking authority, settlement participation, custody, product definition, policy, or production approval. The government entity brings lawful purpose and instruction. PVB brings banking authority and the approved rails. x-change brings the operating grammar. Institution-specific integration connects them.

No production integration is assumed to exist. Institution-specific engineering would require:

1. **Institutional discovery** — establish the approved systems, interfaces, environments, settlement arrangements, credentials, controls, owners, evidence, and reconciliation responsibilities relevant to the selected ceremony.
2. **Interface mapping** — map the common execution behavior to PVB-approved authentication, requests, responses, references, idempotency, statuses, notifications, limits, exceptions, reversals, and provider behavior.
3. **Implementation** — create the maintained integration within approved architecture, security, testing, release, and documentation practices.
4. **Technical validation** — demonstrate agreed behavior under controlled conditions, including success, failure, delay, duplication, uncertain status, and recovery paths.
5. **Continuing maintenance** — manage interface changes, credentials, security updates, provider changes, test evidence, observability, defects, releases, and compatibility.

The integration should preserve provider-specific detail at the institutional boundary while returning the references, status, evidence, and exceptions required by the complete public-finance ceremony. PVB would own or control its approved environment, institutional data, credentials, provider accounts, releases, records, and audit trail, and would retain or establish its direct approved settlement and payment relationships. An approved service provider may perform delegated work within PVB's environment and authority; delegation does not transfer institutional ownership or production decisions. Common provider use would not create shared software tenancy, pooled funds, shared credentials, or shared authority.

Technical validation is necessary where the integration is used, but it is not operational readiness. PVB must still judge whether the complete service can be authorized, operated, supervised, secured, settled, reconciled, supported, evidenced, and governed.
