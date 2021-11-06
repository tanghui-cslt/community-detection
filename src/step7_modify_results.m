%------------------left label-------------------------
%复制到命令行中执行

clear label_left;
load('../data/tt.mat');
label_left=false(31,29,18);
 for i = 96:113
    eval([' load ../results/left/gml/label_left',num2str(i-95,'%02d'),'.mat  ']);
    eval(['label_left(:,:,',num2str(i-95,'%02d'),') = label_left(:,:,',num2str(i-95,'%02d'),') +label_left',num2str(i-95,'%02d'),';']);
 end
 save '../results/left/label_left.mat' 'label_left'
 
data_left = A(243:273,110:138,96:113);
data_left_th = data_left>1300;
final_left=data_left_th & label_left;
 
final_data_left=false(512,512,199);
begin_row = 243;
begin_col = 110;
for i = 96: 113
    %row col 比实际的少一个
    row = 30;
    col = 28;
    final_data_left(begin_row:row+begin_row,begin_col:col+begin_col,i) = final_left(:,:,i-95);
end
save ("../results/final_data_left.mat","final_data_left");


% load ../results/test_huang/tt.mat;
load ../results/test_huang/sp.mat 
load ../results/test_huang/space.mat;

clear A bw;

 u=final_data_left;
[X,Y,Z] = meshgrid((0:511)*space(1),(0:511)*space(2),sp.PatientPositions(:,3)-min(sp.PatientPositions(:,3)));
[faces,verts,colors] = isosurface(X,max(Y(:))-Y,max(Z(:))-Z,u,0.5,Z); 
write_obj("../results/results/threshold_1300_tang1.obj",verts,faces);



%-----------------------------right---------------------------

load('../data/tt.mat');
label_right=false(36,31,18);
 for i = 110: 127
    eval([' load ../results/right/gml/label_right',num2str(i-109,'%02d'),'.mat  ']);
    eval(['label_right(:,:,',num2str(i-109,'%02d'),') = label_right(:,:,',num2str(i-109,'%02d'),') +label_right',num2str(i-109,'%02d'),';']);
 end
 save '../results/right/label_right.mat' 'label_right'
 
 data_right = A(243:278,380:410,110:127);
data_right_th = data_right>1300;
final_right=data_right_th & label_right;
 
final_data_right=false(512,512,199);
begin_row = 243;
begin_col = 380;
for i = 110: 127
    
    row = 35;
    col = 30;

    final_data_right(begin_row:row+begin_row,begin_col:begin_col+col,i) = final_right(:,:,i-109);
end
save ("../results/final_data_right.mat","final_data_right");

load ../results/test_huang/sp.mat 
load ../results/test_huang/space.mat;

clear A bw;

 u=final_data_right;
[X,Y,Z] = meshgrid((0:511)*space(1),(0:511)*space(2),sp.PatientPositions(:,3)-min(sp.PatientPositions(:,3)));
[faces,verts,colors] = isosurface(X,max(Y(:))-Y,max(Z(:))-Z,u,0.5,Z); 
write_obj("../results/results/threshold_1300_tang_right.obj",verts,faces);


