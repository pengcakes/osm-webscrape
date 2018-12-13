clear

load debug001

obj_bldg = parse_osm_bldg_v2('all_irondequoit.csv');

figure;imshow(mosaic);hold on

latmax = max(mosaic_corner(:,2));
latmin = min(mosaic_corner(:,2));
lonmax = max(mosaic_corner(:,1));
lonmin = min(mosaic_corner(:,1));
[M,N,~] = size(mosaic);

for i = 1:numel(obj_bldg);
    yx = obj_bldg(i).poly;
    ix = round((N-1)/(lonmax-lonmin)*(yx(:,2)-lonmin))+1;
    iy = round((1-M)/(latmax-latmin)*(yx(:,1)-latmin))+M;
    drawpolygon([ix iy]);
end


