#!/bin/bash
#SBATCH --job-name=WindZ14Om6
#SBATCH --mail-type=FAIL,END
#SBATCH --mail-user=z.keszthelyi@uva.nl
#SBATCH -n 1 -c 24
#SBATCH -N 1
#SBATCH -t 72:00:00
#SBATCH -p normal

#CD to folder
cd $HOME/winds/Z014Om6

for k in 1 2 3 4

do 
    echo "Creating main directory...$k"  
    mkdir $k 
    mkdir $k/template
    cp -r template $k/
    cp -r inlist_gen.f $k/
    cp -r inlist_pgstar $k/

for j in 20 30 40 50 60                            

do
    cd $HOME/winds/Z014Om6/$k
    echo "Creating sub-directory...$j"
    mkdir $j
    cp -r template/* $j
    cd $j
    sed -i -e "s/extras_cpar(1) =/extras_cpar(1) = 'route$k' /" inlist_grid
    sed -i -e "s/initial_mass =/initial_mass = $j /" inlist_grid
    echo "Running model..."
    ./rn > rn.out
    echo "Finished running model with Route and mass: $k/$j"
    rm -r clean history_columns.list inlist inlist_grid make mk photos profile_columns.list re README_first rn src star
    cd ..
done
    cd ..
done 
