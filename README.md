# workshop-workflows
Workshop materials for *Methods for Automating Job Submission

Researchers commonly find themselves repetitively checking the job scheduler to find the status of jobs and deciding what jobs to submit next. Workflow management software (wms) allows users to automate this process by defining a sequence of tasks to be done. When a workflow is then run, the wms can automatically manage job dependencies, resubmit failed jobs, and delete unneeded intermediate files.

This presentation will use `makeflow` to demonstrate some of these ideas. Other tools such as `snakemake` and Pegasus will be discussed
