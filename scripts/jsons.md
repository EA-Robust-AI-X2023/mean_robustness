## Proposer des configurations pour nos boucles d'entraînement.

Justifier chaque configuration au regard du projet.

### Batch size: 10, 32, 64 et 128

Permet de réduire la la variance des gradients locaux.
Dans _mean is more robust_, la batch size est a priori de 32.

### Tester nos aggrégateurs dans la configuration sans attaque,

Cela permet de mesurer l'écart de performance entre la moyenne et les aggrégateurs robustes dans le cas sans attaque.
Ce sera utile pour montrer que la mauvaise performance des aggrégateurs robustes dans le cas de la label separation est attribuable essentiellement à la mauvaise performance des aggrégateurs robustes dans le cas sans attaque.

### tester sur CIFAR100 et tiny imagenet (200 classes)

Utiliser Resnet-9 ou Resnet-18 (à décider).
Pour Resnet-9, se référer au papier [Rethinking data heterogeneity](https://arxiv.org/pdf/2209.15595) pour les hyperparamètres.

### Pour les datasets avec beaucoup de classes, augmenter le nombre de clients.

## Rédaction des jsons associés

### Dans un premier temps, un json de test:

dirichlet_modified_1 pour reg_softmax et attaque statique:

default_config = {
"benchmark_config": {
"training_algorithm": {
"name": "DSGD",
"parameters": {}
},
"nb_steps": 10000,
"device": "cuda",
"training_seed": 0,
"nb_training_seeds": 3,
"nb_honest_clients": 10,
"f": [1, 2, 3, 4],
"data_distribution_seed": 0,
"nb_data_distribution_seeds": 1,
"data_distribution": [
{
"name": "gamma_similarity_niid",
"distribution_parameter": [1.0, 0.66, 0.33, 0.0]
}
],
},
"model": {
"name": "softmax_mnist",
"dataset_name": "mnist",
"nb_labels": 10,
"loss": "CrossEntropyLoss",
"learning_rate": 0.1,
"learning_rate_decay": 1.0,
"milestones": []
},
"aggregator": [
{
"name": "GeometricMedian",
"parameters": {
"nu": 0.1,
"T": 3
}
},
{
"name": "TrMean",
"parameters": {}
}
],
"pre_aggregators": [
{
"name": "Clipping",
"parameters": {}
},
{
"name": "NNM",
"parameters": {}
}
],
"honest_clients": {
"momentum": 0.9,
"weight_decay": 0.0001,
"batch_size": 25
},
"attack": [
{
"name": "SignFlipping",
"parameters": {}
},
{
"name": "Optimal_InnerProductManipulation",
"parameters": {}
},
{
"name": "Optimal_ALittleIsEnough",
"parameters": {}
}
],
"evaluation_and_results": {
"evaluation_delta": 50,
"batch_size_evaluation": 128,
"evaluate_on_test": True,
"store_per_client_metrics": True,
"store_models": False,
"data_folder": "./data",
"results_directory": "./results"
}
}

### Ensuite, un json de reproduction des résultats du papier pour la régression softmax:

Partitions: iid, dirichlet\_$\alpha=1$, noniid

Attaques: static/dynamic

Modèle: d'abord juste reg_softmax

{
"benchmark_config": {
"training_algorithm": {
"name": "DSGD",
"parameters": {}
},
"nb_steps": 20000,
"device": "cpu",
"training_seed": 1,
"nb_training_seeds": 3,
"nb_honest_clients": 9,
"f": [1],
"data_distribution_seed": 0,
"nb_data_distribution_seeds": 3,
"data_distribution": [
{
"name": "dirichlet_niid_modified",
"distribution_parameter": [10.0,1.0,0.1, 0.03,0.01]
},
{
"name": "iid",
},
{
"name": "extreme_noniid_modified",
}
]
},
"model": {
"name": "softmax_mnist",
"dataset_name": "mnist",
"nb_labels": 10,
"loss": "CrossEntropyLoss",
"learning_rate": 0.01,
"learning_rate_decay": 0,
"milestones": []
},
"aggregator": [
{
"name": "Average",
"parameters": {}
},
{
"name": "Lfighter",
"parameters": {}
},
{
"name": "Faba",
"parameters": {}
},
{
"name": "Krum",
"parameters": {}
},
{
"name": "TrMean",
"parameters": {}
},
{
"name": "CenteredClipping",
"parameters": {
"tau": 0.3
}
},
{
"name": "Median",
"parameters": {
"tau": 0.3
}
}
],
"pre_aggregators": [],
"honest_clients": {
"momentum": 0.9,
"weight_decay": 0.01,
"batch_size": 32
},
"attack": [
{
"name": "DynamicLabelFlipping",
"p": 1.0,
"parameters": {}
},
{
"name": "StaticLabelFlipping",
"p": 1.0,
"parameters": {}
}
],
"evaluation_and_results": {
"evaluation_delta": 50,
"batch_size_evaluation": 128,
"evaluate_on_test": true,
"store_per_client_metrics": true,
"store_models": false,
"data_folder": "../../data",
"results_directory": "results_tests_new_client_dynamic",
"make_feature_measures": true,
"compute_gradient_variance": true,
"compute_gradient_scatterings": true,
"scatter_momentums": false
}
}

### Ensuite, un json de reproduction des résultats complets:

Partitions: iid, dirichlet\_$\alpha= 0.001, 0.01, 0.03, 0.05, 0.1, 1, 10$, noniid

Attaques: static/dynamic

Modèles: reg_softmax, MLP, CNN

{
"benchmark_config": {
"training_algorithm": {
"name": "DSGD",
"parameters": {}
},
"nb_steps": 20000,
"device": "gpu",
"training_seed": 1,
"nb_training_seeds": 3,
"nb_honest_clients": 9,
"f": [1],
"data_distribution_seed": 0,
"nb_data_distribution_seeds": 3,
"data_distribution": [
{
"name": "dirichlet_niid_modified",
"distribution_parameter": [10.0,1.0,0.1, 0.03,0.01]
},
{
"name": "iid",
},
{
"name": "extreme_noniid_modified",
}
]
},
"model": {
"name": ["cnn_mnist", "mlp_mnist_peng"],
"dataset_name": "mnist",
"nb_labels": 10,
"loss": "CrossEntropyLoss",
"learning_rate": 0.01,
"learning_rate_decay": 0,
"milestones": []
},
"aggregator": [
{
"name": "Average",
"parameters": {}
},
{
"name": "Lfighter",
"parameters": {}
},
{
"name": "Faba",
"parameters": {}
},
{
"name": "Krum",
"parameters": {}
},
{
"name": "TrMean",
"parameters": {}
},
{
"name": "CenteredClipping",
"parameters": {
"tau": 0.3
}
},
{
"name": "Median",
"parameters": {
"tau": 0.3
}
}
],
"pre_aggregators": [],
"honest_clients": {
"momentum": 0.9,
"weight_decay": 0.0085,
"batch_size": 32
},
"attack": [
{
"name": "DynamicLabelFlipping",
"p": 1.0,
"parameters": {}
},
{
"name": "StaticLabelFlipping",
"p": 1.0,
"parameters": {}
}
],
"evaluation_and_results": {
"evaluation_delta": 50,
"batch_size_evaluation": 128,
"evaluate_on_test": true,
"store_per_client_metrics": true,
"store_models": false,
"data_folder": "../../data",
"results_directory": "results_tests_new_client_dynamic",
"make_feature_measures": true,
"compute_gradient_variance": true,
"compute_gradient_scatterings": true,
"scatter_momentums": false
}
}

### Ensuite, un json d'extension des résultats du papiers:

tiny imagenet, batch sizes changeantes etc...
