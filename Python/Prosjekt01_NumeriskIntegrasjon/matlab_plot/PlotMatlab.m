%% Matlabfil for plotting av data fra Python-prosjekt
clear all
close all

%% Navn: datafil (offline eller online)
% Du kan laste inn flere .txt-filer og sammenligne.
% Bruk i så fall filename1, filename2 og data1, data2
filename = 'P01_NumeriskIntegrasjon.txt';
data = ParseData(filename);


%% Legg inn verdiene dine (punktum notasjon med 'data')
figure(1)
set(0,'defaultTextInterpreter','latex');
set(0,'defaultAxesFontSize',14)
set(gcf,'Position',[100 200 800 700])

subplot(2,2,1);
plot(data.Tid,data.Flow,'r--o','LineWidth',1)
grid on
hold on
title('Flow')
xlabel('Tid [sek]')
ylabel('[cl/s]')
% axis([XMIN XMAX YMIN YMAX])


subplot(2,2,2);
plot(data.Tid,data.Volum,'g','Marker','.','LineWidth',1)
grid on
hold on
title('Volum')
xlabel('Tid [sek]')
ylabel('[cl]')
%axis([XMIN XMAX YMIN YMAX])


