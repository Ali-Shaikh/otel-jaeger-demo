# OpenTelemetry and Jaeger Demo

A demonstration of distributed tracing with OpenTelemetry and Jaeger using a Python Flask application.

## Overview

This repository contains a simple setup to demonstrate distributed tracing using OpenTelemetry and Jaeger. The project uses a Flask application that simulates a microservice architecture, allowing you to visualise request flows and performance metrics.

### What's Included

- **Flask Application**: A simple web app with custom instrumentation
- **OpenTelemetry Collector**: Receives, processes, and exports telemetry data
- **Jaeger**: Visualises distributed traces

## Prerequisites

- Docker and Docker Compose
- A web browser to interact with the application and view traces

## Quick Start

1. Clone this repository:
   ```bash
   git clone https://github.com/Ali-Shaikh/otel-jaeger-demo.git
   cd otel-jaeger-demo
   ```

2. Build and start the services:
   ```bash
   docker-compose up --build
   ```

3. Access the demo:
   - Flask Application: http://localhost:5001
   - Jaeger UI: http://localhost:16687

4. Generate trace data by visiting:
   - http://localhost:5001/ - Homepage
   - http://localhost:5001/process - Simple processing endpoint
   - http://localhost:5001/chain - Simulated microservice chain

## Project Structure

```
otel-jaeger-demo/
├── app/
│   └── app.py          # Flask application with OpenTelemetry instrumentation
├── docker-compose.yml  # Docker Compose configuration
├── Dockerfile          # Flask application container configuration
├── requirements.txt    # Python dependencies
└── otel-collector-config.yaml  # OpenTelemetry Collector configuration
```

## Understanding the Demo

### What to Look For

1. **Trace View in Jaeger**:
   - Open http://localhost:16687
   - Select "flask-demo-app" from the Service dropdown
   - Click "Find Traces"
   - Explore the hierarchical view of spans

2. **The `/chain` Endpoint**:
   - This endpoint creates a chain of requests, showing how context propagation works
   - You'll see nested spans in the trace view

### Windows Users Note

If you're running Docker Desktop on Windows, ensure your drive is properly shared with Docker. See the detailed guide for more information.

## Detailed Documentation

For a comprehensive guide on this setup, see <a href="https://alishaikh.me/understanding-opentelemetry-a-comprehensive-beginners-guide/" target="_blank" rel="noopener noreferrer">Understanding OpenTelemetry: A Comprehensive Beginner's Guide</a>.

## Licence

This project is licensed under the MIT Licence - see the [LICENSE](LICENSE) file for details. 
