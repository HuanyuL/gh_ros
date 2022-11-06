# inputs > name/typehint/access 
#   > connect/bool/item
#   > ip/str/item
# output
#   > client/roslibpy.Ros

import rhinoscriptsyntax as rs
import roslibpy

if connect:
    c = roslibpy.Ros(host=ip, port=9090)
    c.run()
    print 'client connected %s' % c.is_connected
    client = c
