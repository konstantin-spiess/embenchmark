# Sentence Embedding Benchmark


## Installation

### Prerequisites:

- Python 3.9 or above
- PiP 23.3 or above

### Steps:

1. Because we are downloading and using a lot of data from huggingface, you need to create a .env file and add you [huggingface token](https://huggingface.co/docs/hub/en/security-tokens), otherwise downloading the required models and datasets might fail.
    ```bash
    HF_TOKEN="<your_huggingface_token>"
    ```
2. To run the benchmark, select the task you want to run, e.g. `clustering_benchmarks.ipynb` and run all cells.
3. Display the results and create all associated plots by running the plot notebook, e.g. `clustering_plots.ipynb`.
    The available task and plots are:
    | Task | Plot |
    | --- | --- |
    | `clustering_benchmarks.ipynb` | `clustering_plots.ipynb` |
    | `clustering_benchmarks_cutoff.ipynb` | `clustering_plots_cutoff.ipynb` |
    | `retrieval_benchmark_cqa.ipynb` | `retrieval_plots.ipynb` |
    | `retrieval_benchmark_nqa_chunking.ipynb` | `retrieval_plots.ipynb` |
    | `retrieval_benchmark_nqa_seq.ipynb` | `retrieval_plots.ipynb` |
    | `sts_benchmarks.ipynb` | `sts_plots.ipynb` |
    
