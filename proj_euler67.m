clear all, clc

triangle = dlmread('p067_triangle.txt')

[n_rows,n_cols] = size(triangle);

i = n_rows - 1;
for j = 1:n_cols - 1
if triangle(i,j) + triangle(i+1,j) > triangle(i,j) + triangle(i+1,j+1)
    red_dim(i,j) = triangle(i,j) + triangle(i+1,j);
else 
    red_dim(i,j) = triangle(i,j) + triangle(i+1,j+1);
end
end


for k = 2:n_rows - 1
    i = n_rows - k;
for j = 1:n_cols - k
if triangle(i,j) + red_dim(i+1,j) > triangle(i,j) + red_dim(i+1,j+1)
    red_dim(i,j) = triangle(i,j) + red_dim(i+1,j);
else 
    red_dim(i,j) = triangle(i,j) + red_dim(i+1,j+1);
end
end
end