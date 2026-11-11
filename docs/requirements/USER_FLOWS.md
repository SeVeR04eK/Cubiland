# User Flows

## 1. Document Information

| Field | Value |
|---|---|
| Product | Cubiland |
| Phase | Requirements Engineering |
| Status | Initial Draft — Product Owner Review Required |
| Version | 0.1 |
| Last Updated | 2026-11-11 |
| Author | Andrii Severyn |

## 2. Purpose

This document describes high-level user journeys and system responses. It is intended to align product behaviour before detailed UI/UX design and implementation.

Flows are conceptual. Screen layouts, exact navigation patterns, validation copy, and edge-case policies remain subject to design and requirements review.

## 3. Actors

- **Visitor:** a person who has not signed in.
- **Registered user:** an authenticated user.
- **Premium user:** a registered user with an active Premium entitlement.
- **Administrator:** an authorised platform operator; detailed permissions are TBD.
- **Cubiland system:** application services that validate input, persist data, calculate results, and enforce product rules.

## 4. Flow: Registration and First Access

**Goal:** allow a visitor to create an account and enter Cubiland.

1. Visitor opens Cubiland.
2. System presents available entry points, including registration and sign-in.
3. Visitor chooses registration.
4. Visitor provides the required registration information.
5. System validates the input and checks account-creation constraints.
6. If valid, the system creates the account and establishes an authenticated session.
7. System presents the initial profile or onboarding experience.
8. User proceeds to select a learning path or explore available content.

**Alternative paths**
- Invalid input: show field-level validation and allow correction.
- Account already exists: offer sign-in or account-recovery route.
- Registration service unavailable: preserve recoverable input where safe and explain that registration could not be completed.
- Email verification or other verification requirement: exact policy TBD.

## 5. Flow: Sign-In and Account Recovery

**Sign-in**
1. User opens sign-in.
2. User provides credentials or another approved authentication method.
3. System validates credentials.
4. On success, system establishes a session and opens the user's account context.
5. On failure, system displays a non-sensitive error and permits retry.

**Account recovery**
1. User requests account recovery.
2. System requests the minimum required account identifier.
3. System sends or initiates the approved recovery mechanism.
4. User completes the verification and reset process.
5. System confirms the result.

Supported authentication methods, verification requirements, session policy, and recovery details are TBD.

## 6. Flow: Select a Learning Path

1. Authenticated user opens the learning area.
2. System displays available courses or learning paths.
3. User reviews course description, skill level, and access status.
4. User selects a course.
5. System opens the course overview and indicates progress.
6. User starts an available lesson.

**Alternative paths**
- Course requires Premium: show the access state and the approved Premium information.
- Course is unavailable or unpublished: do not allow the user to start it.
- User has existing progress: resume or open the course overview; exact default behaviour TBD.

## 7. Flow: Complete a Lesson

1. User opens a lesson within a course.
2. System presents lesson content and learning objectives.
3. User studies the content.
4. User completes any embedded demonstration or exercise, if present.
5. User submits the lesson completion action or meets the defined completion condition.
6. System records progress.
7. System displays the next recommended step or returns the user to the course.

Lesson completion rules, progress persistence, content formats, and whether completion can be repeated are TBD.

## 8. Flow: Learn and Practise an Algorithm

1. User opens the algorithm learning area or an algorithm from a lesson.
2. System displays the algorithm, notation, and related explanation.
3. User studies the algorithm.
4. User starts an available practice mode.
5. System presents the practice task.
6. User performs the required action or marks the attempt complete.
7. System records the practice result if supported by the selected exercise.
8. User repeats the exercise or returns to the lesson.

Algorithm notation conventions, practice modes, attempt scoring, and mastery rules are TBD.

## 9. Flow: Timer and Solve Recording

1. User opens the timer.
2. System displays the timer in its ready state.
3. User starts the timer using an approved input method.
4. User stops the timer when the solve is complete.
5. System displays the solve time.
6. System saves the solve record according to the approved save policy.
7. User may inspect, edit, or delete the record where permitted.
8. System updates relevant statistics after a valid record is saved.

**Alternative paths**
- User cancels or abandons a solve: exact handling TBD.
- User records a penalty or invalid solve: penalty model and data representation TBD.
- Save fails: system informs the user and provides a safe retry path; avoid silently losing the result.
- User edits or deletes a solve: statistics must be recalculated or updated consistently.

Timer input methods, inspection rules, penalties, scramble handling, precision, offline behaviour, and solve validation are TBD.

## 10. Flow: Review Solve History and Statistics

1. User opens solve history or statistics.
2. System retrieves the user's permitted solve records.
3. System displays records and available summaries.
4. User applies available filters or selects a time range.
5. System updates the displayed results.
6. User reviews trends and returns to training.

Available statistics, filtering dimensions, aggregation rules, and Premium restrictions are TBD. Statistics must be calculated from the applicable valid solve records and clearly identify the selected scope.

## 11. Flow: Progression, Stars, and Achievements

1. User completes an eligible activity or reaches a milestone.
2. System evaluates the relevant progression and achievement rules.
3. System records the eligible result.
4. System awards the applicable stars and/or achievement.
5. If the achievement has a currency reward, system credits the separate currency balance.
6. System informs the user of the result.
7. User can review progress, achievements, and relevant history.

Stars must not be treated as spendable currency. Duplicate awards, reversals, and reward idempotency rules are specified in `BUSINESS_RULES.md`.

## 12. Flow: Cosmetic Shop

1. User opens the shop.
2. System displays available cosmetic items and their prices.
3. User selects an item.
4. System checks item availability and the user's currency balance.
5. If sufficient, system confirms the purchase according to the approved confirmation policy.
6. System deducts currency and grants the cosmetic item as one consistent transaction.
7. User equips or applies the item where applicable.

**Alternative paths**
- Insufficient balance: show the required and available amounts.
- Item unavailable or already owned: prevent duplicate purchase and explain the state.
- Purchase processing fails: do not deduct currency without granting the item.
- Concurrent purchase attempts: prevent double spending.

Only cosmetic items are intended for the shop. Exact catalogue, pricing, refunds, gifting, and ownership rules are TBD.

## 13. Flow: Free and Premium Access

1. User requests a course, lesson, feature, or other gated resource.
2. System checks the user's current entitlement.
3. If access is included in the user's entitlement, system grants access.
4. If access requires Premium and the user does not have it, system presents the approved upgrade route.
5. If the user obtains Premium, the entitlement is updated after confirmation from the subscription/payment provider.
6. System grants access while the entitlement is active.

Subscription provider, billing flow, cancellation, expiration, grace periods, refunds, and entitlement refresh rules are TBD. Access checks must be enforced server-side for protected resources.

## 14. Flow: Challenges and Competitions

1. User opens the challenges or competitions area.
2. System displays currently available activities and eligibility information.
3. User selects an activity.
4. System presents rules, time window, and participation requirements.
5. User joins or starts the activity.
6. System records eligible participation and results.
7. System displays the outcome and any applicable recognition.

Challenge formats, competition formats, ranking rules, anti-cheat measures, scheduling, and eligibility are TBD.

## 15. Flow: Community Features

1. User opens the community area.
2. System displays available community spaces or conversations.
3. User views or participates according to permissions and community rules.
4. System applies moderation and reporting mechanisms.
5. User can report content or another user where that capability is provided.

Community chat scope, moderation roles, blocking, reporting, retention, and notification policies are TBD.

## 16. Flow: Settings and Profile

1. User opens profile or settings.
2. System displays editable account and preference information.
3. User changes an allowed setting.
4. System validates and saves the change.
5. System confirms the update or explains the validation error.

The exact profile fields, privacy controls, language settings, notification settings, and account deletion process are TBD.

## 17. Flow: Administrator Content Management

1. Administrator authenticates.
2. System verifies administrative permission.
3. Administrator opens the relevant content-management area.
4. Administrator creates, edits, previews, publishes, unpublishes, or archives content according to permissions.
5. System validates the content and records the change.
6. System makes published content available according to its visibility and entitlement rules.

The admin interface, approval workflow, audit log, and permission matrix are TBD.

## 18. Cross-Flow Requirements

- A user's progress and solve records must be associated with the correct account.
- Access to protected resources must be checked consistently.
- Failed writes must not silently create partial reward or purchase transactions.
- User-facing flows must communicate success, validation errors, and recoverable failures.
- Important actions must be safe against accidental duplicate submissions.
- Exact accessibility, localisation, privacy, and security requirements are defined in the corresponding requirements documents.

## 19. Open Decisions

The following journey-related policies are tracked as TBD.

| # | Flow Area | Decision | Status |
|---|---|---|---|
| 1 | Authentication | Registration fields and verification policy | Open |
| 2 | Onboarding | Onboarding questions and learning-path selection logic | Open |
| 3 | Learning | Lesson completion and course progression rules | Open |
| 4 | Practice | Algorithm practice modes and mastery criteria | Open |
| 5 | Timer | Timer controls, penalties, scramble source, and offline support | Open |
| 6 | History | Solve edit/delete policy and statistical recalculation | Open |
| 7 | Progression | Stars, levels, achievement, and currency calculation | Open |
| 8 | Shop | Shop catalogue, purchase confirmation, and refund policy | Open |
| 9 | Monetisation | Free/Premium entitlement matrix and subscription lifecycle | Open |
| 10 | Social | Challenge, competition, and community scope | Open |
| 11 | Settings | User settings, privacy, and account deletion | Open |
| 12 | Administration | Administrator permissions and content workflows | Open |

**Document status:** Initial Draft — requires product-owner review.
