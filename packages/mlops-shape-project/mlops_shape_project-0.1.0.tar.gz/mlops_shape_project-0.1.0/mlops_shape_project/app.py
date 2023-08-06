from mlops_shape_project.data_loader import DataLoader
from mlops_shape_project.dataframe_checker import DataFrameChecker
from mlops_shape_project.feature_engineering_predict import FeatureEngPredict
from mlops_shape_project.pipeline_utils import PipelineCreator

if __name__ == '__main__':

    DATA_PATH = 'data/dataset.parquet'
    CONFIG_PATH = 'artifacts/pipeline.jsonc'

    try:
        dataframe = DataLoader.read_data_dataframe(DATA_PATH)
        if dataframe is None or dataframe.empty:
            raise ValueError('DataFrame is empty or None!')
    except Exception as e:
        print(f'Error loading data: {e}')
        exit()

    checker = DataFrameChecker(dataframe)

    try:
        dataframe_input = checker.pipeline_checker()

    except Exception as e:
        print(f'Error processing DataFrame: {e}')
        exit()

    try:
        pipeline_transform = PipelineCreator.create_pipeline_from_file(
            CONFIG_PATH
        )
        if pipeline_transform is None:
            raise ValueError('Pipeline creation failed!')
    except Exception as e:
        print(f'Error creating pipeline: {e}')
        exit()

    model_predict, dataframe_output = FeatureEngPredict.process_dataframe(
        dataframe_input, pipeline_transform
    )
    print(model_predict)
    print(dataframe_output)
    
    
