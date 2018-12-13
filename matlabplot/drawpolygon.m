function drawpolygon(x0,colors)

%% drawpolygon(x,colors)
% 
%   $Version: 1.0$ $Date: 10/09/2018$
 
%% code history
%  v1.0: 10/09/2018: Wencheng WU

if nargin<2
    colors=[1 0 0];
end

if ~iscell(x0)
    x{1} = x0;
    x0 = x;
end

[m,n] = size(colors);
nx0 = numel(x0);
if m < nx0
    colors = repmat(colors(1,:),[nx0 1]);
end
for i = 1:nx0
    x = x0{i}(:,1);
    y = x0{i}(:,2);
    plot([x;x(1)],[y;y(1)],'color',colors(i,:),'linewidth',2);
    if ~ishold;hold;end
end
