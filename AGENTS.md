This repo is a multi-agent SUV search. Read PROTOCOL.md and PARETO_GUIDE.md before doing anything.
Your role and handoff stage are defined there — CLI agents build tooling in tools/ and file search matches as candidates.
One file per candidate in candidates/; advance only your own workflow stage via the status field.
Append dated log entries; never rewrite another agent's log entries.
