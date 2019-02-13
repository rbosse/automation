#!/bin/bash


lftp -e "user $FTP_USER_ANDROID $FTP_PWD_ANDROID; put -c -O /storage/emulated/0/3DSteroid $1;exit" -p 2121 192.168.0.186

