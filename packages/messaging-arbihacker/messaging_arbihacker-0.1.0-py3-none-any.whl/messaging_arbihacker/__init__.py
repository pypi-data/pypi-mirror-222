from celery import Celery
from kombu import Queue, Exchange


class ArbiCelery(Celery):
    # Names are provided for consistent declaration of tasks in format "[queue].[task name]"
    USER_Q = "user"
    DATA_Q = "data"
    EVENT_Q = "event"
    TASK_Q = "task"
    NOTIFICATION_Q = "notification"
    # Convention for update queue is "update.[entity]"
    UPDATE_Q = "update"

    def __init__(
        self,
        main: str | None = None,
        broker: str | None = None,
        backend: str | None = None,
        **kwargs,
    ):
        super().__init__(main, broker=broker, backend=backend, **kwargs)
        # Create special update queue, other queues created automatically with default settings
        self.conf.task_queues = (
            Queue(
                exchange=Exchange(ArbiCelery.UPDATE_Q, type="topic"),
                routing_key=f"{ArbiCelery.UPDATE_Q}.*",
            ),
        )
        # Apply our custom routing function
        self.conf.task_routes = (ArbiCelery.route_task_by_name,)

    @staticmethod
    def route_task_by_name(name: str, args, kwargs, options, task=None, **kw):
        # custom routing function must follow strict signature
        try:
            queue, task = name.split(".", 1)  # we expect task names to be "[queue].[task name]"
        except ValueError:
            return {"queue": "celery"}  # default queue otherwise
        if queue == ArbiCelery.UPDATE_Q:  # update queue is special, it allows pub/sub with topic exchange
            return {
                "exchange": ArbiCelery.UPDATE_Q,
                "exchange_type": "topic",
                "routing_key": f"{ArbiCelery.UPDATE_Q}.{task}",
            }
        return {"queue": queue}  # simplified output format is allowed
