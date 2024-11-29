from loguru import logger
import time

# Simulate logging over time
if __name__ == "__main__":
    # Counter for log messages
    log_counter = 0

    # Sleep for 1 second by default
    sleep_time = 1
    try:
        while True:
            log_counter += 1
            logger.info(f"Log entry #{log_counter}")
           
            # If log_counter is divisible by 5, sleep for 2 seconds
            if log_counter % 5 == 0:
                time.sleep(sleep_time)  # Sleep for the determined time
    except KeyboardInterrupt:
        print("\nLogging stopped.")

