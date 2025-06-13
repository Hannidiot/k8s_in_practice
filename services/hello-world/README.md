# Hello World Service

A simple Flask application that provides a `/hello` endpoint with random request tracking.

## Features

- **GET /hello**: Returns JSON with:
  - `requestID`: A randomly generated GUID for each request
  - `serverID`: A randomly generated GUID created when the service starts
  - `time`: Current timestamp in ISO format

- **GET /**: Returns service information and available endpoints

## Running the Application

### Local Development
```bash
pip install -r requirements.txt
python main.py
```

### Docker
```bash
# Build the image
docker build -t hello-world-service .

# Run the container
docker run -p 5000:5000 hello-world-service
```

Or use the PowerShell script:
```powershell
.\run-docker.ps1
```

## Testing

Once running, test the endpoints:

```bash
# Root endpoint
curl http://localhost:5000/

# Hello endpoint
curl http://localhost:5000/hello
```

## Example Response

GET `/hello` returns:
```json
{
  "requestID": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
  "serverID": "6ba7b810-9dad-11d1-80b4-00c04fd430c8", 
  "time": "2025-06-13T10:30:45.123456"
}
```

The `serverID` remains the same for all requests until the service is restarted.
