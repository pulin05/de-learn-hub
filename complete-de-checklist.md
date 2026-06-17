# Data Engineering Master Checklist — v2

A comprehensive, exhaustive to-do list covering every major umbrella and sub-topic expected across data engineering roles: analytics engineering, platform engineering, cloud, big data, streaming, ML platforms, and domain-specific tracks. Use checkboxes to track learning progress. Sections 1–5 = beginner readiness. Sections 6–15 = production-grade readiness. Sections 16–25 = advanced and specialisation readiness.

---

## 1. Programming Foundations

### Python Core
- [ ] Learn variables, data types, and type coercion.
- [ ] Learn control flow: if/elif/else, for, while.
- [ ] Learn functions, default arguments, *args, and **kwargs.
- [ ] Learn list comprehensions and generator expressions.
- [ ] Learn lambda functions and functional tools (map, filter, reduce).
- [ ] Learn error handling: try/except/finally, custom exceptions.
- [ ] Learn file I/O: reading and writing CSV, JSON, and plain text.
- [ ] Learn context managers and the `with` statement.
- [ ] Learn Python modules and packages.
- [ ] Learn virtual environments (venv, conda).
- [ ] Learn pip, pyproject.toml, and dependency management.

### Object-Oriented Python
- [ ] Learn classes, instances, `__init__`, and `self`.
- [ ] Learn inheritance, method overriding, and super().
- [ ] Learn dunder methods: `__str__`, `__repr__`, `__len__`, `__iter__`.
- [ ] Learn dataclasses and named tuples.
- [ ] Learn abstract base classes and interfaces.
- [ ] Learn composition vs inheritance.

### Python for Data Engineering
- [ ] Learn requests library for REST API calls.
- [ ] Learn pagination and rate-limit handling in Python.
- [ ] Learn environment variables and secrets via os.environ and dotenv.
- [ ] Learn logging module: levels, handlers, formatters.
- [ ] Learn scheduling with APScheduler or cron integration.
- [ ] Learn multiprocessing and threading basics.
- [ ] Learn asyncio and async/await for concurrent I/O.
- [ ] Learn type hints and mypy for static analysis.
- [ ] Learn pytest: fixtures, parametrize, mocking.
- [ ] Learn profiling with cProfile and line_profiler.
- [ ] Learn Pydantic for data validation and schema enforcement.
- [ ] Learn Polars for fast in-memory data processing.
- [ ] Learn Pandas: DataFrames, groupby, merge, pivot, melt.
- [ ] Learn Pandas performance: chunking, dtypes, vectorisation.

### Other Languages (Awareness Level)
- [ ] Learn Scala basics (used in Spark and Flink ecosystems).
- [ ] Learn SQL-on-everything: when Python vs SQL is the right tool.
- [ ] Learn bash scripting for glue scripts and cron jobs.
- [ ] Learn YAML and TOML for config files.
- [ ] Learn Jinja2 templating (used heavily in dbt and Airflow).

### Software Engineering Practices
- [ ] Learn Git: clone, branch, commit, merge, rebase, cherry-pick.
- [ ] Learn Git workflows: trunk-based development, feature branches.
- [ ] Learn GitHub/GitLab: PRs, code reviews, branch protection.
- [ ] Learn semantic versioning.
- [ ] Learn pre-commit hooks and linters (black, ruff, flake8).
- [ ] Learn Linux and terminal: file system, permissions, pipes, grep, awk, sed.
- [ ] Learn Makefile basics for pipeline task automation.
- [ ] Learn clean code principles: single responsibility, DRY, KISS.
- [ ] Learn modular design and separation of concerns.
- [ ] Learn documentation: docstrings, README, architecture docs.
- [ ] Learn debugging: pdb, VS Code debugger, print-driven debugging.
- [ ] Learn data structures: lists, dicts, sets, queues, heaps.
- [ ] Learn algorithm complexity: Big O for loops, joins, sorts.
- [ ] Learn when algorithmic choice matters in pipeline code.

---

## 2. SQL Mastery

### Fundamentals
- [x] Learn SELECT, FROM, WHERE, ORDER BY, LIMIT.
- [x] Learn GROUP BY, HAVING, and aggregate functions (COUNT, SUM, AVG, MIN, MAX).
- [x] Learn DISTINCT and deduplication with SQL.
- [x] Learn CASE WHEN statements and conditional logic.
- [ ] Learn NULL handling: IS NULL, COALESCE, NULLIF, IFNULL.
- [ ] Learn string functions: CONCAT, TRIM, LOWER, UPPER, SUBSTRING, REPLACE.
- [ ] Learn date and time functions: DATE_TRUNC, EXTRACT, DATE_DIFF, TIMESTAMP.
- [ ] Learn type casting and CAST / CONVERT.

### Joins
- [x] Learn INNER JOIN.
- [x] Learn LEFT JOIN and RIGHT JOIN.
- [x] Learn FULL OUTER JOIN.
- [ ] Learn CROSS JOIN.
- [ ] Learn SELF JOIN.
- [ ] Learn anti-joins using NOT IN, NOT EXISTS, LEFT JOIN + IS NULL.
- [ ] Learn join performance and index usage.
- [ ] Learn fanout problems and row multiplication in joins.

### Advanced Querying
- [ ] Learn subqueries: scalar, correlated, and in FROM clause.
- [ ] Learn common table expressions (CTEs) and recursive CTEs.
- [ ] Learn window functions: ROW_NUMBER, RANK, DENSE_RANK, NTILE.
- [ ] Learn window functions: LAG, LEAD, FIRST_VALUE, LAST_VALUE.
- [ ] Learn window functions: running totals with SUM() OVER, AVG() OVER.
- [ ] Learn frame specification: ROWS BETWEEN, RANGE BETWEEN.
- [ ] Learn UNION, UNION ALL, INTERSECT, EXCEPT.
- [ ] Learn PIVOT and UNPIVOT (or equivalent with CASE WHEN).
- [ ] Learn lateral joins (CROSS JOIN LATERAL / LATERAL VIEW).
- [ ] Learn EXISTS and NOT EXISTS patterns.
- [ ] Learn ARRAY and STRUCT handling in BigQuery / Snowflake.
- [ ] Learn JSON functions: JSON_EXTRACT, JSON_PARSE, PARSE_JSON.
- [ ] Learn UNNEST and FLATTEN for nested and repeated fields.
- [ ] Learn QUALIFY clause (window filter, used in Snowflake, BigQuery).

### Schema and DDL
- [ ] Learn CREATE TABLE, ALTER TABLE, DROP TABLE.
- [ ] Learn primary keys, foreign keys, unique and check constraints.
- [ ] Learn CREATE VIEW and CREATE MATERIALIZED VIEW.
- [ ] Learn CREATE INDEX and DROP INDEX.
- [ ] Learn table partitioning via DDL.
- [ ] Learn CREATE SCHEMA and database-level organisation.
- [ ] Learn stored procedures and user-defined functions (UDFs).
- [ ] Learn temporary tables and session-scoped objects.

### Query Optimisation
- [ ] Learn EXPLAIN / EXPLAIN ANALYZE and reading query plans.
- [ ] Learn index types: B-tree, hash, composite, covering indexes.
- [ ] Learn when indexes help vs when they hurt (write overhead).
- [ ] Learn predicate pushdown and filter early patterns.
- [ ] Learn avoiding SELECT * in production queries.
- [ ] Learn query cost estimation in BigQuery / Snowflake.
- [ ] Learn partition pruning and clustering in warehouses.
- [ ] Learn statistics and ANALYZE / VACUUM in Postgres.
- [ ] Learn materialising expensive CTEs vs scanning them repeatedly.

### Transactions and Concurrency
- [ ] Learn ACID properties: Atomicity, Consistency, Isolation, Durability.
- [ ] Learn BEGIN, COMMIT, ROLLBACK.
- [ ] Learn isolation levels: READ COMMITTED, REPEATABLE READ, SERIALIZABLE.
- [ ] Learn optimistic vs pessimistic locking.
- [ ] Learn MERGE / UPSERT statements.
- [ ] Learn deadlocks and how to avoid them.

### Warehouse-Specific SQL
- [ ] Learn BigQuery: partitioned and clustered tables, BQML, INFORMATION_SCHEMA.
- [ ] Learn Snowflake: time travel, cloning, streams, tasks, VARIANT type.
- [ ] Learn Redshift: distribution keys, sort keys, VACUUM, ANALYZE.
- [ ] Learn DuckDB: local analytical SQL, read_parquet(), read_csv_auto().
- [ ] Learn Trino / Presto: federated queries across data sources.
- [ ] Learn TimescaleDB: hypertables, continuous aggregates, time_bucket().

---

## 3. Database Fundamentals

### Relational Databases
- [ ] Learn relational model: tables, rows, columns, domains.
- [ ] Learn normalisation: 1NF, 2NF, 3NF, BCNF.
- [ ] Learn denormalisation: when and why to break normal forms.
- [ ] Learn ER diagrams: entities, relationships, cardinality.
- [ ] Learn primary keys, surrogate keys, and natural keys.
- [ ] Learn foreign keys and referential integrity.
- [ ] Learn check constraints and not-null constraints.
- [ ] Learn unique constraints and composite keys.
- [ ] Learn indexes: clustered, non-clustered, partial, expression-based.
- [ ] Learn table partitioning: range, list, hash partitioning.
- [ ] Learn OLTP vs OLAP: workload shapes, schema differences.
- [ ] Learn connection pooling (PgBouncer, RDS Proxy).
- [ ] Learn read replicas and high availability basics.
- [ ] Learn backup strategies: full, incremental, WAL archiving.
- [ ] Learn point-in-time recovery (PITR).

### NoSQL Databases
- [ ] Learn document databases: MongoDB, Firestore — schema flexibility, queries.
- [ ] Learn key-value stores: Redis — caching, TTL, pub/sub.
- [ ] Learn wide-column stores: Cassandra — partition keys, clustering keys.
- [ ] Learn graph databases: Neo4j — nodes, edges, Cypher query language.
- [ ] Learn time-series databases: InfluxDB, QuestDB, TimescaleDB.
- [ ] Learn search engines: Elasticsearch — inverted index, full-text search.
- [ ] Learn when NoSQL is the right choice and when it isn't.
- [ ] Learn eventual consistency vs strong consistency trade-offs.
- [ ] Learn CAP theorem: Consistency, Availability, Partition tolerance.
- [ ] Learn BASE model vs ACID model.

### Postgres Deep Dive
- [ ] Learn Postgres architecture: processes, shared buffers, WAL.
- [ ] Learn EXPLAIN ANALYZE and pg_stat_statements.
- [ ] Learn logical replication and WAL-based CDC.
- [ ] Learn Postgres extensions: PostGIS, TimescaleDB, pg_partman.
- [ ] Learn JSONB column type and GIN indexes.
- [ ] Learn table inheritance and partitioned tables.
- [ ] Learn sequences and identity columns.
- [ ] Learn table bloat, VACUUM, and autovacuum tuning.

---

## 4. Data Modeling

### Fundamentals
- [ ] Learn conceptual modeling: entities and high-level relationships.
- [ ] Learn logical modeling: tables, columns, keys — database-agnostic.
- [ ] Learn physical modeling: storage, indexes, partitions — database-specific.
- [ ] Learn the difference between OLTP and OLAP data models.

### Dimensional Modeling (Kimball)
- [ ] Learn star schema: fact table at centre, dimension tables around it.
- [ ] Learn snowflake schema: normalised dimensions branching from dimensions.
- [ ] Learn fact tables: transactional, periodic snapshot, accumulating snapshot.
- [ ] Learn grain: defining what one row in a fact table represents.
- [ ] Learn additive, semi-additive, and non-additive measures.
- [ ] Learn dimension tables: flat, wide, descriptive attributes.
- [ ] Learn slowly changing dimensions (SCD):
  - [ ] SCD Type 0: retain original.
  - [ ] SCD Type 1: overwrite with new value.
  - [ ] SCD Type 2: add new row with effective/expiry dates.
  - [ ] SCD Type 3: add new column for previous value.
  - [ ] SCD Type 4: use a separate history table.
- [ ] Learn degenerate dimensions: dimension keys stored in fact table.
- [ ] Learn junk dimensions: grouping low-cardinality flags.
- [ ] Learn role-playing dimensions: same dimension used in multiple roles.
- [ ] Learn conformed dimensions and enterprise-wide reusability.
- [ ] Learn bridge tables for many-to-many relationships.
- [ ] Learn date and time dimension design.
- [ ] Learn data marts: subject-specific subsets of the warehouse.

### Inmon and Hybrid Approaches
- [ ] Learn Inmon's enterprise data warehouse (EDW) 3NF approach.
- [ ] Learn hub-and-spoke architecture.
- [ ] Learn Data Vault 2.0: hubs, links, satellites.
- [ ] Learn Data Vault: hash keys, load dates, record sources.
- [ ] Learn when to use Kimball vs Inmon vs Data Vault.

### Modern Analytical Modeling
- [ ] Learn wide table / one big table (OBT) pattern.
- [ ] Learn activity schema pattern.
- [ ] Learn dbt project structure as a modeling discipline.
- [ ] Learn semantic layer: MetricFlow, Looker LookML, Cube.
- [ ] Learn metric definitions and governance.
- [ ] Learn customer 360 / entity-centric modeling.
- [ ] Learn event-based modeling for product analytics.
- [ ] Learn graph modeling for relationship data.
- [ ] Learn time-series modeling patterns for financial and IoT data.

---

## 5. ETL and ELT

### Core Concepts
- [ ] Learn ETL: Extract → Transform → Load (transform before loading).
- [ ] Learn ELT: Extract → Load → Transform (transform inside warehouse).
- [ ] Learn why ELT won: warehouse compute is cheap, transformation in SQL is auditable.
- [ ] Learn reverse ETL: warehouse → operational SaaS tools.
- [ ] Learn data pipeline vs data workflow vs data product.

### Extraction Patterns
- [ ] Learn full extraction: read entire source table every run.
- [ ] Learn incremental extraction: watermark on updated_at column.
- [ ] Learn CDC-based extraction: capture every insert/update/delete.
- [ ] Learn API pagination patterns: offset, cursor, link-header.
- [ ] Learn rate limit handling and exponential backoff.
- [ ] Learn parallel extraction across partitions.
- [ ] Learn extraction from flat files: CSV, JSON, Parquet, Avro, XML.
- [ ] Learn web scraping basics and ethical considerations.

### Transformation Patterns
- [ ] Learn cleansing: null handling, whitespace trimming, type casting.
- [ ] Learn deduplication: using ROW_NUMBER() OVER PARTITION BY.
- [ ] Learn standardisation: codes → readable labels, currency normalisation.
- [ ] Learn enrichment: joining lookup tables to add context.
- [ ] Learn aggregation: GROUP BY, window functions for pre-aggregated tables.
- [ ] Learn flattening: nested JSON → relational columns.
- [ ] Learn pivoting and unpivoting.
- [ ] Learn data masking in transformation layer.
- [ ] Learn fuzzy matching and entity resolution.
- [ ] Learn slowly changing dimension handling in transformation.

### Loading Patterns
- [ ] Learn truncate and reload (full refresh).
- [ ] Learn append-only loading for event data.
- [ ] Learn upsert / MERGE loading for transactional data.
- [ ] Learn delete-then-insert pattern.
- [ ] Learn atomic swap using temp tables.
- [ ] Learn partition overwrite for large incremental loads.
- [ ] Learn bulk loading tools: COPY command, bq load, Snowflake COPY INTO.

### Pipeline Reliability
- [ ] Learn idempotency: running the same pipeline twice produces the same result.
- [ ] Learn atomicity in pipelines: all-or-nothing loads.
- [ ] Learn retry logic with exponential backoff and dead letter queues.
- [ ] Learn checkpointing: saving progress to restart mid-pipeline.
- [ ] Learn backfilling: reprocessing historical data after fixing bugs.
- [ ] Learn soft deletes and tombstone records.
- [ ] Learn late-arriving data handling.
- [ ] Learn schema evolution: adding, renaming, removing columns safely.
- [ ] Learn forward and backward compatibility in schemas.
- [ ] Learn data lineage tracking through pipeline steps.

### Tools
- [ ] Learn dbt: models, materializations, ref(), source(), tests, docs.
- [ ] Learn dbt incremental models and unique_key.
- [ ] Learn dbt snapshots for SCD Type 2.
- [ ] Learn dbt packages: dbt_utils, dbt_expectations, audit_helper.
- [ ] Learn dbt Cloud vs dbt Core.
- [ ] Learn Airbyte: connectors, sync modes, schema normalization.
- [ ] Learn Fivetran: managed connectors, transformations, HubSpot, Stripe, Salesforce.
- [ ] Learn Apache Hop or Talend at a conceptual level.
- [ ] Learn Singer / Meltano: taps and targets spec.
- [ ] Learn custom Python pipeline scripts with requests + SQLAlchemy.

### Data Integration Patterns
- [ ] Learn batch vs micro-batch vs streaming trade-offs and when to choose each.
- [ ] Learn push vs pull ingestion: which side initiates the data transfer.
- [ ] Learn webhook-based ingestion: receiving real-time push events from SaaS tools.
- [ ] Learn polling-based ingestion: scheduled pulls vs event-driven triggers.
- [ ] Learn log-based CDC vs trigger-based CDC vs timestamp-based CDC — trade-offs.
- [ ] Learn log-based CDC tools: Debezium, Maxwell, AWS DMS, Striim.
- [ ] Learn trigger-based CDC: database triggers writing to change tables — pitfalls.
- [ ] Learn third-party data ingestion challenges: API versioning, auth changes, schema drift.
- [ ] Learn schema drift handling strategies: detect-and-alert, auto-evolve, reject-and-quarantine.
- [ ] Learn data integration testing: verifying source = destination row counts and checksums.
- [ ] Learn idempotent ingestion design: safe to re-run without duplicating data.
- [ ] Learn fan-out ingestion: one source → multiple destinations simultaneously.
- [ ] Learn reverse ETL concepts: syncing computed warehouse data back to Salesforce, HubSpot, etc.
- [ ] Learn reverse ETL tools: Hightouch, Census — use cases and limitations.
- [ ] Learn operational analytics: triggering business actions from warehouse metrics.

---

## 6. Orchestration

### Core Concepts
- [ ] Learn what orchestration is: coordinating pipeline steps with dependencies.
- [ ] Learn DAG (Directed Acyclic Graph): nodes = tasks, edges = dependencies.
- [ ] Learn scheduling: cron expressions, interval-based, event-triggered.
- [ ] Learn dependency management: task B waits for task A to succeed.
- [ ] Learn retry policies: retry count, retry delay, exponential backoff.
- [ ] Learn failure handling: fail fast vs skip vs alert.
- [ ] Learn SLA monitoring: alert if pipeline doesn't finish within X minutes.
- [ ] Learn parameterisation: running same DAG with different dates or configs.
- [ ] Learn backfill orchestration: triggering historical runs.
- [ ] Learn idempotent task design in orchestrators.
- [ ] Learn sensors: tasks that wait for an external condition (file, API, table).

### Apache Airflow
- [ ] Learn Airflow architecture: scheduler, webserver, workers, metadata DB.
- [ ] Learn Airflow DAG file structure and Python API.
- [ ] Learn operators: PythonOperator, BashOperator, BranchPythonOperator.
- [ ] Learn provider operators: BigQueryOperator, S3ToRedshiftOperator.
- [ ] Learn sensors: FileSensor, ExternalTaskSensor, HttpSensor.
- [ ] Learn XComs: passing data between tasks.
- [ ] Learn Airflow Variables and Connections.
- [ ] Learn TaskFlow API (Airflow 2.x): @task decorator.
- [ ] Learn dynamic task mapping (Airflow 2.3+).
- [ ] Learn Airflow pools and task concurrency limits.
- [ ] Learn Airflow executor types: LocalExecutor, CeleryExecutor, KubernetesExecutor.
- [ ] Learn Airflow deployment: Helm chart on Kubernetes, MWAA, Cloud Composer.
- [ ] Learn Airflow DAG testing and unit tests.

### Alternative Orchestrators
- [ ] Learn Prefect: flows, tasks, deployments, work pools.
- [ ] Learn Prefect: local vs cloud runner, state machine model.
- [ ] Learn Dagster: assets, jobs, schedules, sensors, resources.
- [ ] Learn Dagster: asset-based lineage and software-defined assets.
- [ ] Learn Argo Workflows: Kubernetes-native DAG orchestration.
- [ ] Learn Argo: workflow templates, steps vs DAG, artifact passing.
- [ ] Learn Temporal: durable execution for long-running workflows.
- [ ] Learn Mage: notebook-friendly pipeline tool.
- [ ] Learn cron + systemd for simple single-machine scheduling.
- [ ] Learn Cloud Scheduler (GCP) and EventBridge (AWS) for managed cron.

---

## 7. Data Quality and Testing

### Validation Rules
- [ ] Learn not-null checks on required columns.
- [ ] Learn uniqueness checks on primary key columns.
- [ ] Learn referential integrity checks between tables.
- [ ] Learn accepted-values checks on categorical columns.
- [ ] Learn range checks on numeric columns (min, max, no negative values).
- [ ] Learn regex pattern checks on string columns (emails, phone numbers).
- [ ] Learn cross-column consistency checks (end_date > start_date).
- [ ] Learn row count checks: minimum expected rows per run.
- [ ] Learn freshness checks: table updated within expected window.
- [ ] Learn reconciliation checks: source row count = target row count.
- [ ] Learn aggregate reconciliation: SUM(revenue) matches across systems.
- [ ] Learn duplicate rate monitoring over time.
- [ ] Learn null rate monitoring: alert if null rate increases beyond threshold.

### Testing Frameworks
- [ ] Learn dbt tests: built-in unique, not_null, accepted_values, relationships.
- [ ] Learn dbt-expectations: extended test suite inspired by Great Expectations.
- [ ] Learn Great Expectations: expectations, suites, checkpoints, data docs.
- [ ] Learn Soda Core: YAML-defined checks, CLI-based validation.
- [ ] Learn Monte Carlo / Bigeye: ML-based anomaly detection for pipelines.
- [ ] Learn pytest for unit testing Python transformation logic.
- [ ] Learn writing custom dbt singular tests as SQL queries.

### Data Contracts
- [ ] Learn what a data contract is: schema + quality + SLA agreement between producer and consumer.
- [ ] Learn schema contracts: enforcing column names, types, nullability.
- [ ] Learn semantic contracts: meaning of values, allowed ranges.
- [ ] Learn operational contracts: freshness, row counts, delivery SLAs.
- [ ] Learn tools: Soda, Atlan, DataHub for contract enforcement.
- [ ] Learn how to implement contracts in a dbt project.

### Anomaly Detection
- [ ] Learn statistical anomaly detection: Z-score, IQR-based flagging.
- [ ] Learn volume anomaly detection: unexpected drops or spikes in row count.
- [ ] Learn distribution shift detection: monitoring column distributions over time.
- [ ] Learn ML-based anomaly detection for pipelines (Monte Carlo, Acceldata).
- [ ] Learn probabilistic data quality checks: sampling-based validation for large tables.
- [ ] Learn drift detection: detecting when data distributions shift over time.
- [ ] Learn data observability platforms: Monte Carlo, Acceldata, Bigeye — full platform vs point tools.
- [ ] Learn SLA vs SLI vs SLO specifically for data: freshness SLA, completeness SLO, quality SLI.
- [ ] Learn freshness SLAs: alerting when a table has not been updated within its contracted window.

### Pipeline Testing Best Practices
- [ ] Learn test-driven pipeline development: write tests before models.
- [ ] Learn staging environment testing vs production.
- [ ] Learn CI-based dbt test runs on pull requests.
- [ ] Learn blue-green deployment for warehouse tables.
- [ ] Learn data diff tools: comparing model outputs before and after changes.

---

## 8. Data Warehousing

### Architecture
- [ ] Learn data warehouse architecture: staging → integration → presentation layers.
- [ ] Learn Kimball bus matrix: which dimensions cross which fact tables.
- [ ] Learn hub-and-spoke warehouse architecture (Inmon).
- [ ] Learn semantic layer placement in the warehouse stack.
- [ ] Learn warehouse separation of compute and storage.
- [ ] Learn virtual warehouses / compute clusters and auto-scaling.
- [ ] Learn query routing and workload management.

### BigQuery
- [ ] Learn BigQuery architecture: Dremel engine, Colossus storage, Jupiter network.
- [ ] Learn BigQuery slot-based pricing vs on-demand pricing.
- [ ] Learn partitioned tables: date/timestamp partitioning, integer range partitioning.
- [ ] Learn clustered tables and how clustering improves query performance.
- [ ] Learn BigQuery storage: native tables vs external tables vs federated queries.
- [ ] Learn BigQuery INFORMATION_SCHEMA for metadata queries.
- [ ] Learn BigQuery ML (BQML): training models with SQL.
- [ ] Learn BigQuery scheduled queries and data transfers.
- [ ] Learn BigQuery reservations, commitments, and slot management.
- [ ] Learn BigQuery Omni for multi-cloud queries.
- [ ] Learn BigQuery row-level and column-level access controls.

### Snowflake
- [ ] Learn Snowflake architecture: virtual warehouses, cloud services, storage.
- [ ] Learn Snowflake time travel: querying historical data with AT / BEFORE.
- [ ] Learn Snowflake zero-copy cloning for dev/test environments.
- [ ] Learn Snowflake streams: tracking DML changes on tables.
- [ ] Learn Snowflake tasks: scheduling SQL statements.
- [ ] Learn Snowflake VARIANT type and semi-structured data.
- [ ] Learn Snowflake data sharing: secure share between accounts.
- [ ] Learn Snowflake dynamic tables: declarative materialisation.
- [ ] Learn Snowflake Cortex: native ML and LLM functions.
- [ ] Learn Snowflake cost management: credit usage, warehouse sizing.

### Redshift
- [ ] Learn Redshift architecture: leader node, compute nodes, columnar storage.
- [ ] Learn distribution keys: ALL, EVEN, KEY — trade-offs.
- [ ] Learn sort keys: compound vs interleaved.
- [ ] Learn VACUUM and ANALYZE commands and when to run them.
- [ ] Learn Redshift Spectrum: querying S3 data from Redshift.
- [ ] Learn Redshift Serverless vs provisioned clusters.

### Other Warehouses
- [ ] Learn DuckDB: in-process OLAP, local Parquet querying, dbt-duckdb adapter.
- [ ] Learn ClickHouse: columnar OLAP, MergeTree engine, replication.
- [ ] Learn Apache Druid: real-time OLAP on streaming data.
- [ ] Learn Databricks SQL Warehouse: Lakehouse query engine.
- [ ] Learn Trino / Presto: federated SQL across multiple data sources.

### Performance and Cost Optimisation
- [ ] Learn partition pruning and predicate pushdown.
- [ ] Learn clustering / sort keys for scan reduction.
- [ ] Learn materialised views for expensive repeated aggregations.
- [ ] Learn result caching in Snowflake and BigQuery.
- [ ] Learn approximate aggregation: HyperLogLog for COUNT DISTINCT.
- [ ] Learn query slot management and concurrency scaling.
- [ ] Learn cost attribution per team / project.
- [ ] Learn storage cost vs compute cost trade-offs.

---

## 9. Data Lakes and Lakehouse

### Data Lake Fundamentals
- [ ] Learn data lake concept: store raw data in native format at low cost.
- [ ] Learn object storage: S3, GCS, Azure Blob — key-value at infinite scale.
- [ ] Learn bucket and prefix/path naming conventions.
- [ ] Learn schema-on-read vs schema-on-write.
- [ ] Learn raw / bronze / silver / gold (medallion) architecture.
- [ ] Learn data swamp anti-pattern: unmanaged lake with no governance.
- [ ] Learn metadata management for a data lake.

### File Formats
- [ ] Learn CSV: row-oriented, human-readable, no schema, poor analytics performance.
- [ ] Learn JSON / JSONL: semi-structured, nested, API-native.
- [ ] Learn Avro: row-oriented binary with embedded schema, ideal for Kafka.
- [ ] Learn Parquet: columnar binary, compressed, best for analytical queries.
- [ ] Learn ORC: columnar binary, Hive ecosystem.
- [ ] Learn column pruning and predicate pushdown with Parquet.
- [ ] Learn compression codecs: Snappy, GZIP, ZSTD — trade-offs.
- [ ] Learn file size optimisation: small file problem and compaction.
- [ ] Learn Parquet partitioning by column values.

### Open Table Formats
- [ ] Learn Delta Lake: ACID transactions on Parquet, transaction log.
- [ ] Learn Delta Lake: time travel, MERGE INTO, schema evolution.
- [ ] Learn Apache Iceberg: hidden partitioning, snapshot isolation.
- [ ] Learn Iceberg: schema evolution without rewrite, partition evolution.
- [ ] Learn Apache Hudi: upserts on data lake, copy-on-write vs merge-on-read.
- [ ] Learn when to use Delta vs Iceberg vs Hudi.
- [ ] Learn table format integration with Spark, Trino, Flink, BigQuery.
- [ ] Learn Z-ordering and data skipping for file-level query optimisation.

### Lakehouse Architecture
- [ ] Learn lakehouse: data lake storage + data warehouse query performance.
- [ ] Learn Databricks Lakehouse Platform.
- [ ] Learn Unity Catalog: Databricks governance and fine-grained access.
- [ ] Learn Apache Hive Metastore and Glue Data Catalog.
- [ ] Learn AWS Glue Catalog: schema registry for S3-based tables.
- [ ] Learn querying lake tables: Athena (AWS), BigQuery external, Trino.
- [ ] Learn table compaction and optimisation jobs.
- [ ] Learn vacuum / expire snapshots to manage storage cost.
- [ ] Learn multi-table transactions across lakehouse tables.

---

## 10. Big Data Processing

### Distributed Computing Concepts
- [ ] Learn why distributed computing: single-machine limits on memory and CPU.
- [ ] Learn horizontal vs vertical scaling.
- [ ] Learn data parallelism vs task parallelism.
- [ ] Learn shared-nothing architecture.
- [ ] Learn MapReduce programming model: map phase, shuffle/sort, reduce phase.
- [ ] Learn Hadoop ecosystem at a conceptual level: HDFS, YARN, MapReduce.
- [ ] Learn HDFS: blocks, replication, NameNode, DataNode.

### Distributed Systems Theory
- [ ] Learn CAP theorem deeply: why you can only have 2 of 3 in a distributed system.
- [ ] Learn consistency models: strong consistency, eventual consistency, causal consistency.
- [ ] Learn linearisability: the strongest consistency guarantee — reads always see latest write.
- [ ] Learn quorum reads and writes: majority agreement in distributed systems.
- [ ] Learn consensus algorithms at a conceptual level: Paxos, Raft.
- [ ] Learn leader election: how distributed systems choose a coordinator.
- [ ] Learn replication strategies: synchronous vs asynchronous replication.
- [ ] Learn replication lag and its impact on read-after-write consistency.
- [ ] Learn sharding strategies: range-based, hash-based, directory-based.
- [ ] Learn hot spots in sharding: what happens when one shard gets all traffic.
- [ ] Learn fault tolerance patterns: replication, checksums, write-ahead logs.
- [ ] Learn distributed transactions: two-phase commit (2PC) and its drawbacks.
- [ ] Learn saga pattern: managing distributed transactions without 2PC.
- [ ] Learn exactly-once semantics in distributed pipelines: idempotency + deduplication.
- [ ] Learn network partitions: what happens to a pipeline when nodes can't communicate.

### Apache Spark
- [ ] Learn Spark architecture: driver, executors, cluster manager.
- [ ] Learn RDDs: resilient distributed datasets — partitions, transformations, actions.
- [ ] Learn Spark DataFrames and Datasets.
- [ ] Learn Spark SQL: SparkSession, reading/writing tables.
- [ ] Learn Spark transformations: select, filter, groupBy, join, withColumn.
- [ ] Learn Spark actions: count, show, collect, write.
- [ ] Learn lazy evaluation: transformations build a plan, actions execute it.
- [ ] Learn Spark execution plan: DAG of stages and tasks.
- [ ] Learn shuffles: what triggers them, why they're expensive.
- [ ] Learn partitioning: default parallelism, repartition vs coalesce.
- [ ] Learn broadcast joins: avoid shuffle for small-large joins.
- [ ] Learn caching and persistence: cache(), persist(), storage levels.
- [ ] Learn Spark memory model: execution memory vs storage memory.
- [ ] Learn common Spark performance issues: data skew, OOM, small files.
- [ ] Learn Adaptive Query Execution (AQE) in Spark 3.x.
- [ ] Learn Delta Lake with Spark: read, write, merge, time travel.
- [ ] Learn PySpark: Python API for Spark.
- [ ] Learn Spark on Kubernetes vs YARN vs standalone.
- [ ] Learn Databricks: notebooks, clusters, jobs, Repos, Unity Catalog.
- [ ] Learn Spark Structured Streaming (covered in section 11).

### Other Processing Frameworks
- [ ] Learn Apache Flink: stateful stream processing, event time, checkpoints.
- [ ] Learn Flink vs Spark: streaming-first vs batch-first architectures.
- [ ] Learn Beam: unified batch and streaming model, portable pipelines.
- [ ] Learn Dask: parallel Pandas for Python-native workloads.
- [ ] Learn Ray: distributed Python for ML workloads.

---

## 11. Streaming and Real-Time Systems

### Core Concepts
- [ ] Learn event streaming vs message queuing: key differences.
- [ ] Learn event: immutable record of something that happened.
- [ ] Learn event time vs processing time vs ingestion time.
- [ ] Learn out-of-order events and late data.
- [ ] Learn delivery semantics: at-most-once, at-least-once, exactly-once.
- [ ] Learn backpressure: what happens when consumers are slower than producers.
- [ ] Learn exactly-once semantics: idempotent consumers + transactional producers.

### Apache Kafka
- [ ] Learn Kafka architecture: brokers, ZooKeeper / KRaft, controller.
- [ ] Learn topics, partitions, and replication factor.
- [ ] Learn producers: acks=0, acks=1, acks=all — durability trade-offs.
- [ ] Learn consumers and consumer groups.
- [ ] Learn offset management: auto-commit vs manual commit.
- [ ] Learn consumer lag and lag monitoring.
- [ ] Learn retention: time-based and size-based log retention.
- [ ] Learn log compaction: keeping only latest value per key.
- [ ] Learn Kafka Schema Registry: Avro/Protobuf schema enforcement.
- [ ] Learn Kafka Connect: source and sink connectors.
- [ ] Learn Kafka Streams: stateful stream processing in Java/Scala.
- [ ] Learn KSQL / ksqlDB: SQL interface for stream processing on Kafka.
- [ ] Learn Kafka security: TLS, SASL, ACLs.
- [ ] Learn Confluent Platform vs open-source Kafka.
- [ ] Learn MSK (AWS Managed Kafka), Confluent Cloud, Redpanda.

### Stream Processing
- [ ] Learn Apache Flink: distributed stream processor.
- [ ] Learn Flink jobs, operators, and parallelism.
- [ ] Learn Flink state: keyed state, operator state, RocksDB backend.
- [ ] Learn Flink checkpoints and savepoints for fault tolerance.
- [ ] Learn windowing: tumbling, sliding, session windows.
- [ ] Learn watermarks: handling late data in event-time processing.
- [ ] Learn Flink SQL: stream-SQL joins, aggregations, temporal joins.
- [ ] Learn Spark Structured Streaming: micro-batch and continuous modes.
- [ ] Learn Spark Streaming: trigger policies, output modes (append, update, complete).
- [ ] Learn Google Dataflow / Apache Beam: unified batch+stream.
- [ ] Learn Materialize: streaming SQL database on Kafka.

### Cloud Streaming Services
- [ ] Learn AWS Kinesis Data Streams: shards, sequence numbers, retention.
- [ ] Learn AWS Kinesis Data Firehose: managed delivery to S3, Redshift.
- [ ] Learn AWS MSK (Managed Streaming for Kafka).
- [ ] Learn GCP Pub/Sub: topics, subscriptions, push vs pull delivery.
- [ ] Learn GCP Dataflow: managed Beam runner.
- [ ] Learn Azure Event Hubs: Kafka-compatible managed streaming.

### IoT and Edge
- [ ] Learn MQTT protocol: pub/sub, QoS levels, retained messages, LWT.
- [ ] Learn MQTT brokers: Mosquitto, HiveMQ, AWS IoT Core.
- [ ] Learn edge computing: filtering and aggregation at the source.
- [ ] Learn IoT-to-Kafka bridge patterns.
- [ ] Learn time-series data challenges: volume, velocity, out-of-order writes.

---

## 12. Cloud Platforms

### Cloud Fundamentals
- [ ] Learn cloud service models: IaaS, PaaS, SaaS.
- [ ] Learn regions, availability zones, and multi-AZ design.
- [ ] Learn cloud networking: VPC, subnets, security groups, NAT, VPN.
- [ ] Learn cloud IAM: users, roles, policies, service accounts.
- [ ] Learn principle of least privilege.
- [ ] Learn secrets management: AWS Secrets Manager, GCP Secret Manager, HashiCorp Vault.
- [ ] Learn cloud cost models: on-demand, reserved, spot/preemptible.
- [ ] Learn tagging strategy for cost attribution.
- [ ] Learn cloud monitoring: CloudWatch (AWS), Cloud Monitoring (GCP), Azure Monitor.

### AWS for Data Engineering
- [ ] Learn S3: buckets, objects, versioning, lifecycle policies, storage classes.
- [ ] Learn AWS Glue: serverless ETL, Glue Catalog, Crawlers.
- [ ] Learn AWS Athena: serverless SQL on S3.
- [ ] Learn AWS Redshift: managed warehouse.
- [ ] Learn AWS EMR: managed Spark/Hadoop cluster.
- [ ] Learn AWS Lambda: serverless compute for event-driven pipelines.
- [ ] Learn AWS Step Functions: orchestrating Lambda and ECS tasks.
- [ ] Learn AWS SQS: managed message queue.
- [ ] Learn AWS Kinesis: managed streaming.
- [ ] Learn AWS DMS: database migration and CDC.
- [ ] Learn AWS RDS and Aurora: managed relational databases.
- [ ] Learn AWS DynamoDB: managed NoSQL key-value store.
- [ ] Learn AWS IAM: roles, policies, instance profiles, cross-account access.
- [ ] Learn AWS Cost Explorer and Savings Plans.

### GCP for Data Engineering
- [ ] Learn GCS: buckets, object lifecycle, storage classes.
- [ ] Learn BigQuery: warehouse, ML, data transfer service.
- [ ] Learn Cloud Dataflow: managed Beam.
- [ ] Learn Cloud Pub/Sub: managed streaming messaging.
- [ ] Learn Cloud Composer: managed Airflow.
- [ ] Learn Dataproc: managed Spark/Hadoop.
- [ ] Learn Cloud Functions: serverless event-driven compute.
- [ ] Learn Cloud Run: managed containerised services.
- [ ] Learn GKE: managed Kubernetes on GCP.
- [ ] Learn Vertex AI: ML platform with feature store, pipelines, model registry.
- [ ] Learn Looker and Looker Studio for BI on GCP.
- [ ] Learn Cloud Spanner: globally distributed relational database.
- [ ] Learn Firestore: serverless document database.
- [ ] Learn GCP IAM: service accounts, workload identity federation.

### Azure for Data Engineering (Awareness)
- [ ] Learn Azure Data Lake Storage Gen2 (ADLS).
- [ ] Learn Azure Synapse Analytics: integrated warehouse and Spark.
- [ ] Learn Azure Data Factory: managed ETL/ELT pipelines.
- [ ] Learn Azure Event Hubs: Kafka-compatible streaming.
- [ ] Learn Azure Databricks: managed Databricks on Azure.
- [ ] Learn Azure Purview: data governance and cataloging.

---

## 13. DevOps and Platform Engineering

### Containers
- [ ] Learn Docker: images, containers, layers, Dockerfile.
- [ ] Learn Docker Compose: multi-container local development.
- [ ] Learn Docker networking and volumes.
- [ ] Learn building minimal, reproducible Docker images.
- [ ] Learn Docker registry: Docker Hub, GCR, ECR, Artifact Registry.
- [ ] Learn container security: non-root users, image scanning.

### Kubernetes
- [ ] Learn Kubernetes architecture: control plane, nodes, kubelet, API server.
- [ ] Learn Kubernetes objects: Pod, Deployment, Service, ConfigMap, Secret.
- [ ] Learn namespaces and resource quotas.
- [ ] Learn Helm: package manager for Kubernetes, charts, values.yaml.
- [ ] Learn PersistentVolumes and PersistentVolumeClaims.
- [ ] Learn Kubernetes Jobs and CronJobs.
- [ ] Learn Kubernetes resource requests and limits.
- [ ] Learn Kubernetes RBAC: ClusterRole, Role, RoleBinding.
- [ ] Learn Horizontal Pod Autoscaler (HPA).
- [ ] Learn Kubernetes Ingress and service exposure.
- [ ] Learn GKE, EKS, AKS: managed Kubernetes offerings.
- [ ] Learn Argo Workflows on Kubernetes for pipeline orchestration.

### CI/CD
- [ ] Learn CI/CD concepts: continuous integration, delivery, deployment.
- [ ] Learn GitHub Actions: workflows, jobs, steps, runners, secrets.
- [ ] Learn GitLab CI: .gitlab-ci.yml, pipelines, runners.
- [ ] Learn Cloud Build (GCP): managed CI for GCP-native projects.
- [ ] Learn CI for dbt: run dbt test on pull requests.
- [ ] Learn CI for Python: pytest, linting, type checking in pipelines.
- [ ] Learn artefact management: Docker image tagging, versioned packages.
- [ ] Learn deployment strategies: blue-green, canary, rolling.
- [ ] Learn environment promotion: dev → staging → production.

### Infrastructure as Code
- [ ] Learn Terraform: providers, resources, state, plan, apply.
- [ ] Learn Terraform modules and remote state.
- [ ] Learn Terraform workspaces for environment management.
- [ ] Learn Terragrunt: DRY Terraform configuration.
- [ ] Learn Pulumi: infrastructure as code in Python.
- [ ] Learn Google Cloud Deployment Manager / AWS CloudFormation (awareness).
- [ ] Learn managing Airflow, Kafka, and dbt infrastructure with Terraform.

### Reliability and Operations
- [ ] Learn SLI, SLO, SLA for data pipelines.
- [ ] Learn error budget concept.
- [ ] Learn on-call practices for data platform teams.
- [ ] Learn graceful degradation and circuit breaker patterns.
- [ ] Learn blue-green deployments for zero-downtime pipeline changes.
- [ ] Learn database migration strategies with zero downtime.

---

## 14. Security and Governance

### Authentication and Authorisation
- [ ] Learn authentication vs authorisation.
- [ ] Learn service accounts and workload identity for pipelines.
- [ ] Learn OAuth 2.0 and OpenID Connect basics.
- [ ] Learn API key management and rotation.
- [ ] Learn role-based access control (RBAC) in warehouses and cloud.
- [ ] Learn attribute-based access control (ABAC).
- [ ] Learn row-level security (RLS) in BigQuery, Snowflake, Redshift.
- [ ] Learn column-level security: masking policies, column access policies.
- [ ] Learn dynamic data masking in Snowflake and BigQuery.

### Advanced Security
- [ ] Learn zero-trust architecture: never trust, always verify — no implicit internal trust.
- [ ] Learn zero-trust applied to data pipelines: mutual TLS, service mesh basics.
- [ ] Learn secrets rotation: automated rotation of DB passwords and API keys without downtime.
- [ ] Learn secrets sprawl: the risk of secrets in environment variables, logs, and code.
- [ ] Learn data access auditing strategies: logging every query to a governed audit table.
- [ ] Learn secure data sharing: Snowflake secure shares, BigQuery Analytics Hub.
- [ ] Learn network egress controls: preventing data exfiltration via VPC Service Controls.
- [ ] Learn supply chain security: verifying container images and pipeline dependencies.

### Data Privacy and Compliance
- [ ] Learn PII identification and classification.
- [ ] Learn data masking techniques: full masking, partial masking, tokenisation.
- [ ] Learn pseudonymisation vs anonymisation.
- [ ] Learn encryption at rest: cloud-managed keys vs customer-managed keys (CMEK).
- [ ] Learn encryption in transit: TLS, mTLS for pipeline connections.
- [ ] Learn GDPR fundamentals: right to erasure, data minimisation, lawful basis.
- [ ] Learn CCPA fundamentals (California consumer privacy).
- [ ] Learn HIPAA fundamentals (health data in the US).
- [ ] Learn audit logging: who accessed what data and when.
- [ ] Learn data retention and deletion policies.
- [ ] Learn right-to-erasure implementation in data pipelines.

### Data Governance
- [ ] Learn data governance framework: ownership, stewardship, policies.
- [ ] Learn data cataloging: what is a catalog, why it matters.
- [ ] Learn data catalog tools: DataHub, Apache Atlas, Alation, Atlan, Collibra, Amundsen.
- [ ] Learn metadata types: technical, operational, business, and social.
- [ ] Learn data lineage: column-level and table-level lineage tracking.
- [ ] Learn lineage tools: OpenLineage, Marquez, DataHub lineage.
- [ ] Learn data ownership: assigning owners to datasets.
- [ ] Learn data quality SLAs as a governance artifact.
- [ ] Learn data classification: public, internal, confidential, restricted.
- [ ] Learn data mesh concepts: domain ownership, data as a product, federated governance.

### Metadata Management and Cataloging (Deep Dive)
- [ ] Learn data discovery: how analysts and engineers find datasets without asking Slack.
- [ ] Learn technical metadata: schema, column types, row counts, partition info, storage size.
- [ ] Learn business metadata: friendly descriptions, owners, domain tags, glossary terms.
- [ ] Learn operational metadata: last updated, pipeline run status, freshness, SLA adherence.
- [ ] Learn social metadata: usage frequency, popularity, who queries this table most.
- [ ] Learn schema registry concepts: centralised schema versioning for Avro, Protobuf, JSON Schema.
- [ ] Learn Confluent Schema Registry: subject naming strategies, compatibility modes (BACKWARD, FORWARD, FULL).
- [ ] Learn dataset versioning strategies: snapshot-based, append-only, Delta/Iceberg time travel.
- [ ] Learn column-level lineage: tracing a specific column back to its raw source.
- [ ] Learn impact analysis: given a source schema change, which downstream models break?
- [ ] Learn catalog integration with dbt: pushing dbt docs into DataHub or Atlan.
- [ ] Learn catalog integration with Airflow: surfacing DAG lineage in the catalog.
- [ ] Learn data glossary: business term definitions linked to physical columns.
- [ ] Learn metadata-driven pipeline automation: generating pipelines from catalog metadata.

---

## 15. Observability and Operations

### Observability Pillars
- [ ] Learn the three pillars: logs, metrics, and traces.
- [ ] Learn structured logging: JSON logs with context fields.
- [ ] Learn log levels: DEBUG, INFO, WARNING, ERROR, CRITICAL.
- [ ] Learn log aggregation tools: ELK stack, Loki, Cloud Logging.
- [ ] Learn metrics: counters, gauges, histograms, summaries.
- [ ] Learn Prometheus: scraping, metric types, PromQL.
- [ ] Learn Grafana: dashboards for metrics and logs.
- [ ] Learn distributed tracing: spans, trace IDs, OpenTelemetry.
- [ ] Learn OpenTelemetry: standard instrumentation for logs, metrics, traces.

### Pipeline Monitoring
- [ ] Learn pipeline health metrics: row count, duration, error rate, freshness.
- [ ] Learn Airflow monitoring: task duration trends, DAG success rate.
- [ ] Learn dbt run monitoring: model timing, test failure rates.
- [ ] Learn warehouse query monitoring: slot usage, query duration, cost per query.
- [ ] Learn data freshness monitoring: alerting when tables are stale.
- [ ] Learn volume anomaly monitoring: alert on unexpected row count changes.
- [ ] Learn LangFuse / Phoenix for LLM pipeline observability (AI-native pipelines).

### Alerting and Incident Response
- [ ] Learn alerting tools: PagerDuty, OpsGenie, Slack alerts via webhooks.
- [ ] Learn alert fatigue: the danger of too many noisy alerts.
- [ ] Learn SLA breaches: automated alerts before SLA is missed.
- [ ] Learn incident response: acknowledge, investigate, mitigate, post-mortem.
- [ ] Learn runbooks: documented recovery procedures for common failures.
- [ ] Learn root-cause analysis and blameless post-mortems.
- [ ] Learn error triage: distinguishing data errors from infrastructure errors.
- [ ] Learn rerun and recovery: how to re-trigger failed pipeline runs safely.

### Cost Monitoring
- [ ] Learn warehouse cost attribution: tagging queries by team and project.
- [ ] Learn BigQuery cost control: slot reservations, query byte estimation.
- [ ] Learn Snowflake cost control: warehouse sizing, auto-suspend, budgets.
- [ ] Learn cloud storage cost monitoring: lifecycle rules to archive cold data.
- [ ] Learn Spark cost monitoring: executor hours, shuffle bytes.

---

## 15b. Serialization and File Formats (Deep Dive)

### Row-Oriented Formats
- [ ] Learn CSV: no schema, no types, human-readable, universal compatibility, terrible analytics performance.
- [ ] Learn JSON: flexible, nested, verbose, widely used for APIs and event streams.
- [ ] Learn JSONL (JSON Lines): one JSON object per line — ideal for streaming and log ingestion.
- [ ] Learn XML: legacy enterprise format — knowing how to parse it matters for some domains.
- [ ] Learn Avro: row-oriented binary format with schema embedded in the file header.
- [ ] Learn Avro schema evolution: BACKWARD, FORWARD, FULL compatibility modes.
- [ ] Learn Avro with Kafka Schema Registry: enforcing schema contracts on event streams.

### Columnar Formats
- [ ] Learn Parquet: columnar binary, row groups, column chunks, page encoding.
- [ ] Learn Parquet column pruning: queries only read the columns they need.
- [ ] Learn Parquet predicate pushdown: filters applied at the file level before reading rows.
- [ ] Learn ORC: columnar format native to the Hive ecosystem — indexes, bloom filters.
- [ ] Learn Parquet vs ORC: when to use which in Spark, Hive, and Presto ecosystems.

### Binary Serialization Protocols
- [ ] Learn Protocol Buffers (Protobuf): Google's binary serialization — smaller than JSON, typed, fast.
- [ ] Learn Protobuf schema definition (.proto files) and code generation.
- [ ] Learn Protobuf schema evolution: field numbers, reserved fields, default values.
- [ ] Learn MessagePack: binary JSON alternative — smaller, faster, no schema required.
- [ ] Learn Thrift: Facebook's serialization framework — similar goals to Protobuf.
- [ ] Learn when to use Avro vs Protobuf vs JSON: streaming schemas vs API payloads vs simplicity.

### Compression
- [ ] Learn compression trade-off: smaller file size vs CPU cost to compress/decompress.
- [ ] Learn Snappy: fast, moderate compression — default in many Spark/Parquet configs.
- [ ] Learn GZIP/ZLIB: high compression, slower — good for cold storage.
- [ ] Learn ZSTD: modern codec balancing speed and ratio — increasingly preferred.
- [ ] Learn LZ4: extremely fast decompression — useful for real-time analytics.
- [ ] Learn column-level encoding in Parquet: dictionary encoding, RLE, bit packing.
- [ ] Learn when NOT to compress: small files, already-compressed formats.

---

## 15c. Multi-Region, Scalability, and Disaster Recovery

### Geo-Distributed Systems
- [ ] Learn why multi-region matters: latency for global users, regulatory data residency.
- [ ] Learn active-active vs active-passive multi-region architectures.
- [ ] Learn multi-region data replication: synchronous vs asynchronous cross-region replication.
- [ ] Learn replication lag in geo-distributed systems and its impact on consistency.
- [ ] Learn data residency requirements: GDPR, India DPDP — where data must physically reside.
- [ ] Learn geo-partitioning: routing data to regions based on user location.

### Disaster Recovery
- [ ] Learn RTO (Recovery Time Objective): maximum acceptable downtime after a failure.
- [ ] Learn RPO (Recovery Point Objective): maximum acceptable data loss measured in time.
- [ ] Learn backup strategies for data pipelines: warehouse snapshots, lake versioning, config backups.
- [ ] Learn failover strategies: automated vs manual failover, DNS-based failover.
- [ ] Learn cross-region warehouse replication: BigQuery dataset replication, Snowflake replication groups.
- [ ] Learn disaster recovery testing: periodic drills, chaos engineering basics.
- [ ] Learn point-in-time recovery for databases and lakehouse tables.

### Scalability Patterns
- [ ] Learn horizontal scaling for data pipelines: adding more workers vs bigger machines.
- [ ] Learn stateless vs stateful pipeline design and scaling implications.
- [ ] Learn workload isolation: separating ETL loads from BI query traffic in a warehouse.
- [ ] Learn multi-tenancy patterns in data platforms: schema-per-tenant, row-level isolation.
- [ ] Learn queue-based load levelling: buffering work to smooth out traffic spikes.
- [ ] Learn auto-scaling: Spark on K8s dynamic allocation, Snowflake auto-suspend/resume.

---

## 15d. Stakeholder Collaboration and Communication

> Often the most underrated skill gap for data engineers moving into senior roles.

### Requirement Gathering
- [ ] Learn how to translate a business question into a data model and pipeline design.
- [ ] Learn requirement gathering techniques: structured interviews, user story mapping.
- [ ] Learn identifying implicit requirements: data freshness expectations, acceptable latency.
- [ ] Learn documenting data requirements: sources, transformations, outputs, consumers.
- [ ] Learn scoping conversations: distinguishing MVP from the full vision.

### Working with Analysts and Data Scientists
- [ ] Learn what analysts need from data engineers: clean, documented, trusted tables.
- [ ] Learn what data scientists need: raw features, versioned datasets, reproducibility.
- [ ] Learn how to write dbt model descriptions and column docs that non-engineers can read.
- [ ] Learn data contract negotiation: agreeing on schema stability, freshness, and access patterns.
- [ ] Learn how to handle "the numbers don't look right" conversations constructively.
- [ ] Learn educating stakeholders on data quality: helping them understand why a quick fix can break things.

### Defining and Communicating SLAs
- [ ] Learn how to define data SLAs with stakeholders: freshness windows, error budgets.
- [ ] Learn how to communicate pipeline incidents to non-technical stakeholders.
- [ ] Learn writing runbooks and pipeline documentation for handoffs.
- [ ] Learn how to prioritise a pipeline backlog with business context.
- [ ] Learn how to say no to requests and propose better alternatives diplomatically.

### Documentation for Non-Technical Users
- [ ] Learn writing dataset documentation: what this table is, who owns it, when it updates.
- [ ] Learn data dictionary creation: column-level definitions in plain language.
- [ ] Learn architecture diagrams for stakeholder communication (not just engineers).
- [ ] Learn building self-serve data guides: helping analysts explore data independently.

---



### Design Patterns
- [ ] Learn factory pattern for connector/source abstraction.
- [ ] Learn strategy pattern for swappable transformation logic.
- [ ] Learn template method pattern for pipeline step inheritance.
- [ ] Learn singleton pattern for database connection pooling.
- [ ] Learn observer pattern for event-driven pipeline triggers.
- [ ] Learn repository pattern for decoupling data access from business logic.

### API Design and Integration
- [ ] Learn REST API design principles: resources, verbs, status codes.
- [ ] Learn GraphQL basics: queries, mutations, subscriptions.
- [ ] Learn gRPC: protobuf schema, service definitions, streaming.
- [ ] Learn webhook patterns: receiving push events from SaaS tools.
- [ ] Learn API versioning and backward compatibility.
- [ ] Learn rate limiting, retries, circuit breakers in API clients.
- [ ] Learn OpenAPI / Swagger spec for API documentation.

### Performance Engineering
- [ ] Learn profiling Python code: cProfile, Py-Spy.
- [ ] Learn Spark performance tuning: partition sizing, broadcast, AQE.
- [ ] Learn database query plan analysis and index tuning.
- [ ] Learn memory management in Python data pipelines.
- [ ] Learn columnar processing with Polars for large in-memory datasets.
- [ ] Learn vectorised operations vs row-by-row iteration.

### Concurrency and Parallelism
- [ ] Learn threading vs multiprocessing vs async in Python.
- [ ] Learn asyncio patterns for I/O-bound pipeline tasks.
- [ ] Learn parallel pipeline execution strategies.
- [ ] Learn connection pool sizing for parallel database writes.
- [ ] Learn Spark parallelism: tasks per stage, core allocation.

### Maintainability
- [ ] Learn code review best practices for data pipelines.
- [ ] Learn refactoring strategies for legacy pipelines.
- [ ] Learn writing pipeline documentation: purpose, inputs, outputs, dependencies.
- [ ] Learn change management for schema and pipeline changes.
- [ ] Learn technical debt tracking in data platform teams.

---

## 16. Advanced Software Engineering for Data

### Design Patterns
- [ ] Learn factory pattern for connector/source abstraction.
- [ ] Learn strategy pattern for swappable transformation logic.
- [ ] Learn template method pattern for pipeline step inheritance.
- [ ] Learn singleton pattern for database connection pooling.
- [ ] Learn observer pattern for event-driven pipeline triggers.
- [ ] Learn repository pattern for decoupling data access from business logic.

### API Design and Integration
- [ ] Learn REST API design principles: resources, verbs, status codes.
- [ ] Learn GraphQL basics: queries, mutations, subscriptions.
- [ ] Learn gRPC: protobuf schema, service definitions, streaming.
- [ ] Learn webhook patterns: receiving push events from SaaS tools.
- [ ] Learn API versioning and backward compatibility.
- [ ] Learn rate limiting, retries, circuit breakers in API clients.
- [ ] Learn OpenAPI / Swagger spec for API documentation.

### Performance Engineering
- [ ] Learn profiling Python code: cProfile, Py-Spy.
- [ ] Learn Spark performance tuning: partition sizing, broadcast, AQE.
- [ ] Learn database query plan analysis and index tuning.
- [ ] Learn memory management in Python data pipelines.
- [ ] Learn columnar processing with Polars for large in-memory datasets.
- [ ] Learn vectorised operations vs row-by-row iteration.
- [ ] Learn join optimisation strategies: hash join, merge join, nested loop — when each applies.
- [ ] Learn skew handling in distributed systems: salting keys, splitting skewed partitions.
- [ ] Learn caching layers: in-memory caches (Redis), result caches (warehouse), CDN for APIs.
- [ ] Learn workload isolation: preventing ETL jobs from killing BI query performance.

### Concurrency and Parallelism
- [ ] Learn threading vs multiprocessing vs async in Python.
- [ ] Learn asyncio patterns for I/O-bound pipeline tasks.
- [ ] Learn parallel pipeline execution strategies.
- [ ] Learn connection pool sizing for parallel database writes.
- [ ] Learn Spark parallelism: tasks per stage, core allocation.

### Maintainability
- [ ] Learn code review best practices for data pipelines.
- [ ] Learn refactoring strategies for legacy pipelines.
- [ ] Learn writing pipeline documentation: purpose, inputs, outputs, dependencies.
- [ ] Learn change management for schema and pipeline changes.
- [ ] Learn technical debt tracking in data platform teams.

---

## 17. Analytics Engineering

> Analytics engineering sits at the intersection of data engineering and data analysis. It focuses on building reliable, modelled, documented data for consumption by analysts and BI tools.

- [ ] Learn the analytics engineer role vs data engineer vs data analyst.
- [ ] Learn dbt as the primary analytics engineering tool.
- [ ] Learn dbt project structure: models, tests, sources, seeds, snapshots, macros.
- [ ] Learn dbt macros: writing reusable Jinja functions.
- [ ] Learn dbt seeds: loading static CSV lookup tables.
- [ ] Learn dbt snapshots: implementing SCD Type 2 with dbt.
- [ ] Learn dbt exposures: documenting BI dashboards and ML models that use dbt models.
- [ ] Learn dbt metrics layer / MetricFlow: defining metrics in code.
- [ ] Learn dbt documentation: auto-generated docs site, column descriptions.
- [ ] Learn dbt lineage graph: visualising model dependencies.
- [ ] Learn semantic layer tools: Cube, Looker LookML, MetricFlow.
- [ ] Learn metric governance: single definition of "revenue" across the company.
- [ ] Learn BI tool integration: Looker, Tableau, Metabase, Redash connecting to warehouse models.
- [ ] Learn self-serve analytics enablement: building models analysts can query without engineering.
- [ ] Learn data product thinking: treating a dbt model as a product with an owner and SLA.

---

## 18. ML and AI Data Engineering

### Feature Engineering Pipelines
- [ ] Learn feature engineering: transforming raw data into ML-ready inputs.
- [ ] Learn feature types: numeric, categorical, embedding, temporal.
- [ ] Learn feature normalisation and standardisation.
- [ ] Learn one-hot encoding, label encoding, target encoding.
- [ ] Learn time-series features: lag features, rolling aggregates, EWMA.
- [ ] Learn feature pipelines: batch vs real-time feature computation.
- [ ] Learn training-serving skew: ensuring train and inference features match.

### Feature Stores
- [ ] Learn feature store concept: centralised, versioned, reusable features.
- [ ] Learn offline store vs online store in feature stores.
- [ ] Learn point-in-time correctness: avoiding future data leakage.
- [ ] Learn feature store tools: Feast, Tecton, Vertex AI Feature Store, Hopsworks.
- [ ] Learn feature serving for low-latency inference.

### ML Pipelines and MLOps
- [ ] Learn ML pipeline stages: data → features → training → evaluation → deployment.
- [ ] Learn data versioning for ML: DVC, Delta Lake time travel, Iceberg snapshots.
- [ ] Learn experiment tracking: MLflow, Weights and Biases.
- [ ] Learn model registry: versioning and staging models before production.
- [ ] Learn model training pipelines: Kubeflow, Vertex AI Pipelines, SageMaker Pipelines.
- [ ] Learn model serving: REST endpoints, batch scoring, streaming inference.
- [ ] Learn data drift detection: monitoring input distributions after deployment.
- [ ] Learn model monitoring: tracking prediction distributions and performance.
- [ ] Learn LangChain and LangGraph for LLM pipeline orchestration.
- [ ] Learn RAG pipelines: chunking, embedding, vector store, retrieval, generation.
- [ ] Learn vector databases: Pinecone, Weaviate, pgvector, Chroma.
- [ ] Learn LangFuse / Arize for LLM observability.
- [ ] Learn LoRA and QLoRA fine-tuning pipelines and data preparation.
- [ ] Learn synthetic data generation for training data augmentation.

### Data for AI
- [ ] Learn dataset versioning and reproducibility.
- [ ] Learn annotation pipelines and labelling workflows.
- [ ] Learn data flywheel concept: more usage → more data → better models.
- [ ] Learn evaluation datasets: holdout sets, benchmark design.
- [ ] Learn data poisoning risks in training pipelines.

---

## 19. Domain-Specific Knowledge

### BI and Analytics Engineering
- [ ] Learn dashboarding concepts: charts, filters, drilldowns, time comparisons.
- [ ] Learn KPI and metric design: choosing the right numerator and denominator.
- [ ] Learn reporting layers: raw → aggregate → presentation.
- [ ] Learn semantic modeling: LookML, Cube schema, MetricFlow.
- [ ] Learn self-serve analytics: empowering analysts without engineering bottlenecks.
- [ ] Learn cohort analysis data patterns.
- [ ] Learn funnel analysis data patterns.
- [ ] Learn A/B test data pipelines: experiment assignment, metric computation.

### Fintech and Banking
- [ ] Learn auditability requirements: immutable audit trail, lineage to source.
- [ ] Learn compliance-sensitive pipeline design: SOX, PCI-DSS awareness.
- [ ] Learn fraud and risk data flows: transaction scoring pipelines.
- [ ] Learn reconciliation: matching bank records to internal ledgers.
- [ ] Learn regulatory reporting pipelines: Basel III, RBI reporting.
- [ ] Learn market data pipelines: OHLCV, order book, tick data.
- [ ] Learn time-series financial data modeling in TimescaleDB / QuestDB.
- [ ] Learn financial data vendors: Bloomberg, Refinitiv, NSE data APIs.
- [ ] Learn low-latency processing and co-location concepts.
- [ ] Learn algorithmic trading data requirements: backtesting data pipelines.

### Healthcare
- [ ] Learn HIPAA compliance: PHI handling, de-identification standards.
- [ ] Learn HL7 and FHIR: healthcare data exchange standards.
- [ ] Learn EHR data pipelines: patient, encounter, diagnosis records.
- [ ] Learn privacy-preserving analytics: aggregation thresholds, k-anonymity.
- [ ] Learn clinical trial data pipelines and regulatory submissions.

### E-commerce and Retail
- [ ] Learn clickstream pipelines: page views, add-to-cart, purchase funnels.
- [ ] Learn attribution modeling: first-touch, last-touch, multi-touch.
- [ ] Learn recommendation system data flows: collaborative filtering inputs.
- [ ] Learn inventory and supply chain data pipelines.
- [ ] Learn customer lifetime value (LTV) modeling.
- [ ] Learn product catalog data modeling.
- [ ] Learn real-time inventory and pricing pipelines.

### Ad-tech and Marketing
- [ ] Learn event tracking: client-side events, server-side events.
- [ ] Learn campaign data pipelines: impressions, clicks, conversions.
- [ ] Learn identity resolution: cookie IDs, device IDs, hashed emails.
- [ ] Learn attribution models and multi-touch attribution pipelines.
- [ ] Learn third-party cookie deprecation and first-party data strategies.
- [ ] Learn bidding and auction data pipelines at high volume.

### EdTech
- [ ] Learn learner event pipelines: video watch, quiz attempts, completions.
- [ ] Learn learning outcome modeling: completion rate, NPS, cohort performance.
- [ ] Learn LMS (Learning Management System) data extraction.
- [ ] Learn course recommendation data pipelines.
- [ ] Learn engagement scoring for learner churn prediction.

---

## 20. System Design for Data Platforms

- [ ] Learn data platform architecture components and how they connect.
- [ ] Learn designing a batch ELT pipeline from scratch.
- [ ] Learn designing a real-time streaming pipeline from scratch.
- [ ] Learn designing a lakehouse from object storage to BI.
- [ ] Learn designing a multi-tenant data platform.
- [ ] Learn horizontal scalability patterns for data systems.
- [ ] Learn designing for fault tolerance and high availability.
- [ ] Learn designing data systems for compliance: audit trails, access control.
- [ ] Learn capacity planning: estimating storage, compute, cost.
- [ ] Learn API gateway patterns for data platform access.
- [ ] Learn data mesh architecture: domain ownership, data products, federated governance.
- [ ] Learn data fabric: integrated metadata-driven architecture.
- [ ] Learn event-driven architecture for data systems.
- [ ] Learn Lambda architecture: batch + speed layers.
- [ ] Learn Kappa architecture: streaming-only simplification of Lambda.
- [ ] Learn CQRS (Command Query Responsibility Segregation) in data systems.
- [ ] Learn designing idempotent, exactly-once pipelines.
- [ ] Learn partition strategy design for warehouses and lakes.
- [ ] Learn schema registry design for an organisation.
- [ ] Learn trade-off analysis: consistency vs availability, cost vs latency.

---

## 21. Data Mesh and Modern Architecture

- [ ] Learn data mesh principles: domain ownership, data as a product, self-serve platform, federated governance.
- [ ] Learn data domain definition: what constitutes a domain in your org.
- [ ] Learn data product thinking: treating datasets as products with owners, SLAs, and documentation.
- [ ] Learn data product interfaces: output ports, input ports, contracts.
- [ ] Learn federated computational governance: org-wide policies applied locally.
- [ ] Learn self-serve data platform: tooling that lets domain teams own pipelines.
- [ ] Learn data mesh organisational patterns and team topology.
- [ ] Learn data mesh implementation with tools like Atlan, DataHub, dbt.
- [ ] Learn data fabric vs data mesh: centralised metadata intelligence vs distributed ownership.

---

## 22. Specialisation Tracks

### Analytics Engineering Track
- [ ] Master dbt: models, macros, packages, tests, docs, snapshots.
- [ ] Learn semantic layer tools deeply (MetricFlow, Cube, LookML).
- [ ] Learn warehouse performance tuning for BI workloads.
- [ ] Learn self-serve analytics patterns and enablement.
- [ ] Build a complete multi-source dbt project with a semantic layer.

### Streaming Engineering Track
- [ ] Master Kafka: deep configuration, schema registry, Kafka Connect.
- [ ] Learn Flink: stateful processing, checkpoints, Flink SQL.
- [ ] Learn exactly-once pipeline design.
- [ ] Learn stream-table duality and changelog streams.
- [ ] Build a real-time pipeline: API → Kafka → Flink → ClickHouse → dashboard.

### Platform Engineering Track
- [ ] Master Kubernetes for data: operators, Argo Workflows, Spark on K8s.
- [ ] Learn Terraform for infrastructure provisioning of data systems.
- [ ] Learn internal developer platform (IDP) concepts for data teams.
- [ ] Learn GitOps patterns for pipeline deployment.
- [ ] Build a self-serve pipeline platform with templates and CI/CD.

### Cloud Data Engineering Track
- [ ] Deep dive into one cloud (GCP recommended given your BigQuery experience).
- [ ] Learn cloud-native managed services deeply: Dataflow, Pub/Sub, Composer.
- [ ] Learn cloud cost engineering: FinOps for data teams.
- [ ] Learn multi-cloud and hybrid cloud data architectures.

### ML Data Engineering Track
- [ ] Learn feature store architecture and implementation.
- [ ] Learn training data pipelines and dataset versioning.
- [ ] Learn model monitoring and data drift pipelines.
- [ ] Learn LLM pipeline engineering: RAG, fine-tuning data prep, evaluation.
- [ ] Build an end-to-end ML feature pipeline with a feature store.

### Warehouse Engineering Track
- [ ] Learn advanced Snowflake / BigQuery administration and performance.
- [ ] Learn warehouse cost optimisation and governance.
- [ ] Learn warehouse-native ML and semantic layer deployment.
- [ ] Build a production-grade warehouse with dbt, tests, and BI.

---

## 23. Projects to Build

### Foundational Projects
- [ ] Build a Python script to extract from a public REST API and load to Postgres.
- [ ] Build a batch ETL pipeline with incremental extraction and error handling.
- [ ] Build a dbt project on top of a raw dataset (at least 3 layers: staging → intermediate → mart).
- [ ] Build a data quality framework with automated tests using dbt-expectations or Great Expectations.
- [ ] Build a simple Airflow DAG with retries, sensors, and alerting.

### Intermediate Projects
- [ ] Build a CDC pipeline from Postgres to BigQuery using Debezium + Kafka.
- [ ] Build a streaming Kafka pipeline with a Python producer and consumer.
- [ ] Build a Parquet-based data lake with medallion architecture on GCS or local filesystem.
- [ ] Build a customer 360 / entity-centric model in dbt joining 3+ source systems.
- [ ] Build a dashboard-ready analytics pipeline with dbt + Looker Studio / Metabase.
- [ ] Build a cost-monitored BigQuery project with partitioning and clustering.

### Advanced Projects
- [ ] Build a real-time streaming pipeline: API → Kafka → Flink/Spark Streaming → warehouse.
- [ ] Build a lakehouse project with Delta Lake / Iceberg: ACID, time travel, schema evolution.
- [ ] Build a data platform with CI/CD: GitHub Actions runs dbt tests on every PR.
- [ ] Build a feature engineering pipeline for a financial ML model (Kalkey signal generation).
- [ ] Build a RAG pipeline (Mind Palace style) with chunking, embedding, vector store, and LangGraph.
- [ ] Build an agentic data pipeline with LangGraph for document intelligence (ClinicalAgent / EdTech variant).
- [ ] Build a self-serve orchestration platform with Argo Workflows on Kubernetes.

### Portfolio Project (End-to-End)
- [ ] Design and build one complete end-to-end data platform project that includes:
  - [ ] Source extraction (API, DB, or file).
  - [ ] Orchestration (Airflow or Argo).
  - [ ] Transformation (dbt with tests and docs).
  - [ ] Storage (warehouse or lakehouse).
  - [ ] Observability (logging, alerting, freshness checks).
  - [ ] BI or ML consumption layer.
  - [ ] README with architecture diagram.
  - [ ] CI/CD pipeline for dbt tests.

---

## 24. Interview Preparation

### SQL Practice
- [ ] Practice window functions: ROW_NUMBER, LAG, LEAD, running totals.
- [ ] Practice complex GROUP BY with HAVING and conditional aggregation.
- [ ] Practice self joins and recursive CTEs.
- [ ] Practice deduplication using ROW_NUMBER() OVER PARTITION BY.
- [ ] Practice median and percentile queries without built-in functions.
- [ ] Practice pivot queries using CASE WHEN.
- [ ] Practice explaining query execution plans.
- [ ] Solve 50+ SQL problems on LeetCode, StrataScratch, or DataLemur.

### Python Practice
- [ ] Practice file parsing: CSV, JSON, nested structures.
- [ ] Practice API calls with pagination and error handling.
- [ ] Practice data transformation with Pandas / Polars.
- [ ] Practice writing testable, modular pipeline code.
- [ ] Practice algorithmic problems relevant to data: sorting, grouping, dedup.

### Data Modeling Practice
- [ ] Practice designing star schema from a business scenario.
- [ ] Practice SCD Type 2 design and implementation.
- [ ] Practice entity-relationship design given requirements.
- [ ] Practice choosing grain for a fact table.
- [ ] Practice designing a customer 360 or similar entity model.

### System Design Practice
- [ ] Practice designing a batch ELT pipeline (sources, schedule, transforms, monitoring).
- [ ] Practice designing a real-time streaming pipeline for a given use case.
- [ ] Practice designing a lakehouse architecture.
- [ ] Practice capacity planning and cost estimation.
- [ ] Practice trade-off discussions: batch vs streaming, SQL vs NoSQL, managed vs self-hosted.
- [ ] Practice explaining the difference between ETL and ELT.
- [ ] Practice describing your production projects: architecture, scale, decisions.

### Behavioural and Stakeholder Practice
- [ ] Practice STAR format (Situation, Task, Action, Result) for project stories.
- [ ] Practice explaining technical trade-offs to non-technical stakeholders.
- [ ] Practice describing how you handle pipeline failures in production.
- [ ] Practice explaining your approach to data quality.
- [ ] Practice discussing team collaboration and data ownership challenges.
- [ ] Practice explaining how you prioritise in a multi-project environment.

---

## 25. Continuous Learning Habits

- [ ] Follow data engineering blogs: Substack, Towards Data Engineering, DataEngineeringWeekly.
- [ ] Follow practitioners on LinkedIn: Zach Wilson, Joe Reis, Tristan Handy.
- [ ] Read foundational books: "Fundamentals of Data Engineering" (Reis & Housley), "Designing Data-Intensive Applications" (Kleppmann).
- [ ] Read "The Data Warehouse Toolkit" (Kimball) for dimensional modeling.
- [ ] Watch conference talks: Data + AI Summit, dbt Coalesce, Kafka Summit.
- [ ] Build in public: write LinkedIn or Medium posts about projects.
- [ ] Contribute to open-source: dbt packages, Airbyte connectors, OpenLineage.
- [ ] Participate in Kaggle data engineering competitions and challenges.
- [ ] Maintain a personal knowledge base (Mind Palace / Obsidian) of what you learn.
- [ ] Review architecture decisions from real companies: Airbnb, Uber, Netflix engineering blogs.

---

## Suggested Progression

| Stage | Sections | Goal |
|-------|----------|------|
| Beginner | 1 – 5 | Python, SQL, databases, data modeling, ETL/ELT basics |
| Intermediate | 6 – 12 | Orchestration, quality, warehousing, lakes, Spark, streaming, cloud |
| Advanced | 13 – 17 | DevOps, governance, metadata, serialization, DR, stakeholder skills, software engineering, analytics engineering |
| Specialised | 18 – 23 | ML pipelines, domain knowledge, system design, data mesh, specialisation track |
| Portfolio-ready | 24 – 26 | Projects, interview prep, continuous learning |

**Recommended path for your profile (Pulin):** You are already strong in sections 1–9 and have hands-on production experience in dbt, Airflow/Argo, BigQuery, and LangGraph. Focus next on: §10 (Spark — skew, AQE, broadcast), §11 (Kafka+Flink streaming depth), §13 (Terraform/IaC), §15b (Protobuf — used in Kafka production), §15c (DR/RTO/RPO for senior roles), §15d (stakeholder skills for Associate Director positioning), §18 (ML/AI pipelines — RAG, feature stores), §20 (system design interview prep), and §24 (portfolio end-to-end project).
