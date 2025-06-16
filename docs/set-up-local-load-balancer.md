# Set up local LoadBalancer

## Background

service type = LoadBalancer is usually provided by cloud provider (AWS,Azure,GCP...), if you want to expose your deployment and make it accessible on your local machine, you can
1. use NodePort (map to port of node machine) - recommended if you are just debugging
2. install a LoadBalancer plugin - if you want to mimic cloud infrastructure

This doc will talk about option 2 - how to install and run a LoadBalancer if you are using Kind

## References
1. https://github.com/kubernetes-sigs/cloud-provider-kind?tab=readme-ov-file#install
2. https://kind.sigs.k8s.io/docs/user/loadbalancer/