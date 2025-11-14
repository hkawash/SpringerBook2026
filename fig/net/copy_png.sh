#!/bin/sh

for net in 'att' 'ali'; do 
    echo $net
    mkdir -p $net
    for i in `seq -w 0 20 280`; do
        echo $i
        cp /mnt/c/researchU/02Modeling/code/fig_with_alignment/network_w${net}_color/0${i}.png ${net}/0${i}.png
    done
done
