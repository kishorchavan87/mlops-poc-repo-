import kfp
from kfp import dsl

@dsl.pipeline(name="training-pipeline")
def train_pipeline():
    dsl.ContainerOp(
        name="train-step",
        image="us-central1-docker.pkg.dev/your-project/my-docker-repo/train:latest",
        command=["python","train.py"]
    )

if __name__ == "__main__":
    kfp.compiler.Compiler().compile(train_pipeline, "train_pipeline.yaml")
