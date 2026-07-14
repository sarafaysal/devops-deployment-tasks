# Forward Proxy using Nginx

## Objective
Configure Nginx as a Forward Proxy to forward client requests to external websites.

## Technologies Used
- Ubuntu (WSL2)
- Nginx

## Configuration
- Created a Forward Proxy server on port **8088**.
- Configured `proxy_pass` and `resolver`.
- Verified Nginx configuration.
- Tested internet access through the proxy using `curl`.

## Commands Used

```bash
sudo nginx -t
sudo service nginx reload
sudo ss -tlnp | grep 8088
curl -x http://localhost:8088 http://example.com
curl -x http://localhost:8088 http://httpbin.org/ip
```

## Result

Successfully configured and tested a Forward Proxy using Nginx.

## Screenshots

- Nginx configuration test
- Port 8088 listening
- Example Domain through proxy
- HTTPBin IP response
- Nginx Forward Proxy configuration
