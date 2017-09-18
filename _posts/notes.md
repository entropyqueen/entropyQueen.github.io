Hydrabus 101
===

# Introduction

Since my last post, [@hydrabus][1] contacted me on twitter to ask for a review on the HydraBus, which I mentioned at the end of my last post.

# First contact: setting things up

## udev rules

Create the file /etc/udev/rules.d/90-hydrabus.rules

```
SUBSYSTEM=="tty", ATTRS{idVendor}=="1d50", ATTRS{idProduct}=="60a7", GROUP="users", MODE="0666", SYMLINK+="hydrabus"
```

Reload the rules :

```
sudo udevadm control --reload-rules 
```

Reset the hydrabus using the reset button.
Now you should see a device at `/dev/hydrabus`

## Putty configuration

Click Serial.
Serial line is `/dev/hydrabus`, speed is `115200`.

Save it under `Hydrabus`

Click connect.

*ADD SCREENSHOT HERE*

Or, using GNUScreen: 

```
screen /dev/hydrabus 115200
```

For my own personal use, I chose to add an alias to this command, in my .bashrc file:

```
alias hydrabus='screen /dev/hydrabus 115200'
```

So now, it really is super simple to use the device !

# First contact: discovery

## Help and system informations

The `help` command is quite straightforward:

```
> help
Available commands
   help           Available commands
   history        Command history
   clear          Clear screen
   show           Show information
   logging        Turn logging on or off
   sd             SD card management
   adc            Read analog values
   dac            Write analog values
   pwm            Write PWM
   frequency      Read frequency
   gpio           Get or set GPIO pins
   spi            SPI mode
   i2c            I2C mode
   1-wire         1-wire mode
   2-wire         2-wire mode
   3-wire         3-wire mode
   uart           UART mode
   nfc            NFC mode
   can            CAN mode
   sump           SUMP mode
   jtag           JTAG mode
   random         Random number
   flash          NAND flash mode
   debug          Debug mode
> 
```

Let's show some informations about the board: 

```
> help show 
Show information
   system
   memory
   threads
   sd
   debug
> show system
HydraFW (HydraBus) v0.8-beta-51-g248383f-dirty 2017-09-09
sysTime: 0x00625d01.
cyclecounter: 0x257e7802 cycles.
cyclecounter64: 0x00000001257e7811 cycles.
10ms delay: 1680028 cycles.

MCU Info
DBGMCU_IDCODE:0x10076413
CPUID:        0x410FC241
Flash UID:    0x57003C 0x34365111 0x39333434
Flash Size:   1024KB

Kernel:       ChibiOS 4.0.0
Compiler:     GCC 4.9.3 20150529 (release) [ARM/embedded-4_9-branch revision 227977]
Architecture: ARMv7E-M
Core Variant: Cortex-M4F
Port Info:    Advanced kernel mode
Platform:     STM32F4x5 High Performance with DSP and FPU
Board:        HydraBus 1.0
Build time:   Sep 12 2017 - 00:33:42
>
> show memory
core free memory : 23712 bytes
heap fragments   : 0
heap free total  : 0 bytes
heap free largest: 0 bytes
>
> show threads
stklimit    stack     addr refs prio     state         name
00000000 20000724 20018980    1  128  SLEEPING         main
200176b0 200176fc 200177c8    1    1     READY         idle
20017898 2001794c 20017a20    1    2     READY     usb_pump
20017af0 20017c0c 20017c78    1    2 SUSPENDED     usb_pump
20019360 2001a1a4 2001a318    1  128   CURRENT console USB1
>
> show sd
Failed to connect to SD card.
>
> show debug
Debugging is disabled.

```

## Getting into UART mode

To start uart mode, just type `uart`

```
> uart
Device: UART1
Speed: 9600 bps
Parity: none
Stop bits: 1
```

As always, `help` is available:

```
uart1> help
Configuration: uart [device (1/2)> [speed (value in bauds)] [parity (none/even/odd)] [stop-bits (1/2)]
Interaction: <read/write (value:repeat)>
   show           Show UART parameters
   trigger        Setup UART trigger
   device         UART device (1/2)
   speed          Bus bitrate
   parity         Parity (none/even/odd)
   stop-bits      Stop bits (1/2)
   read           Read byte (repeat with :<num>)
   hd             Read byte (repeat with :<num>) and print hexdump
   write          Write byte (repeat with :<num>)
   <integer>      Write byte (repeat with :<num>)
   <string>       Write string

   &              Delay 1 usec (repeat with :<num>)
   %              Delay 1 msec (repeat with :<num>)
   ~              Write a random byte (repeat with :<num>)
   bridge         UART bridge mode
   exit           Exit UART mode
uart1> speed 115200 
```

As shown in the help message, we could have configured everything in one command. But the good thing is that we can still change the parameters before doing anything.

```
uart1> speed 115200 
Final speed: 115226 bps(0.03% err)
uart1> show
Device: UART1
Speed: 115200 bps
Parity: none
Stop bits: 1
uart1> 
```

These parameter seems cool enough, let's access our RPI using UART connexion:

In order to know where to plug our cables, there is a neat option for that:

```
uart1> show pins
TX: PA9
RX: PA10
```

Connect those pins and the GND pin to the RPI board.
Keep in mind that you will need to inverse the pins (RX on the hydrabus goes to TX on the RPI and TX on the hydrabus goes to RX on the RPI)

*ADD PICTURE HERE*

```
uart1> bridge 
Interrupt by pressing user button.


Raspbian GNU/Linux 8 raspberrypi ttyAMA0

raspberrypi login: 
Raspbian GNU/Linux 8 raspberrypi ttyAMA0

raspberrypi login: pi
Password: 
Last login: Wed Jul  5 12:01:54 UTC 2017 on tty1
Linux raspberrypi 4.9.35+ #1014 Fri Jun 30 14:34:49 BST 2017 armv6l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
pi@raspberrypi:~$ id
uid=1000(pi) gid=1000(pi) groups=1000(pi),4(adm),20(dialout),24(cdrom),27(sudo),29(audio),44(video),46(plugdev),60(games),100(users),101(input),108(netdev),997(gpio),998(i2c),999(spi)
pi@raspberrypi:~$ 
```

Great we can use the Hydrabus as a UART interface to other devices!
Let's now dive a bit more into the details and possibilities with an example on how to use it as a JTAG/SWD interface 

Quit the bridge mode by pressing the button named `UBTN` on the device and then type `exit` to return to normal mode.

## JTAG/SWD using openOCD

 
