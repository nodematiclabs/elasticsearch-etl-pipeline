# Elasticsearch ETL Pipelines

Installing Postgres:
```bash
helm upgrade --install quickstart oci://registry-1.docker.io/bitnamicharts/postgresql \
    --set primary.service.type=LoadBalancer \
    --set primary.service.annotations="networking.gke.io/load-balancer-type: Internal" \
    --set auth.database=elastic
export POSTGRES_PASSWORD=$(kubectl get secret --namespace default postgres-postgresql -o jsonpath="{.data.postgres-password}" | base64 -d)
```

Installing Elastic should follow the standard [installation instructions](https://www.elastic.co/guide/en/cloud-on-k8s/2.8/k8s-deploy-eck.html), but use [elastic.yaml](elastic.yaml) for the Elasticsearch instance.