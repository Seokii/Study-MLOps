from kfp.components import InputPath, OutputPath, create_component_from_func
from kfp.dsl import pipeline
from functools import partial
import kfp

@partial(
    create_component_from_func,
    packages_to_install = ["pandas", "dill", "scikit-learn==1.0.1"],
)
def load_iris_data(
        data_path: OutputPath("csv"),
        target_path: OutputPath("csv"),
):
    import pandas as pd
    from sklearn.datasets import load_iris
    iris = load_iris()

    data = pd.DataFrame(iris["data"], columns=iris["feature_names"])
    target = pd.DataFrame(iris["target"], columns=["target"])

    data.to_csv(data_path, index=False)
    target.to_csv(target_path, index=False)


@partial(
    create_component_from_func,
    packages_to_install = ["pandas", "dill", "scikit-learn==1.0.1"],
)
def train_from_csv(
    train_data_path: InputPath("csv"),
    train_target_path: InputPath("csv"),
    model_path: OutputPath("dill"),
    kernel: str,
):
    import dill
    import pandas as pd
    from sklearn.svm import SVC

    train_data = pd.read_csv(train_data_path)
    train_target = pd.read_csv(train_target_path)

    clf = SVC(kernel=kernel)
    clf.fit(train_data, train_target)

    with open(model_path, mode="wb") as file_writer:
        dill.dump(clf, file_writer)


@pipeline(name="complex_pipeline")
def complex_pipeline(kernel: str):
    iris_data = load_iris_data()
    model = train_from_csv(
        train_data = iris_data.outputs["data"],
        train_target = iris_data.outputs["target"],
        kernel = kernel,
    )

if __name__ == "__main__":
    kfp.compiler.Compiler().compile(complex_pipeline, "complex_pipeline.yaml")