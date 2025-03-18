from flask import Flask, request
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
import time
import random
import requests

# Configure the tracer
resource = Resource(attributes={
    SERVICE_NAME: "flask-demo-app"
})

provider = TracerProvider(resource=resource)
otlp_exporter = OTLPSpanExporter(endpoint="otel-collector:4317", insecure=True)
span_processor = BatchSpanProcessor(otlp_exporter)
provider.add_span_processor(span_processor)
trace.set_tracer_provider(provider)

# Get a tracer
tracer = trace.get_tracer(__name__)

# Create Flask app
app = Flask(__name__)

# Instrument Flask
FlaskInstrumentor().instrument_app(app)

# Instrument requests library
RequestsInstrumentor().instrument()


@app.route('/')
def home():
    return "Welcome to the OpenTelemetry Demo! Try /process or /chain"


@app.route('/process')
def process():
    # Create a custom span
    with tracer.start_as_current_span("process-request") as span:
        # Add attributes to the span
        span.set_attribute("request.type", "process")

        # Simulate variable processing time
        process_time = random.uniform(0.1, 0.5)
        span.set_attribute("process.time_seconds", process_time)

        # Add an event
        span.add_event("Starting processing")

        # Simulate work
        time.sleep(process_time)

        # Sometimes introduce errors for demonstration
        if random.random() < 0.1:  # 10% chance of error
            span.set_status(trace.StatusCode.ERROR, "Simulated process failure")
            return "Process failed!", 500

        span.add_event("Finished processing")
        return f"Processing completed in {process_time:.2f} seconds!"


@app.route('/chain')
def chain():
    # This simulates a chain of microservices
    with tracer.start_as_current_span("chain-request") as span:
        span.set_attribute("request.type", "chain")

        # Simulate first step
        time.sleep(0.1)

        # Call our own API as if it were another service
        try:
            # Use the service name instead of localhost
            response = requests.get(f"http://flask-app:5000/process")
            return f"Chain complete! Process response: {response.text}"
        except Exception as e:
            span.set_status(trace.StatusCode.ERROR, str(e))
            return f"Chain failed: {str(e)}", 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 