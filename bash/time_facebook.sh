#! /bin/bash
echo '......Chengbin HOU @SUSTech 2019......';

echo '------------------- DynRWSG -----------------------------------------' > bash/log/time_facebook_DynRWSG.txt;
python src/main.py --method DynRWSG --task lp --graph data/facebook/facebook.pkl --num-walks 20 --restart-prob 0.2 --update-threshold 0.1 --emb-dim 128 --workers 40  >> bash/log/time_facebook_DynRWSG.txt;
echo '--done--' >> bash/log/time_facebook_DynRWSG.txt;
echo '--DynRWSG done--';

echo '------------------- DeepWalk -----------------------------------------' > bash/log/time_facebook_DeepWalk.txt;
python src/main.py --method DeepWalk --task lp --graph data/facebook/facebook.pkl --num-walks 20 --restart-prob 0.2 --update-threshold 0.1 --emb-dim 128 --workers 40  >> bash/log/time_facebook_DeepWalk.txt;
echo '--done--' >> bash/log/time_facebook_DeepWalk.txt;
echo '--DeepWalk done--';

echo '------------------- HOPE -----------------------------------------' > bash/log/time_facebook_HOPE.txt;
python src/main.py --method HOPE --task lp --graph data/facebook/facebook.pkl --num-walks 20 --restart-prob 0.2 --update-threshold 0.1 --emb-dim 128 --workers 40  >> bash/log/time_facebook_HOPE.txt;
echo '--done--' >> bash/log/time_facebook_HOPE.txt;
echo '--HOPE done--';

echo '------------------- GraRep -----------------------------------------' > bash/log/time_facebook_GraRep.txt;
python src/main.py --method GraRep --task lp --graph data/facebook/facebook.pkl --num-walks 20 --restart-prob 0.2 --update-threshold 0.1 --emb-dim 128 --workers 40  >> bash/log/time_facebook_GraRep.txt;
echo '--done--' >> bash/log/time_facebook_GraRep.txt;
echo '--GraRep done--';

echo '......well done......';