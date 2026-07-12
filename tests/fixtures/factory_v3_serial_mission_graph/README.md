# Factory V3 Serial Mission-Graph Fixtures

Deterministic advisory fixtures for the research-only serial parent/child
mission-graph contract.

- `valid_serial_graph.json` models one completed feature, one eligible feature,
  and one pending dependent feature.
- `invalid/` covers cycles, concurrent active children, authority-ceiling
  breaches, premature continuation, and false parent completion.
- `expected/all.json` pins the complete advisory report.

These fixtures do not dispatch workers, create runtime authority, approve a new
profile, or prove a live epic mission.
