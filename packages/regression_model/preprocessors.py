import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class CategoricalImputer(BaseEstimator, TransformerMixin):
    """Categorical data missing value imputer."""

    def __init__(self):
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

    def fit(self, X: pd.DataFrame, y: pd.Series = None) -> 'CategoricalInputer':
        """Fit stetement to accomodate the sklearn pipeline"""

        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        """Apply the transforms to the dataframe."""

        X = X.copy()
        for feature in self.variables:
            X[feature] = X[feature].fillna("Missing")

        return X