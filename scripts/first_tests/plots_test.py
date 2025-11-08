from byzfl.benchmark.evaluate_results import test_accuracy_curve_modified, loss_heatmap, plot_gradients_scattering, plot_workers_feature_variance

path_training_results = "results_tests_new_client_dynamic"
path_to_plot = "plot"

test_accuracy_curve_modified(
    path_training_results,
    path_to_plot
)

# loss_heatmap(path_training_results, path_to_plot)

# plot_workers_feature_variance(path_training_results, path_to_plot)

# plot_maximum_regular_feature_mean(path_training_results, path_to_plot)

plot_gradients_scattering(path_training_results, path_to_plot)