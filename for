#!/bin/bash
#comooocdc
old=""
count=0
for file in $(ls /home/nas/share/CACHEDEV1/backup/Backup); do
	if [ $count -eq 0 ]; then
		old=$file
	fi
	if [ $(($file)) -lt $(($old)) ]; then
		old=$file
	fi

	sum=$((count=$count+1))
done
oldd=""
countt=0
for filee in $(ls /home/nas/share/CACHEDEV2/data/Backup); do
	if [ $countt -eq 0 ]; then
		oldd=$filee
	fi
	if [ $(($filee)) -lt $(($oldd)) ]; then
		oldd=$filee
	fi
        sum=$((countt=$countt+1))
done
archive=$(date +"%Y%m%d")
if [ $old -lt $oldd ]; then
	rm -r /home/nas/share/CACHEDEV1/backup/Backup/$old
		mkdir /home/nas/share/CACHEDEV1/backup/Backup/$archive
			sshpass -p 123 scp -r server@192.168.18.254:/home/server/Vol_1 /home/nas/share/CACHEDEV1/backup/Backup/$archive
				echo se borro $old y se creo $archive
	               else 
		rm -r /home/nas/share/CACHEDEV2/data/Backup/$oldd
			mkdir /home/nas/share/CACHEDEV2/data/Backup/$archive
				sshpass -p 123 scp -r server@192.168.18.254:/home/server/Vol_1 /home/nas/share/CACHEDEV2/data/Backup/$archive
					echo se borro $oldd y se creo $archive
fi
echo el backup ha terminado

