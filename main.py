from src.pipeline.data_loading import data_load
from src.pipeline.model_building import model_build
from src.pipeline.training import train


data_load.main()

model_build.main()

train.main()