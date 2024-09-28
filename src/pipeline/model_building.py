from src.config import ConfigManager
from src.components.model_building import Model
from src import logger


step = "Step_2: Prepare The Downloaded Model For Training"


class model_build:
    def main():
        config = ConfigManager()
        model_config = config.get_model_config()
        model = Model(model_config)
        model.download()
        model.update()


if __name__ == '__main__':
    try:
        logger.info(f"\n>>>>>>>  {step} has started...  <<<<<<<")
        model_build.main()
        logger.info(f"<<<<<<<  {step} was completed successfully  >>>>>>>\n")
    except Exception as e:
        logger.exception(e)
        raise e