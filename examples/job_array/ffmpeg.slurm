#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu=1GB
#SBATCH --time=00:10:00
module load ffmpeg

song_file="data/symphonie_fantastique/berlioz_symphonie_2_un_bal_vals.mp3"
frame_dir="output/berlioz_symphonie_2_un_bal_vals/images"
out_file="output/berlioz_symphonie_2_un_bal_vals.mp4"

ffmpeg \
-framerate 60 -i ${frame_dir}/frame%09d.png \
-i ${song_file} \
-pix_fmt yuv420p \
-threads ${SLURM_CPUS_PER_TASK} \
${out_file}
