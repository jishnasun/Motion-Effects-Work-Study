%-----------------------------------------------------------------------
% Job saved on 27-Mar-2025 15:12:38 by cfg_util (rev $Rev: 7345 $)
% spm SPM - Unknown
% cfg_basicio BasicIO - Unknown
%-----------------------------------------------------------------------
matlabbatch{1}.cfg_basicio.run_ops.runjobs.jobs = {'/neurodesktop-storage/python files/matlabbatch_realign_single_subject_all_runs_emptydir.m'};
matlabbatch{1}.cfg_basicio.run_ops.runjobs.inputs{1}{1}.indir = {'/home/jovyan/data/derivatives/avp/sub-1435220200204'}; % Input file path for each subject file
matlabbatch{1}.cfg_basicio.run_ops.runjobs.inputs{2}{1}.indir = {'/data/derivatives/avp/sub-1469120221102'}; % These two are left as examples, can paste this and change path and index to do any number of jobs in one run 
matlabbatch{1}.cfg_basicio.run_ops.runjobs.save.dontsave = false; % Note that the subject files must be in teh directory specified in matlabbatch_realign_single_subject_all_runs_emptydir.m
matlabbatch{1}.cfg_basicio.run_ops.runjobs.missing = 'skip';
