---
layout: post
title: "HydraBus presentation"
categories: blog
excerpt:
tags: []
image:
  feature:
date: 2017-08-04 16:49:25 +0200
modified: 2017-08-04 16:49:25 +0200
---

So last time, I wrote a post about the bus pirate, which had its small success. It attracted a few people and eventually, [@hydrabus][1] found it and this happened:

![twitter screenshot][2]

Needless to say that I accepted, and here we are! So, thanks a lot to [@hydrabus][1] for the proposition!

[1]: https://twitter.com/hydrabus
[2]: /images/posts/hydrabus/twitter_screenshot.png

# HydraBus:
## Overview

![HydraBus][4]

To have an idea of the size of the pcb, it is a standard [DangerousPrototypes][3] PCB, which leads to the HydraBus being the same size as the BusPirate:

![Hydrabus and buspirate][5]

Here is a list of what the HydraBus can do so far:

 * Communicate with multiple protocols: UART, SPI, I²C, JTAG, SWD, CAN…
 * Python scripting
 * Save data to micro SD card
 * USB OTG port

Also, it basically is no different from a micro-controller (STM32F415) connected to some pins, so have fun hacking it ;)

### Documentation

Hydrabus.com
Github repositories & wiki

[3]: http://dangerousprototypes.com/
[4]: /images/posts/hydrabus/hydrabus.jpg
[5]: /images/posts/hydrabus/hydrabus_buspirate.jpg

## Cables

Unlike the bus pirate, there is no standard cables for the HydraBus yet, so I just used a bunch of wire jumpers with some grabbers.

![wire jumper and grabber][6]

For the USB cable, we need a micro USB type B.

[6]: /images/posts/hydrabus/wire_jumper.jpg

# Basic setup

## Optional udev rule

For the same reason than with the bus pirate, I like to setup an udev rule for the Hydrabus, allowing for easier usage. Here is my rule: 

Create the file `/etc/udev/rules.d/98-hydrabus.rules`, containing the following:
```bash
SUBSYSTEM=="tty", ATTRS{idVendor}=="1d50", ATTRS{idProduct}=="60a7", GROUP="users", MODE="0666", SYMLINK+="hydrabus"
```

And reload the udev rules:

```bash
udevadm control --reload-rules
```

Basically, if you haven't read my post on buspirate, this rule matches the idVendor and idProduct of the Hydrabus and creates a symlink at `/dev/hydrabus`, which will become handy later on.

I noticed that there are udev rules on the Hydrafw repository on [github][hydrafw], but I don't know what they're supposed to do, so I did not use them :3

[hydrafw]: https://github.com/hydrabus/hydrafw

## Talking to your HydraBus

In order to setup a communication between your HydraBus and the computer, I personaly use PuTTY

# Usage for SPI

## Configuring the HydraBus for SPI
 
## Pinout

# JTAG with openOCD

## JTAG pinout

## OpenOCD installation and configuration

### Installation

See BP

### Configuration

HydraBus configuration for OpenOCD

# Conclusions

Thanks
Great tool

