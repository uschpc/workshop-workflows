#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu-1GB
#SBATCH --time=00:10:00
#SBATCH --array=0-9
#SBATCH --account=renney_710
module load python ffmpeg

# How many seconds to process per job
duration=4
time_index=$((SLURM_ARRAY_TASK_ID*duration))
song_file="data/symphonie_fantastique/berlioz_symphonie_2_un_bal_vals.mpr"
out_dir="output/berlioz_symphonie_2_un_bal_vals"

echo "Processing time_index:${time_index}"

python3 ./scripts/rosa_fft.py -f ${song_file} -i ${time_index} -t ${duration} -o ${out_dir}
