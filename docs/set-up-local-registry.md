# Set up local Container Registry

Why do we need a registry? - k8s worker node needs to pull and run images from registry. In order to simplify the process, we need a local registry

## Option 1. Use registry service
[Reference](https://hub.docker.com/_/registry)

Run Registry Service:
```bash
docker run -d -p {port}:5000 --name local-registry registry:2
```

with persistent storage:
```bash
docker run -d -p {port}:5000 --name local-registry -v /path/to/registry-data:/var/lib/registry registry:2
```

## Option 2. Use built-in registry in Kind

Not proven worked, you can refer to [This Page](https://kind.sigs.k8s.io/docs/user/local-registry/) for more info.

