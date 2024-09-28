from src.config import ConfigManager
from src.components.data_loading import Data
from src import logger


step = "Step_1: Download Data From Kaggle"


class data_load:
    def main():
        config = ConfigManager()
        data_config = config.get_data_config()
        data_ingestion = Data(data_config=data_config)
        data_ingestion.download()


if __name__ == '__main__':
    try:
        logger.info(f"\n>>>>>>>  {step} has started...  <<<<<<<")
        data_load().main()
        logger.info(f"<<<<<<<  {step} was completed successfully  >>>>>>>\n")
    except Exception as e:
        logger.exception(e)
        raise e