# Appendix F — Frequently Asked Questions

## What is the Program?

It is the institution-specific initiative through which a thrift bank establishes a reusable governed operating Capability for banking services. It combines maintained software, institution-specific integration, controlled deployment, governance, testing, evidence, and continuing support.

## Why is this different from Internet Banking?

Internet Banking is a customer channel. The Capability operates beneath channels and coordinates the financial state, purpose, conditions, authorized instruction, execution, evidence, and reconciliation of the banking service. Internet Banking, Mobile Banking, branches, corporate portals, and partner APIs remain the bank's channels.

## Why is settlement connectivity not enough?

A rail or API can move funds. It does not by itself define the customer request, apply policy, establish authority, recognize and reserve resources, gather evidence, manage exceptions, support customers, or reconcile the complete service.

## What does x-change do?

x-change coordinates governed banking ceremonies through a reusable operating grammar. It does not provide banking authority, accept deposits, hold customer funds, create stored value, own the customer relationship, or become the settlement institution.

## What does `emi-core` do?

`emi-core` defines the maintained common contract for preparing and submitting approved instructions, preserving references, receiving status, handling provider responses and ambiguity, and supporting reconciliation. It does not contain the commercial meaning of a Facility.

## Why is a bank-specific driver necessary?

Bank APIs differ in authentication, certificates, request formats, signatures, idempotency, webhooks, status models, limits, errors, reversals, reconciliation evidence, and versioning. `3neti/emi-{bank}` maps the common contract to one institution's approved behavior. It requires discovery, mapping, implementation, certification, and maintenance; it is not automatically available.

## Does the bank own its settlement account?

Yes. The bank owns or establishes the relevant account, participation, provider relationship, credentials, limits, and execution authority under its approved arrangements.

## Does the bank own the customer relationship?

Yes. The products, terms, communications, data responsibilities, service obligations, and customer and deposit relationships remain with the bank.

## Does the bank own production?

The bank owns or controls the approved production environment and retains production authorization. Delegated providers operate only within defined authority.

## Is NetBank required?

No. The Program presumes no exclusive settlement institution. The bank uses settlement arrangements it has established and approved.

## What remains the bank's responsibility?

Banking authority, product and customer responsibility, policy, custody, settlement relationships, infrastructure approval, credentials, production decisions, operations, Treasury, security, risk, compliance, support, accounting, reconciliation, and readiness remain institutional responsibilities.

## What does ODTI maintain?

ODTI maintains the licensed x-change software, `emi-core`, supported components, documentation, reference architecture, testing capability, and the bank-specific driver within agreed scope. ODTI does not declare the bank operationally ready.

