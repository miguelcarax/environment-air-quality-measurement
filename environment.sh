# Postgres database env vars
export POSTGRES_HOST=postgres
export POSTGRES_PORT=5432
export POSTGRES_USER=postgres
export POSTGRES_PASSWORD=$(cat /dev/urandom | base64 | head -c 32)

# API REST env vars
export POSTGRES_API_USER=api
export POSTGRES_API_PASSWORD=$(cat /dev/urandom | base64 | head -c 32)
export POSTGRES_API_SCHEMA=api

# API Cache env vars
export REDIS_HOST=redis
export REDIS_PORT=6379
export BACKEND_HOST=api-rest
export BACKEND_PORT=5000
