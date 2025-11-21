from byzfl.benchmark import run_benchmark

if __name__ == "__main__":  # Required for multiprocessing
    n = 30  # Number of trainings to run in parallel
    run_benchmark(n)
