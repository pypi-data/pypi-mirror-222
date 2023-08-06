import os

from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.openai import OpenAIInstrumentor
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

TRACER_NAME = "traceloop.tracer"
TRACELOOP_API_ENDPOINT = "https://api.traceloop.io/v1/traces"


class Tracer:
    __instance = None

    @staticmethod
    def init():
        api_key = os.getenv("TRACELOOP_API_KEY")
        traceloop_api_endpoint = os.getenv("TRACELOOP_API_ENDPOINT") if os.getenv(
            "TRACELOOP_API_ENDPOINT") else TRACELOOP_API_ENDPOINT
        provider = TracerProvider()
        exporter = OTLPSpanExporter(
            endpoint=TRACELOOP_API_ENDPOINT,
            headers={
                "Authorization": f"Bearer {api_key}",
            }
        )
        processor = BatchSpanProcessor(exporter)
        provider.add_span_processor(processor)
        trace.set_tracer_provider(provider)
        Tracer.__instance = trace.get_tracer(TRACER_NAME)
        OpenAIInstrumentor().instrument()

    @staticmethod
    def instance():
        if Tracer.__instance is None:
            raise Exception("Tracer is not initialized")
        return Tracer.__instance
