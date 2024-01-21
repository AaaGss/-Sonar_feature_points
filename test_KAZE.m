clc;clear;close;
I0 = imread('1111.png');
I = rgb2gray(I0);
points = detectKAZEFeatures(I);
imshow(I)
hold on
plot(selectStrongest(points,25))
hold off