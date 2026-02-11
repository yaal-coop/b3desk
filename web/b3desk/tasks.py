import os

import requests
from celery import Celery
from celery.schedules import crontab
from celery.utils.log import get_task_logger

REDIS_URL = os.environ.get("REDIS_URL")
DEBUG = os.environ.get("FLASK_DEBUG")

celery = Celery("tasks")
celery.conf.broker_url = f"redis://{REDIS_URL}"
celery.conf.result_backend = f"redis://{REDIS_URL}"
celery.conf.beat_schedule = {
    "delete-old-meetings-every-day-at-5-am": {
        "task": "delete-old-meetings",
        "schedule": crontab(minute=00, hour=5),
    },
}

logger = get_task_logger(__name__)


@celery.task(name="delete-old-meetings")
def delete_old_meetings():
    """Celery cron task to delete expired meetings from database."""
    from datetime import datetime

    from b3desk import create_app

    app = create_app()
    with app.app_context():
        from b3desk.models import db
        from b3desk.models.meetings import DATA_RETENTION
        from b3desk.models.meetings import Meeting
        from b3desk.models.meetings import save_voiceBridge_and_delete_meeting

        old_meetings = [
            meeting
            for meeting in db.session.query(Meeting).filter(
                Meeting.last_connection_utc_datetime < datetime.now() - DATA_RETENTION,
            )
        ]
        logger.info(
            "Celery cron task: %d expired meetings to delete", len(old_meetings)
        )
        for meeting in old_meetings:
            save_voiceBridge_and_delete_meeting(meeting)
            logger.info(
                "Celery cron task: %s id:%s named:%s deleted",
                "shadow_meeting" if meeting.is_shadow else "meeting",
                meeting.id,
                meeting.name,
            )


@celery.task(name="background_upload")
def background_upload(endpoint, xml):
    """Celery task to upload XML documents to BigBlueButton API in background."""
    logger.info("BBB API request %s: xml:%s", endpoint, xml)

    session = requests.Session()
    if DEBUG:  # pragma: no cover
        # In local development environment, BBB is not served as https
        session.verify = False

    response = session.post(
        endpoint,
        headers={"Content-Type": "application/xml"},
        data=xml,
    )

    logger.info("BBB API response %s", response.text)
    return True
