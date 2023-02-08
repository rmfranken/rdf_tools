This repository has the sole purpose of making it easy to run linked data file conversions and shacl validations with an organized folder structure.
There is also a docker file which allows you to run the shacl validation in a virtual environment and limit its resource usage.

Inside the dockerfile you can choose between using pyShacl or TopBraid SHACL.
TopBraid shacl is superior, so is the default. Topbraid shacl also has ability to run an entire folder of instance data.


To run the dockerfile and be able to see the output:

docker run [container name]

The output (including timing of each file) should be written to terminal.
If you happen to be a DockerGod, please update this readMe if you know how to write the output to a file on local disk.

