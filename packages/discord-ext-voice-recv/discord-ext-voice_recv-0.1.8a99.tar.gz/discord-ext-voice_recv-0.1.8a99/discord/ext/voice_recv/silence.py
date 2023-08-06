# -*- coding: utf-8 -*-

from __future__ import annotations

import logging
import threading

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Callable, Any

    from .rtp import RTPPacket, FakePacket

    Packet = RTPPacket | FakePacket
    SilenceGenFN = Callable[[], Any]

log = logging.getLogger(__name__)

__all__ = [
    'SilenceGenerator'
]


class SilenceGenerator:
    def __init__(self,
        callback: SilenceGenFN,
        *,
        grace_period: float=0.5,
        decay_rate: float=0.9
    ):
        self.callback = callback
        self.grace_period = grace_period
        self.decay_rate = decay_rate

        self._workers: dict[int, SilenceGenWorker] = {}

    def push_packet(self, packet: Packet):
        ...

    def stop(self):
        for worker in list(self._workers.values()):
            worker.stop()

        self._workers.clear()


class SilenceGenWorker(threading.Thread):
    DELAY = 0.02

    def __init__(self,
        callback: SilenceGenFN,
        *,
        grace_period: float=0.5,
        decay_rate: float=0.9
    ):
        super().__init__(daemon=True)

        self.callback = callback
        self.grace_period = grace_period
        self.decay_rate = decay_rate

        self._end = threading.Event()
        self._loops: int = 0

    def _do_run(self):
        while not self._end.is_set():
            ...

    def run(self):
        try:
            self._do_run()
        except Exception as e:
            raise e

    def stop(self):
        self._end.set()
