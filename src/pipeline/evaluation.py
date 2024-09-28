from src.config import ConfigManager
from src.components.evaluation import Eval
from src import logger


step = "Step_4: Evaluate The Trained Model"
eval_file_path = 'eval.json'


class eval:
    def main():
        config = ConfigManager().get_eval_config()
        evaluate = Eval(config)
        evaluate.eval(eval_file_path)


if __name__ == '__main__':
    try:
        logger.info(f"\n>>>>>>>  {step} has started...  <<<<<<<")
        eval.main()
        logger.info(f"<<<<<<<  {step} was completed successfully and the file saved at {eval_file_path}  >>>>>>>\n")
    except Exception as e:
        logger.exception(e)
        raise e