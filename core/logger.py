from storage.database import SessionLocal, Log
from utils import should_offload
from storage.sheets import append_to_sheet

def store_event(event):
    db = SessionLocal()
    try:
        log_entry = Log(
            user=event["user"],
            timestamp=event["timestamp"],
            text=event["text"],
            tags=event["tags"]
        )
        db.add(log_entry)
        db.commit()
    finally:
        db.close()

    if should_offload():
        print("TODO: Offload to Google Sheets when threshold is hit.")
