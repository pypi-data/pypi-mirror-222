"""
The custom written differable operator for reimage tasks, that differs the execution for 2 hours by default
"""
import asyncio
import time
from datetime import datetime, timedelta
from typing import Any, AsyncIterator, Dict, List, Tuple

from airflow.triggers.base import BaseTrigger, TriggerEvent
from airflow.utils import timezone


class ReImageTrigger(BaseTrigger):
    """ReImage Trigger with async run override"""

    def __init__(
        self,
        job_id: str,
        xcom_task_id: str,
        moment: datetime,
        hosts_info: Dict[str, Any],
        failed_hosts_info: List[Dict[str, Any]],
        attempt: int,
        *args,
        **kwargs,
    ):
        self.job_id = job_id
        self.xcom_task_id = xcom_task_id
        self.moment = moment
        self.hosts_info = hosts_info
        self.failed_hosts_info = failed_hosts_info
        self.attempt = attempt
        self.args = args
        self.kwargs = kwargs
        self.log.info(f"args: {args}")
        self.log.info(f"kwargs: {kwargs}")
        super().__init__(*args, **kwargs)

    def serialize(self) -> Dict[str, Any]:
        return (
            "herald.reimage.defer_operator.ReImageTrigger",
            {
                "job_id": self.job_id,
                "xcom_task_id": self.xcom_task_id,
                "moment": self.moment,
                "attempt": self.attempt,
                "hosts_info": self.hosts_info,
                "failed_hosts_info": self.failed_hosts_info,
            },
        )

    async def run(self) -> AsyncIterator[TriggerEvent]:
        """run method; this will get executed for async
        Reference code from DateTimeTrigger

        :return AsyncIterator[TriggerEvent]: yields the triggered event
        :yield Iterator[AsyncIterator[TriggerEvent]]: trigger event
        """
        # logging self variables
        self.log.info("Logging self variables")
        self.log.info(f"job_id: {self.job_id}")
        self.log.info(f"xcom_task_id: {self.xcom_task_id}")
        self.log.info(f"moment: {self.moment}")
        self.log.info(f"attempt: {self.attempt}")
        self.log.info(f"hosts_info: {self.hosts_info}")
        self.log.info(f"failed_hosts_info: {self.failed_hosts_info}")
        self.log.info("ReImageTrigger Started...")
        self.log.info("Incrementing the attempt value")
        self.attempt += 1
        # Sleep in successively small increments starting from 1 hour down to 10 seconds at a time
        for step in 3600, 60, 10:
            seconds_remaining = (self.moment - timezone.utcnow()).total_seconds()
            while seconds_remaining > 2 * step:
                self.log.info(f"{int(seconds_remaining)} seconds remaining; sleeping {step} seconds")
                await asyncio.sleep(delay=step)
                seconds_remaining = (self.moment - timezone.utcnow()).total_seconds()
        # Sleep a second at a time otherwise
        while self.moment > timezone.utcnow():
            self.log.info("sleeping 1 second...")
            await asyncio.sleep(delay=1)
        # Send event
        self.log.info(f"current attempt value in trigger: {self.attempt}")
        event = {
            "job_id": self.job_id,
            "xcom_task_id": self.xcom_task_id,
            "moment": self.moment,
            "attempt": self.attempt,
            "hosts_info": self.hosts_info,
            "failed_hosts_info": self.failed_hosts_info,
        }
        self.log.info(f"Sending event: {event}")
        self.log.info("ReImageTrigger Ended...")
        yield TriggerEvent(event)
