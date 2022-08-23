- Experimental set up: please refer to NHPA experimental setup section and THPA experimental setup guidelines.

- Application to be deployed can be found in app/ directory. 1 application deployment is deployed on each node. You should replace nodeName in the yaml file with your actual node name.

- In NHPA, HPA is enabled for each edge node in the cluster:

	+ Execute the following for each deployment (to get deployment name, use "kubectl get deployment"):

		"kubectl autoscale deployment <deployment_name> --min=3 --max=12 --cpu-percent=80"

	+ To check hpa status, use "kubectl get hpa"


*** Performance evaluation ***

- Section V_B

	+ Execute the following script on each node at the same time (must enter root) and check the pod distribution (to get service name and its cluster ip, use "kubectl get service")

		"docker run --cpus 3 --rm ricoli/hey -c <numOfConcurrentReqs> -z <duration> -n 100000 -q 50 --disable-keepalive http://serviceIP:port/hello"


- Section V_C


	+ Execute the following script on Node 1 only (must enter root) and get the response time and throughput from the output.

                "docker run --cpus 3 --rm ricoli/hey -c <numOfConcurrentReqs> -z <duration> -n 100000 -q 50 --disable-keepalive http://serviceIP:port/hello"

- Section V_D


	+ Execute the following script on each node at the same time (must enter root) and get the response time and throughput from all nodes. Note that for each traffic distribution, throughput of all node should be aggregated.

                "docker run --cpus 3 --rm ricoli/hey -c <numOfConcurrentReqs> -z <duration> -n 100000 -q 50 --disable-keepalive http://serviceIP:port/hello"

- Data and python code for the evaluation can be found in NHPA_graphs directory
