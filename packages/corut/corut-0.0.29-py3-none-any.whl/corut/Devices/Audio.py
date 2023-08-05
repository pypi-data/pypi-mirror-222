#!/usr/bin/env python3
# -*    - coding: utf-8 -*-

"""
It is aimed to facilitate audio reading and analysis processes.
"""

__author__ = 'ibrahim CÖRÜT'
__email__ = 'ibrhmcorut@gmail.com'

import gc
import matplotlib.pyplot as plt
import pyaudio
import wave
from numpy import ndarray
from scipy.io import wavfile
from .. import print_error
from ..Decorators import try_except


class Audio:
    def __init__(self, rate=48000, channels=2, input_device_index=0, frames_per_buffer=1024):
        self.__pa = None
        self.__wave_file = None
        self.__stream = None
        self.__rate = rate
        self.__channels = channels
        self.__bit_format = pyaudio.paInt16
        self.__input_device_index = input_device_index
        self.__frames_per_buffer = frames_per_buffer

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()

    @try_except
    def __prepare_file(self, file_name):
        self.__pa = pyaudio.PyAudio()
        wave_file = wave.open(file_name, 'wb')
        wave_file.setnchannels(self.__channels)
        wave_file.setsampwidth(self.__pa.get_sample_size(self.__bit_format))
        wave_file.setframerate(self.__rate)
        return wave_file

    def __get_callback(self):
        # noinspection PyUnusedLocal
        def callback(in_data, frame_count, time_info, status):
            self.__wave_file.writeframes(in_data)
            return in_data, pyaudio.paContinue
        return callback

    def record(self, file_name, duration):
        print(f'-------------> Record ---> File Name:{file_name} --- Duration:{duration}')
        try:
            self.__wave_file = self.__prepare_file(file_name)
            try:
                self.__stream = self.__pa.open(
                    rate=self.__rate,
                    channels=self.__channels,
                    format=self.__bit_format,
                    input=True,
                    input_device_index=self.__input_device_index,
                    frames_per_buffer=self.__frames_per_buffer
                )
            except OSError as e:
                print('?'*99)
                print(f'{"?"*33} Audio Record Problem:{e}')
                print(f'{"?"*33} Check PC line inputs and Stereo connections.')
                print('?'*99)
                self.__stream = None
            if self.__stream:
                for _ in range(int(self.__rate / self.__frames_per_buffer * duration)):
                    audio = self.__stream.read(self.__frames_per_buffer)
                    self.__wave_file.writeframes(audio)
        except Exception as error:
            print_error(error, locals())
        self.stop()

    def start(self, file_name):
        print(f'-------------> Start Recording ---> File Name:{file_name}')
        try:
            self.__wave_file = self.__prepare_file(file_name)
            try:
                self.__stream = self.__pa.open(
                    rate=self.__rate,
                    channels=self.__channels,
                    format=self.__bit_format,
                    input=True,
                    input_device_index=self.__input_device_index,
                    frames_per_buffer=self.__frames_per_buffer,
                    stream_callback=self.__get_callback()
                )
            except OSError as e:
                print('?'*99)
                print(f'{"?"*33} Audio Record Problem:{e}')
                print(f'{"?"*33} Check PC line inputs and Stereo connections.')
                print('?'*99)
                self.__stream = None
            if self.__stream:
                self.__stream.start_stream()
        except Exception as error:
            print(f'-------------> ### Error!! ### Start Recording Problem:{error}')
            self.__stream = None
        return self

    @try_except
    def stop(self):
        print(f'-------------> Stop Recording')
        try:
            if self.__stream is not None:
                self.__stream.stop_stream()
                print(f'-------------> Stream Stopped')
            if self.__stream is not None:
                self.__stream.close()
                print(f'-------------> Stream Closed')
            if self.__pa is not None:
                self.__pa.terminate()
            if self.__wave_file is not None:
                self.__wave_file.close()
                print(f'-------------> Wave File Closed')
        except Exception as error:
            print_error(error, locals())
        finally:
            try:
                self.__init__()
                gc.collect()
            except Exception as e:
                print(e)
        print(f'-------------> Stop Recording Success!')

    @staticmethod
    @try_except
    def convert_pcm_to_wav(pcm_file, wav_file, channels=2, bits=16, sample_rate=44100):
        with open(pcm_file, 'rb') as f:
            pcm_data = f.read()
        print(f'PCM File read successful:{pcm_file}')
        if bits % 8 != 0:
            raise ValueError("bits % 8 must == 0. now bits:" + str(bits))
        with wave.open(wav_file, 'wb') as f:
            f.setnchannels(channels)
            f.setsampwidth(bits // 8)
            f.setframerate(sample_rate)
            f.writeframes(pcm_data)
        print('PCM file to WAV file conversion completed successfully.')

    @staticmethod
    def check_audio(file_name, limit=1000):
        print(f'-------------> Check Audio ---> File Name:{file_name} --- Limit:{limit}')
        data_min, data_max, data = 0, 0, None
        try:
            fs, data = wavfile.read(file_name)
            print(f'-------------> Wave File Read Success!')
            if isinstance(data, ndarray) and data.__len__() > 10:
                data_min, data_max = data[5:-5].min(), data[5:-5].max()
            plt.plot(data)
            plt.savefig(f'{str(file_name)[:-4]}___graphic_view.png')
            plt.close('all')
            del fs, data
            gc.collect()
            print(f'-------------> Wave File Analyze Success!')
        except Exception as error:
            print_error(error, locals())
        status = data_min < -limit and data_max > limit
        print(f'-------------> Wave File Check Status:{status}  ---> Min:{data_min}/Max:{data_max}')
        return status, data_min, data_max
