"""
HTTPS SECURITY CONFIGURATION:

1. HTTPS Enforcement:
   - SECURE_SSL_REDIRECT: Redirects all HTTP traffic to HTTPS
   - SECURE_PROXY_SSL_HEADER: Ensures Django recognizes HTTPS behind proxy

2. HSTS Policy:
   - SECURE_HSTS_SECONDS: 1-year HSTS policy for browser enforcement
   - Includes subdomains and allows preloading for maximum security

3. Secure Cookies:
   - Session and CSRF cookies only sent over HTTPS connections

4. Security Headers:
   - X-Frame-Options: DENY (prevents clickjacking)
   - X-Content-Type-Options: nosniff (prevents MIME sniffing)
   - X-XSS-Protection: Enabled (browser XSS filter)

5. CSP Headers:
   - Restricts content loading to same origin only
   - Prevents framing entirely

REQUIREMENTS:
- SSL certificate installed on web server
- Reverse proxy configured to set X-Forwarded-Proto header
- ALLOWED_HOSTS properly configured for production domains
"""