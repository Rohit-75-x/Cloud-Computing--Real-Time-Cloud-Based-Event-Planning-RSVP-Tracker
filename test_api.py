import sys
import os

# Ensure backend directory is in path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'backend')))

from fastapi.testclient import TestClient
from backend.app import app

client = TestClient(app)

def run_tests():
    print("[START] Starting automated tests for Event RSVP Tracker API...\n")

    # 1. Create Event Test
    print("[TEST] Creating a new event with capacity 2...")
    response = client.post("/api/events", json={
        "title": "Cloud Computing Workshop",
        "capacity": 2,
        "date": "2026-10-15T10:00:00",
        "venue": "Virtual Room A"
    })
    assert response.status_code == 200
    event_id = response.json()["event_id"]
    print(f"[OK] Event created successfully. ID: {event_id}\n")

    # 2. RSVP User 1
    print("[TEST] User 1 RSVPs as GOING...")
    res1 = client.post(f"/api/events/{event_id}/rsvp", json={"user_id": "user_1", "status": "GOING"})
    assert res1.json()["status"] == "GOING"
    print("[OK] User 1 RSVP recorded as GOING.\n")

    # 3. RSVP User 2
    print("[TEST] User 2 RSVPs as GOING...")
    res2 = client.post(f"/api/events/{event_id}/rsvp", json={"user_id": "user_2", "status": "GOING"})
    assert res2.json()["status"] == "GOING"
    print("[OK] User 2 RSVP recorded as GOING. (Capacity is now full: 2/2)\n")

    # 4. Enforce Capacity / Waitlist Test
    print("[TEST] User 3 RSVPs as GOING (Should be Waitlisted due to capacity)...")
    res3 = client.post(f"/api/events/{event_id}/rsvp", json={"user_id": "user_3", "status": "GOING"})
    assert res3.json()["status"] == "WAITLISTED"
    print("[OK] User 3 was automatically WAITLISTED! Capacity control working.\n")

    # 5. Dashboard Analytics Test
    print("[TEST] Fetching live analytics for Organizer Dashboard...")
    analytics_res = client.get(f"/api/events/{event_id}/analytics")
    data = analytics_res.json()["analytics"]
    print(f"[STATS] Dashboard Counts: {data}")
    assert data["GOING"] == 2
    assert data["WAITLISTED"] == 1
    print("[OK] Analytics successfully aggregated.\n")
    
    print("[SUCCESS] ALL TESTS PASSED SUCCESSFULLY! The API is rock solid.")

if __name__ == "__main__":
    run_tests()
