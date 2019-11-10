BACKUPTIME=`date +%b-%d-%y`

DESTINATION=/root/mysite/backup/database/backup-$BACKUPTIME.tar.gz

SOURCEFILE=/root/mysite/db.sqlite3

tar -cpzf $DESTINATION $SOURCEFILE
