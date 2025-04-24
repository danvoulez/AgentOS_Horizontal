
import logging, uuid, sys
FORMAT='[%(asctime)s] %(levelname)s %(trace_id)s %(name)s: %(message)s'
class TraceAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        kwargs.setdefault('extra', {})['trace_id'] = kwargs['extra'].get('trace_id', uuid.uuid4().hex)
        return msg, kwargs

def get_logger(name:str="agentos"):
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(logging.Formatter(FORMAT))
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return TraceAdapter(logger,{})
