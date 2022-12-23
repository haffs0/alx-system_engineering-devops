# Script that installs and configures Nginx
exec {'update':
  provider => shell,
  path     => '/usr/bin:/usr/sbin:/bin',
  command  => 'sudo apt-get -y update',
}

exec {'install':
  provider => shell,
  path     => '/usr/bin:/usr/sbin:/bin',
  command  => 'sudo apt-get -y install nginx',
}

exec {'echo_html':
  provider => shell,
  path     => '/usr/bin:/usr/sbin:/bin',
  command  => 'sudo echo "Hello World!" | sudo tee /var/www/html/index.nginx-debian.html',
}

exec {'sed_config':
  command  => 'sudo sed -i "37i location /redirect_me {\n return 301 http://www.youtube.com/watch?v=QH2-TGUlwu4;\n}\n" /etc/nginx/sites-available/default',
  provider => shell,
  path     => '/usr/bin:/usr/sbin:/bin',
}

exec {'stop':
  command  => 'sudo service nginx stop',
  provider => shell,
  path     => '/usr/bin:/usr/sbin:/bin',
}

exec {'start':
  command  => 'sudo service nginx start',
  provider => shell,
  path     => '/usr/bin:/usr/sbin:/bin',
}
