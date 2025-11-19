This folder is dedicated to replicating the results in Peng et al, only for the softmax regression.

The hyperparameters are set to match the implementation of momentum of the paper:
lr= 0.001
alpha_momentum=9
weight decay = 0.001


To run experiments in the back with ssh, use tmux:

Étape	Commande	Effet
1	tmux new -s train	Crée une session persistante “train”
2	source venv/bin/activate	Active ton environnement Python
    python train.py | tee logs/train_softmax.log
4	Ctrl + B, D	Détache la session (tu peux te déconnecter)
5	tmux attach -t train	Rouvre ta session tmux
6	tail -f logs/train.log	Visualise les logs en continu


