# Script to build Docker images for all services

# Set error action preference
$ErrorActionPreference = "Stop"

# Function to build a Docker image
function Build-DockerImage {
    param (
        [string]$ServicePath,
        [string]$ImageName,
        [string]$Tag = "latest"
    )
    
    Write-Host "Building $ImageName from $ServicePath..." -ForegroundColor Cyan
    try {
        docker build -t "$ImageName`:$Tag" $ServicePath
        if ($LASTEXITCODE -eq 0) {
            Write-Host "Successfully built $ImageName`:$Tag" -ForegroundColor Green
            return $true
        }
        else {
            Write-Host "Failed to build $ImageName`:$Tag" -ForegroundColor Red
            return $false
        }
    }
    catch {
        Write-Host "Error building $ImageName`: $_" -ForegroundColor Red
        return $false
    }
}

# Array of services to build
$services = @(
    @{
        Path = ".\hello-world"
        Name = "hello-world-service"
        Tag = "latest"
    },
    @{
        Path = ".\simple-batch-job"
        Name = "simple-batch-job"
        Tag = "v1"
    }
)

# Build each service
$failedBuilds = 0
foreach ($service in $services) {
    if (-not (Build-DockerImage -ServicePath $service.Path -ImageName $service.Name -Tag $service.Tag)) {
        $failedBuilds++
    }
}

# Exit with appropriate status code
if ($failedBuilds -gt 0) {
    Write-Host "Build completed with $failedBuilds failures" -ForegroundColor Red
    exit 1
}
else {
    Write-Host "All builds completed successfully" -ForegroundColor Green
    exit 0
}
