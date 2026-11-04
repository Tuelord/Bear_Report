# Bear Buddy --- All 9 Mermaid Diagrams Source Code

File tổng hợp toàn bộ 9 mã nguồn Mermaid của báo cáo Bear Buddy. Bạn có thể sao chép trực tiếp vào [Mermaid Live Editor](https://mermaid.live) hoặc biên dịch bằng `mmdc` (Mermaid CLI) để xuất thành file ảnh PNG/SVG.

---

## Figure 3.1: Use-Case Diagram of the Bear Buddy System

File riêng: `diagrams/01_use_case_diagram.mmd`

```mermaid
flowchart LR
    %% Actors
    Child(["Child Learner\n(PERS01 - Minh)"])
    Parent(["Parent\n(PERS02 - Ms. An)"])
    Teacher(["Support Teacher\n(PERS03 - Ms. Mai)"])
    AISpeech(["AI & Speech Services\n(TTS / STT / AI API)"])

    subgraph BearBuddy ["Bear Buddy Application System"]
        direction TB

        subgraph ChildModeGroup ["Child Mode Subsystem (Story Experience)"]
            UC06(["UC06: View Story Context & Listen to Narration (S08-S09)"])
            UC07(["UC07: Perform Decision Activity (S10)"])
            UC08(["UC08: Observe Consequence, View Why & Retry (S11-S12)"])
            UC09(["UC09: Request Pause (Break) or Need Help (S13)"])
            UC10(["UC10: Practice Voice Interaction in Scenario E (S24)"])
        end

        subgraph CaregiverModeGroup ["Caregiver Mode Subsystem (Preparation, Management & Review)"]
            UC01(["UC01: Complete Onboarding & Caregiver Verification (S01-S02)"])
            UC02(["UC02: Manage Child Profiles & Teacher Access Links (S03, S20)"])
            UC03(["UC03: Configure Support & Accessibility Settings (S04, S19)"])
            UC04(["UC04: Browse, Search & Preview Social Stories (S05-S07)"])
            UC05(["UC05: Receive Explainable AI Story Suggestions (S18)"])
            UC11(["UC11: View Session History & Versioned Review (S15-S16)"])
            UC12(["UC12: Manage Learning Plan & Activity Reminders (S17, S19)"])
            UC13(["UC13: Manage Privacy, Microphone & Data Consent (S20)"])
            UC14(["UC14: Access Help/FAQ & Submit Feedback/Issue Reports (S21-S23)"])
        end
    end

    %% Actor Associations - Child
    Child --> UC06
    Child --> UC07
    Child --> UC08
    Child --> UC09
    Child --> UC10

    %% Actor Associations - Parent
    Parent --> UC01
    Parent --> UC02
    Parent --> UC03
    Parent --> UC04
    Parent --> UC05
    Parent --> UC11
    Parent --> UC12
    Parent --> UC13
    Parent --> UC14

    %% Actor Associations - Teacher (Authorized scope)
    Teacher --> UC01
    Teacher --> UC04
    Teacher --> UC11
    Teacher --> UC14

    %% External Service Associations
    UC05 --> AISpeech
    UC06 --> AISpeech
    UC10 --> AISpeech

    %% Include / Extend Relationships
    UC07 -.->|"<<include>>"| UC06
    UC08 -.->|"<<include>>"| UC07
    UC09 -.->|"<<extend>>"| UC06
    UC10 -.->|"<<extend>>"| UC07
    UC05 -.->|"<<extend>>"| UC04
```

---

## Figure 3.2: Context Diagram of the Bear Buddy System

File riêng: `diagrams/02_context_diagram.mmd`

```mermaid
flowchart LR
    Child["Child Learner\n(PERS01 - Minh)"]
    Parent["Parent\n(PERS02 - Ms. An)"]
    Teacher["Support Teacher\n(PERS03 - Ms. Mai)"]
    System(["0.0\nBear Buddy\nApplication System"])
    SpeechSvc["On-Device Speech & Audio\n(Native TTS / STT)"]
    AISvc["AI Recommendation Service\n(Grounded API)"]
    NotifySvc["OS Notification Service\n(Local Reminders)"]

    Child -->|"Tap choices, Replay, Retry,\nPause/Need Help, Short speech (Scenario E)"| System
    System -->|"Contextual illustrations, Short text, Narration,\nAction -> Reaction -> Why feedback"| Child

    Parent -->|"Profile setup, Accessibility settings,\nStory selection, Access links, AI goals, Reminders"| System
    System -->|"Story preview, Explainable AI suggestions,\nVersioned session review, Consent status"| Parent

    Teacher -->|"Link verification, Story selection & preview,\nSession launch, Observational review"| System
    System -->|"Authorized profiles, Story preview,\nScoped session review records"| Teacher

    System -->|"Narration text / Ephemeral audio buffer (Scenario E)"| SpeechSvc
    SpeechSvc -->|"Single-stream audio / Keyword match result"| System

    System -->|"Anonymized situational goal & skill tags"| AISvc
    AISvc -->|"Recommended story IDs & Match reasons"| System

    System -->|"Scheduled reminder time & days"| NotifySvc
    NotifySvc -->|"Caregiver reminder notifications"| Parent
```

---

## Figure 3.3: Level 0 Data Flow Diagram of the Bear Buddy System

File riêng: `diagrams/03_dfd_level_0.mmd`

```mermaid
flowchart TB
    %% External Entities
    Child["Child Learner (PERS01)"]
    Parent["Parent (PERS02)"]
    Teacher["Support Teacher (PERS03)"]
    SpeechSvc["Native TTS / STT Service"]
    AISvc["AI Recommendation Service"]
    NotifySvc["OS Notification Service"]

    %% Processes
    P1(("1.0\nProfile, Role Access\n& Accessibility\nManagement"))
    P2(("2.0\nVersioned Library,\nSearch & Story\nPreview"))
    P3(("3.0\nInteractive Story\nEngine & Player\n(Child Mode)"))
    P4(("4.0\nScenario E Voice\n& Touch Fallback\nProcessor"))
    P5(("5.0\nSession Logging,\nVersioned Review\n& Learning Plan"))
    P6(("6.0\nExplainable AI,\nHelp/FAQ &\nIssue Reporting"))

    %% Data Stores
    D1[("D1: Profiles & Access Links")]
    D2[("D2: Accessibility & Privacy")]
    D3[("D3: Versioned Story Library")]
    D4[("D4: Session & Interaction Logs")]
    D5[("D5: Plans, Reminders & Feedback")]

    %% Flows - Process 1
    Parent -->|"Profile data, Teacher link, Accessibility config"| P1
    Teacher -->|"Auth credentials & Authorized profile selection"| P1
    P1 <-->|"Read/Write profiles & role links"| D1
    P1 <-->|"Read/Write font, audio, motion & consent"| D2

    %% Flows - Process 2
    Parent -->|"Search query, Category filter, Preview request"| P2
    Teacher -->|"Search & Preview request"| P2
    P2 <-->|"Query stories & story_version"| D3
    P2 -->|"Story details & full scene preview"| Parent
    P2 -->|"Launch selected story_version"| P3

    %% Flows - Process 3
    D2 -->|"Apply font scale, speech rate, reduce motion"| P3
    D3 -->|"Load scenes, choices & Why explanations"| P3
    Child -->|"Tap choice, Replay, Retry, Pause, Need Help"| P3
    P3 -->|"Narration text utterance"| SpeechSvc
    SpeechSvc -->|"Single-stream audio playback"| P3
    P3 -->|"Scene illustration, Reaction & Why explanation"| Child
    P3 -->|"Log chronological interaction events & status"| P5

    %% Flows - Process 4
    Child -->|"Spoken phrase or Parallel touch card selection"| P4
    D2 -->|"Verify Microphone consent"| P4
    P4 -->|"Ephemeral audio stream (if Voice used)"| SpeechSvc
    SpeechSvc -->|"Recognized keyword transcript"| P4
    P4 -->|"Confirmed choice / Touch fallback trigger"| P3

    %% Flows - Process 5
    P5 <-->|"Write/Read session logs pinned to story_version"| D4
    D3 -->|"Resolve exact historical story_version text"| P5
    P5 -->|"Descriptive Session Review (no ASD scoring)"| Parent
    P5 -->|"Scoped Session Review"| Teacher
    Parent -->|"Select planned stories & reminder time"| P5
    P5 <-->|"Save learning plan & reminder config"| D5
    P5 -->|"Schedule local notification"| NotifySvc
    NotifySvc -->|"Caregiver reminder alert"| Parent

    %% Flows - Process 6
    Parent -->|"Situational goal input / Feedback submission"| P6
    D2 -->|"Check AI history sharing consent"| P6
    D3 -->|"Valid library catalog metadata"| P6
    P6 -->|"Anonymized goal & skill query"| AISvc
    AISvc -->|"Recommended story IDs & explanations"| P6
    P6 -->|"Explainable suggestions & alternative options"| Parent
    P6 -->|"Queue feedback report"| D5
```

---

## Figure 4.1: Five Structural Stages of a Bear Buddy Story

File riêng: `diagrams/04_story_five_stages.mmd`

```mermaid
flowchart LR
    G1["1. Context Setup\n(Scene Context - S09)\nWho, where, what is happening"] --> G2["2. Social Cue & Task\n(Explicit Cue - S09/S10)\nHighlight facial, gesture & situational cues"]
    G2 --> G3["3. Decision Activity\n(Choice / Tap-to-Order - S10/S24)\nPredict & select a response"]
    G3 --> G4["4. Consequence & Why\n(Outcome & Reason - S11/S12)\nAction -> Reaction -> Why"]
    G4 --> G5["5. Consolidation\n(Closure & Summary - S14)\nAffirm key concept & adult review"]
    G4 -.->|"Replay / Retry\n(Penalty-Free)"| G3
```

---

## Figure 6.1: Three-Layer Offline-First Architecture Diagram

File riêng: `diagrams/05_system_architecture.mmd`

```mermaid
flowchart TB
    subgraph PresentationLayer ["Presentation Layer (SwiftUI Views - S01..S24)"]
        direction LR
        CaregiverUI["Caregiver Mode Views\n(S01-S07, S15-S23)\nOnboarding, Library, Review, Plan, Settings"]
        GateUI["Caregiver Gate & Role Guard\n(S02, S20)"]
        ChildUI["Child Mode Views\n(S08-S14, S24)\nOrientation, Context, Decision, Consequence, Why"]
    end

    subgraph DomainServiceLayer ["Application & Domain Layer (MVVM ViewModels & Modules)"]
        direction TB
        MOD01["MOD01: Account, Profile &\nRole Access Manager"]
        MOD02["MOD02: Versioned Story\nLibrary Repository"]
        MOD03["MOD03: Interactive Story\nEngine & Loop Controller"]
        MOD04["MOD04: Accessibility &\nAudio Narration Controller"]
        MOD05["MOD05: Scenario E Voice &\nTouch Fallback Controller"]
        MOD06["MOD06: Session Logger,\nReview & Plan Manager"]
        MOD07["MOD07: Explainable Parent\nAI Coach Service"]
    end

    subgraph DataInfrastructureLayer ["Local Persistence & Platform Infrastructure Layer"]
        direction LR
        MOD08[("MOD08: SQLite3 Local Database\n(Profiles, Versioned Stories,\nSessions, Plans, Audit Logs)")]
        LocalAssets[("Local Media Bundle\n(Illustrations & Audio)")]
        OSServices["iOS Native Frameworks\n(AVSpeechSynthesizer,\nSFSpeechRecognizer,\nUNUserNotificationCenter)"]
        ExternalAI["External AI Recommendation API\n(Grounded & Anonymized Gateway)"]
    end

    CaregiverUI --> MOD01
    CaregiverUI --> MOD02
    CaregiverUI --> MOD06
    CaregiverUI --> MOD07
    GateUI --> MOD01

    ChildUI --> MOD03
    ChildUI --> MOD04
    ChildUI --> MOD05

    MOD01 --> MOD08
    MOD02 --> MOD08
    MOD02 --> LocalAssets
    MOD03 --> MOD02
    MOD03 --> MOD04
    MOD03 --> MOD05
    MOD03 --> MOD06
    MOD06 --> MOD08
    MOD06 --> OSServices
    MOD04 --> OSServices
    MOD05 --> OSServices
    MOD07 --> MOD02
    MOD07 --> MOD08
    MOD07 -.->|"HTTPS (Opt-in & Anonymized)"| ExternalAI
```

---

## Figure 6.2: SQLite Entity-Relationship Diagram (ERD)

File riêng: `diagrams/06_sqlite_erd.mmd`

```mermaid
erDiagram
    CAREGIVERS ||--o{ CHILD_PROFILES : "owns (Primary Parent)"
    CAREGIVERS ||--o{ PROFILE_ACCESS_LINKS : "granted_to (Teacher)"
    CHILD_PROFILES ||--o{ PROFILE_ACCESS_LINKS : "shared_via"
    CHILD_PROFILES ||--|| ACCESSIBILITY_SETTINGS : "configured_with"
    CHILD_PROFILES ||--o{ LEARNING_SESSIONS : "participates_in"
    CHILD_PROFILES ||--o{ LEARNING_PLANS : "has_planned"
    CHILD_PROFILES ||--o{ CONSENT_AUDIT_LOGS : "records_consent"

    STORIES ||--|{ STORY_VERSIONS : "has_versions"
    STORY_VERSIONS ||--|{ STORY_STEPS : "contains_steps"
    STORY_STEPS ||--o{ STEP_OPTIONS : "offers_choices"

    STORY_VERSIONS ||--o{ LEARNING_SESSIONS : "experienced_in"
    CAREGIVERS ||--o{ LEARNING_SESSIONS : "supervised_by"
    LEARNING_SESSIONS ||--|{ SESSION_INTERACTIONS : "logs_events"
    STORIES ||--o{ LEARNING_PLANS : "scheduled_in"

    CAREGIVERS {
        TEXT caregiver_id PK
        TEXT display_name
        TEXT role_type "PARENT | TEACHER"
        TEXT pin_or_auth_hash
        TEXT created_at
    }

    CHILD_PROFILES {
        TEXT child_id PK
        TEXT owner_parent_id FK
        TEXT nickname
        TEXT avatar_key
        TEXT communication_notes
        TEXT support_level_notes
        TEXT created_at
    }

    PROFILE_ACCESS_LINKS {
        TEXT link_id PK
        TEXT child_id FK
        TEXT teacher_caregiver_id FK
        TEXT permission_scope "VIEW_AND_RUN_SESSION"
        TEXT link_status "ACTIVE | REVOKED"
        TEXT granted_at
        TEXT revoked_at
    }

    ACCESSIBILITY_SETTINGS {
        TEXT child_id PK, FK
        REAL font_scale_factor "1.0 to 2.0"
        INTEGER high_contrast_enabled "0 or 1"
        INTEGER auto_narration_enabled "0 or 1"
        REAL speech_rate "0.35 to 0.65"
        INTEGER reduce_motion_enabled "0 or 1"
        INTEGER scenario_e_voice_enabled "0 or 1"
        TEXT preferred_interaction_mode "TAP | TAP_AND_VOICE"
        TEXT updated_at
    }

    STORIES {
        TEXT story_id PK
        TEXT category_code "CAT01..CAT04"
        TEXT current_version_id FK
        INTEGER is_demo_seed "0 or 1"
        INTEGER completion_count_30d
    }

    STORY_VERSIONS {
        TEXT story_version_id PK
        TEXT story_id FK
        TEXT version_number "e.g., 1.0, 1.1"
        TEXT title_vi
        TEXT goal_summary
        TEXT target_cues_summary
        TEXT author_name
        TEXT reviewer_name
        TEXT published_at
    }

    STORY_STEPS {
        TEXT step_id PK
        TEXT story_version_id FK
        INTEGER step_order
        TEXT step_type "CONTEXT | DECISION | SCENARIO_E | CLOSURE"
        TEXT scene_image_asset
        TEXT narration_text
        TEXT social_cue_highlight
        TEXT prompt_question
        TEXT target_voice_phrase
    }

    STEP_OPTIONS {
        TEXT option_id PK
        TEXT step_id FK
        INTEGER display_order
        TEXT option_label
        TEXT option_image_asset
        TEXT reaction_image_asset
        TEXT reaction_text
        TEXT why_explanation_text
        INTEGER is_constructive_choice "0 or 1"
    }

    LEARNING_SESSIONS {
        TEXT session_id PK
        TEXT child_id FK
        TEXT caregiver_id FK
        TEXT story_id FK
        TEXT story_version_id FK
        TEXT session_status "IN_PROGRESS | PAUSED | COMPLETED"
        INTEGER last_step_order
        TEXT started_at
        TEXT ended_at
        TEXT caregiver_reflection_note
    }

    SESSION_INTERACTIONS {
        TEXT interaction_id PK
        TEXT session_id FK
        TEXT step_id FK
        TEXT option_id FK "NULL if Replay/Pause/Help"
        TEXT action_type "CHOOSE_TAP | CHOOSE_VOICE | REPLAY | RETRY | PAUSE | HELP"
        INTEGER attempt_number
        TEXT created_at
    }

    LEARNING_PLANS {
        TEXT plan_id PK
        TEXT child_id FK
        TEXT story_id FK
        TEXT reminder_time_hhmm
        TEXT reminder_days_mask
        INTEGER notification_enabled "0 or 1"
        TEXT status "PLANNED | DONE"
    }

    CONSENT_AUDIT_LOGS {
        TEXT log_id PK
        TEXT child_id FK
        TEXT caregiver_id FK
        TEXT consent_type "MICROPHONE | AI_HISTORY_USE | TEACHER_LINK"
        TEXT new_state "GRANTED | REVOKED"
        TEXT timestamp
    }
```

---

## Figure 6.3: Sequence Diagram 1: Story Learning Flow and Review

File riêng: `diagrams/07_sequence_story_learning.mmd`

```mermaid
sequenceDiagram
    actor Caregiver as Caregiver (PERS02/PERS03)
    actor Child as Child Learner (PERS01)
    participant UI as SwiftUI Views (S07..S16)
    participant Engine as MOD03: StoryEngine
    participant Audio as MOD04: SpeechController
    participant Logger as MOD06: Session & Review
    participant DB as MOD08: SQLite Database

    Caregiver->>UI: Open Story Details & Preview (S07)
    UI->>DB: Query story metadata & active story_version
    DB-->>UI: Return StoryVersion + Steps + Options
    Caregiver->>UI: Tap "Start with Child" (Enter Child Mode)
    UI->>Logger: createSession(child_id, caregiver_id, story_version_id)
    Logger->>DB: INSERT INTO learning_sessions (IN_PROGRESS)

    loop For each scene in story (S09 -> S12)
        Engine->>UI: Render Story Context & Social Cues (S09)
        Engine->>Audio: speakSingleStream(narration_text)
        Audio-->>Child: Play narration (preventing audio overlap)

        Child->>UI: Tap Choice Card on Decision Activity (S10)
        UI->>Engine: selectOption(step_id, option_id)
        Engine->>Logger: logInteraction(CHOOSE_TAP, step_id, option_id, attempt)
        Logger->>DB: INSERT INTO session_interactions

        Engine->>UI: Render Consequence (S11) & Why Explanation (S12)
        Engine->>Audio: speakSingleStream(reaction_text + why_explanation)

        alt Child taps "Replay" (Listen Again)
            Child->>UI: Tap "Replay" button (S12)
            UI->>Logger: logInteraction(REPLAY, step_id)
            Engine->>Audio: stopCurrentAndReplay()
        else Child taps "Try Another Way" (Penalty-Free Retry)
            Child->>UI: Tap "Try Another Way" (S12)
            UI->>Logger: logInteraction(RETRY, step_id)
            Engine->>UI: Return to Decision Activity (S10)
        else Child taps "Pause" or "Need Help" (S13)
            Child->>UI: Tap "Pause / Need Help"
            UI->>Audio: stopImmediately()
            UI->>Logger: logInteraction(PAUSE_OR_HELP, step_id)
            Logger->>DB: UPDATE learning_sessions SET status='PAUSED'
            UI-->>Child: Display calm Pause & Help screen (S13)
        end
    end

    Engine->>UI: Display Session End screen (S14 - No Auto-Play)
    Logger->>DB: UPDATE learning_sessions SET status='COMPLETED'

    Caregiver->>UI: Pass Caregiver Gate & Open Session Review (S16)
    UI->>Logger: getSessionReview(session_id)
    Logger->>DB: SELECT session + interactions JOIN story_versions ON story_version_id
    DB-->>UI: Return exact choices & explanations from experienced story_version
    UI-->>Caregiver: Render descriptive observational review (S16)
```

---

## Figure 6.4: Sequence Diagram 2: Scenario E Voice Interaction and Touch Fallback

File riêng: `diagrams/08_sequence_voice_interaction.mmd`

```mermaid
sequenceDiagram
    actor Child as Child Learner (PERS01)
    participant S24 as S24: Scenario E View
    participant VoiceMod as MOD05: VoiceController
    participant OSSTT as iOS SFSpeechRecognizer
    participant Engine as MOD03: StoryEngine
    participant DB as MOD08: SQLite Database

    Engine->>DB: Check scenario_e_voice_enabled & Microphone Consent
    DB-->>Engine: Voice configuration state
    Engine->>S24: Render model phrase + "Tap to Speak" + Parallel Touch Cards

    alt Path 1: Child taps an illustrated Touch Card directly (No speech used)
        Child->>S24: Tap illustrated Choice Card
        S24->>Engine: confirmChoiceByTap(option_id)
        Engine->>DB: Log CHOOSE_TAP (Fully valid completion)
        Engine->>S24: Advance to Consequence screen (S11)
    else Path 2: Child taps "Tap to Speak"
        Child->>S24: Tap "Tap to Speak" button
        S24->>VoiceMod: startBoundedListening(target_phrase, maxDuration=4s)

        alt Microphone Permission Denied (Microphone Denied)
            VoiceMod-->>S24: Return Microphone Denied state (S23)
            S24-->>Child: Highlight parallel Touch Cards for immediate tap selection
        else On-Device Ephemeral Speech Recognition
            VoiceMod->>OSSTT: Process audio buffer in RAM (Never saved to disk)
            OSSTT-->>VoiceMod: Recognized transcript string

            alt Transcript matches target functional keyword
                VoiceMod-->>S24: Confirm keyword match
                S24->>Engine: confirmChoiceByVoice(option_id)
                Engine->>DB: Log CHOOSE_VOICE
                Engine->>S24: Advance to Consequence screen (S11)
            else Unclear speech or timeout (Speech Not Recognized)
                VoiceMod-->>S24: Return Speech Not Recognized state (S23)
                S24-->>Child: Display "Not heard clearly. Choose a picture or try again"
                Child->>S24: Tap Touch Card to proceed without friction
                S24->>Engine: confirmChoiceByTap(option_id)
            end
        end
    end
```

---

## Figure 6.5: State Diagram: Story Player State Machine

File riêng: `diagrams/09_state_machine.mmd`

```mermaid
stateDiagram-v2
    [*] --> CaregiverPreview : Caregiver selects story (S07)
    CaregiverPreview --> ChildOrientation : Tap "Start" (If first session - S08)
    CaregiverPreview --> ContextPresentation : Tap "Start" (S09)
    ChildOrientation --> ContextPresentation : Child ready (S09)

    state ChildModeActive {
        ContextPresentation : S09 - Story Context & Social Cues\n(Single-stream narration)
        DecisionActivity : S10 / S24 - Decision Activity\n(Tap Choice Card or Bounded Voice + Fallback)
        ConsequenceView : S11 - Character Reaction\n(Action -> Reaction)
        WhyExplanation : S12 - Contextual Why Explanation\n(Reaction -> Why)
        PausedOrHelp : S13 - Paused / Need Help State\n(Halt audio, persist step index)

        ContextPresentation --> DecisionActivity : Tap Next
        DecisionActivity --> ConsequenceView : Select option (Tap / Voice)
        ConsequenceView --> WhyExplanation : Advance to explanation

        WhyExplanation --> WhyExplanation : Tap "Replay" (Listen again)
        WhyExplanation --> DecisionActivity : Tap "Try Another Way" (Retry)
        WhyExplanation --> ContextPresentation : Tap "Next" (More scenes remain)

        ContextPresentation --> PausedOrHelp : Tap Pause / Need Help
        DecisionActivity --> PausedOrHelp : Tap Pause / Need Help
        WhyExplanation --> PausedOrHelp : Tap Pause / Need Help
        PausedOrHelp --> ContextPresentation : Resume at paused context scene
        PausedOrHelp --> DecisionActivity : Resume at paused decision step
    }

    WhyExplanation --> SessionCompleted : Final scene completed (S14)
    PausedOrHelp --> CaregiverReview : Caregiver authenticates to end early
    SessionCompleted --> CaregiverReview : Caregiver authenticates & reviews (S16)
    CaregiverReview --> [*]
```

---
