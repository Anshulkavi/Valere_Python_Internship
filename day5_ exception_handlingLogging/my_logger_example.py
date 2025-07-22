import logging

#configure logger
logging.basicConfig(
    level = logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers = [
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

def divide(x, y):
    logging.debug(f"Trying to divide {x} by {y}")
    try:
        result = x / y
    except ZeroDivisionError as e:
        logging.error("Attempted division by zero!", exc_info=True)
    else:
        logging.info(f"Division successful: {result}")
        return result        

def main():
    logging.info("Program started") 
    divide(10, 2)
    divide(5,0)
    logging.warning("This is just a warning message")
    logging.critical("Something really critical happened")
    logging.info("Program finished")

if __name__ == "__main__":
    main()