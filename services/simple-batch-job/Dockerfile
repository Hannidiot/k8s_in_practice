FROM python:3.11-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY batch_processor.py .

# Make the script executable
RUN chmod +x batch_processor.py

# Create a non-root user for security
RUN useradd -m -u 1000 batchuser && chown -R batchuser:batchuser /app
USER batchuser

# Run the batch job
CMD ["python", "batch_processor.py"]
