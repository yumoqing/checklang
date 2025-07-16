port=$1
userid=$(id -un)
groupid=$(id -gn)
workdir=$(pwd)
package=$(basename $workdir)

cat <<EOF > $package.service
[Unit]
Wants=systemd-networkd.service

[Service]
User=$userid
Group=$groupid
WorkingDirectory=$workdir
Type=forking
ExecStart=$workdir/start.sh
ExecStop=$workdir/stop.sh
StandardOutput=append:/var/log/$package/$package.log
StandardError=append:/var/log/$package/$package.log
SyslogIdentifier=$package

[Install]
WantedBy=multi-user.target
EOF

cat <<EOF > $workdir/start.sh
#!/usr/bin/bash

$workdir/$package.env/bin/python $workdir/app/$package.py -p $port
EOF

cat <<EOF > $workdir/stop.sh
#!/usr/bin/bash

ps -ef|grep "$package.py"|grep -v grep|awk '{print("kill -9", $2)}'|sh
EOF

chmod +x $workdir/*.sh
python3 -m venv $package.env
$package.env/bin/pip install setuptools wheel
$package.env/bin/pip install -r requirements.txt
sudo mkdir /var/log/$package
sudo cp $package.service /etc/systemd/system
sudo systemctl enable $package
sudo systemctl start $package


