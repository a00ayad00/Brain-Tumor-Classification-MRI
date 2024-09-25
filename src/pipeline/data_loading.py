from src.config import ConfigManager
from src.components.data_loading import DataIngestion
from src import logger


step = "Step_1: Download Data From Kaggle"


class data_load:
    def main():
        config = ConfigManager()
        data_config = config.get_data_config()
        data_ingestion = DataIngestion(data_config=data_config)
        data_ingestion.download()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>  {step} has started...  <<<<<<<")
        data_load().main()
        logger.info(f"<<<<<<<  {step} was completed successfully  >>>>>>>")
    except Exception as e:
        logger.exception(e)
        raise e