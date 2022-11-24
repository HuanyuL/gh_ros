# inputs > name/typehint/access 
#   > client/roslibpy.ROS/item
#   > param name/str/item
#   > origin/plane/item
#   > planes/plane/tree 

import math
import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import roslibpy

def publish_pose(pose):
    pose_pub = roslibpy.Topic(
        client, topic, 'geometry_msgs/Pose')
    if client is None:
        print'Client is not connected'
        return
    if client.is_connected:
        pose_pub.publish(roslibpy.Message({'position': {'x': pose[0], 'y': pose[1], 'z': pose[2]}, 'orientation': {
                         'w': pose[3], 'x': pose[4], 'y': pose[5], 'z': pose[6]}}))
    else:
        print('client is not connected')

def plane_to_pose(frame_origin, frame):

    matrix = rg.Transform.PlaneToPlane(frame_origin, frame).Transpose()
    trace = matrix.M00 + matrix.M11 + matrix.M22

    q = rg.Quaternion()

    if trace > 0.0:
        s = math.sqrt(trace + 1.0)
        q.A = s * 0.5
        s = 0.5 / s
        q.B = (matrix.M12 - matrix.M21) * s
        q.C = (matrix.M20 - matrix.M02) * s
        q.D = (matrix.M01 - matrix.M10) * s
    else:
        if matrix.M00 >= matrix.M11 and matrix.M00 >= matrix.M22:
            s = math.sqrt(1.0 + matrix.M00 - matrix.M11 - matrix.M22)
            inv_s = 0.5 / s
            q.B = 0.5 * s
            q.C = (matrix.M01 + matrix.M10) * inv_s
            q.D = (matrix.M02 + matrix.M20) * inv_s
            q.A = (matrix.M12 - matrix.M21) * inv_s
        elif matrix.M11 > matrix.M22:
            s = math.sqrt(1.0 + matrix.M11 - matrix.M00 - matrix.M22)
            inv_s = 0.5 / s
            q.B = (matrix.M10 + matrix.M01) * inv_s
            q.C = 0.5 * s
            q.D = (matrix.M21 + matrix.M12) * inv_s
            q.A = (matrix.M20 - matrix.M02) * inv_s
        else:
            s = math.sqrt(1.0 + matrix.M22 - matrix.M00 - matrix.M11)
            inv_s = 0.5 / s
            q.B = (matrix.M20 + matrix.M02) * inv_s
            q.C = (matrix.M21 + matrix.M12) * inv_s
            q.D = 0.5 * s
            q.A = (matrix.M01 - matrix.M10) * inv_s

    return [frame.OriginX/1000, frame.OriginY/1000, frame.OriginZ/1000, q.A, q.B, q.C, q.D]

publish_pose(plane_to_pose(origin,plane))