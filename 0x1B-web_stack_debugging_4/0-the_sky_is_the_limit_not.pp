# Bringing the nginx limit higher

# Increase the Limit of the default file
exec{'fix--for-nginx':
command => 'sed -i "s/15/4096/" /etc/default/nginx',
path    => '/usr/local/bin/:/bin/'
}

# Restart nginx
exec{'nginx-restart':
command => 'nginx restart',
path    => '/etc/init.d/'
}
