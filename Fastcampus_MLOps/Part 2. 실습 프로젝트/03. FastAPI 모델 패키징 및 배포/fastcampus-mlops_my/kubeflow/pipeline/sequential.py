import kfp
from kfp import dsl


def gcs_download_op(url):
    return dsl.ContainerOp(
        name="GCS - Download",
        image="google/cloud-sdk:279.0.0",
        command=["sh", "-c"],
        arguments=["gsutil cat $0 | tee $1", url, "/tmp/results.txt"],
        file_outputs={
            "data": "/tmp/results.txt",
        },
    )


def echo_op(text):
    return dsl.ContainerOp(
        name="echo",
        image="library/bash:4.4.23",
        command=["sh", "-c"],
        arguments=['echo "$0"', text],
    )


@dsl.pipeline(
    name="sequential-pipeline", description="A pipeline with two sequential steps."
)
def sequential_pipeline(
    url: str = "gs://ml-pipeline/sample-data/shakespeare/shakespeare1.txt",
):
    """A pipeline with two sequential steps."""

    download_task = gcs_download_op(url)
    echo_task = echo_op(download_task.output)


# Compile the pipeline
if __name__ == "__main__":
    kfp.compiler.Compiler().compile(
        pipeline_func=sequential_pipeline, package_path="build/sequential.tar.gz"
    )
