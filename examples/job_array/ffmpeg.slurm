#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu=1GB
#SBATCH --time=00:10:00
module load ffmpeg

ffmpeg -framerate 60 -i output/berlioz_symphonie_2_un_bal_vals/images/frame%09d.png -i data/symphonie_fantastique/berlioz_symphonie_2_un_bal_vals.mp3 -pix_fmt yuv410p -threads ${SLURM_CPUS_PER_TASK} output/berlioz_symphonie_2_un_bal_vals.mp4 -y




