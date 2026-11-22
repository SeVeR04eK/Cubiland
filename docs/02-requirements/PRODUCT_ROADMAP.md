# Product Roadmap

## 1. Document Information

| Field | Value |
|---|---|
| Product | Cubiland |
| Phase | Requirements Engineering |
| Status | Updated Draft |
| Version | 0.2 |
| Last Updated | 2026-11-22 |
| Author | Andrii Severyn |

## 2. Purpose

This roadmap describes a proposed sequence for product delivery. It is a capability-based planning view, not a committed schedule. Dates, estimates, and release commitments are TBD.

The roadmap preserves the broader Cubiland product vision while separating the initial MVP from later expansion.

## 3. Roadmap Principles

- Deliver a coherent learning-to-practice journey before expanding into many secondary features.
- Prioritise product foundations and data integrity.
- Keep stars separate from spendable currency.
- Ensure cosmetic shop items do not provide gameplay advantages.
- Introduce Premium only with a clear and documented entitlement model.
- Validate assumptions through user feedback and product analytics.
- Do not assign release dates until scope, dependencies, and delivery capacity are understood.

## 4. Proposed Phases

### Phase A — Product and Technical Foundations

**Objective:** establish the foundation required to build and operate Cubiland.

Candidate scope:
- Approved PRD and requirements baseline.
- UX/UI design for core user journeys.
- Application architecture and data model.
- Authentication and account foundation.
- Content management approach for courses and lessons.
- Initial analytics and event definitions.
- Development, testing, and deployment environments.
- Security, privacy, and operational baseline.

**Exit conditions:**
- Core requirements are approved.
- Core user flows have reviewed designs.
- Architecture supports the agreed MVP.
- Critical risks and external dependencies are documented.

### Phase B — Core Learning and Practice MVP

**Objective:** deliver the primary learning-to-practice experience for the 3×3×3 cube.

**Confirmed MVP scope (decisions confirmed 2026-11-22):**
- Registration, sign-in, and user profile.
- Beginner 3×3×3 course.
- Course and lesson progress.
- Integrated timer.
- Solve recording and history.
- Basic statistics and performance analysis.
- Essential settings required by the MVP.

**Explicitly excluded from MVP:**
- 3×3×3 CFOP and Full CFOP courses.
- In-game currency and cosmetic shop.
- Stars, achievements, and progression levels.
- Leaderboards.
- Practice challenges and challenge-based training modes.
- Premium subscriptions and Premium features.
- Payment integration.

**Exit conditions:**
- A user can create an account and access the beginner course.
- A user can study lessons and retain progress.
- A user can time solves and save records.
- A user can inspect solve history and agreed basic statistics.
- Core flows pass acceptance tests.
- Production readiness and privacy/security checks are completed.

### Phase C — Progression and Engagement

**Objective:** introduce the approved progression and reward experience.

Candidate scope:
- Achievement catalogue and milestone evaluation.
- Stars and approved star-award rules.
- Progression levels, if the level model is approved.
- Separate in-game currency balance and transaction ledger.
- Initial cosmetic shop catalogue.
- Initial tasks or challenges, if selected for this release.
- Leaderboards, if ranking rules and integrity controls are approved.

**Dependencies:**
- Approved `BUSINESS_RULES.md`.
- Defined reward catalogue and amounts.
- Idempotent reward processing.
- Approved leaderboard and anti-abuse rules where relevant.

**Exit conditions:**
- Rewards are granted according to approved rules.
- Duplicate processing cannot duplicate one-time rewards.
- Currency and purchases remain consistent.
- Cosmetic items do not change gameplay outcomes.

### Phase D — Expanded Learning and Premium

**Objective:** expand educational content and introduce the approved commercial model.

Candidate scope:
- Expanded method/course catalogue, including CFOP content.
- Algorithm reference and practice tools.
- Video lessons.
- Premium lessons and approved Premium features.
- Subscription and entitlement integration.
- Free/Premium access matrix.
- Subscription lifecycle handling.

**Dependencies:**
- Confirmed CFOP and Full CFOP definitions.
- Approved content production plan.
- Approved Premium feature matrix and pricing.
- Selected billing provider (provisional choice: Stripe with Stripe Billing) and legal review.

**Exit conditions:**
- Entitlements are enforced consistently.
- Subscription state is reflected accurately.
- Premium restrictions are explained clearly.
- Learning access behaves according to the approved policy.

### Phase E — Community and Competitive Features

**Objective:** expand social participation and competitive engagement.

Candidate scope:
- Community chat or discussion features.
- User reporting and moderation tools.
- Competitions.
- Expanded leaderboards.
- Additional challenges and events.
- Anti-cheat and dispute-handling processes.

**Dependencies:**
- Community policy and moderation operations.
- Competition formats and ranking rules.
- Abuse prevention and operational support.

### Phase F — Discovery, Localisation, and Puzzle Expansion

**Objective:** broaden the platform's content reach and supported experiences.

Candidate scope:
- Additional interface languages.
- Scramble of the Day.
- Speedcubing news.
- Additional solving methods.
- Support for other twisty puzzles.
- Further profile and cosmetic customisation.

Release order and scope depend on user demand, validation, and product capacity.

## 5. Feature-to-Phase Planning

| Capability | Proposed phase | Status |
|---|---|---|
| Authentication and profile | A–B | MVP confirmed |
| Beginner 3×3×3 course | B | MVP confirmed |
| Timer | B | MVP confirmed |
| Solve history | B | MVP confirmed |
| Basic statistics | B | MVP confirmed |
| Settings | B | Partial MVP (essential only) |
| Stars | C | Post-MVP; rules TBD |
| Achievements | C | Post-MVP; catalogue and rules TBD |
| Levels | C | Post-MVP; progression model TBD |
| In-game currency | C | Post-MVP; economy rules TBD |
| Cosmetic shop | C | Post-MVP; catalogue and pricing TBD |
| Tasks and challenges | C or E | Post-MVP; scope TBD |
| CFOP course | D | Post-MVP; scope TBD |
| Full CFOP | D or later | Post-MVP; definition TBD |
| Algorithm practice | D | Post-MVP; scope TBD |
| Video lessons | D | Post-MVP; content and access TBD |
| Premium lessons | D | Post-MVP; entitlement rules TBD |
| Premium subscription | D | Post-MVP; Stripe provisional choice |
| Community chat | E | Post-MVP; moderation scope TBD |
| Competitions | E | Post-MVP; format and rules TBD |
| Leaderboards | C or E | Post-MVP; depends on ranking rules |
| Scramble of the Day | F | Post-MVP; priority TBD |
| Languages | F | Post-MVP; initial languages TBD |
| Speedcubing news | F | Post-MVP; source and editorial model TBD |
| Other puzzles | F | Post-MVP; product scope TBD |
| Lesson Reminders | TBD | Schedule, cadence, and notification channels require clarification |

## 6. Dependencies

- User flows and UI/UX designs depend on an approved product scope.
- Architecture depends on functional, non-functional, and business requirements.
- Statistics depend on the solve-record model and approved calculation rules.
- Stars, achievements, levels, and currency depend on approved progression rules.
- Shop implementation depends on currency transaction integrity and item ownership rules.
- Premium implementation depends on a feature entitlement matrix and subscription policy.
- Competitions and leaderboards depend on result validation, ranking, and anti-cheat rules.
- Community features depend on moderation and reporting requirements.

## 7. Release Readiness Checklist

Before any public release, review:
- Scope and acceptance criteria approved.
- Critical user flows tested.
- Security and privacy review completed.
- Data backup and recovery procedures tested.
- Monitoring and error reporting available.
- Content reviewed and published.
- Support arrangements defined.
- Known limitations and release notes prepared.
- Rollback or recovery procedure documented.

## 8. Planning Items Still TBD

- MVP feature freeze and exact scope.
- Release naming and versioning policy.
- Delivery capacity and estimates.
- Target dates and milestones.
- Beta-testing approach and participant recruitment.
- Launch regions and supported languages.
- Premium launch timing and pricing.
- Analytics targets and go/no-go thresholds.

**Document status:** Initial Draft. This roadmap is directional and does not constitute a delivery commitment.
