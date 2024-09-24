from src.config import ConfigManager
from src.components.data_load import DataIngestion
from src import logger


step = "Step_1: Download Data From Kaggle"


def main():
    config = ConfigManager()
    data_config = config.get_data_config()
    data_ingestion = DataIngestion(data_config=data_config)
    data_ingestion.download()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>  {step} has started...  <<<<<<<")
        main()
        logger.info(f"<<<<<<<  {step} was completed successfully  >>>>>>>")
    except Exception as e:
        logger.exception(e)
        raise e