%% Matlabfil for plotting av data fra Python-prosjekt
clear all
close all

%% Navn: datafil (offline eller online)
% Du kan laste inn flere .txt-filer og sammenligne.
% Bruk i så fall filename1, filename2 og data1, data2
filename = 'Offline_P02_Filtrering_01.txt';
data = ParseData(filename);


%% Legg inn verdiene dine (punktum notasjon med 'data')
figure(1)
set(0,'defaultTextInterpreter','latex');
set(0,'defaultAxesFontSize',14)
set(gcf,'Position',[100 200 800 700])

subplot(2,2,1);
plot(data.Tid,data.Temp,'LineWidth',1)
grid on
hold on
title('Målt temperatur')
xlabel('Tid [sek]')
ylabel('Temperatur [C]')
% axis([XMIN XMAX YMIN YMAX])


subplot(2,2,2);
plot(data.Tid,data.Temp_FIR,'g','LineWidth',1)
grid on
hold on
title('Temp_FIR')
xlabel('Tid [sek]')
legend('$u$','$y_1$','$y_2$','interpreter','latex')
%axis([XMIN XMAX YMIN YMAX])



subplot(2,2,3);
plot(data.Tid,data.Temp_IIR,'b','LineWidth',1)
grid on
hold on
title('Temp_IIR')
xlabel('Tid [sek]')
ylabel('[\%]')
% axis([XMIN XMAX YMIN YMAX])


