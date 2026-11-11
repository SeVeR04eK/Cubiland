# MVP Definition

**Document status:** Proposed MVP scope  
**Version:** 1.0  
**Last updated:** 2026-11-11  
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
| MVP | Marked `Yes / Inc.` in the initial prioritization |
| Premium | Not planned as Premium-only content |

**Open scope decision:** The exact meaning of `Inc.` and the amount of CFOP content included in the MVP must be defined. The current plan retains CFOP in the MVP scope pending that definition.

### 4.3 Full CFOP

Full CFOP is listed separately in the feature plan and marked Must-have. The initial notes also associate it with an approximate sub-20 goal.

Its relationship to the general 3×3×3 CFOP course must be defined during requirements work. The separate entry is preserved until the course structure is specified.

### 4.4 Other Courses

Additional solving methods and puzzle courses are part of the broader product direction but are not included in the initial MVP scope.

Their release timing and Free/Premium treatment will be determined as the product roadmap develops.

## 5. Core MVP Capabilities

The current MVP plan includes the following capabilities:

| Capability | MVP status | Purpose |
|---|---|---|
| User profile and authentication | Included | Create an account and preserve user progress |
| 3×3×3 Beginner Course | Included | Provide the initial learning path |
| 3×3×3 CFOP | Included in principle; exact content scope to be defined | Support progression beyond beginner solving |
| Timer | Included | Measure solving times during practice |
| Statistics and analysis | Included | Review solving performance and progress |
| In-game currency | Marked for MVP | Support the planned reward system; detailed rules to be specified |
| Self-promotion | TBD pending definition | Optional sharing of personal milestones or profile links |
| Settings | MVP notation is `50/50` | Core settings and initial release scope to be specified |

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

### 7.3 Achievements

- Achievements recognize notable user milestones and accomplishments.
- Selected achievements may grant in-game currency.
- Achievement conditions and reward amounts will be defined during requirements work.

### 7.4 Levels and Progression

Levels are part of the intended progression experience. Their relationship to course access, stars, experience points (XP), achievements, and other progression mechanics remains to be defined.

## 8. Features Planned Beyond the MVP

The following features remain part of the broader product plan and are currently outside the initial MVP scope or have a later release target:

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

The following items will be resolved during Requirements Engineering. Items already settled are noted with the date and owner.

| # | Decision | Status | Note |
|---|---|---|---|
| 1 | Exact MVP content and structure of the CFOP course | Open | |
| 2 | Relationship between the CFOP course and the separate Full CFOP feature | Open | Two entries partially overlap; course structure must be specified first. |
| 3 | Meaning of the original `Inc.` notation | Open | Original notation retained to preserve provenance. |
| 4 | Basic and advanced scope of statistics | Open | |
| 5 | MVP behavior of training plans and practice sessions | Open | |
| 6 | Initial behavior of stars, achievements, currency, and levels | Open | |
| 7 | Meaning and behavior of the Self-promotion feature | **Deferred 2026-11-11** | Downgraded to Should-have, MVP TBD. Treated as social sharing of milestones / profile links pending a real spec. |
| 8 | MVP scope of Settings | Open | Original notation `50/50` retained. |
| 9 | Free/Premium boundaries and subscription benefits | Open | |
| 10 | Numerical MVP success targets | Open | Target values and measurement windows to be set before the MVP validation period. |
