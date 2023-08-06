import numpy as np
import pandas as pd


class DataFrameChecker:
    """Class responsible for checking, transforming, and validating DataFrames."""

    def __init__(self, dataframe):
        """
        Initializes the DataFrameChecker with a pandas DataFrame.

        Args:
            dataframe (pd.DataFrame): The input pandas DataFrame to be checked and transformed.
        """
        self.dataframe = dataframe

    def check_empty_dataframe(self):
        """
        Check if the DataFrame is empty.

        Raises:
            ValueError: If the DataFrame is empty.

        Returns:
            DataFrameChecker: Returns self to allow method chaining.
        """
        if self.dataframe.empty:
            raise ValueError('The DataFrame is empty!')
        return self

    def fill_na_and_drop(self):
        """
        Fill null values with zero.

        Returns:
            DataFrameChecker: Returns self to allow method chaining.
        """
        self.dataframe = self.dataframe.fillna(0)

        if 'time' in self.dataframe.columns:
            self.dataframe.drop(columns=['time'], inplace=True)
        return self

    def check_expected_columns(self):
        """
        Verify the DataFrame contains the expected columns.

        Raises:
            ValueError: If any expected column is missing.

        Returns:
            DataFrameChecker: Returns self to allow method chaining.
        """
        expected_columns = ['vibration_x', 'vibration_y', 'vibration_z']
        existing_columns = self.dataframe.columns
        for col in expected_columns:
            if col not in existing_columns:
                raise ValueError(f"Expected column '{col}' not found!")
        return self

    def check_positive_values(self):
        """
        Check if all columns have only positive values.

        Raises:
            ValueError: If any column contains negative values.

        Returns:
            DataFrameChecker: Returns self to allow method chaining.
        """
        if (self.dataframe < 0).any().any():
            raise ValueError('The DataFrame contains negative values!')
        return self

    def check_datatype_float(self):
        """
        Validate the datatype of all columns to ensure they are float.

        Raises:
            ValueError: If any column doesn't have a float datatype.

        Returns:
            DataFrameChecker: Returns self to allow method chaining.
        """
        for column in self.dataframe.columns:
            if self.dataframe[column].dtype != np.float64:
                raise ValueError(
                    f'Column {column} does not have float datatype!'
                )
        return self

    def get_dataframe(self):
        """
        Get the processed pandas DataFrame.

        Returns:
            pd.DataFrame: The validated and transformed pandas DataFrame.
        """
        return self.dataframe

    def pipeline_checker(self):
        """
        Execute a series of checks and transformations on the DataFrame.

        Returns:
            pd.DataFrame: The validated and transformed pandas DataFrame.
        """

        self.check_empty_dataframe()
        self.fill_na_and_drop()
        self.check_expected_columns()
        self.check_positive_values()
        self.check_datatype_float()

        return self.get_dataframe()
