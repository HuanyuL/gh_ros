# gh_ros

## description

repo contains examples for bridging data between grasshopper and ros

- using compass fab
  - turtlesim
      - twist publisher
      - pose subcriber
   - pose and pose array publisher
- using roslibpy
    - pose publisher  
    - pose array publisher
    - set ros param
- YAML file writer: writes list of poses to a yaml file that can be parsed in ROS


## compas fab

### GH

see installation instructions [here](https://gramaziokohler.github.io/compas_fab/latest/getting_started.html)

### ROS

requires rosbridge

```bash
sudo apt install ros-noetic-rosbridge-suite
```

```bash
roslaunch rosbridge_server rosbridge_websocket.launch
```

## roslibpy

### GH

To install roslibpy follow instructions [here](https://roslibpy.readthedocs.io/en/latest/readme.html#installation). You will need to add IronPython to PATH variable for this to work. In case this does not work try the method described [here](http://wiki.bk.tudelft.nl/toi-pedia/Installing_IronPython_modules_for_Grasshopper)

### ROS

[setup](https://roslibpy.readthedocs.io/en/latest/reference/index.html#ros-setup-1)

```bash
sudo apt install ros-noetic-rosbridge-suite
```

```bash
roslaunch rosbridge_server rosbridge_websocket.launch
```

Reference

[roslibpy](https://roslibpy.readthedocs.io/en/latest/)
