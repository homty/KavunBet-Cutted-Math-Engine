# Math Engine roadmap

## Phase 0 — showcase cleanup

- [x] Retain only the ways game example.
- [x] Remove upstream-facing documentation and branded assets.
- [x] Remove the embedded optimizer and cloud uploader.
- [x] Remove non-ways calculation strategies.
- [x] Keep license attribution.
- [x] Keep a focused CI test workflow.

## Phase 1 — isolate the evaluation core

- [ ] Define `EvaluationRequest` and `EvaluationResult` domain models.
- [ ] Define explicit limits for spins, reel count, stops, symbols, and request size.
- [ ] Replace mutable singleton configuration with one configuration per evaluation.
- [ ] Load candidate BASE/FREE reel CSV content without modifying repository files.
- [ ] Make seeded evaluations reproducible.
- [ ] Return RTP, hit rate, maximum win, and requested interval/ways metrics.

## Phase 2 — define the gRPC contract

- [ ] Add a versioned `proto/math_engine/v1/evaluation.proto` contract.
- [ ] Add `EvaluateCandidate` and health-check RPCs.
- [ ] Map protobuf messages to domain models at the transport boundary.
- [ ] Define validation, timeout, cancellation, and error status behavior.
- [ ] Generate Python client/server code reproducibly.

## Phase 3 — build the service

- [ ] Implement the gRPC server and evaluation application service.
- [ ] Bound concurrent CPU work with a worker/semaphore policy.
- [ ] Propagate deadlines and cancellation into simulation work.
- [ ] Add structured logs with job and candidate correlation IDs.
- [ ] Add readiness and liveness checks.

## Phase 4 — verification

- [ ] Unit-test CSV validation, configuration mapping, and metrics.
- [ ] Add deterministic golden tests for known reels and seeds.
- [ ] Add gRPC integration tests for success and error cases.
- [ ] Test request limits, deadlines, cancellation, and concurrent calls.
- [ ] Add an Optimizer-to-MathEngine contract test.

## Phase 5 — packaging and Azure deployment

- [ ] Build a minimal non-root Docker image.
- [ ] Run CI linting, tests, type checks, and image build.
- [ ] Push the image to Azure Container Registry.
- [ ] Deploy privately with internal service discovery and gRPC/HTTP2.
- [ ] Configure CPU/memory limits, autoscaling, logs, and metrics.

## Phase 6 — integration completion

- [ ] Connect the Optimizer worker to the generated gRPC client.
- [ ] Store result metadata in Cosmos DB.
- [ ] Store candidate/best reel CSV artifacts in Azure Blob Storage.
- [ ] Expose best-result selection through the Optimizer REST API.
- [ ] Run an end-to-end optimization with no more than 5,000 spins per candidate.
