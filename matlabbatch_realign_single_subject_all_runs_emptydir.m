%-----------------------------------------------------------------------
% Job saved on 28-Mar-2025 02:59:20 by cfg_util (rev $Rev: 7345 $)
% spm SPM - Unknown
% cfg_basicio BasicIO - Unknown
%-----------------------------------------------------------------------
matlabbatch{1}.cfg_basicio.file_dir.dir_ops.cfg_cd.dir = {'/home/jovyan/data/derivatives/ya'};
matlabbatch{2}.cfg_basicio.file_dir.dir_ops.cfg_named_dir.name = 'Subject Folder';
matlabbatch{2}.cfg_basicio.file_dir.dir_ops.cfg_named_dir.dirs = {'<UNDEFINED>'};
matlabbatch{3}.cfg_basicio.file_dir.file_ops.file_fplist.dir(1) = cfg_dep('Named Directory Selector: Subject Folder(1)', substruct('.','val', '{}',{2}, '.','val', '{}',{1}, '.','val', '{}',{1}, '.','val', '{}',{1}), substruct('.','dirs', '{}',{1}));
matlabbatch{3}.cfg_basicio.file_dir.file_ops.file_fplist.filter = '.*run.*\.nii';
matlabbatch{3}.cfg_basicio.file_dir.file_ops.file_fplist.rec = 'FPListRec';
matlabbatch{4}.cfg_basicio.file_dir.file_ops.cfg_file_split.name = 'fMRI Runs';
matlabbatch{4}.cfg_basicio.file_dir.file_ops.cfg_file_split.files(1) = cfg_dep('File Selector (Batch Mode): Selected Files (.*run.*\.nii)', substruct('.','val', '{}',{3}, '.','val', '{}',{1}, '.','val', '{}',{1}, '.','val', '{}',{1}), substruct('.','files'));
matlabbatch{4}.cfg_basicio.file_dir.file_ops.cfg_file_split.index = {
                                                                     1
                                                                     2
                                                                     3
                                                                     4
                                                                     5
                                                                     6
                                                                     7
                                                                     }';
matlabbatch{5}.spm.spatial.realign.estimate.data{1}(1) = cfg_dep('File Set Split: fMRI Runs (1)', substruct('.','val', '{}',{4}, '.','val', '{}',{1}, '.','val', '{}',{1}, '.','val', '{}',{1}), substruct('{}',{1}));
matlabbatch{5}.spm.spatial.realign.estimate.data{2}(1) = cfg_dep('File Set Split: fMRI Runs (2)', substruct('.','val', '{}',{4}, '.','val', '{}',{1}, '.','val', '{}',{1}, '.','val', '{}',{1}), substruct('{}',{2}));
matlabbatch{5}.spm.spatial.realign.estimate.data{3}(1) = cfg_dep('File Set Split: fMRI Runs (3)', substruct('.','val', '{}',{4}, '.','val', '{}',{1}, '.','val', '{}',{1}, '.','val', '{}',{1}), substruct('{}',{3}));
matlabbatch{5}.spm.spatial.realign.estimate.data{4}(1) = cfg_dep('File Set Split: fMRI Runs (4)', substruct('.','val', '{}',{4}, '.','val', '{}',{1}, '.','val', '{}',{1}, '.','val', '{}',{1}), substruct('{}',{4}));
matlabbatch{5}.spm.spatial.realign.estimate.data{5}(1) = cfg_dep('File Set Split: fMRI Runs (5)', substruct('.','val', '{}',{4}, '.','val', '{}',{1}, '.','val', '{}',{1}, '.','val', '{}',{1}), substruct('{}',{5}));
matlabbatch{5}.spm.spatial.realign.estimate.data{6}(1) = cfg_dep('File Set Split: fMRI Runs (6)', substruct('.','val', '{}',{4}, '.','val', '{}',{1}, '.','val', '{}',{1}, '.','val', '{}',{1}), substruct('{}',{6}));
matlabbatch{5}.spm.spatial.realign.estimate.data{7}(1) = cfg_dep('File Set Split: fMRI Runs (7)', substruct('.','val', '{}',{4}, '.','val', '{}',{1}, '.','val', '{}',{1}, '.','val', '{}',{1}), substruct('{}',{7}));
matlabbatch{5}.spm.spatial.realign.estimate.eoptions.quality = 0.9;
matlabbatch{5}.spm.spatial.realign.estimate.eoptions.sep = 4;
matlabbatch{5}.spm.spatial.realign.estimate.eoptions.fwhm = 5;
matlabbatch{5}.spm.spatial.realign.estimate.eoptions.rtm = 0;
matlabbatch{5}.spm.spatial.realign.estimate.eoptions.interp = 2;
matlabbatch{5}.spm.spatial.realign.estimate.eoptions.wrap = [0 0 0];
matlabbatch{5}.spm.spatial.realign.estimate.eoptions.weight = '';
