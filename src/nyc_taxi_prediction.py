import bentoml
from bentoml.adapters import DataframeInput
from bentoml.frameworks.sklearn import SklearnModelArtifact


@bentoml.ver(major=1, minor=0)
@bentoml.artifacts([SklearnModelArtifact('model')])
@bentoml.env(pip_packages=['scikit-learn==0.23.2'])
class NycTaxiPredictionRFService(bentoml.BentoService):
    @bentoml.api(input=DataframeInput(), batch=True)
    def predict(self, df):
        print(f"Prediction! data : {df}")
        return self.artifacts.model.predict(df)
