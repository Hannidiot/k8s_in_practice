#!/usr/bin/env python3
import os
import time
import random
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def simulate_data_processing(batch_size=100, processing_time=2, failure_rate=0):
    """Simulate processing a batch of data items"""
    logger.info(f"Starting batch job processing {batch_size} items")
    
    processed_items = 0
    failed_items = 0
    
    for i in range(batch_size):
        try:
            # Simulate processing time
            time.sleep(processing_time / batch_size)
            
            # Simulate occasional failures (5% failure rate)
            if random.random() < failure_rate:
                raise Exception(f"Processing failed for item {i+1}")
            
            processed_items += 1
            
            if (i + 1) % 20 == 0:
                logger.info(f"Processed {i+1}/{batch_size} items")
                
        except Exception as e:
            failed_items += 1
            logger.warning(f"Failed to process item {i+1}: {str(e)}")
    
    return processed_items, failed_items

def main():
    """Main batch job execution"""
    start_time = datetime.now()
    logger.info("Batch job started")
    
    # Get configuration from environment variables
    batch_size = int(os.getenv('BATCH_SIZE', '50'))
    processing_time = int(os.getenv('PROCESSING_TIME', '10'))
    job_name = os.getenv('JOB_NAME', 'unnamed-batch-job')
    failure_rate = float(os.getenv('FAILURE_RATE', '0'))  # 0 failure rate
    
    logger.info(f"Job configuration: name={job_name}, batch_size={batch_size}, processing_time={processing_time}s, failure_rate={failure_rate}")
    
    try:
        # Process the batch
        processed, failed = simulate_data_processing(batch_size, processing_time, failure_rate)
        
        # Log results
        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()
        
        logger.info(f"Batch job completed successfully!")
        logger.info(f"Processed: {processed} items")
        logger.info(f"Failed: {failed} items")
        logger.info(f"Duration: {duration:.2f} seconds")
        
        # Exit with appropriate code
        if failed > 0:
            logger.warning(f"Job completed with {failed} failures")
            exit(1)
        else:
            logger.info("Job completed successfully with no failures")
            exit(0)
            
    except Exception as e:
        logger.error(f"Batch job failed with error: {str(e)}")
        exit(1)

if __name__ == "__main__":
    main()
