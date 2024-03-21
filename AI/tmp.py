import ray
ray.init( )
print(ray.cluster_resources())  # This should print the resources available in your Ray cluster
