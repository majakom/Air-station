# Mosquitto Configuration

## 1. Configure broker address

Create `mosquitto/certificates/server/server.cnf` from `server.cnf.example` and replace the placeholder in `[alt_names]` with the broker's LAN IP address.

## 2. Generate CA

Run from the project root:

```powershell
openssl req -x509 -newkey rsa:4096 -nodes -sha256 -days 3650 -keyout mosquitto/certificates/ca/ca.key -out mosquitto/certificates/ca/ca.crt -config mosquitto/certificates/ca/ca.cnf -extensions v3_ca
```

## 3. Generate broker certificate

Generate the broker's private key and certificate signing request (CSR):

```powershell
openssl req -new -newkey rsa:2048 -nodes -sha256 -keyout mosquitto/certificates/server/server.key -out mosquitto/certificates/server/server.csr -config mosquitto/certificates/server/server.cnf
```

Sign the broker certificate using your CA:

```powershell
openssl x509 -req -in mosquitto/certificates/server/server.csr -CA mosquitto/certificates/ca/ca.crt -CAkey mosquitto/certificates/ca/ca.key -CAcreateserial -out mosquitto/certificates/server/server.crt -days 365 -sha256 -extfile mosquitto/certificates/server/server.cnf -extensions server_cert
```

## 4. Create or update MQTT user

### Create a new password file

> **Warning:** This overwrites the existing password file and removes all previously configured users

#### Docker CLI

```powershell
docker compose run --rm --entrypoint mosquitto_passwd mosquitto -c /mosquitto/config/passwd <MQTT_USERNAME>-client
```

#### Local mosquitto CLI
```powershell
mosquitto_passwd -c mosquitto/config/passwd <MQTT_USERNAME>-client
```

### Add new user or edit existing user in passwd

#### Docker CLI

```powershell
docker compose run --rm --entrypoint mosquitto_passwd mosquitto /mosquitto/config/passwd <MQTT_USERNAME>-client
```

#### Local mosquitto CLI

```powershell
mosquitto_passwd mosquitto/config/passwd <MQTT_USERNAME>-client
```

## 5. Generate client certificate

Run on the client device (or project root for testing):

```powershell
openssl req -new -newkey rsa:2048 -nodes -sha256 -keyout client.key -out client.csr -subj "/CN=<MQTT_USERNAME>-client"
```

Transfer `client.csr` to the server and sign it:

```powershell
openssl x509 -req -in client.csr -CA mosquitto/certificates/ca/ca.crt -CAkey mosquitto/certificates/ca/ca.key -CAcreateserial -out client.crt -days 365 -sha256 -extfile mosquitto/certificates/ca/ca.cnf -extensions client_cert
```

Copy `client.crt` and `ca.crt` back to the client. Keep `client.key` on the client device.

## 6. Start Mosquitto

```powershell
docker compose up -d mosquitto
```

## 7. View Mosquitto logs in terminal (Optional)

```powershell
docker compose logs -f mosquitto
```

## 8. Test the Mosquitto broker (Optional)

Test TLS client authentication, publishing, and subscribing using the `<MQTT_USERNAME>-client` certificate.

The examples below assume that:
- The broker listens on port `8883`.
- The client certificate files are available as `client.crt` and `client.key` in project root for Mosquitto CLI and in chosen path for docker CLI.
- The CA certificate file is available as `ca.crt` in `mosquitto/certificates/ca/` directory.
- The ACL allows `<MQTT_USERNAME>-client` to read and write `test/topic` or ACL is not turned on.

### Option A: Local Mosquitto CLI installation

Run these commands from the project root, with `mosquitto_pub` and `mosquitto_sub` installed.

**Terminal 1 — Subscribe:**

```powershell
mosquitto_sub -h localhost -p 8883 --cafile mosquitto/certificates/ca/ca.crt --cert client.crt --key client.key -u <MQTT_USERNAME>-client -P "<MQTT_PASSWORD>" -t "test/topic" -v
```

**Terminal 2 — Publish:**

```powershell
mosquitto_pub -h localhost -p 8883 --cafile mosquitto/certificates/ca/ca.crt --cert client.crt --key client.key -u <MQTT_USERNAME>-client -P "<MQTT_PASSWORD>" -t "test/topic" -m "Hello from Mosquitto"
```

### Option B: Docker-only CLI tools

No local Mosquitto installation is required. These commands use the Mosquitto Docker image to run the client utilities.

First, ensure the client files are accessible inside the container. There are two options:
1. **Use the existing certificates directory.** Place the files in `mosquitto/certificates/client/`. This directory is already mounted into the container through `./mosquitto/certificates:/mosquitto/certificates:ro`.
2. **Use a separate directory**. If the client files are stored elsewhere, add a volume mapping to the mosquitto service in docker-compose.yml:

```yaml
volumes:
  - ./path/to/client-certs:/mosquitto/certificates/client:ro
```
Replace ./path/to/client-certs with the actual path to your client certificate files.

**Terminal 1 — Subscribe:**

```powershell
docker compose run --rm --entrypoint mosquitto_sub mosquitto -h mosquitto -p 8883 --cafile /mosquitto/certificates/ca/ca.crt --cert /mosquitto/certificates/client/client.crt --key /mosquitto/certificates/client/client.key -u <MQTT_USERNAME>-client -P "<MQTT_PASSWORD>" -t "test/topic" -v
```

**Terminal 2 — Publish:**

```powershell
docker compose run --rm --entrypoint mosquitto_pub mosquitto -h mosquitto -p 8883 --cafile /mosquitto/certificates/ca/ca.crt --cert /mosquitto/certificates/client/client.crt --key /mosquitto/certificates/client/client.key -u <MQTT_USERNAME>-client -P "<MQTT_PASSWORD>" -t "test/topic" -m "Hello from Mosquitto"
```

### Option C: Other device

Use either method above, replacing -h with the broker's LAN IP address and updating the certificate paths to match their locations on the client device.

### Expected result

The subscriber should display:

```text
test/topic Hello from Mosquitto
```