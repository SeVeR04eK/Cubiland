# Celery Application
# This is a minimal stub to allow Celery worker and beat to start.
# Full implementation will be added when background tasks are developed.

from celery import Celery

# Celery app will be configured with environment variables
# For now, this is a placeholder that allows the worker to start
app = Celery("cubiland")
