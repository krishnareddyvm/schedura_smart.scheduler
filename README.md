# SmartScheduler

An AI-assisted productivity planner built with Streamlit. SmartScheduler combines task management, calendar planning, goal tracking, habit building, and analytics into a single dashboard that adapts to your preferences.

## Quick Start

- Ensure Python 3.11+ is available (the project was developed against 3.11).
- Create and activate a virtual environment, then install dependencies (via `uv sync`, `pip install -r`, or `pip install .`).
- From the project root, launch the UI: `streamlit run app.py`
- Open the provided localhost URL (defaults to `http://localhost:8501`) and complete the onboarding wizard.

Project icon

If you place an app icon image in `assets/` (name it `schedura_icon.png`, `icon.png`, or `favicon.png`), the app will use it as the page icon/favcon when it starts. See `assets/ICON_INSTALL.md` for details.

`data/user_data.json` stores your personalized configuration. Keep running Streamlit from the repo root so the app can read and write this file.

## Navigating the App

SmartScheduler uses Streamlit’s sidebar navigation. After onboarding you’ll see a multi-page interface with the following sections:

- **Dashboard (Home)** – Your daily snapshot, quick-add for tasks, habit streaks, and AI suggestions. Appears immediately after the onboarding form.
- **Tasks** – Full task manager with filtering, AI classification, and priority matrix.
- **Calendar** – Monthly/weekly/daily planners, event editor, ICS import/export, and Google Calendar sync scaffold.
- **Goals** – Long-term goal tracker with milestones and progress analytics.
- **Health & Habits** – Habit cards, streak tracking, daily check-ins, and health dashboards.
- **Analytics** – Cross-cutting metrics, charts, and AI-generated productivity insights.
- **Settings** – Profile preferences, category management, appearance toggles, and data tooling.

Use the sidebar to switch pages at any time. Streamlit remembers state within the running session.

## Onboarding & Profile

1. Launch the app and fill in the onboarding form (name, productivity patterns, health priorities).
2. SmartScheduler seeds default categories (Work, Personal, Health, Learning) and empty lists for tasks, goals, habits, and calendar events.
3. You can revise any profile preference later under **Settings → Profile**.

## Tasks Page

- **Filters**: Narrow by category, completion status, priority band (Critical/High/Medium/Low), and due-date ranges (Today, Next 7 Days, This Month, Custom).
- **Task List**: Inline checkboxes complete tasks and award points; edit/delete buttons open the form populated with existing data.
- **Add / Edit**: Titles, descriptions, categories, due dates, importance, and urgency sliders. AI suggests categories, importance, and urgency based on the title/description.
- **Priority Matrix**: Visualizes open tasks on an Eisenhower matrix and provides category completion charts plus AI “next tasks” recommendations.

## Calendar Page

- **Views**: Toggle Month, Week, Day, and Agenda layouts with quick navigation buttons.
- **Event Cards**: Colored by category, showing time spans, descriptions, and locations.
- **Add / Edit Events**: Specify title, description, location, category, and start/end times. Optionally convert a task into an event; SmartScheduler can suggest an optimal time slot based on your productivity profile and existing events.
- **Import / Export**: Download all events as an `.ics` file or import events from an ICS upload.
- **Google Calendar**: Buttons and fields for OAuth flow and syncing (requires supplying credentials/authorization code).

## Goals Page

- **Active Goals**: Filter by category, status, or target timeframe. Track percentage complete, target dates, and associated milestones.
- **Milestones**: Checkboxes update progress automatically; completing all milestones can mark the goal finished.
- **Add / Edit**: Define title, description, target date, category, and milestone list. Editing reuses the same form.
- **Analytics**: Plot goal progress, display completion metrics, and analyze completion durations.

## Health & Habits Page

- **Sidebar Check-ins**: One-click daily check-ins for each habit, with streak summaries and health priorities listed below.
- **Habit Cards**: Show frequency, descriptions, current/best streaks, and quick links to view history or delete.
- **History & Heatmap**: Visual heatmaps, recent check-in logs, and streak reset controls per habit.
- **Dashboards**: Plot streak trends, 7-day completion rates, check-ins by weekday, and offer smart health tips.
- **Add Habit**: Create habits with title, description, frequency, and category (health-focused categories surface first).

## Analytics Page

- **Time Range**: Analyze Last 7/30/90 days, All Time, or specify a custom range.
- **Category Filter**: Focus on specific categories or view them all.
- **Overview Metrics**: Task/goal completion rates, average habit streaks, and calendar event counts.
- **Charts**: Task completion trends, time-by-category, priority matrices, productivity by hour, habit streak charts, and goal progress visuals.
- **AI Insights**: Narrative highlights on productivity patterns, streaks to rebuild, category focus, and completion trends.

## Settings Page

- **Profile**: Update productivity peaks, break cadence, goal planning cadence, health priorities, and display name.
- **Categories**: Create/edit/delete color-coded categories with usage stats and stacked bar charts (deletion blocked if still in use).
- **Appearance**: Toggle dark/light themes (requires refresh) and see upcoming customization ideas.
- **Data Management**: Export/import JSON snapshots of all session data, reset progress, or reload from disk.

## Data & Persistence

- All state is stored in `data/user_data.json`. Delete it to reset the app.
- `save_user_data` writes after every change; `initialize_session_state` loads existing data on startup.
- Keep backups via **Settings → Data Management** before clearing data or switching machines.

## Troubleshooting

- **Port already in use**: Stop other Streamlit instances or run `streamlit run app.py --server.port 8502`.
- **Blank page**: Ensure the virtual environment is active and dependencies are installed; rerun `uv sync` or `pip install .` if needed.
- **Data not persisting**: Confirm you launched from the repo root so `data/user_data.json` can be found.
- **OAuth/Google Calendar**: You must supply your own client credentials; follow prompts in the sidebar during the integration flow.

## Development Notes

- Core entrypoint: `app.py`
- Feature pages: `pages/01_Tasks.py` through `pages/06_Settings.py`
- Utilities: `utils/` (data management, AI task classifier, calendar helpers, visualizations)
- Icons and assets: `assets/`

Video [Link](https://drive.google.com/file/d/1M6lRwNZHqXIaGwbrobXMenG-9ngpQZUg/view?usp=sharing)
PPT [Link](https://www.canva.com/design/DAG3jANI9IM/Px1p2onHiDJ6V4sWjkLTHQ/edit?utm_content=DAG3jANI9IM&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)
Report [Link](https://docs.google.com/document/d/1aSMvTCXIEwrQNmqjffPeiaypL8hV3J8W/edit?usp=drive_link&ouid=104500843271335283469&rtpof=true&sd=true)
