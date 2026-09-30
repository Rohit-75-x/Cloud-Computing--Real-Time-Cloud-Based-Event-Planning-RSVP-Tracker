# Real-Time Cloud-Based Event Planning & RSVP Tracker

## Overview
Real-time cloud-based event planning and RSVP platform featuring event management, live RSVP tracking, cloud authentication, capacity control, notifications, analytics, and scalable cloud architecture.

## Features
- **Role-Based Workflows:** Organizer and Attendee dashboards.
- **Real-Time Tracking:** Live updates of RSVP counts without manual refresh using Cloud Firestore.
- **Capacity Management:** Transaction-safe capacity enforcement prevents overbooking.
- **Waitlist Logic:** Automatic queueing when an event reaches maximum capacity.
- **REST APIs:** Secured via JWT authentication.

## Folder Structure
```
Cloud-Event-RSVP-Tracker/
├── frontend/               # React, Vite, Tailwind UI
├── backend/                # Python FastAPI REST endpoints
├── firebase/               # Firestore security rules and indices
└── docs/                   # Documentation and project reports
```

## Setup Instructions (Local Simulation)
1. **Clone & Environment:**
   `git clone <repo>`
2. **Backend Setup:**
   ```bash
   cd backend
   pip install -r requirements.txt
   uvicorn app:app --reload
   ```
3. **Frontend Setup:**
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

## Cloud Deployment (Student-Friendly Approach)
- **Frontend:** Deploy to Firebase Hosting (`firebase deploy --only hosting`) or Vercel.
- **Backend:** Deploy FastAPI to Render or Google Cloud Run.
- **Database:** Firebase Firestore (Free Tier).

## Screenshots Checklist Proofs
*Screenshots should be saved in `/docs/screenshots/` showing:*
1. Multi-browser real-time demonstration
2. Capacity utilization preventing a +1 RSVP
3. Organizer Dashboard analytics
4. Firebase Database records structure

## Author
Built as a Cloud Computing course project demonstrating SaaS architecture, real-time databases, and transactional safety.
