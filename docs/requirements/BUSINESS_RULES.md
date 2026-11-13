# Business Rules

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

This document defines product-level rules that govern access, learning progress, solve records, progression, rewards, the shop, subscriptions, and competitive features.

A rule marked **TBD** is intentionally unresolved. It must not be implemented based on an assumption.

## 3. General Rules

| ID | Rule |
|---|---|
| BR-GEN-001 | A user's private data and progress belong to that user's account. |
| BR-GEN-002 | Product rules must be applied consistently across the user interface and server-side operations. |
| BR-GEN-003 | A user must not receive a benefit or entitlement solely because a client-side interface claims that an action succeeded. |
| BR-GEN-004 | Duplicate processing of the same eligible event must not grant duplicate one-time rewards. |
| BR-GEN-005 | Unpublished or unavailable content must not be accessible through ordinary user-facing flows. |

## 4. Account and Profile Rules

| ID | Rule |
|---|---|
| BR-ACC-001 | Account identity and uniqueness are determined by the approved registration policy. **TBD** |
| BR-ACC-002 | A user may access private account data only after successful authentication and authorisation. |
| BR-ACC-003 | Profile fields and visibility rules are limited to the approved profile specification. **TBD** |
| BR-ACC-004 | Account suspension, deletion, and recovery policies must be defined before public launch. **TBD** |

## 5. Learning and Course Rules

| ID | Rule |
|---|---|
| BR-LRN-001 | The initial learning focus is the 3×3×3 cube. |
| BR-LRN-002 | The beginner course is part of the current MVP candidate scope. |
| BR-LRN-003 | A user may access a course or lesson only if it is published and the user has the required entitlement. |
| BR-LRN-004 | Course order, prerequisites, lesson completion conditions, and ability to revisit completed lessons are **TBD**. |
| BR-LRN-005 | The distinction and release scope of the CFOP and Full CFOP feature entries are **TBD**. |
| BR-LRN-006 | Additional puzzle types and methods may be added in later product stages; exact scope is **TBD**. |

## 6. Solve and Statistics Rules

| ID | Rule |
|---|---|
| BR-SLV-001 | A saved solve record must belong to exactly one user account. |
| BR-SLV-002 | A solve record must contain a duration and the timestamp required for history and analysis. |
| BR-SLV-003 | Additional metadata such as scramble, penalty, session, device, or method is **TBD**. |
| BR-SLV-004 | The system must define how invalid, cancelled, penalised, or DNF attempts are represented before statistics are finalised. **TBD** |
| BR-SLV-005 | Statistics must be calculated using explicitly defined inclusion and exclusion rules. |
| BR-SLV-006 | When an eligible solve is edited or deleted, dependent statistics must reflect the updated dataset. |
| BR-SLV-007 | Exact statistical formulas, sample sizes, rounding, and time-window definitions are **TBD**. |

## 7. Stars

| ID | Rule |
|---|---|
| BR-STR-001 | Stars are an achievement or score metric. |
| BR-STR-002 | Stars are not spendable currency. |
| BR-STR-003 | Stars may contribute to leaderboards. |
| BR-STR-004 | The events, thresholds, and formulas used to award stars are **TBD**. |
| BR-STR-005 | Whether stars can be lost, reset, or adjusted after a correction is **TBD**. |
| BR-STR-006 | Leaderboard eligibility, ranking, tie-breaking, and season rules are **TBD**. |

## 8. In-Game Currency

| ID | Rule |
|---|---|
| BR-CUR-001 | In-game currency is a separate system from stars. |
| BR-CUR-002 | Currency may be awarded for selected achievements or milestones. |
| BR-CUR-003 | Currency is spent in the shop. |
| BR-CUR-004 | Currency earning events, reward amounts, limits, and eligibility are **TBD**. |
| BR-CUR-005 | Currency spending prices and item availability are **TBD**. |
| BR-CUR-006 | Currency transactions must be recorded so that grants and deductions can be audited. |
| BR-CUR-007 | A failed purchase must not deduct currency without granting the purchased item. |
| BR-CUR-008 | Duplicate processing of a reward event must not credit currency more than once. |
| BR-CUR-009 | Whether currency can expire, be transferred, refunded, or adjusted administratively is **TBD**. |

## 9. Achievements and Levels

| ID | Rule |
|---|---|
| BR-ACH-001 | Achievements recognise defined user milestones or accomplishments. |
| BR-ACH-002 | Selected achievements may award in-game currency. |
| BR-ACH-003 | Achievement definitions, conditions, repeatability, and reward values are **TBD**. |
| BR-ACH-004 | A one-time achievement reward may be granted only once per eligible user and achievement. |
| BR-LVL-001 | Levels are part of the user progression experience. |
| BR-LVL-002 | The relationship between levels, XP, stars, achievements, and course access is **TBD**. |
| BR-LVL-003 | Level thresholds, maximum level, resets, and level rewards are **TBD**. |

## 10. Cosmetic Shop

| ID | Rule |
|---|---|
| BR-SHP-001 | The shop is intended for cosmetic items only. |
| BR-SHP-002 | Cosmetic items may include themes, profile decorations, and timer appearance customisations. |
| BR-SHP-003 | Cosmetic purchases must not provide gameplay advantages. |
| BR-SHP-004 | A purchase requires sufficient currency and an available item. |
| BR-SHP-005 | Currency deduction and item granting must be treated as one consistent purchase operation. |
| BR-SHP-006 | Item catalogue, price, ownership limits, equip rules, refunds, and gifting are **TBD**. |

## 11. Free and Premium Rules

| ID | Rule |
|---|---|
| BR-PRE-001 | Cubiland is planned to provide Free and Premium access models. |
| BR-PRE-002 | Access to restricted content and features depends on the user's current entitlement. |
| BR-PRE-003 | The exact Free/Premium feature matrix is **TBD**. |
| BR-PRE-004 | Premium status must be based on trusted subscription or entitlement data, not a client-provided flag. |
| BR-PRE-005 | Subscription expiration, cancellation, grace periods, refunds, and entitlement revocation are **TBD**. |
| BR-PRE-006 | Premium must not be assumed to grant gameplay advantages through cosmetic purchases. |

## 12. Challenges and Competitions

| ID | Rule |
|---|---|
| BR-CHL-001 | Challenges must have published participation conditions before users can join. |
| BR-CHL-002 | Challenge scoring and reward rules are **TBD**. |
| BR-CMP-001 | Competitions must define eligibility, timing, result validation, and ranking rules before launch. |
| BR-CMP-002 | Anti-cheat and dispute-handling policies are **TBD**. |
| BR-CMP-003 | Whether leaderboards are global, friends-only, seasonal, method-specific, or otherwise segmented is **TBD**. |

## 13. Community Rules

| ID | Rule |
|---|---|
| BR-COM-001 | Community features, if released, must operate under published community rules. |
| BR-COM-002 | Moderation, reporting, blocking, and enforcement policies are **TBD**. |
| BR-COM-003 | Content visibility and user-generated-content retention rules are **TBD**. |

## 14. Content and Notifications

| ID | Rule |
|---|---|
| BR-CNT-001 | Learning content must be approved and published before being made available to users. |
| BR-CNT-002 | The source, update frequency, and editorial ownership of speedcubing news are **TBD**. |
| BR-CNT-003 | The schedule, cadence, and notification channels for Lesson Reminders are **TBD** and must be clarified before requirements are defined. |

## 15. Open Decisions Register

| Decision ID | Topic | Current state |
|---|---|---|
| DEC-001 | CFOP versus Full CFOP scope | TBD |
| DEC-002 | Lesson Reminders schedule, cadence, and notification channels | TBD |
| DEC-003 | Stars earning formula and leaderboard impact | TBD |
| DEC-005 | Currency earning/spending rules | TBD |
| DEC-006 | Achievement catalogue and rewards | TBD |
| DEC-007 | Level and XP model | TBD |
| DEC-008 | Free/Premium feature matrix | TBD |
| DEC-009 | Statistics included in Free and Premium | TBD |
| DEC-010 | Shop catalogue and prices | TBD |
| DEC-011 | Solve penalties and DNF treatment | TBD |
| DEC-012 | Competition and leaderboard rules | TBD |
| DEC-013 | Challenge formats and rewards | TBD |
| DEC-014 | Community moderation policy | TBD |
| DEC-015 | Initial languages | TBD |
| DEC-016 | Subscription provider and lifecycle policy | TBD |

**Document status:** Initial Draft.
