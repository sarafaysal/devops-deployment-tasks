# Apache Deployment

## Objective

Deploy a website using the Apache HTTP Server.

## Technologies Used

- Ubuntu 24.04 (WSL2)
- Apache2

## Steps Performed

1. Installed Apache2.
2. Changed Apache to use port 8081 because Nginx uses port 80.
3. Restarted the Apache service.
4. Verified the default Apache page.

## Commands Used

```bash
sudo apt install apache2
sudo service apache2 restart
sudo service apache2 status
apache2 -v
```

## Testing

- http://localhost:8081

## Result

Apache was successfully installed and configured on port 8081.

## Screenshots

- Apache Home Page
- Apache Status
- Apache Version
