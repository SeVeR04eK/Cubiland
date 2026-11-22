# Product Requirements Document (PRD)

## 1. Document Information

| Field | Value |
|---|---|
| Product | Cubiland |
| Phase | Requirements Engineering |
| Status | Updated Draft |
| Version | 0.2 |
| Last Updated | 2026-11-22 |
| Author | Andrii Severyn |

## 2. Product Overview

Cubiland is a gamified learning and training platform for twisty-puzzle enthusiasts. Its initial focus is the 3×3×3 Rubik's Cube.

The platform brings together structured courses, lessons, algorithm learning and practice, exercises, a speedcubing timer, solve history, performance statistics, and progression mechanics.

Cubiland is intended to support users at different skill levels: complete beginners, developing learners, intermediate speedcubers, and advanced speedcubers. The longer-term product direction includes support for additional solving methods and other twisty puzzles.

## 3. Product Vision

Make learning and improving at twisty puzzles more structured, engaging, and accessible by combining education, deliberate practice, performance feedback, and gamified progression in one platform.

## 4. Problem Statement

People learning and practising speedcubing may rely on several separate resources, including tutorials, algorithm references, online timers, notes, and statistics tools.

This fragmented workflow can make it harder to follow a clear learning path, decide what to practise next, connect learning material with practical exercises, keep solve history and performance data together, track progress, and maintain motivation.

Cubiland aims to address this problem through an integrated learning and training experience. These problem statements are product hypotheses and should be validated through user research and product testing.

## 5. Target Audience

Cubiland is intended for a broad international B2C audience. The intended age positioning is broad accessibility; age-related privacy, consent, and parental-consent obligations (including COPPA and GDPR-K) must be assessed for every launch jurisdiction.

Primary audience segments:
1. **Complete beginners** — people who want to learn how to solve a 3×3×3 cube from the beginning.
2. **Developing learners** — people who know the basics and want a structured path towards more advanced methods.
3. **Intermediate speedcubers** — people who want to improve solving times, practise algorithms, and analyse performance.
4. **Advanced speedcubers** — experienced users who may benefit from structured drills, detailed statistics, challenges, and competitive features.

Personas and audience assumptions are documented in `../01-product-discovery`.

## 6. Product Goals

### 6.1 Primary Goals

- Provide structured learning paths for the 3×3×3 cube.
- Connect lessons and algorithm learning with practical exercises.
- Provide an integrated speedcubing timer and solve history.
- Help users understand performance through statistics and analysis.
- Encourage consistent practice through progression and gamification.
- Support a sustainable product model with Free and Premium access.

### 6.2 Candidate Success Metrics

Exact definitions, targets, and measurement periods are TBD.

| Area | Candidate metric |
|---|---|
| Activation | Percentage of registered users who start or complete their first learning activity |
| Learning | Course and lesson completion rates |
| Practice | Practice sessions and recorded solves per active user |
| Retention | Returning users over defined time periods |
| Progress | Change in users' solve times over a defined observation period |
| Engagement | Participation in challenges and achievement completion |
| Monetisation | Premium conversion and subscription retention |

Metric definitions, event instrumentation, and target values will be specified before implementation.

## 7. Core User Journey

1. A user registers or signs in.
2. The user selects an appropriate learning path or skill level.
3. The user studies a lesson or algorithm.
4. The user practises through an exercise or training session.
5. The user uses the timer to record solves.
6. The platform stores solve results and updates relevant statistics.
7. The user reviews progress and receives progression feedback.
8. The user continues learning, practising, and completing goals.

Detailed flows, including alternative and error paths, are documented in `USER_FLOWS.md`.

## 8. Product Scope

### 8.1 MVP Candidate Scope

The confirmed MVP scope includes:
- User registration, authentication, and profile.
- A beginner 3×3×3 course.
- A 3×3×3 solving timer.
- Solve history.
- Core statistics and performance analysis.
- Essential settings required by the MVP.

**Explicitly excluded from MVP:**
- 3×3×3 CFOP and Full CFOP courses.
- In-game currency and cosmetic shop.
- Stars, achievements, and progression levels.
- Leaderboards.
- Practice challenges and challenge-based training modes.
- Premium subscriptions and Premium features.
- Payment integration.

The MVP boundary is confirmed against the Phase 1 `MVP_DEFINITION.md` and `FEATURE_PRIORITIZATION.md` (decisions confirmed 2026-11-22).

### 8.2 Planned Product Capabilities

The broader product vision includes:
- Beginner and advanced courses, including CFOP content.
- Algorithm learning and practice.
- Video lessons and premium lessons.
- Training tasks and challenges.
- Scramble of the Day.
- Multiple languages.
- Speedcubing news.
- Community chat.
- Competitions.
- Leaderboards.
- Achievements and progression levels.
- In-game currency and a cosmetic shop.
- Premium subscription.
- User settings.

Their release phase and detailed scope are to be determined; listing them here does not imply that all are part of the MVP.

## 9. Gamification and Economy Overview

Detailed rules are specified in `BUSINESS_RULES.md`.

### 9.1 Stars

- Stars represent achievement or performance recognition.
- Stars may contribute to leaderboards.
- Stars are not spendable currency.

### 9.2 In-game Currency

- Currency is separate from stars.
- Currency may be awarded for selected achievements or milestones.
- Currency is spent in the shop.
- The shop is intended for cosmetic items, such as themes, profile decorations, and timer appearance.
- Cosmetic purchases must not provide gameplay advantages.

**Decision confirmed 2026-11-22:** In-game currency is explicitly excluded from the MVP and will be considered for a later phase.

### 9.3 Achievements and Levels

- Achievements recognise defined user milestones or accomplishments.
- Selected achievements may award in-game currency.
- Levels are part of the progression experience.
- The exact relationship between levels, experience points, stars, achievements, course access, and rewards is TBD.

**Decision confirmed 2026-11-22:** Stars, achievements, and progression levels are explicitly excluded from the MVP and will be considered for a later phase.

## 10. Monetisation

Cubiland is planned to use a Free and Premium model.

The product must define:
- which capabilities are available to all users;
- which capabilities or content require Premium;
- how Premium access is granted and managed;
- how subscription status affects access to content and features;
- what happens when a subscription expires or is cancelled.

The exact feature split, subscription plans, prices, billing intervals, trial policy, and regional availability are TBD. No specific paywall behaviour should be implemented until these decisions are approved.

**Decision confirmed 2026-11-22:** Premium subscriptions and payment integration are explicitly excluded from the MVP. The provisional preferred payment solution for a future monetization phase is Stripe with Stripe Billing, but this is not an MVP requirement.

## 11. User and System Roles

| Role | Description |
|---|---|
| Visitor | A person who has not authenticated; public access is TBD |
| Registered user | An authenticated Cubiland user |
| Premium user | A registered user with an active Premium entitlement |
| Administrator | An authorised person who manages platform content or operations; permissions are TBD |

Premium is an entitlement associated with a user account, not necessarily a separate account type. The final role and permission model will be defined in the functional requirements.

## 12. High-Level Functional Areas

| Area | High-level capability |
|---|---|
| Account and profile | Registration, authentication, profile, and account settings |
| Learning | Courses, lessons, learning paths, and educational content |
| Algorithms | Algorithm reference, learning, and practice |
| Training | Exercises, tasks, and structured practice |
| Timer | Solve timing and scramble-related functionality |
| Solve records | Save, view, and manage recorded solves |
| Statistics | Analyse solve times and training progress |
| Progression | Levels, stars, achievements, and milestones |
| Economy | Currency rewards and cosmetic shop |
| Social and competition | Community, leaderboards, challenges, and competitions |
| Content and discovery | Scramble of the Day, speedcubing news, and multilingual content |
| Subscription | Free and Premium entitlements |
| Administration | Content and platform management; detailed scope TBD |

This table defines product areas, not a final technical architecture.

## 13. Non-Goals and Boundaries

- The first product focus is the 3×3×3 cube; broader puzzle support is planned for future consideration.
- The shop is intended for cosmetic items, not gameplay advantages.
- Stars and in-game currency are separate systems and must not be treated as interchangeable.
- This PRD does not prescribe a backend framework, frontend framework, database, hosting provider, or deployment architecture.
- This PRD does not define final UI layouts or visual design.
- This PRD does not establish final pricing, subscription terms, or Premium feature entitlements.

## 14. Product Constraints and Principles

- Support users with different levels of speedcubing knowledge.
- Connect learning content to practical exercises wherever applicable.
- Make solve records useful for tracking progress.
- Use gamification to encourage learning and practice without granting gameplay advantages through cosmetic purchases.
- Make requirements testable and traceable to user needs.
- Mark unconfirmed decisions as TBD rather than assuming answers.
- Maintain product documentation and repository artefacts in English.

## 15. Open Questions

The following questions are tracked as TBD decisions. Where a decision has already been made, it is noted with the date.

| # | Question | Status | Note |
|---|---|---|---|
| 1 | What exact learning methods and course content are included in the MVP? | **Decided 2026-11-22** | Only the beginner 3×3×3 course is included in MVP. CFOP is excluded. |
| 2 | Is CFOP included in the MVP, and what is the distinction between the CFOP and Full CFOP feature entries? | **Decided 2026-11-22** | Both CFOP and Full CFOP are excluded from MVP. |
| 3 | What is the intended schedule, cadence, and notification channels for Lesson Reminders? | Open | Reminder functionality is intended as a cron-style reminder for users to take lessons. |
| 4 | Which statistics are available to free users, and which require Premium? | Open | Original notation `50/50` retained. |
| 5 | Which challenges or tasks are included in the initial release? | **Decided 2026-11-22** | Practice challenges are excluded from MVP. |
| 6 | How are user levels calculated, and what do they unlock? | **Decided 2026-11-22** | Levels are excluded from MVP. |
| 7 | How are stars awarded, and exactly how do they affect leaderboards? | **Decided 2026-11-22** | Stars are excluded from MVP. |
| 8 | Which achievements exist, and which achievements award currency? | **Decided 2026-11-22** | Achievements are excluded from MVP. |
| 9 | What are the currency earning and spending rules? | **Decided 2026-11-22** | Currency is excluded from MVP. |
| 10 | Which cosmetic items are available in the shop at launch? | **Decided 2026-11-22** | Shop is excluded from MVP. |
| 11 | What is the exact Free/Premium feature and content split? | Open | Premium is excluded from MVP. |
| 12 | What are the account, profile, and settings requirements? | Open | Only essential settings included in MVP. |
| 13 | Which languages are supported initially? | Open | |
| 14 | What administrative tools are required to manage courses, algorithms, and other content? | Open | |
| 15 | Which timer capabilities and scramble sources are required for the first release? | Open | |
| 16 | What are the initial success targets and analytics requirements? | Open | Target values and measurement windows to be set before the MVP validation period. |

## 16. Risks and Assumptions

| Type | Item | Treatment |
|---|---|---|
| Assumption | Users value having learning, practice, timing, and statistics in one platform | Validate through interviews, prototypes, and usage data |
| Assumption | Gamified progression can support consistent practice | Validate through product experiments and retention data |
| Risk | Initial feature scope may become too broad | Control scope through explicit MVP boundaries and prioritisation |
| Risk | Unclear reward rules may lead to inconsistent implementation | Define business rules before implementation |
| Risk | Premium boundaries may disrupt the learning journey if poorly designed | Validate the Free/Premium split and test the user experience |
| Risk | Competitor feature information may be incomplete or change | Verify competitor capabilities during periodic research |

## 17. Definition of Done

This PRD is ready for approval when:
- The product vision and problem statement are agreed.
- Target audience and primary user needs are clear.
- Product goals and candidate success metrics are documented.
- The high-level user journey is understood.
- MVP scope and later capabilities are distinguished.
- Gamification concepts are described without conflating stars and currency.
- Free and Premium are acknowledged, with unresolved entitlements marked TBD.
- Open questions and assumptions are visible and assigned for resolution.
- The document is consistent with the approved Phase 1 discovery materials.

---

**Document status:** Initial Draft.
