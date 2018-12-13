function obj_bldg = parse_osm_bldg_v2(filein)

%%  parse_osm_bldg();%
% 
%   $Version: 1.0$ $Date: 12/06/2018$
 
%% code history
%  v1.0: 12/06/2018: Wencheng WU

if nargin<1;filein='all_irondequoit.csv';end

data = importdata(filein);

nn1 = numel(data);
for i = 1:nn1
    cur_str = char(data(i));
    i1e = strfind(cur_str,'"[')-1;
    % string for building ID and description
    str1 = cur_str(1:i1e);
    i2s = i1e+2;
    % string for building geo-locations
    str2 = cur_str(i2s:end);
    obj_bldg(i).id = str2num(str1);
    idxstr21 = strfind(str2,'[[[');
    if numel(idxstr21) ~= 1;error('format error');end
    str2temp = str2(3:idxstr21-1);
    if isempty(str2temp)
        obj_bldg(i).description = {'NA'};
        idxstr22 = strfind(str2,']]]');
    else
        idxtemp = strfind(str2temp,''',');
        if isempty(idxtemp);
            idxtemp = strfind(str2temp,'",');
        end
%         try
        obj_bldg(i).description = cellstr(str2temp(1:idxtemp(end)-1));
%         catch
%             keyboard
%         end
        idxstr22 = strfind(str2,']]]]');
    end
    if numel(idxstr22) ~= 1;
        keyboard
        error('format error');
    end
    str3 = str2(idxstr21+1:idxstr22+1);
    obj_bldg(i).poly = parse_geoval(str3);
end


function val = parse_geoval(str3)

idxstr31 = strfind(str3,'[[');
idxstr32 = strfind(str3,']]');
n1 = numel(idxstr31);
n2 = numel(idxstr32);

if n1 ~= n2;error('format error --- val = parse_geoval(str3) ---');end

val = zeros(n1,2);
for i = 1:n1
    idxs = idxstr31(i);
    idxe = idxstr32(i)+1;
    eval(['a = ' str3(idxs:idxe) ';']);
    val(i,:) = a;
end

% drawpolygon(val)


