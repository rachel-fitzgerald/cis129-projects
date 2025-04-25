# cis129-projects
This is going to be for all of my labs

# Tethered: A Relationship Wellness App

Tethered is a conceptual software solution designed to help couples strengthen their connection through daily check-ins, shared goals, and thoughtful prompts. Built for emotional well-being and intentional communication, Tethered provides a user-friendly and supportive space for couples to grow together.

---

## Problem Statement

Modern relationships often suffer from lack of intentional communication, especially in busy daily routines. While many apps exist for messaging or calendar sharing, few focus on **emotional well-being and daily connection** in a structured yet gentle way.

---

## Solution Overview

**Tethered** proposes a mobile application with:
- **Daily Check-In Prompts**
- **Mood Tracking**
- **Shared Journal Entries**
- **Relationship Goals**
- **Reflective Questions**

Unlike traditional messaging apps, Tethered is purpose-built to encourage mindful connection through brief, meaningful interactions.

---

## Key Features

- Personalized daily check-ins and mood tracking  
- Customizable relationship goals and milestones  
- Private shared journal space for reflections  
- Simple, clean user interface with calming design  

---

## Pseudocode Sample: Daily Check-In Logic

```pseudo
IF currentUserHasNotCheckedInToday:
    DISPLAY dailyPrompt
    RECEIVE userResponse
    STORE response in journalEntry
    IF partnerHasCheckedIn:
        SHOW partnerResponse
        ENABLE reflection feature
