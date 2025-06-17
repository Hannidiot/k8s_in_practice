# Set up local LoadBalancer

## Background

service type = LoadBalancer is usually provided by cloud provider (AWS,Azure,GCP...), if you want to expose your deployment and make it accessible on your local machine, you can
1. use NodePort (map to port of node machine) - recommended if you are just debugging
2. install a LoadBalancer plugin - if you want to mimic cloud infrastructure

This doc will talk about option 2 - how to install and run a LoadBalancer if you are using Kind

## Steps

1. download cloud-provider-kind from (github release pages)[https://github.com/kubernetes-sigs/cloud-provider-kind/releases]
2. follow instructions in readme file of above github repo
    1. create a kind cluster (with multiple node) - see ${project_folder}/config/kind/kind-multi-nodes.yaml
    2. remove label to make workloads not run on control plane nodes
    3. run cloud-provider-kind.exe as administrator (or it fails to start tunnel)
3. create demo service and load balancer, see ${project_folder}/config/kubectl/loadbalancer_etp_local.yaml
4. happy playing

## References
1. https://github.com/kubernetes-sigs/cloud-provider-kind?tab=readme-ov-file#install
2. https://kind.sigs.k8s.io/docs/user/loadbalancer/