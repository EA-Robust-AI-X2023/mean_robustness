from byzfl.benchmark.evaluate_results import test_accuracy_curve_modified,plot_gradients_scattering, loss_heatmap, plot_workers_feature_variance, evaluate_impact_exclusivity

path_training_results = "results"
path_to_plot = "plot"


colors = [
    (0.000, 0.447, 0.741),   # blue
    (0.850, 0.325, 0.098),   # red-orange
    (0.466, 0.674, 0.188),   # green
    (0.494, 0.184, 0.556),   # purple
    (0.929, 0.694, 0.125),   # yellow
    (0.301, 0.745, 0.933),   # cyan
    (0.635, 0.078, 0.184),   # dark red
    (0.7,   0.2,   0.5),     # magenta blend
    (0.2,   0.2,   0.2),     # dark gray
    (0.7,   0.7,   0.7)      # light gray
]
tab_sign = [
    '-',
    '--',
    '-.',
    ':',
    (0, (5, 1)),     # dashed, fine
    (0, (3, 1, 1, 1)),  # dash-dot-dot
    (0, (1, 1)),     # densely dotted
    (0, (3, 5, 1, 5)),  # dash-space patterns
    (0, (5, 10)),    # very sparse dash
    'solid'
]
markers = [
    'o',   # circle
    's',   # square
    '^',   # triangle up
    'v',   # triangle down
    '<',   # triangle left
    '>',   # triangle right
    'D',   # diamond
    'P',   # plus-filled
    'X',   # x-filled
    '*'    # star
]


test_accuracy_curve_modified(
    path_training_results,
    path_to_plot,
    colors=colors,
    tab_sign=tab_sign,
    markers=markers
)


# plot_gradients_scattering(path_training_results, path_to_plot)

evaluate_impact_exclusivity(path_training_results,
    path_to_plot,
    colors=colors,
    tab_sign=tab_sign,
    markers=markers)