# Factory V3 Serial Mission-State Fixtures

These fixtures pin a clean three-child lifecycle and its deterministic final
summary. Negative transition and malformed persistence cases are constructed
from the same graph in `tests/test_factory_v3_serial_mission_state.py` so each
test isolates one invariant without duplicating a large authored-state file.

The fixtures are advisory evidence only. They do not run implementation or
verification commands, dispatch workers, grant authority, or prove a live
fresh-worker or attended serial-epic mission.
