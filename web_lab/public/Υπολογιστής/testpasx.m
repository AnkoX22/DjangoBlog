clc;
clear;
% Ορίστε τις παραμέτρους χρόνου
t_start = 0;
t_end = 0.0025; % για παράδειγμα, διάρκεια 0.01 δευτερολέπτων
sampling_rate = 10000; % 10 kHz

% Δημιουργήστε τιμές χρόνου
t_values = linspace(t_start, t_end, (t_end - t_start) * sampling_rate);

% Δημιουργία του σήματος
signal = sin(4000 * 2 * pi * t_values) + sin(6000 * 2 * pi * t_values);

% Εμφάνιση του σήματος στο πεδίο του χρόνου
figure;
subplot(2, 1, 1);
plot(t_values, signal);
title('Time Domain Signal');
xlabel('Time (s)');
ylabel('Amplitude');
grid on;

% Προσθήκη παραθύρου (π.χ., παραθυράκι Hanning)
window = hanning(length(signal));
windowed_signal = signal .* window';

% Εμφάνιση του παραθυροποιημένου σήματος
subplot(2, 1, 2);
plot(t_values, windowed_signal);
title('Windowed Signal');
xlabel('Time (s)');
ylabel('Amplitude');
grid on;

% Υπολογισμός του FFT
fft_result = fft(windowed_signal);
freq = linspace(0, sampling_rate, length(fft_result));

% Εμφάνιση του φάσματος συχνοτήτων
figure;
plot(freq, abs(fft_result));
title('Fourier Transform of Windowed Signal');
xlabel('Frequency (Hz)');
ylabel('Magnitude');
grid on;
