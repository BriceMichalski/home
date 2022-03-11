def to_traefik_middleware(mdwname):
    return "kube-core-" + mdwname + "@kubernetescrd"



class FilterModule(object):
    def filters(self):
        return {
            'to_traefik_middleware': to_traefik_middleware
        }
