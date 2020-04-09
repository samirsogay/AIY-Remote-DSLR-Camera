#!/usr/bin/env python3
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Run a recognizer using the Google Assistant Library.

The Google Assistant Library has direct access to the audio API, so this Python
code doesn't need to record audio. Hot word detection "OK, Google" is supported.

It is available for Raspberry Pi 2/3 only; Pi Zero is not supported.
"""

import logging
import platform
import subprocess
import sys

import aiy.assistant.auth_helpers
from aiy.assistant.library import Assistant
import aiy.voice.audio
from aiy.board import Board, Led
from google.assistant.library.event import EventType

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
)


def power_off_pi():
    subprocess.call('sudo shutdown now', shell=True)
    subprocess.call('timeout -k 0m 5s  /home/pi/raspidmx/pngview/pngview -b 0 -l 3 /home/pi/png/shutdown.png &', shell=True)

def reboot_pi():
    subprocess.call('sudo reboot', shell=True)
    subprocess.call('timeout -k 0m 5s  /home/pi/raspidmx/pngview/pngview -b 0 -l 3 /home/pi/png/rebooting.png &', shell=True)

def hdmi_script():
    subprocess.call('/home/pi/HDMI.sh &', shell=True)
    subprocess.call('timeout -k 0m 5s  /home/pi/raspidmx/pngview/pngview -b 0 -l 3 /home/pi/png/starting.png &', shell=True)

def hdmi_script_stop():
    subprocess.call('pkill raspivid', shell=True)
    subprocess.call('timeout -k 0m 5s  /home/pi/raspidmx/pngview/pngview -b 0 -l 3 /home/pi/png/stopping.png &', shell=True)
def photo():
    subprocess.call('irsend SEND_ONCE Sony_RMT-DSLR2 BTN_TRIGGER', shell=True)
    subprocess.call('timeout -k 0m 5s  /home/pi/raspidmx/pngview/pngview -b 0 -l 3 /home/pi/png/processing.png &', shell=True)
def photo2():
    subprocess.call('irsend SEND_ONCE Sony_RMT-DSLR2 KEY_TRIGGER_2SEC', shell=True)
    subprocess.call('timeout -k 0m 5s  /home/pi/raspidmx/pngview/pngview -b 0 -l 3 /home/pi/png/processing.png &', shell=True)
def video():
    subprocess.call('irsend SEND_ONCE Sony_RMT-DSLR2 BTN_TRIGGER_VIDEO', shell=True)
    subprocess.call('timeout -k 0m 5s  /home/pi/raspidmx/pngview/pngview -b 0 -l 3 /home/pi/png/processing.png &', shell=True)
def display():
    subprocess.call('irsend SEND_ONCE Sony_RMT-DSLR2 BTN_DISPLAY', shell=True)
    subprocess.call('timeout -k 0m 5s  /home/pi/raspidmx/pngview/pngview -b 0 -l 3 /home/pi/png/processing.png &', shell=True)
def histogram():
    subprocess.call('irsend SEND_ONCE Sony_RMT-DSLR2 BTN_HISTO', shell=True)
    subprocess.call('timeout -k 0m 5s  /home/pi/raspidmx/pngview/pngview -b 0 -l 3 /home/pi/png/processing.png &', shell=True)
def index():
    subprocess.call('irsend SEND_ONCE Sony_RMT-DSLR2 BTN_INDEX', shell=True)
    subprocess.call('timeout -k 0m 5s  /home/pi/raspidmx/pngview/pngview -b 0 -l 3 /home/pi/png/processing.png &', shell=True)
def rotate():
    subprocess.call('irsend SEND_ONCE Sony_RMT-DSLR2 BTN_ROTATE', shell=True)
    subprocess.call('timeout -k 0m 5s  /home/pi/raspidmx/pngview/pngview -b 0 -l 3 /home/pi/png/processing.png &', shell=True)
def playback():
    subprocess.call('irsend SEND_ONCE Sony_RMT-DSLR2 BTN_PLAYBACK', shell=True)
    subprocess.call('timeout -k 0m 5s  /home/pi/raspidmx/pngview/pngview -b 0 -l 3 /home/pi/png/processing.png &', shell=True)
def slideshow():
    subprocess.call('irsend SEND_ONCE Sony_RMT-DSLR2 BTN_SLIDE', shell=True)
    subprocess.call('timeout -k 0m 5s  /home/pi/raspidmx/pngview/pngview -b 0 -l 3 /home/pi/png/processing.png &', shell=True)
def trash():
    subprocess.call('irsend SEND_ONCE Sony_RMT-DSLR2 BTN_TRASH', shell=True)
    subprocess.call('timeout -k 0m 5s  /home/pi/raspidmx/pngview/pngview -b 0 -l 3 /home/pi/png/processing.png &', shell=True)
def zoomin():
    subprocess.call('irsend SEND_ONCE Sony_RMT-DSLR2 KEY_T', shell=True)
    subprocess.call('timeout -k 0m 5s  /home/pi/raspidmx/pngview/pngview -b 0 -l 3 /home/pi/png/processing.png &', shell=True)
def zoomout():
    subprocess.call('irsend SEND_ONCE Sony_RMT-DSLR2 KEY_W', shell=True)
    subprocess.call('timeout -k 0m 5s  /home/pi/raspidmx/pngview/pngview -b 0 -l 3 /home/pi/png/processing.png &', shell=True)
def menu():
    subprocess.call('irsend SEND_ONCE Sony_RMT-DSLR2 KEY_MENU', shell=True)
    subprocess.call('timeout -k 0m 5s  /home/pi/raspidmx/pngview/pngview -b 0 -l 3 /home/pi/png/processing.png &', shell=True)
def up():
    subprocess.call('irsend SEND_ONCE Sony_RMT-DSLR2 KEY_UP', shell=True)
    subprocess.call('timeout -k 0m 5s  /home/pi/raspidmx/pngview/pngview -b 0 -l 3 /home/pi/png/processing.png &', shell=True)
def down():
    subprocess.call('irsend SEND_ONCE Sony_RMT-DSLR2 KEY_DOWN', shell=True)
    subprocess.call('timeout -k 0m 5s  /home/pi/raspidmx/pngview/pngview -b 0 -l 3 /home/pi/png/processing.png &', shell=True)
def right():
    subprocess.call('irsend SEND_ONCE Sony_RMT-DSLR2 BTN_RIGHT', shell=True)
    subprocess.call('timeout -k 0m 5s  /home/pi/raspidmx/pngview/pngview -b 0 -l 3 /home/pi/png/processing.png &', shell=True)
def left():
    subprocess.call('irsend SEND_ONCE Sony_RMT-DSLR2 BTN_LEFT', shell=True)
    subprocess.call('timeout -k 0m 5s  /home/pi/raspidmx/pngview/pngview -b 0 -l 3 /home/pi/png/processing.png &', shell=True)
def select():
    subprocess.call('irsend SEND_ONCE Sony_RMT-DSLR2 BTN_SELECT', shell=True)
    subprocess.call('timeout -k 0m 5s  /home/pi/raspidmx/pngview/pngview -b 0 -l 3 /home/pi/png/processing.png &', shell=True)
def camprint():
    subprocess.call('irsend SEND_ONCE Sony_RMT-DSLR2 KEY_PRINT', shell=True)
    subprocess.call('timeout -k 0m 5s  /home/pi/raspidmx/pngview/pngview -b 0 -l 3 /home/pi/png/processing.png &', shell=True)

def process_event(assistant, event):
    
    if event.type == EventType.ON_START_FINISHED:
        
        subprocess.call('timeout -k 0m 5s  /home/pi/raspidmx/pngview/pngview -b 0 -l 3 /home/pi/png/ready.png &', shell=True)
        if sys.stdout.isatty():
            print('Say "OK, Google" then speak, or press Ctrl+C to quit...')

    elif event.type == EventType.ON_CONVERSATION_TURN_STARTED:
        
        subprocess.call('timeout -k 0m 5s  /home/pi/raspidmx/pngview/pngview -b 0 -l 3 /home/pi/png/listening.png &', shell=True)

    elif event.type == EventType.ON_RECOGNIZING_SPEECH_FINISHED and event.args:
        print('You said:', event.args['text'])
        text = event.args['text'].lower()
        if text == 'power off':
            assistant.stop_conversation()
            power_off_pi()
        if text == 'turn off':
            assistant.stop_conversation()
            power_off_pi()
        elif text == 'reboot':
            assistant.stop_conversation()
            reboot_pi()
        elif text == 'start monitor':
            assistant.stop_conversation()
            hdmi_script()
        elif text == 'stop monitor':
            assistant.stop_conversation()
            hdmi_script_stop()
        elif text == 'start display':
            assistant.stop_conversation()
            hdmi_script()
        elif text == 'stop display':
            assistant.stop_conversation()
            hdmi_script_stop()
        elif text == 'take photo':
            assistant.stop_conversation()
            photo()
        elif text == 'take photo with delay':
            assistant.stop_conversation()
            photo2()
        elif text == 'start video':
            assistant.stop_conversation()
            video()
        elif text == 'stop video':
            assistant.stop_conversation()
            video()
        elif text == 'start recording':
            assistant.stop_conversation()
            video()
        elif text == 'stop recording':
            assistant.stop_conversation()
            video()
        elif text == 'display':
            assistant.stop_conversation()
            display()
        elif text == 'histogram':
            assistant.stop_conversation()
            histogram()
        elif text == 'index':
            assistant.stop_conversation()
            index()
        elif text == 'rotate':
            assistant.stop_conversation()
            rotate()
        elif text == 'playback':
            assistant.stop_conversation()
            playback()
        elif text == 'slideshow':
            assistant.stop_conversation()
            slideshow()
        elif text == 'zoom in':
            assistant.stop_conversation()
            zoomin()
        elif text == 'zoom out':
            assistant.stop_conversation()
            zoomout()
        elif text == 'menu':
            assistant.stop_conversation()
            menu()
        elif text == 'trash':
            assistant.stop_conversation()
            trash()
        elif text == 'go up':
            assistant.stop_conversation()
            up()
        elif text == 'go down':
            assistant.stop_conversation()
            down()
        elif text == 'go right':
            assistant.stop_conversation()
            right()
        elif text == 'go left':
            assistant.stop_conversation()
            left()
        elif text == 'select':
            assistant.stop_conversation()
            select()
        elif text == 'print':
            assistant.stop_conversation()
            camprint()

    elif event.type == EventType.ON_END_OF_UTTERANCE:
        
        subprocess.call('timeout -k 0m 5s  /home/pi/raspidmx/pngview/pngview -b 0 -l 3 /home/pi/png/thinking.png &', shell=True)

    elif (event.type == EventType.ON_CONVERSATION_TURN_FINISHED
          or event.type == EventType.ON_CONVERSATION_TURN_TIMEOUT
          or event.type == EventType.ON_NO_RESPONSE):
        
        subprocess.call('timeout -k 0m 5s  /home/pi/raspidmx/pngview/pngview -b 0 -l 3 /home/pi/png/ready.png &', shell=True)

    elif event.type == EventType.ON_ASSISTANT_ERROR and event.args and event.args['is_fatal']:
        sys.exit(1)


def main():
    if platform.machine() == 'armv6l':
        print('Cannot run hotword demo on Pi Zero!')
        exit(-1)

    credentials = aiy.assistant.auth_helpers.get_assistant_credentials()
    with Assistant(credentials) as assistant:
        for event in assistant.start():
            process_event(assistant, event)


if __name__ == '__main__':
    main()
