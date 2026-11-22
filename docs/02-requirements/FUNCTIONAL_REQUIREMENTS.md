# Functional Requirements

## 1. Document Information

| Field | Value |
|---|---|
| Product | Cubiland |
| Phase | Requirements Engineering |
| Status | Updated Draft |
| Version | 0.2 |

## 2. Purpose

This document defines observable system capabilities and expected behaviour. Requirements are written to be testable where possible. Values and policies not yet decided are marked TBD.

Requirement priority:
- **MUST:** required for the agreed release or system integrity.
- **SHOULD:** important, but may be scheduled later.
- **COULD:** optional capability.
- **TBD:** priority or release assignment is unresolved.

## 3. Account and Authentication

| ID | Requirement | Priority |
|---|---|---|
| FR-ACC-001 | The system MUST allow a visitor to register an account using the approved registration method. | MUST |
| FR-ACC-002 | The system MUST validate registration input before creating an account. | MUST |
| FR-ACC-003 | The system MUST prevent duplicate accounts according to the approved account-identity policy. | MUST |
| FR-ACC-004 | The system MUST allow registered users to authenticate using supported credentials or identity providers. | MUST |
| FR-ACC-005 | The system MUST provide a secure sign-out operation that invalidates or terminates the applicable session. | MUST |
| FR-ACC-006 | The system SHOULD provide an account-recovery process. | SHOULD |
| FR-ACC-007 | The system MUST associate user-owned data with the authenticated account. | MUST |
| FR-ACC-008 | The system MUST enforce authorisation before returning or modifying protected account data. | MUST |
| FR-ACC-009 | The system MUST support account/profile updates for approved editable fields. | MUST |
| FR-ACC-010 | The system MUST define and implement an account deletion process before public launch. | TBD |

Registration fields, verification, authentication providers, session duration, and recovery policy are TBD.

## 4. Profile and Settings

| ID | Requirement | Priority |
|---|---|---|
| FR-PRF-001 | The system MUST provide an authenticated user with access to their profile. | MUST |
| FR-PRF-002 | The system MUST allow users to update approved profile fields. | MUST |
| FR-PRF-003 | The system MUST validate profile changes before persistence. | MUST |
| FR-SET-001 | The system MUST provide settings for preferences approved for the relevant release. | TBD |
| FR-SET-002 | The system SHOULD support language preferences when multiple languages are available. | TBD |
| FR-SET-003 | The system MUST enforce privacy and visibility preferences where such preferences are offered. | TBD |

The profile field list and privacy defaults are TBD.

## 5. Courses and Lessons

| ID | Requirement | Priority |
|---|---|---|
| FR-LRN-001 | The system MUST present the published beginner 3×3×3 course to users entitled to access it. | MUST |
| FR-LRN-002 | The system MUST represent a course as an ordered collection of learning units or lessons. | MUST |
| FR-LRN-003 | The system MUST display course structure and the user's recorded progress. | MUST |
| FR-LRN-004 | The system MUST allow an entitled user to open an available lesson. | MUST |
| FR-LRN-005 | The system MUST persist lesson progress for an authenticated user. | MUST |
| FR-LRN-006 | The system SHOULD allow a user to resume a course using persisted progress. | SHOULD |
| FR-LRN-007 | The system MUST prevent access to unpublished content through normal user-facing routes. | MUST |
| FR-LRN-008 | The system MUST check entitlement before serving Premium-restricted content. | MUST |
| FR-LRN-009 | The system SHOULD support video lesson content if included in the approved release. | TBD |
| FR-LRN-010 | The system MAY support additional solving methods and puzzles in later releases. | TBD |

Lesson completion conditions, prerequisites, content schema, and CFOP scope are TBD.

## 6. Algorithms and Exercises

| ID | Requirement | Priority |
|---|---|---|
| FR-ALG-001 | The system SHOULD provide an algorithm catalogue for supported methods and categories. | SHOULD |
| FR-ALG-002 | Each published algorithm MUST include its approved notation representation. | SHOULD |
| FR-ALG-003 | The system SHOULD provide an explanation or learning resource for an algorithm where content is available. | SHOULD |
| FR-ALG-004 | The system SHOULD provide algorithm practice exercises. | SHOULD |
| FR-ALG-005 | The system MUST record exercise outcomes when the exercise is defined as progress-tracked. | TBD |
| FR-ALG-006 | The system MUST check access entitlement for restricted algorithm content or exercises. | MUST |

Supported notation, algorithm metadata, practice modes, and mastery calculation are TBD.

## 7. Timer and Solve Records

| ID | Requirement | Priority |
|---|---|---|
| FR-TMR-001 | The system MUST provide a timer capable of measuring a solve duration. | MUST |
| FR-TMR-002 | The timer MUST expose clearly defined ready, running, and stopped states. | MUST |
| FR-TMR-003 | The system MUST display the result of a completed timing attempt. | MUST |
| FR-TMR-004 | The system MUST allow a completed solve to be saved to the authenticated user's history. | MUST |
| FR-TMR-005 | A saved solve MUST have a unique record identifier and an association with its owner. | MUST |
| FR-TMR-006 | A solve record MUST store the duration and the timestamp needed for history and statistics. | MUST |
| FR-TMR-007 | The system SHOULD store additional solve metadata when supported by the approved timer rules. | TBD |
| FR-TMR-008 | The system SHOULD allow an authorised user to edit or delete their own solve record. | SHOULD |
| FR-TMR-009 | The system MUST prevent users from modifying another user's solve records. | MUST |
| FR-TMR-010 | The system MUST ensure that changes to solve records are reflected in dependent statistics. | MUST |
| FR-TMR-011 | The system MUST provide a recoverable response when saving a solve fails. | MUST |

Timer input methods, timing precision, inspection, penalties, DNF handling, scramble generation/source, offline mode, and metadata are TBD.

## 8. Statistics and Analysis

| ID | Requirement | Priority |
|---|---|---|
| FR-STA-001 | The system MUST provide a solve-history view for the authenticated user. | MUST |
| FR-STA-002 | The system MUST calculate approved basic statistics from the applicable solve records. | MUST |
| FR-STA-003 | The system MUST define which records are included or excluded from each statistic. | MUST |
| FR-STA-004 | The system SHOULD support filtering by approved time range or session. | SHOULD |
| FR-STA-005 | The system SHOULD present performance trends over time. | SHOULD |
| FR-STA-006 | The system MUST apply entitlement checks to Premium-restricted statistics. | MUST |
| FR-STA-007 | The system MUST update or recalculate affected statistics after a solve record is created, edited, or deleted. | MUST |

Exact statistics (for example, average types, best, worst, median, trend windows), DNF/penalty treatment, and Free/Premium split are TBD.

## 9. Progression, Stars, and Achievements

**Decision confirmed 2026-11-22:** Stars, achievements, progression levels, and leaderboards are explicitly excluded from the MVP. The requirements in this section are retained for future phase planning.

| ID | Requirement | Priority |
|---|---|---|
| FR-GAM-001 | The system MUST maintain stars separately from spendable in-game currency. | TBD (Post-MVP) |
| FR-GAM-002 | The system MUST award stars only when an approved star-award rule is satisfied. | TBD (Post-MVP) |
| FR-GAM-003 | The system SHOULD provide an achievement catalogue and user achievement status. | TBD (Post-MVP) |
| FR-GAM-004 | The system MUST prevent the same one-time achievement reward from being granted more than once. | TBD (Post-MVP) |
| FR-GAM-005 | The system MUST maintain a separate in-game currency balance for each eligible user. | TBD (Post-MVP) |
| FR-GAM-006 | The system MUST record currency grants and deductions as traceable transactions. | TBD (Post-MVP) |
| FR-GAM-007 | The system MUST grant currency only for approved reward events. | TBD (Post-MVP) |
| FR-GAM-008 | The system SHOULD display user progression level and relevant progress. | TBD (Post-MVP) |
| FR-GAM-009 | The system MUST apply approved leaderboard eligibility and ranking rules when displaying rankings. | TBD (Post-MVP) |
| FR-GAM-010 | The system MUST prevent cosmetic purchases from changing gameplay outcomes or competitive performance. | TBD (Post-MVP) |

Level formula, XP existence, star-award rules, achievement catalogue, reward values, and leaderboard rules are TBD.

## 10. Cosmetic Shop

**Decision confirmed 2026-11-22:** The cosmetic shop is explicitly excluded from the MVP. The requirements in this section are retained for future phase planning.

| ID | Requirement | Priority |
|---|---|---|
| FR-SHP-001 | The system COULD display a catalogue of available cosmetic items. | TBD (Post-MVP) |
| FR-SHP-002 | The system COULD display item price, availability, and ownership state. | TBD (Post-MVP) |
| FR-SHP-003 | The system MUST verify sufficient currency before completing a currency purchase. | TBD (Post-MVP) |
| FR-SHP-004 | The system MUST deduct currency and grant the purchased item atomically or provide equivalent transactional guarantees. | TBD (Post-MVP) |
| FR-SHP-005 | The system MUST prevent duplicate ownership or duplicate charging where items are non-repeatable. | TBD (Post-MVP) |
| FR-SHP-006 | The system MUST prevent a purchase if the item is unavailable or the balance is insufficient. | TBD (Post-MVP) |
| FR-SHP-007 | The system SHOULD allow a user to equip or apply owned cosmetics where applicable. | TBD (Post-MVP) |
| FR-SHP-008 | The system MUST restrict shop items to cosmetic effects under the current product principle. | TBD (Post-MVP) |

Catalogue, pricing, repeatability, refunds, gifting, and equipped-item limits are TBD.

## 11. Challenges, Competitions, and Community

| ID | Requirement | Priority |
|---|---|---|
| FR-CHL-001 | The system COULD display published challenges and their participation rules. | COULD |
| FR-CHL-002 | The system COULD record eligible challenge participation and results. | COULD |
| FR-CMP-001 | The system MAY support competitions with defined eligibility, time windows, and result rules. | TBD |
| FR-CMP-002 | The system MAY provide leaderboards based on approved ranking rules. | TBD |
| FR-COM-001 | The system MAY provide community discussion or chat capabilities. | TBD |
| FR-COM-002 | If community features are released, the system MUST provide an approved moderation and reporting mechanism. | TBD |

Competition formats, moderation policies, anti-cheat controls, and community permissions are TBD.

## 12. Content Discovery and Localisation

| ID | Requirement | Priority |
|---|---|---|
| FR-DIS-001 | The system COULD display a Scramble of the Day. | COULD |
| FR-DIS-002 | The system COULD publish speedcubing news content. | COULD |
| FR-I18N-001 | The system MAY support multiple interface languages. | TBD |
| FR-I18N-002 | The system MUST avoid mixing untranslated interface strings within a supported locale, subject to localisation architecture. | TBD |

Initial languages, content sources, editorial process, and localisation scope are TBD.

## 13. Premium and Entitlements

**Decision confirmed 2026-11-22:** Premium subscriptions and payment integration are explicitly excluded from the MVP. The requirements in this section are retained for future phase planning. The provisional preferred payment solution for a future monetization phase is Stripe with Stripe Billing.

| ID | Requirement | Priority |
|---|---|---|
| FR-PRE-001 | The system MUST represent whether an account has an active Premium entitlement. | TBD (Post-MVP) |
| FR-PRE-002 | The system MUST check entitlement before granting access to Premium-restricted resources. | TBD (Post-MVP) |
| FR-PRE-003 | The system MUST distinguish Free access from Premium access according to an approved feature matrix. | TBD (Post-MVP) |
| FR-PRE-004 | The system MUST update entitlement state based on trusted subscription status information. | TBD (Post-MVP) |
| FR-PRE-005 | The system MUST handle entitlement expiration or cancellation according to an approved policy. | TBD (Post-MVP) |
| FR-PRE-006 | The system SHOULD explain the access requirement when a user attempts to open Premium-restricted content. | TBD (Post-MVP) |

Payment provider, subscription plans, pricing, trials, grace periods, refunds, cancellation UX, and regional rules are TBD.

## 14. Administration and Content Management

| ID | Requirement | Priority |
|---|---|---|
| FR-ADM-001 | The system MUST restrict administrative functions to authorised administrators. | MUST |
| FR-ADM-002 | The system MUST support creation and editing of approved learning content. | MUST |
| FR-ADM-003 | The system MUST support publishing and unpublishing content. | MUST |
| FR-ADM-004 | The system MUST validate required content fields before publication. | MUST |
| FR-ADM-005 | The system SHOULD record relevant administrative changes for audit purposes. | SHOULD |
| FR-ADM-006 | The system SHOULD support management of algorithms and exercises. | SHOULD |
| FR-ADM-007 | The system MUST enforce role-based permissions for administrative actions. | MUST |

Admin roles, content approval, audit retention, and operational tooling are TBD.

## 15. Notifications and Reminders

The Phase 1 inventory contains a "Lesson Reminders" feature: a cron-style reminder that notifies users to take their lessons on a recurring schedule.

| ID | Requirement | Priority |
|---|---|---|
| FR-NOT-001 | Reminder and notification functionality MUST NOT be specified beyond confirmed product intent. | TBD |
| FR-NOT-002 | If notifications are approved, users MUST be able to manage the supported notification preferences. | TBD |

The reminder schedule/cron cadence, notification channels, opt-in policy, and reminder cadence require clarification.

## 16. Cross-Cutting Functional Requirements

- All user-owned resources MUST be scoped to the correct owner.
- Protected operations MUST enforce authorisation on the server side.
- Reward and purchase operations MUST be safe against duplicate processing.
- The system MUST provide clear success and failure outcomes for user-initiated operations.
- The system MUST preserve data consistency between source records and derived statistics.
- The system MUST not grant gameplay advantages through cosmetic shop purchases.

## 17. Requirement Traceability

Requirements map to user stories by functional area:
- Account: `US-ACC-*`
- Profile/settings: `US-ACC-*`
- Learning: `US-LRN-*`
- Algorithms: `US-ALG-*`
- Timer/solves: `US-TMR-*`
- Statistics: `US-STA-*`
- Gamification: `US-GAM-*`
- Shop: `US-SHP-*`
- Challenges/competitions/community: `US-CHL-*`, `US-CMP-*`, `US-COM-*`
- Discovery/localisation: `US-DIS-*`, `US-I18N-*`
- Premium: `US-PRE-*`
- Administration: `US-ADM-*`

**Document status:** Initial Draft.
