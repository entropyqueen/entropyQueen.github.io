---
layout: post
title: "Bus pirate presentation"
categories: blog
excerpt:
tags: []
image:
  feature:
date: 2017-07-20 10:49:25 +0200
modified: 2017-07-20 10:49:25 +0200
---
Hello people,

for this first post, I wanted to make a small presentation of the bus pirate, which is a hardware tool I use a lot in my experimentations on IoT.

# Overview
## Bus pirate

![Bus Pirate][bus_pirate]

The bus pirate is a small hardware board that permits an easy interfacing between your computer and some of the important protocols that we found in hardware communications, such as: 
 * UART
 * JTAG/SWD
 * SPI
 * I²C
 * And more…

It is useful for debugging, reading memories, sniffing data, writing data…

It have been developed by [Dangerous Prototypes](http://dangerousprototypes.com/), you can find many resources and documentation there.
There is currently multiples versions of the bus pirate, I personally have the Bus Pirate v3.6 but the most recent one is the version 4. You can find the design improvement [here](http://dangerousprototypes.com/docs/Bus_Pirate_v4_design_overview), and a comparison between the two version [here](http://dangerousprototypes.com/docs/Bus_Pirate_v4_vs_v3_comparison).
The point that still bugs me with the v4 is that there is no support for JTAG over openOCD yet. Though it might come in a near future, I'd recommend ordering the version 3.6.

## Cables

In order to properly work with this tool, you will need at least a USB cable with a USB mini B port and a set of cables/probes to attach to the device you want to test/speak with/attack.

I use two types of probes cables: 
* One with clippers attached: ![Clipper cable][clipper_cable]
* One without, with some external clippers: ![cable without clippers][cable_without_clipper]
![clippers][clippers]

Here is the pinout of both cables:
![cable pinout][cable_pinout]

# Basic setup

udev rules
minicom / putty / picocom

# Usage for UART

pinout
setup w/ screens

# JTAG/SWD with openOCD

install openOCD
BP pinout
basic setup for BP interface
how to get your target config

# Conclusion and alternatives

In conclusion, I'd say that it is a nice tool to have to mess around IoT devices, it is easy of use, pretty cheap, and leaves room for improvement since it is open source.
However, it is slow, and I had some issues sniffing communications in I²C between a NOR memory and its micro-controller because the operating frequency of the IoT device was much higher than what the bus pirate can handle. A faster alternative called HardSploit is being developed by the French company Serma safety and security. I had the opportunity to try it during a formation, and I might make a post about it someday in the future. Currently, HardSploit have an open source community version, which costs around 300€. It's not as cheap as the bus pirate, but it is more user friendly.
Another alternative I came across on the web is the HydraBus, which seems to be pretty interesting given all the protocols it theoretically handle, the use of a Cortex M4 micro-controller and all this for only $69. Unfortunately, I couldn't test it yet.

That's all for today, see you folks!

[bus_pirate]: /images/posts/Bus_Pirate/bus_pirate.jpg "Bus Pirate"
[clipper_cable]: https://statics3.seeedstudio.com/images/probekit_LRG.jpg "Clipper Cable"
[cable_without_clipper]: /images/posts/Bus_Pirate/cable_without_clippers.jpg "Cable without clippers"
[clippers]: /images/posts/Bus_Pirate/clippers.jpg "Clippers"
[cable_pinout]: http://dangerousprototypes.com/docs/images/1/1a/Seed-cable.png "Dangerous prototypes seeed cable"

[seed_studio]: https://www.seeedstudio.com/Bus-Pirate-v3.6-universal-serial-interface-p-609.html
