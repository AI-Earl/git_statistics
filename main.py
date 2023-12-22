from app import app
from app.utility.logger import logger
from config import config

if __name__ == '__main__':
    logger.info(f'System Run in \033[31m{config.MODE}\033[0m Mode.')
    app.run(host="0.0.0.0", port=config.PORT)
