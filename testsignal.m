w = dlmread('spectrum', ' ', 10, 1);

i = 1;
while (i <= size(w,1))
  if (max(abs(w(i, :))) == 0)
    w(i,:) = [];
  end
  i = i + 1;
end
imagesc(10*log(w/1000.0))