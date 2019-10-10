
---
layout: post
title: "SIGSEGv2 Little Secret Detected Writeup poem"
categories: blog
excerpt:
tags: []
image:
  feature:
date: 2019-10-10 15:11:16 +0200
modified: 2019-10-10 15:11:16 +0200
---

# Little Secret Detected Write Up

###### Introduction

On a remote server, far on a distant port  
lays an application, which will log our actions.  
Despite what you might think, there is no protection.  
we've found the error, and this is our report.  

###### Exploration

Successful connection, it then requires a name.  
What a foolish question! Cause this will be its doom.  
Next step gives us a choice, let us enter the room:  
one will `ls` the files, two will read them by name.  

###### listing

Selecting the first choice, a research prompt is shown,  
only one char allowed, why an input so small?  
But we do not need more, one star to print them all,  
others break the `system`, might be a road to pown.  

###### reading

Not many restrictions, except for permissions.  
Starting from the `old_logs`, using the dot and slash,  
we may travel the path, but in here lies no crash.  
Then with all files read, time for exploitation!  

###### Exploitation

Set the name to `-a`, for `ls` an option.  
Used as such when listing, hidden name uncovered,  
we now read this latter. With this flag recovered,  
we conclude our tale, about the solution.  

eq.

