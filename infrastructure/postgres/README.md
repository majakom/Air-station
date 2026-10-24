# PostgreSQL

PostgreSQL is managed by the root `docker-compose.yml` alongside the other local services.

## Configure

From the repository root, copy `.env.example` to `.env` and set `POSTGRES_PASSWORD` to a local password. Other variables can also be changed here from defaults.

If omitted, `POSTGRES_DB` defaults to `smarthome_postgres`, `POSTGRES_USER` to `smarthome`, and `POSTGRES_PORT` to `5432`. The password has no default and must be set.

## Start

Run from the project root:

```powershell
docker compose up -d postgres
```

## View logs in terminal (Optional)

Run from the project root:

```powershell
docker compose logs -f postgres
```

## Persistence

Database files are stored in the named Docker volume `postgres_data`, so recreating the container does not remove them. Do not run `docker compose down -v` unless you intend to delete this database volume and its data.
