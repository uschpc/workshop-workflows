#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu-1GB
#SBATCH --time=00:10:00
#SBATCH --array=1-3
module load python ffmpeg

song_files=(`ls data/symphonie_fantastique`)


#song_file="data/symphonie_fantastique/berlioz_symphonie_2_un_bal_vals.mp3"
song_file=${song_files[$SLURM_ARRAY_TASK_ID]}
song_name=`basename $song_file .mp3`
out_dir="output/$song_name"

echo "Processing: $song_name"

python3 ./scripts/rosa_fft.py -f ${song_file} -o ${out_dir}
