THis folder is dedicated to conduct tests, especially on byzfl changes.

In order to run experiments in this folder, with its config.json, you should run the scripts of the folder from the folder directly (cd scripts/folder-name; python tests_train.py).

Typically, you will want to test some implementation in a branch of our byzfl fork.

For this:

- First disinstall byzfl: pip uninstall byzfl -y (on windows)

- Then install your branch : pip install git+https://github.com/EA-Robust-AI-X2023/byzfl.git@branch-name
