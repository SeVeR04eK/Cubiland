# MVP Definition

**Document status:** Confirmed MVP scope  
**Version:** 1.1  
**Last updated:** 2026-11-22  
**Author:** Andrii Severyn

## 1. MVP Purpose

The Minimum Viable Product (MVP) is the first usable release of Cubiland. Its purpose is to deliver the core learning and training experience to real users and evaluate whether the platform helps them learn, practice, and track their speedcubing progress.

The MVP establishes the foundation for the broader product vision. Features outside the initial release remain part of the planned product unless they are explicitly reconsidered.

Detailed functional behavior and acceptance criteria will be defined during Requirements Engineering.

## 2. Core Product Concept

Cubiland is a gamified speedcubing platform where users learn solving methods, practice algorithms, complete training activities, record solving times, and review their progress.

The initial product focus is the 3×3×3 Rubik's Cube. The planned learning scope includes beginner content and CFOP. The platform is intended to support additional courses and puzzle types as it evolves.

## 3. Core User Journey

The initial user journey is:

1. A visitor opens Cubiland.
2. The user creates an account or signs in.
3. The user selects a skill level or learning path.
4. The user opens a suitable course.
5. The user studies lessons and algorithms.
6. The user completes related exercises or training sessions.
7. The user records solving times using the timer.
8. The platform saves learning progress and solve history.
9. The user reviews statistics and continues training.

The exact onboarding, course-selection, and progression rules will be specified in the requirements phase.

## 4. Initial Course Scope

### 4.1 3×3×3 Beginner Course

| Attribute | Definition |
|---|---|
| Description | Beginner course covering a basic solving method and cube notation |
| User value | Learn the fundamentals of solving a 3×3×3 cube |
| MVP | Included |
| Premium | Not planned as Premium-only content |
| Learning goal | The initial planning target references a solving time of approximately sub-1 minute |

The sub-1-minute target is an illustrative learning goal, not a guaranteed result or a formal acceptance criterion.

### 4.2 3×3×3 CFOP

| Attribute | Definition |
|---|---|
| Description | Learning content for the CFOP advanced solving method |
| User value | Learn an advanced method and improve solving performance |
| MVP | **Excluded** — CFOP is not part of the MVP |
| Premium | TBD for future release |

**Decision confirmed 2026-11-22:** CFOP is explicitly excluded from the MVP. The beginner course is the only solving-method content included in the initial release. CFOP will be considered for a later phase.

### 4.3 Full CFOP

Full CFOP is explicitly excluded from the MVP. It is a future enhancement that may be delivered after the beginner course and core platform are established.

**Decision confirmed 2026-11-22:** Full CFOP is not part of the MVP and will be considered for a later release phase.

### 4.4 Other Courses

Additional solving methods and puzzle courses are part of the broader product direction but are not included in the initial MVP scope.

Their release timing and Free/Premium treatment will be determined as the product roadmap develops.

## 5. Core MVP Capabilities

The current MVP plan includes the following capabilities:

| Capability | MVP status | Purpose |
|---|---|---|
| User profile and authentication | Included | Create an account and preserve user progress |
| 3×3×3 Beginner Course | Included | Provide the initial learning path |
| 3×3×3 CFOP | **Excluded** | Not part of MVP; planned for future phase |
| Timer | Included | Measure solving times during practice |
| Statistics and analysis | Included | Review solving performance and progress |
| Settings | Partially included | Only essential settings for the first release |

Training plans and practice sessions are part of the core product concept. Their detailed MVP behavior will be defined in Requirements Engineering.

## 6. Proposed Core Experience

The MVP should connect learning and practice rather than present them as unrelated tools.

The intended experience is:

- Users can access structured learning content.
- Lessons introduce solving concepts or algorithms.
- Users can practice the relevant material.
- Timed solves can be recorded.
- Progress and solving statistics can be reviewed.
- The platform provides a basis for continued learning and training.

The detailed interaction rules, data to be stored, and measurable acceptance criteria will be documented in Phase 2.

## 7. Gamification and Reward System

Cubiland includes a gamification concept with distinct progression and reward mechanics.

### 7.1 Stars

- Stars are an achievement and score metric.
- Users may earn stars for completing lessons, exercises, or other defined activities.
- Stars may contribute to leaderboards.
- Stars are not spendable currency.

The exact star-awarding rules and leaderboard behavior will be defined separately.

### 7.2 In-game Currency

- Currency is awarded occasionally for selected achievements or milestones.
- Currency is separate from stars.
- Users can spend currency in the in-platform shop.
- Currency is intended for cosmetic items and personalization rather than gameplay advantages.

**Decision confirmed 2026-11-22:** In-game currency is explicitly excluded from the MVP. It will be considered for a later phase when the progression and reward system is implemented.

### 7.3 Achievements

- Achievements recognize notable user milestones and accomplishments.
- Selected achievements may grant in-game currency.
- Achievement conditions and reward amounts will be defined during requirements work.

### 7.4 Levels and Progression

Levels are part of the intended progression experience. Their relationship to course access, stars, experience points (XP), achievements, and other progression mechanics remains to be defined.

## 8. Features Planned Beyond the MVP

The following features remain part of the broader product plan and are currently outside the initial MVP scope or have a later release target:

- 3×3×3 CFOP and Full CFOP courses.
- In-game currency and cosmetic shop.
- Stars, achievements, and progression levels.
- Leaderboards.
- Practice challenges and challenge-based training modes.
- Premium subscriptions and Premium features.
- Payment integration.
- Additional courses and puzzle types.
- Community chat and rooms.
- Tasks and challenges.
- Video lessons.
- Scramble of the Day.
- Additional interface and content languages.
- Speedcubing news.
- Premium lessons and other Premium content.
- Shop and cosmetic customization.
- Competitions.
- Expanded social and profile-related functionality.

The feature prioritization document preserves the current priority and Free/Premium notes for each item.

## 9. Free and Premium Model

Cubiland is planned to include Free and Premium access.

The initial feature plan marks some learning content and video lessons as Premium, while the beginner course, timer, and several core capabilities are not planned as Premium-only.

The complete Free/Premium boundary, subscription benefits, billing options, and restrictions will be defined after the core user journeys and feature requirements are specified.

## 10. MVP Success Measures

The initial planning materials do not yet define numerical success targets. The following measures are proposed for evaluation:

- User registration and onboarding completion.
- Beginner course start and completion rates.
- Lesson-to-practice conversion.
- Number and frequency of recorded solves.
- Return rate for learning and training sessions.
- User progress through lessons and learning paths.
- User feedback on lesson clarity and training usefulness.
- Interest in Premium content and willingness to pay.

Target values and measurement windows will be defined before the MVP validation period.

## 11. Scope Decisions to Finalize

The following items will be resolved during Requirements Engineering. Items already settled are noted with the date.

| # | Decision | Status | Note |
|---|---|---|---|
| 1 | Exact MVP content and structure of the CFOP course | **Decided 2026-11-22** | CFOP is excluded from MVP. |
| 2 | Relationship between the CFOP course and the separate Full CFOP feature | **Decided 2026-11-22** | Both are excluded from MVP and planned for future phases. |
| 3 | Meaning of the original `Inc.` notation | **Decided 2026-11-22** | Resolved by explicit MVP exclusions. |
| 4 | Basic and advanced scope of statistics | Open | MVP includes basic statistics; advanced scope TBD for future. |
| 5 | MVP behavior of training plans and practice sessions | Open | Challenge-based practice is excluded from MVP. |
| 6 | Initial behavior of stars, achievements, currency, and levels | **Decided 2026-11-22** | All excluded from MVP; planned for future phase. |
| 7 | MVP scope of Settings | Open | Only essential settings included in MVP. |
| 9 | Free/Premium boundaries and subscription benefits | Open | Premium and payment integration excluded from MVP. |
| 10 | Numerical MVP success targets | Open | Target values and measurement windows to be set before the MVP validation period. |
