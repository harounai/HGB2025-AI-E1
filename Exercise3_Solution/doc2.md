# Activity 3 – Monitoring user experience in near real-time
For this activity the plan was to implement a Spark Structured Streaming application that continuously monitors crash-related events from Kafka. And it should aggregates events in 1-s intervals grouped by user_id, and output results when the crash count exceeds a defined threshold.

## Implementation Attempt
A Spark Structured Streaming application was prepared to read log events from a Kafka topic and process them in real time. The intended logic included filtering log messages containing the term "crash", restricting the severity level to High or Critical, grouping events by user_id, and applying event-time windowed aggregation with watermarking to handle late-arriving data.

The application was executed inside a Docker-based Spark cluster, and a load generator was configured to continuously publish log events to Kafka.

## Issues Encountered
During execution, multiple technical issues were encountered related to the containerized environment and streaming setup. These included problems with Docker networking, container state inconsistencies, and difficulties running the Spark Structured Streaming application reliably despite correct configurations.

Although the Spark cluster and Kafka services were running, the streaming application could not be executed successfully to completion. As a result, no stable streaming output or Web UI evidence could be produced for Activity 3.

## Conclusion
Despite multiple attempts, Activity 3 could not be fully completed due to persistent infrastructure and runtime issues that could not be resolved within the given timeframe. However, the implementation effort and encountered problems provided valuable insight into the complexity of deploying and debugging real-time streaming applications in distributed, containerized environments.