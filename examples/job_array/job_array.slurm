#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=1GB
#SBATCH --time=00:10:00
#SBATCH --array=0-3

module load python ffmpeg libsndfile

song_files=(`ls ../../data/symphonie_fantastique/*.mp3`)


song_file=${song_files[$SLURM_ARRAY_TASK_ID]}
song_name=`basename $song_file .mp3`
out_dir="output/$song_name"

echo "Processing: $song_name"

python3 ../../scripts/rosa_fft.py -f ../../data/symphonie_fantastique/${song_file} -o ${out_dir}
