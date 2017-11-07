# Gunicorn configuration file.

# Bind.
bind = '127.0.0.1:8081'
# Backlog.
# Number of pending connections.
backlog = 2048
# Workers.
# Number of cores * 2 + 1.
# I have 4 cores, so 4 * 2 + 1 = 9.
workers = 9
# Worker class.
worker_class = 'sync'
# Worker connections.
# Number of connections to one worker.
worker_connections = 1000
# Timeout.
# If worker doesn't notify server in
# this timeout, it will be cilled and
# changed to another worker.
timeout = 30
# Keep Alive.
# After this timeout server will close
# connection to "keep alived" client.
keepalive = 2
# Process Name.
# Used in top, htop, ps, e.t.c.
proc_name = 'ask_mmasyagin_gunicorn'
