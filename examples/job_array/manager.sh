#!/bin/bash

# save 4th word using ' ' as delmiter
# AKA the job id
jid=$(sbatch examples/job_array/job_array.slurm | cut -d ' ' -f 4)

sbatch --dependency=afterok:${jid} examples/job_array/ffmpeg.slurm
