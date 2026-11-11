# Acceptance Criteria

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

This document defines observable conditions that must be satisfied for selected user stories and functional requirements to be accepted.

Criteria use a Given/When/Then style where practical. These criteria are initial and must be refined after unresolved business rules are approved.

## 3. Account and Authentication

### AC-ACC-01 — Successful registration
- **Given** a visitor provides valid registration information,
- **When** the visitor submits the registration form,
- **Then** the system creates one account and confirms the outcome.

### AC-ACC-02 — Invalid registration
- **Given** a visitor provides missing or invalid required information,
- **When** the visitor submits the registration form,
- **Then** the system does not create an account and identifies the fields that require correction.

### AC-ACC-03 — Existing account
- **Given** the registration information conflicts with an existing account under the approved uniqueness policy,
- **When** the visitor submits registration,
- **Then** the system does not create a duplicate account and presents a safe next step.

### AC-ACC-04 — Successful sign-in
- **Given** a registered user provides valid authentication credentials,
- **When** the user submits the sign-in request,
- **Then** the system establishes an authenticated session and provides access to permitted account features.

### AC-ACC-05 — Failed sign-in
- **Given** a user provides invalid credentials,
- **When** the user attempts to sign in,
- **Then** the system denies access and displays a non-sensitive error.

### AC-ACC-06 — Account data isolation
- **Given** two different authenticated users,
- **When** either user requests private profile, progress, or solve data,
- **Then** the system returns only data that the requesting user is authorised to access.

## 4. Courses and Lessons

### AC-LRN-01 — Course catalogue visibility
- **Given** a user opens the learning area,
- **When** published courses are available to that user,
- **Then** the system displays those courses with their approved access status.

### AC-LRN-02 — Open an available lesson
- **Given** a user is entitled to access a published lesson,
- **When** the user selects that lesson,
- **Then** the system displays the lesson content.

### AC-LRN-03 — Restricted lesson
- **Given** a lesson requires an entitlement the user does not have,
- **When** the user attempts to open the lesson,
- **Then** the system denies the restricted content and displays the approved access explanation.

### AC-LRN-04 — Persist lesson progress
- **Given** an authenticated user completes a lesson according to its approved completion rule,
- **When** the completion is accepted,
- **Then** the system records the user's progress and displays the updated state.

### AC-LRN-05 — Resume learning
- **Given** a user has previously recorded course progress,
- **When** the user returns to that course,
- **Then** the system displays the persisted progress and the approved continuation option.

## 5. Algorithms and Exercises

### AC-ALG-01 — Algorithm presentation
- **Given** an algorithm is published,
- **When** an entitled user opens it,
- **Then** the system displays the approved algorithm notation and associated metadata.

### AC-ALG-02 — Practice result
- **Given** an exercise is configured to track progress,
- **When** the user completes the exercise,
- **Then** the system records the result according to that exercise's approved scoring rules.

Practice scoring and mastery criteria remain TBD until approved.

## 6. Timer and Solve Records

### AC-TMR-01 — Timer lifecycle
- **Given** the timer is ready,
- **When** the user starts and then stops the timer,
- **Then** the timer displays one completed elapsed-time result.

### AC-TMR-02 — Save a solve
- **Given** an authenticated user has a completed solve result,
- **When** the user saves the result,
- **Then** the system creates one solve record associated with that user.

### AC-TMR-03 — Solve history
- **Given** a user has saved solve records,
- **When** the user opens solve history,
- **Then** the system displays only records the user is authorised to view.

### AC-TMR-04 — Failed save
- **Given** a solve save operation cannot be completed,
- **When** the system reports the failure,
- **Then** it does not falsely indicate that the record was saved and provides a recoverable next step where possible.

### AC-TMR-05 — Edit or delete a solve
- **Given** a user is authorised to edit or delete their own solve record,
- **When** the user confirms the operation,
- **Then** the system applies the change and updates affected statistics.

### AC-TMR-06 — Record ownership
- **Given** a user attempts to modify another user's solve record,
- **When** the request is processed,
- **Then** the system rejects the operation.

Timer precision, penalty, DNF, and scramble-specific criteria are TBD.

## 7. Statistics

### AC-STA-01 — Basic statistics
- **Given** a user has eligible solve records,
- **When** the user opens statistics,
- **Then** the system displays the approved statistics calculated from the defined record set.

### AC-STA-02 — Empty history
- **Given** a user has no eligible solve records,
- **When** the user opens statistics,
- **Then** the system displays an appropriate empty state rather than misleading numerical results.

### AC-STA-03 — Statistics after record change
- **Given** a solve record included in a statistic is edited or deleted,
- **When** the operation succeeds,
- **Then** affected statistics reflect the updated eligible records.

### AC-STA-04 — Premium-restricted statistics
- **Given** a statistic requires Premium,
- **When** a user without the required entitlement requests it,
- **Then** the system does not disclose the restricted result and displays the approved access state.

## 8. Stars, Achievements, and Currency

### AC-GAM-01 — Separate balances
- **Given** a user has stars and in-game currency,
- **When** the user views progression or economy information,
- **Then** the system presents stars and currency as distinct values and does not allow stars to be spent as currency.

### AC-GAM-02 — Eligible star award
- **Given** an event satisfies an approved star-award rule,
- **When** the event is processed,
- **Then** the system records the applicable star award according to that rule.

### AC-GAM-03 — Achievement award idempotency
- **Given** a one-time achievement has already been awarded to a user,
- **When** the same achievement event is processed again,
- **Then** the system does not grant the achievement or its one-time reward again.

### AC-GAM-04 — Currency reward
- **Given** a user completes an event with an approved currency reward,
- **When** the event is accepted,
- **Then** the system credits the configured currency amount and records the transaction.

### AC-GAM-05 — No unapproved reward
- **Given** an event does not satisfy an approved reward rule,
- **When** it is processed,
- **Then** the system does not grant stars, achievements, or currency for that event.

### AC-GAM-06 — Duplicate event
- **Given** a reward event has already been processed,
- **When** the same event is delivered again,
- **Then** the system does not duplicate its one-time rewards.

Exact reward amounts and triggers are TBD.

## 9. Cosmetic Shop

### AC-SHP-01 — Sufficient balance purchase
- **Given** an item is available and the user has sufficient currency,
- **When** the purchase succeeds,
- **Then** the configured currency amount is deducted and the item is granted.

### AC-SHP-02 — Insufficient balance
- **Given** the user's balance is below the item price,
- **When** the user attempts to purchase the item,
- **Then** the system rejects the purchase and does not deduct currency.

### AC-SHP-03 — Unavailable item
- **Given** an item is unavailable,
- **When** the user attempts to purchase it,
- **Then** the system rejects the purchase and does not deduct currency.

### AC-SHP-04 — Purchase consistency
- **Given** a purchase operation fails,
- **When** the system completes failure handling,
- **Then** the user is not left charged without the item being granted.

### AC-SHP-05 — Cosmetic-only effect
- **Given** a user owns and equips a shop item,
- **When** the item is applied,
- **Then** it changes only its approved cosmetic presentation and does not alter gameplay outcomes.

## 10. Premium Entitlements

### AC-PRE-01 — Active Premium access
- **Given** a user has a valid active Premium entitlement,
- **When** the user requests a Premium resource,
- **Then** the system grants access.

### AC-PRE-02 — No Premium entitlement
- **Given** a user does not have the required Premium entitlement,
- **When** the user requests a Premium resource,
- **Then** the system denies access and presents the approved upgrade or access information.

### AC-PRE-03 — Expired entitlement
- **Given** a Premium entitlement has expired according to the trusted entitlement source,
- **When** the system evaluates access,
- **Then** it applies the approved post-expiration access policy.

## 11. Administration

### AC-ADM-01 — Authorised content management
- **Given** an administrator has the required permission,
- **When** the administrator creates or updates content with valid required fields,
- **Then** the system saves the content in the appropriate state.

### AC-ADM-02 — Unauthorised administration
- **Given** a user does not have the required administrative permission,
- **When** the user attempts an administrative operation,
- **Then** the system rejects the operation.

### AC-ADM-03 — Publishing validation
- **Given** content is missing required publication fields,
- **When** an administrator attempts to publish it,
- **Then** the system prevents publication and identifies the missing requirements.

## 12. Cross-Cutting Acceptance Criteria

- User-facing success messages must be shown only after the relevant operation has succeeded.
- Failed operations must not leave inconsistent currency, item ownership, or solve/statistics state.
- Protected resources must be inaccessible through direct requests when the user lacks permission.
- Empty states, loading states, and recoverable error states must be defined for each major user journey.
- Critical flows must be tested on the supported browsers and device classes.

## 13. Criteria Requiring Further Definition

The following cannot be finalised until business rules are approved:
- Exact course completion and prerequisite conditions.
- CFOP and Full CFOP scope.
- Algorithm exercise scoring and mastery.
- Timer precision, penalties, DNF, and scramble behaviour.
- Exact statistics formulas and record inclusion.
- Star thresholds, levels, achievement catalogue, and reward amounts.
- Currency earning limits and shop catalogue/prices.
- Free/Premium feature matrix and subscription lifecycle.
- Challenge and competition scoring, eligibility, and anti-cheat rules.
- Community moderation and reporting outcomes.
- Notification and reminder behaviour.

**Document status:** Initial Draft — requires product-owner review.
