# Non-Functional Requirements

## 1. Document Information

| Field | Value |
|---|---|
| Product | Cubiland |
| Phase | Requirements Engineering |
| Status | Initial Draft |
| Version | 0.1 |
| Last Updated | 2026-11-11 |
| Author | Andrii Severyn |

## 2. Purpose

This document defines quality attributes and operational constraints for Cubiland. Numeric service-level targets are deliberately marked TBD where product scale, hosting, and release commitments have not yet been established.

Priorities:
- **MUST:** baseline requirement for a safe and usable product.
- **SHOULD:** target for the initial production-ready product.
- **TBD:** requires a measurable target or product decision.

## 3. Performance

| ID | Requirement | Priority |
|---|---|---|
| NFR-PERF-001 | Common user interactions SHOULD complete within an agreed response-time budget under expected load. | TBD |
| NFR-PERF-002 | The timer MUST measure elapsed solve time independently of avoidable network round trips during an active solve. | MUST |
| NFR-PERF-003 | Timer display precision and measurement accuracy MUST be defined and tested before release. | MUST |
| NFR-PERF-004 | Statistics queries SHOULD remain responsive for the expected user history size. | TBD |
| NFR-PERF-005 | The system SHOULD paginate or otherwise bound large histories and catalogues. | SHOULD |

Response-time percentiles, timer precision, maximum history size, and expected load are TBD.

## 4. Availability and Reliability

| ID | Requirement | Priority |
|---|---|---|
| NFR-REL-001 | The production service SHOULD meet an agreed availability target. | TBD |
| NFR-REL-002 | The system MUST avoid silent loss of a solve result after the user has been told it was saved. | MUST |
| NFR-REL-003 | Reward and purchase processing MUST preserve data consistency under retries and concurrent requests. | MUST |
| NFR-REL-004 | The system SHOULD provide health checks and operational monitoring for production services. | SHOULD |
| NFR-REL-005 | Backup and recovery procedures MUST be defined before production launch. | MUST |
| NFR-REL-006 | Recovery Point Objective (RPO) and Recovery Time Objective (RTO) MUST be defined before production launch. | MUST |

Availability target, backup frequency, retention, RPO, and RTO are TBD.

## 5. Security

| ID | Requirement | Priority |
|---|---|---|
| NFR-SEC-001 | Authentication credentials MUST be handled using established secure practices; plaintext passwords MUST NOT be stored. | MUST |
| NFR-SEC-002 | Protected resources MUST enforce server-side authentication and authorisation. | MUST |
| NFR-SEC-003 | Sensitive data MUST be transmitted over encrypted connections in production. | MUST |
| NFR-SEC-004 | Secrets, API keys, and production credentials MUST NOT be committed to source control. | MUST |
| NFR-SEC-005 | The system MUST validate and safely handle untrusted user input. | MUST |
| NFR-SEC-006 | Administrative operations MUST require explicit authorisation and appropriate permissions. | MUST |
| NFR-SEC-007 | Security-relevant events SHOULD be logged without exposing credentials or unnecessary personal data. | SHOULD |
| NFR-SEC-008 | Dependencies SHOULD be monitored and updated to address known security vulnerabilities. | SHOULD |
| NFR-SEC-009 | Rate limits and abuse protections SHOULD be applied to authentication and other sensitive endpoints. | SHOULD |

Detailed threat model, security testing standard, encryption/key-management policy, and rate limits are TBD.

## 6. Privacy and Data Governance

| ID | Requirement | Priority |
|---|---|---|
| NFR-PRIV-001 | The system MUST collect only data necessary for defined product purposes. | MUST |
| NFR-PRIV-002 | The system MUST document the purpose and retention policy for personal data categories. | MUST |
| NFR-PRIV-003 | Users MUST be provided with appropriate privacy information and controls before public launch. | MUST |
| NFR-PRIV-004 | Access to personal data MUST be restricted to authorised purposes and roles. | MUST |
| NFR-PRIV-005 | Data export and account deletion requirements MUST be assessed and implemented as applicable before public launch. | MUST |
| NFR-PRIV-006 | Analytics SHOULD use data minimisation and avoid collecting unnecessary direct identifiers. | SHOULD |

Applicable jurisdictions, legal basis, retention periods, export format, deletion exceptions, and analytics consent policy require legal/product review. The intended age positioning is broad accessibility; age-related privacy and consent requirements (including COPPA and GDPR-K) must be assessed for every launch jurisdiction.

## 7. Usability and Accessibility

| ID | Requirement | Priority |
|---|---|---|
| NFR-UX-001 | Core learning and timer flows MUST provide clear and understandable interaction feedback. | MUST |
| NFR-UX-002 | Navigation and terminology SHOULD remain consistent across learning, practice, timer, and statistics areas. | SHOULD |
| NFR-UX-003 | The interface SHOULD support keyboard operation for core web interactions. | TBD |
| NFR-UX-004 | Text, controls, and feedback SHOULD meet an agreed accessibility standard. | TBD |
| NFR-UX-005 | Important information MUST not be communicated by colour alone. | MUST |
| NFR-UX-006 | Error messages MUST explain the problem and, where possible, the corrective action. | MUST |

Target accessibility standard, supported assistive technologies, and usability benchmarks are TBD.

## 8. Compatibility and Responsiveness

| ID | Requirement | Priority |
|---|---|---|
| NFR-COMP-001 | The product MUST define supported browsers and versions before public release. | MUST |
| NFR-COMP-002 | Core user journeys SHOULD work on supported desktop and mobile viewport sizes. | SHOULD |
| NFR-COMP-003 | The timer interaction model MUST be tested on each supported input/device category. | MUST |
| NFR-COMP-004 | The system SHOULD degrade gracefully when optional browser capabilities are unavailable. | SHOULD |

Browser matrix, minimum device specifications, and native mobile application scope are TBD.

## 9. Scalability and Capacity

| ID | Requirement | Priority |
|---|---|---|
| NFR-SCALE-001 | The system SHOULD support growth in users, solve records, course content, and concurrent sessions without requiring product-level redesign. | SHOULD |
| NFR-SCALE-002 | Capacity assumptions and load-test scenarios MUST be documented before production launch. | MUST |
| NFR-SCALE-003 | Resource-intensive statistics and leaderboard operations SHOULD be designed to avoid unbounded work. | SHOULD |

Expected registered users, concurrent users, solve volume, storage growth, and load targets are TBD.

## 10. Maintainability and Testability

| ID | Requirement | Priority |
|---|---|---|
| NFR-MAINT-001 | The codebase MUST use documented conventions and maintainable project structure. | MUST |
| NFR-MAINT-002 | Critical business rules MUST be covered by automated tests. | MUST |
| NFR-MAINT-003 | API contracts and externally observable behaviour SHOULD be documented. | SHOULD |
| NFR-MAINT-004 | Database schema changes MUST be managed through versioned migrations. | MUST |
| NFR-MAINT-005 | Build, test, and deployment processes SHOULD be repeatable and automated. | SHOULD |
| NFR-MAINT-006 | Logs, metrics, and traces SHOULD support diagnosis of production failures. | SHOULD |

Coverage thresholds, code-quality gates, branching strategy, and release automation are TBD.

## 11. Data Integrity

| ID | Requirement | Priority |
|---|---|---|
| NFR-DATA-001 | Each user's solve history and progress MUST remain isolated from other users. | MUST |
| NFR-DATA-002 | Currency balances and transaction history MUST remain consistent. | MUST |
| NFR-DATA-003 | Duplicate event delivery MUST NOT result in duplicate one-time rewards or purchases. | MUST |
| NFR-DATA-004 | Derived statistics MUST be reproducible from the underlying eligible solve records and defined calculation rules. | MUST |
| NFR-DATA-005 | Data updates involving multiple dependent records MUST use appropriate transactional or consistency controls. | MUST |

## 12. Internationalisation

| ID | Requirement | Priority |
|---|---|---|
| NFR-I18N-001 | User-facing text SHOULD be structured so that additional languages can be supported without rewriting application logic. | SHOULD |
| NFR-I18N-002 | Date, time, and number formatting SHOULD follow the user's selected locale where applicable. | SHOULD |
| NFR-I18N-003 | The system MUST define a canonical storage format for timestamps and convert them for display. | MUST |

Initial languages, locale fallback, translation workflow, and timezone policy are TBD.

## 13. Operational Requirements

- Production and non-production environments MUST be separated.
- Production secrets MUST be stored outside the repository.
- Deployments MUST have a documented rollback or recovery procedure.
- Critical failures SHOULD generate actionable alerts.
- Logs MUST avoid storing passwords, access tokens, payment credentials, or unnecessary personal data.
- Operational ownership and support expectations are TBD.

## 14. Open Decisions

The following quality attributes and operational constraints are tracked as TBD.

| # | Decision | Status | Note |
|---|---|---|---|
| 1 | What availability target is appropriate for the first public release? | Open | |
| 2 | What response-time targets and load assumptions should be used? | Open | |
| 3 | What timer accuracy and display precision are required? | Open | Critical for speedcubing timing integrity. |
| 4 | Which browsers, devices, and viewport sizes are supported? | Open | |
| 5 | Which accessibility standard will be targeted? | Open | |
| 6 | What are the backup, retention, RPO, and RTO targets? | Open | |
| 7 | What privacy, consent, age-related, and data-retention obligations apply in launch jurisdictions? | **Deferred 2026-11-11** | Age positioning revised from "0+" in discovery to reflect COPPA/GDPR-K compliance realities. |
| 8 | What scale and load-test targets should be used? | Open | |
| 9 | What automated test coverage and quality gates are required? | Open | |
| 10 | What monitoring, alerting, and support processes are required? | Open | |

**Document status:** Initial Draft.
