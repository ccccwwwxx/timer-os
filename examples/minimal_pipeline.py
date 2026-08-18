"""Illustrative wiring only; no private Timer OS logic is included."""


def process_event(event, brain, scheduler, body):
    brain.ingest(event)
    state = brain.snapshot()
    for decision in scheduler.decide(state):
        body.execute(decision)
