# AIY-Remote-DSLR-Camera
Google AIY Voice controlled DSLR RIG
This project modifies a google AIY Voice Kit into a voice controlled DSLR rig. The official raspberry pi screen acts as a monitor using the B101 module from Auvidea. The tutorial video is at https://www.youtube.com/watch?v=0SB3pGDNrA0

The file structure is as below
/home/pi/HDMI.sh<br />
/etc/lirc/hardware.conf<br />
/etc/lirc/lircd.conf.d/lircd.conf<br />
/etc/lirc/lirc_options.conf<br />
/lib/systemd/system/lircd.service<br />
/lib/systemd/system/my_assistant.service<br />
/home/pi/png<br />
/home/pi/AIY-voice-kit-python/src/examples/voice/assistant_library_with_local_commands_remote.py<br />



