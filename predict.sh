for k in {101..110}
do
    for j in {0..13}
    do
        python predict.py --model ./checkpoints/checkpoint_epoch10.pth --scale 1 --classes 1 -i /home/ciplab/data/unseen/kubric360_v2/${k}/${j}_rgb_test.png -o ./results/${k}/${j}_mask_pred.png
    done
done