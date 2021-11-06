%------------------left label-------------------------
load('../data/tt.mat');
ori_label_left = bw(243:273,110:138,96:113);
for i = 96: 113
    eval(['ori_label_left',num2str(i-95,'%02d'),'=[];']);
    eval(['ori_label_left',num2str(i-95,'%02d'),'=ori_label_left(:,:,',num2str(i-95),');']);
    eval([' save ../data/step0_left_data/ori_label_left',num2str(i-95,'%02d'),'.mat  ','ori_label_left',num2str(i-95,'%02d')]);
end

% -------------------left data-------------------------
% path = '../data/thin/IM';
load('../data/tt.mat');
for i = 96: 113
%     a = 3;
    % img_path = [path,int2str(i)];
    eval(['data_left',num2str(i-95,'%02d'),'=A(243:273,110:138,',num2str(i),' ); ']);

    eval([' save ../data/step0_left_data/data_left',num2str(i-95,'%02d'),'.mat  ','data_left',num2str(i-95,'%02d')]);
end

%------------------------------------------------------
%------------------right label-------------------------
%------------------------------------------------------
load('../data/tt.mat');
ori_label_right = bw(243:278,380:410,110:127);
% label_right = tt(243:278,380:410,110:127);
 for i = 110: 127
    eval(['ori_label_right',num2str(i-109,'%02d'),'=[];']);
    eval(['ori_label_right',num2str(i-109,'%02d'),'=ori_label_right(:,:,',num2str(i-109),');']);
    eval([' save ../data/step0_right_data/ori_label_right',num2str(i-109,'%02d'),'.mat  ','ori_label_right',num2str(i-109,'%02d')]);
 end

 %------------------right data-------------------------
% path = '../data/thin/IM';
for i = 110: 127
    % img_path = [path,int2str(i)];
    eval(['data_right',num2str(i-109,'%02d'),'=A(243:278,380:410,',num2str(i),'); ']);
%     eval(['data_right',num2str(i-109,'%02d'),'=','data_right',num2str(i-109,'%02d'),'(243:278,380:410);']);
    eval([' save ../data/step0_right_data/data_right',num2str(i-109,'%02d'),'.mat  ','data_right',num2str(i-109,'%02d')]);
end