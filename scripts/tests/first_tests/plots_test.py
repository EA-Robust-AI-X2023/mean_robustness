from byzfl.benchmark.evaluate_results import test_accuracy_curve_modified,plot_gradients_scattering, loss_heatmap, plot_workers_feature_variance

path_training_results = "results"
path_to_plot = "plot"

test_accuracy_curve_modified(
    path_training_results,
    path_to_plot
)

# plot_gradients_scattering(path_training_results, path_to_plot)