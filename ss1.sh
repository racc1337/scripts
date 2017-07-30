#!/bin/bash
echo "URL:"
read var
youtube-dl --extract-audio --audio-format mp3 $var
read -p "Download more files? (y/n) " answer
case ${answer:0:1} in
    y|Y )
        bash ss1.sh
    ;;
    * )
        sftp -P 1234 user@10.0.0.11
    ;;
esac
