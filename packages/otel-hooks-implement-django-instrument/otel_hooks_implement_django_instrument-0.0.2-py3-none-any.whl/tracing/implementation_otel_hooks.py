import logging
from tracing.hooks import log_hook, name_callback, otel_request_hook, span_callback, otel_response_hook
from opentelemetry.instrumentation.django import DjangoInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.instrumentation.logging import LoggingInstrumentor
from tracing.tracers.jaeger import provider


def implement():
    DjangoInstrumentor().instrument(
        tracer_provider=provider,
        request_hook=otel_request_hook,
        response_hook=otel_response_hook
    )
    RequestsInstrumentor().instrument(
        tracer_provider=provider,
        name_callback=name_callback,
        span_callback=span_callback
    )
    LoggingInstrumentor().instrument(
        tracer_provider=provider,
        set_logging_format=True,
        log_level=logging.INFO,
        log_hook=log_hook
    )
