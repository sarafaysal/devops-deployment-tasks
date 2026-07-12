# SSL Certificate Deployment using Nginx

## Objective

Configure HTTPS for the Python Employee Directory application using a self-signed SSL certificate.

## Technologies Used

- Ubuntu 24.04 (WSL2)
- Nginx
- OpenSSL
- Gunicorn
- Flask

## Steps Performed

1. Generated a self-signed SSL certificate using OpenSSL.
2. Configured Nginx to listen on port 443.
3. Added SSL certificate and private key.
4. Configured Nginx to proxy HTTPS requests to Gunicorn.
5. Reloaded Nginx and verified the configuration.

## Commands Used

```bash
openssl req -x509 -nodes -days 365 -newkey rsa:2048
sudo nginx -t
sudo service nginx reload
curl -k https://employee.local
```

## Result

The Employee Directory application is successfully accessible over HTTPS using a self-signed SSL certificate.

## Screenshots

- HTTPS Browser
- Nginx Configuration Test
- HTTPS Curl Output
- SSL Certificate Files
