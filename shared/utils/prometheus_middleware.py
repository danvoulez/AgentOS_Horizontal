
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response
import time

REQUEST_COUNT = Counter('http_requests_total','Total HTTP requests',['method','endpoint','http_status'])
REQUEST_LATENCY = Histogram('http_request_latency_seconds','Latency',['endpoint'])

class PrometheusMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        start = time.time()
        response = await call_next(request)
        elapsed = time.time()-start
        REQUEST_COUNT.labels(request.method, request.url.path, response.status_code).inc()
        REQUEST_LATENCY.labels(request.url.path).observe(elapsed)
        return response

def metrics_route():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
