import os
import logging
from functools import wraps
from datetime import datetime

def setup_logger():
    """Setup the logger to save logs to a file in a `log` folder."""
    log_dir = "log"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Log filename with timestamp
    log_filename = os.path.join(log_dir, f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
    
    logging.basicConfig(
        filename=log_filename,
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    return logging.getLogger()

logger = setup_logger()

def logFunc(func):
    """Decorator to log the execution of a function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Function '{func.__name__}' started.")
        try:
            result = func(*args, **kwargs)
            logger.info(f"Function '{func.__name__}' completed successfully.")
            return result
        except Exception as e:
            logger.error(f"Function '{func.__name__}' raised an error: {str(e)}", exc_info=True)
            raise
    return wrapper

# Example usage
@logFunc
def foo():
    print("Executing foo...")
    # Simulate an error
    raise ValueError("An error occurred in foo.")

if __name__ == "__main__":
    try:
        foo()
    except Exception:
        print("Error captured in logs.")
