# Virtual Hosting using Nginx

## Objective

Configure Nginx Virtual Hosting to host multiple websites on a single server using different domain names.

---

## Technologies Used

- Ubuntu 24.04 (WSL2)
- Nginx
- HTML
- Windows Hosts File

---

## Websites Created

### Website 1

- Domain: `portfolio.local`
- Root Directory: `/var/www/portfolio.local`

### Website 2

- Domain: `employee.local`
- Root Directory: `/var/www/employee.local`

---

## Steps Performed

1. Created two website directories.
2. Added HTML pages for each website.
3. Created separate Nginx server blocks.
4. Enabled both virtual hosts.
5. Updated the Windows hosts file.
6. Reloaded Nginx.
7. Verified both websites opened successfully.

---

## Architecture

```
Browser
      │
      ▼
+----------------+
|     Nginx      |
+----------------+
      │
 ┌────┴────┐
 │         │
 ▼         ▼
portfolio.local    employee.local
 │                 │
 ▼                 ▼
Website 1       Website 2
```

---

## Screenshots

### Portfolio Website

![Portfolio Website](screenshots/portfolio-local.png)

### Employee Website

![Employee Website](screenshots/employee-local.png)

---

## Result

Successfully configured Nginx Virtual Hosting to serve multiple websites using different domain names on a single server.
