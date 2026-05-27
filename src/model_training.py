from sklearn.linear_model import LinearRegression

from xgboost import XGBRegressor

from lightgbm import LGBMRegressor


def train_models(
    X_train,
    y_train
):

    models = {}

    models[
        'Linear Regression'
    ] = LinearRegression()

    models[
        'XGBoost'
    ] = XGBRegressor(
        random_state=42
    )

    models[
        'LightGBM'
    ] = LGBMRegressor(
        random_state=42
    )

    for name, model in models.items():

        model.fit(
            X_train,
            y_train
        )

    return models
