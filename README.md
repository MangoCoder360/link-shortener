# Link Shortener

## Docker Compose:

```yaml
services:
    link-shortener:
        container_name: link-shortener
        ports:
            - 8000:8000
        image: ghcr.io/mangocoder360/link-shortener:latest
```