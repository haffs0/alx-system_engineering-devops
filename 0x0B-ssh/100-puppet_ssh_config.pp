#client configuration file

exec {
 command => "echo "IdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config",
 path => '/usr/bin'
}

exec {
 command => "echo "PasswordAuthentication no" >> /etc/ssh/ssh_config",
 path => '/usr/bin'
}
