import numpy as np
import pyaudio
from pydub import AudioSegment, effects
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

p = pyaudio.PyAudio()
sound = AudioSegment.from_file(file='1.mp3')
left, right = sound.split_to_mono()
fr = left.frame_rate
size = len(left.get_array_of_samples())
channels = left.channels
stream = p.open(
    format=p.get_format_from_width(left.sample_width,),
    channels=channels,
    rate=fr,
    output=True
)
stream.start_stream()

fig, ax = plt.subplots()
ax.set_ylim(0, 0.5)
ax.set_axis_off()
window = int(0.02 * fr)
f = np.linspace(20, 20*1000, window // 2)
lf = ax.plot(f, np.zeros(window // 2), lw = 1)[0]

def update(frames):
    if stream.is_active():
        slice = left.get_sample_slice(frames, frames + window)
        data = slice.raw_data
        stream.write(data)
        y = np.array(slice.get_array_of_samples()) / 30000
        yft = np.abs(np.fft.fft(y)) / (window // 2)
        lf.set_ydata(yft[:window // 2])
    return [lf]

def main():
    ani = FuncAnimation(fig, update, frames=range(0, size, window), interval=0, blit=True)
    plt.show()

if __name__ == "__main__":
    main()
