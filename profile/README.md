# CortexRidge

Your operations run themselves.

CortexRidge builds software for the people who keep data systems running — developers, DBAs, SREs, and AI engineers. Fifteen years of database platform engineering, turned into tools that do the work instead of describing it.

---

## What we build

**CortexBolt** — the autonomous operations platform for your data stack. It watches your databases, decides with AI, and runs the work across databases, APIs, and services. You approve what matters. Live, and free to start.

**CortexMaps** — a self-hostable live-tracking layer. Keep the map your users already see, and move the parts that cost the most — accurate positioning, arrival times, live location — onto infrastructure you own. Measured at a 140× lower bill across six months of production traffic.

---

## Writing

We publish working notes from the operational layer: PostgreSQL, ClickHouse, MySQL, MongoDB, and what it takes to run them at production scale.

<!-- BLOG:START -->
- [Workflows in Practice: Disk Space Monitoring](https://cortexridge.com/blog/workflows-in-practice-disk-space-monitoring/) — One webhook call checks a server's disk, records the reading, alerts the customer, and archives the run. A five-node CortexBolt workflow, step by step.
- [The Economy Of Embeddings](https://cortexridge.com/blog/pgvector-cost-economy-of-embeddings/) — An embedding has four costs, and one dwarfs the rest: RAM. Follow a single vector through its life and see where the database bill really comes from.
- [PostgreSQL LISTEN/NOTIFY Is Not Durable — Here's the Fix with pg_durable](https://cortexridge.com/blog/postgresql-listen-notify-not-durable-pg-durable/) — PostgreSQL LISTEN/NOTIFY loses messages when nobody is listening. See how pg_durable adds durable signals and workflows that survive restarts.
- [Fifteen years of databases, end to end](https://cortexridge.com/blog/welcome-to-cortexridge/) — Fifteen years of database platforms at AWS, Oracle, Tessell, OpenSCG, and EnterpriseDB — and how they became CortexBolt, the autonomous operations platform.
<!-- BLOG:END -->

All articles at **[cortexridge.com/blog](https://cortexridge.com/blog/)**.

---

## Who is behind this

**Dinesh Kumar** — founder. Fifteen years building and operating database platforms at AWS, Oracle's OCI PostgreSQL group, Tessell, OpenSCG, and EnterpriseDB, leading the engineering teams behind PostgreSQL platforms serving more than 20 million requests a day.

Author of two PostgreSQL books: a PL/pgSQL developer guide and a high-performance cookbook, both written for working DBAs and migration engineers. Open-source patches and community talks alongside.

The operational problems that wake teams at 3 AM — autovacuum falling behind, replication lag, query plans that flip in production, the slow erosion of a once-fast schema — are the problems CortexBolt is built on.

---

## Contact

- Website — [cortexridge.com](https://cortexridge.com)
- Blog — [cortexridge.com/blog](https://cortexridge.com/blog/)
- LinkedIn — [linkedin.com/company/cortexridge](https://www.linkedin.com/company/cortexridge)
- Email — dinesh.kumar@cortexridge.com
