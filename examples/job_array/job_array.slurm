#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=1GB
#SBATCH --time=00:10:00
#SBATCH --array=0-92
module load python
module load libsndfile
module load ffmpeg

# How many seconds to process per job
duration=4

time_index=$((SLURM_ARRAY_TASK_ID*duration))

echo "Processing time_index:${time_index}"

python3 ./scripts/rosa_fft.py -f data/symphonie_fantastique/berlioz_symphonie_2_un_bal_vals.mp3 -i ${time_index} -t ${duration} -o output/berlioz_symphonie_2_un_bal_vals

