# Math Engine architecture

## Responsibility

The Math Engine is a stateless evaluation worker. Given a configuration, reel CSVs, a spin limit, and a seed, it runs the ways/free-spin model and returns reproducible metrics.

## System flow

1. The frontend sends optimization settings to the Optimizer REST API.
2. The Optimizer creates candidates and owns the optimization lifecycle.
3. The Optimizer calls the Math Engine through gRPC for candidate evaluation.
4. The Math Engine validates the request, runs a bounded simulation, and returns metrics.
5. The Optimizer compares results and stores job/config/result metadata in Cosmos DB.
6. Reel CSVs and large result artifacts are stored in Azure Blob Storage.
7. The frontend reads job progress and selectable best results through the Optimizer API.

## Repository boundary

This repository owns:

- ways and free-spin game rules;
- reel CSV decoding and validation;
- deterministic simulation;
- metric calculation;
- the gRPC evaluation contract and server;
- Math Engine tests and container image.

This repository does not own:

- REST endpoints for the frontend;
- simulated annealing or candidate generation;
- optimization-job persistence;
- user authentication;
- Cosmos DB or Blob Storage writes.

The service should receive artifact content or a short-lived signed Blob URL. It should not receive Cosmos DB credentials.
