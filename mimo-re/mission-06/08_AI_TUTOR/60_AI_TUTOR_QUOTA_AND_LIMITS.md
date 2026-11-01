# Mission 6 — AI Tutor Quota and Limits

## Scope
Rate/usage limits visible to the client.

## Method
Count endpoint + field extraction + subscription interaction (AI gated behind plan?).

## Findings (VERIFIED_STATIC)
1. The only counter is `userMessageCount` (`AiTutorialConversationMessageCount`) fetched by
   `GET …/aiTutor/…/messages/count`; **no limit value** is present in the payload, so the threshold lives
   server-side.
2. No client-side blocking branch was recovered — a 402/403 from the start endpoint would be the only
   enforcement point (`INFERRED`).
3. `ui.upgrade.*` references tutor classes, suggesting the tutor upsell is tied to a paid plan
   (`INFERRED_HIGH`).
4. Subscription state comes from RevenueCat (`isPremium`), not from an AI-specific entitlement.

## Evidence labels
1, 4 **VERIFIED_STATIC**; 2, 3 **INFERRED**.

## Open questions
`Q-98` numeric quota; `Q-99` whether quota resets daily/weekly; `Q-100` free-tier availability.

## Reproduction
`grep -rn 'messages/count' ../mission-05/evidence/API_CATALOG_V2.csv`
