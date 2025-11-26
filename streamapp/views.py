import time
from django.http import StreamingHttpResponse

LOG_FILE_PATH = "/app/logs/mylog.txt"


def stream_logs(request):
    def event_stream():
        with open(LOG_FILE_PATH, "r") as f:
            f.seek(0, 2)  # Move to end like tail -f
            while True:
                line = f.readline()
                if line:
                    yield f"data: {line}\n\n"
                time.sleep(0.5)

    return StreamingHttpResponse(
        event_stream(),
        content_type="text/event-stream",
    )
