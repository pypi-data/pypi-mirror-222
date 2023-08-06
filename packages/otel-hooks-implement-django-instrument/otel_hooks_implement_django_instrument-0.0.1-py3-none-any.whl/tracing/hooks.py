import json


def otel_request_hook(span, request):
    if span and span.is_recording() and hasattr(request, "body"):
        span.add_event(
            "log",
            {
                "request_body": request.body.decode("utf-8")
            }
        )


def otel_response_hook(span, request, response):
    if span and span.is_recording() and hasattr(response, "data"):
        response_data = ""
        try:
            response_data = json.dumps(response.data)
        except Exception:
            response_data = json.dumps(str(response.data))
        finally:
            span.add_event(
                "log",
                {
                    "response_data": response_data
                }
            )


def log_hook(span, record):
    if span and span.is_recording():
        span.add_event(
            "log",
            {
                record.levelname: json.dumps(record.msg),
                "file": record.pathname,
                "line": record.lineno
            }
        )


def span_callback(span, response):
    if span and span.is_recording():
        payload = {
            "ERROR": "No response from server"
        }
        if response:
            response_headers = json.dumps(dict(response.headers))
            if 200 <= response.status_code < 300:
                payload = {
                    "INFO": json.dumps({
                        "responseHeaders": response_headers,
                        "responseBody": response.text
                    })
                }
            else:
                payload["ERROR"] = json.dumps({
                    "responseHeaders": response_headers,
                    "reason": response.reason,
                    "responseBody": response.text if hasattr(response, "text") else ""
                })
        span.add_event(
            "log",
            payload
        )


def name_callback(method, url):
    return f"{method} {url}"
