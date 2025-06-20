# Simple Batch Job

This is a simple Python batch job that can be run as a Kubernetes Job resource.

## Features

- Simulates data processing with configurable batch size and processing time
- Includes error handling and logging
- Configurable via environment variables
- Proper exit codes for Kubernetes Job status
- Resource limits and requests defined
- Automatic cleanup after completion

## Building and Running

### 1. Build the Docker image

```bash
docker build -t simple-batch-job:v1 .
```

### 2. Run locally (optional)

```bash
docker run --rm -e BATCH_SIZE=50 -e PROCESSING_TIME=10 -e JOB_NAME=test-job -e FAILURE_RATE=0 simple-batch-job:v1
```

### 3. Deploy to Kubernetes

```bash
kubectl apply -f job.yaml
```

### 4. Monitor the job

```bash
# Check job status
kubectl get jobs

# View job logs
kubectl logs job/simple-batch-job

# Get detailed job information
kubectl describe job simple-batch-job
```

### 5. Clean up

```bash
kubectl delete job simple-batch-job
```

## Configuration

The batch job can be configured using environment variables:

- `JOB_NAME`: Name identifier for the job
- `BATCH_SIZE`: Number of items to process (default: 50)
- `PROCESSING_TIME`: Total processing time in seconds (default: 10)

## Job Characteristics

- **Restart Policy**: Never (failed containers won't be restarted)
- **Backoff Limit**: 3 retries before marking as failed
- **Active Deadline**: 5 minutes maximum runtime
- **TTL**: Automatic cleanup after 1 hour of completion
