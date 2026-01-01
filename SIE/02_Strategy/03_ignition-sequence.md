---
title: Strategic Intelligence Engine Ignition Sequence
id: 2.1
type:
  - PROCESS
steward: Adam Bernard
version: 8.0 (Business Blueprint)
last_updated: 2025-09-22
audience: Internal Use, Consulting Clients
---

# 🧩 Ignition v8.0 — FluentForm Field Map (Business Blueprint Only)

## **Step 1 – Welcome & Orientation**

- **HTML Block (Intro Text)**
    
    > “We’re about to create your **Marketing Blueprint**. This will be your **Flight Plan** — your single source of truth for brand and marketing clarity.”
    
- **Field: Business Name** _(Single Line Text)_
    
- **Field: Your Full Name** _(Single Line Text)_
    
- **Field: Work Email (required)** _(Email field)_
    
- **Field: Phone (optional)** _(Phone field)_
    

---

## **Step 2 – Idea Validation (Optional for Startups)**

- **Radio Button: “Where are you in your journey?”**
    
    - ( ) “We have an established business / validated idea.” _(Skip validator)_
    - ( ) “We’d like to test our idea first.” _(Show Idea Validator)_
- **Conditional Container: Idea Validator**
    
    - **Field: Idea Kernel** _(Textarea)_
    - **Field: Constraint Canvas** _(Textarea)_

👉 **Schema target:** `opportunity_and_solution` → pre-validation notes.

---

## **Step 3 – Foundational Identity**

- **Field: Vision Statement (The Why)** _(Textarea)_
- **Field: 5-Year Aspiration (Future Goal)** _(Textarea)_
- **Field: Mission Statement (The How)** _(Textarea)_
- **Field: Market Category** _(Single Line Text)_ (e.g., “AI Content Governance for WordPress”)
- **Multi-select: Brand Personality Traits** _(Checkbox list aligned with schema: Trustworthy, Data‑Driven, Collaborative, Expert, etc.)_

👉 **Schema target:** `core_identity`

---

## **Step 4 – Ideal Customer Profile (ICP)**

- **Field: Segment Name** _(e.g. “Mid-market SaaS Companies”)_ _(Single Line Text)_
- **Field: Demographics & Role(s)** _(Textarea)_
- **Field: Jobs-to-be-Done (what do they need to accomplish?)** _(Textarea)_
- **Field: Pain Points** _(Textarea)_
- *_Field: “Where do they hang out?” (watering holes, communities, platforms)_ _(Textarea)_

👉 **Schema target:** `opportunity_and_solution.ideal_customer_profile`

---

## **Step 5 – Offerings & Value Ladder**

- **Repeatable Section (add multiple offerings)**:
    - **Offering Name** _(Single Line Text)_
    - **Offering Description** _(Textarea)_
    - **Target Customer / Segment** _(Single Line Text)_
    - **Price Point** _(Single Line Text)_
    - **Strategic Value Unlocked** _(Textarea)_

👉 **Schema target:** `offerings_and_financials.commercial_offerings[]`

---

## **Step 6 – Brand Voice & Content Pillars**

- **Multi-select: Brand Voice Tone** _(Friendly, Bold, Expert, Storytelling, etc.)_
- **Repeatable Field: Content Pillar Topics (3–5)** _(Single Line Text)_

👉 **Schema target:** `opportunity_and_solution.unique_value_proposition` + `brand_kit`

---

## **Step 7 – Systems & Operations**

- **Multi-select: Current Tech Stack** _(CRM, CMS, Payments, Email, Analytics, etc.)_
- **Dropdown: Marketing Maturity**
    - Manual / Semi-Automated / Fully Automated
- **Field: Geographic Service Area** _(Single Line Text)_

👉 **Schema target:** `operations_and_roadmap.technology_stack.mvp_stack`

---

## **Step 8 – Competitive Landscape (Optional, but powerful)**

- **Repeatable Section (add up to 3)**:
    - **Competitor Category** _(Single Line Text)_
    - **Strengths** _(Textarea)_
    - **Weaknesses** _(Textarea)_
    - **Why We Win vs Them** _(Textarea)_

👉 **Schema target:** `opportunity_and_solution.competitive_landscape[]`

---

## **Step 9 – Handoff & Ownership Setup**

- **Checkbox:** “Yes, I understand this Blueprint will become my **single source of truth**.”
- **Optional: Agency/Referrer Name** _(Single Line Text)_
- **Email (for deliverable access)** _(defaults to Step 1 email, optional override if different)_

👉 **Schema target:** `metadata.steward` + CRM tags for partner attribution

---

# 🚀 Key Implementation Notes

1. **Field Labels → Schema Properties**
    
    - Keep IDs or admin labels in FluentForms identical to schema keys (e.g., `core_identity.vision`) → makes mapping to JSON trivial.
2. **Use Repeaters** for Offerings + Competitors so you capture arrays properly.
    
3. **Keep Branching Minimal**
    
    - Only Step 2 (Validation vs Skip) should use conditional logic. Everything else is linear and simple.
4. **Pipeline Targets**
    
    - FluentCRM: Store raw intake.
    - Zapier / WP Fusion / Custom Script: Transform → JSON conforming to `1.2 Schema.md`.
    - Insert into Obsidian/Client Vault as frontmatter for their Blueprint.