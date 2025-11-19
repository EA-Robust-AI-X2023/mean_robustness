This folder is dedicated to replicating the results in Peng et al, only for the softmax regression.

Here, we replicate with a batch size of 1000, as in the paper's code to compute A and ksi.


To run experiments in the back with ssh, use tmux:

Étape	Commande	Effet
1	tmux new -s train	Crée une session persistante “train”
2	source venv/bin/activate	Active ton environnement Python
    python train.py | tee logs/train_softmax.log
4	Ctrl + B, D	Détache la session (tu peux te déconnecter)
5	tmux attach -t train	Rouvre ta session tmux
6	tail -f logs/train.log	Visualise les logs en continu


