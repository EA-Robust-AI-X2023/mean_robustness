THis folder is dedicated to testing the new fork of byzfl (byzfl-test)

Typically, you will want to test some implementation in a branch of our byzfl fork.

For this:

- First disinstall byzfl: pip uninstall byzfl -y (on windows)

- Then install your branch : pip install git+https://github.com/EA-Robust-AI-X2023/byzfl-test.git@branch-name


To run experiments in the back with ssh, use tmux:

Étape	Commande	Effet
1	tmux new -s train	Crée une session persistante “train”
2	source venv/bin/activate	Active ton environnement Python
    python train.py | tee logs/train_softmax.log
4	Ctrl + B, D	Détache la session (tu peux te déconnecter)
5	tmux attach -t train	Rouvre ta session tmux
6	tail -f logs/train.log	Visualise les logs en continu


