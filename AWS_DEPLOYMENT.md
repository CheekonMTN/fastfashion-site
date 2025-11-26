# AWS Deployment Guide

This guide covers the essential changes and steps needed to deploy your Django application to AWS.

## Required Changes

### 1. Environment Variables

Set these environment variables in your AWS environment (Elastic Beanstalk, EC2, etc.):

```bash
# Required
SECRET_KEY=your-production-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com,your-eb-env.elasticbeanstalk.com

# Optional (for RDS database)
DATABASE_URL=postgresql://user:password@host:5432/dbname

# Optional (for HTTPS)
SECURE_SSL_REDIRECT=True
```

**Generate a new SECRET_KEY:**
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 2. Static Files

For AWS Elastic Beanstalk, static files are automatically collected during deployment. Make sure to run:

```bash
python manage.py collectstatic --noinput
```

This is typically done automatically by Elastic Beanstalk if you include it in your deployment configuration.

### 3. Database

**Option A: Keep SQLite (Development/Testing only)**
- Works for small projects
- Not recommended for production
- File-based, can be lost on server restart

**Option B: Use AWS RDS (Recommended for Production)**
- Set up PostgreSQL or MySQL on RDS
- Update `DATABASE_URL` environment variable
- The settings.py already supports this via `dj-database-url`

### 4. Deployment Options

#### Option A: AWS Elastic Beanstalk (Easiest)

1. **Install EB CLI:**
   ```bash
   pip install awsebcli
   ```

2. **Initialize EB:**
   ```bash
   eb init -p python-3.11 fastfashion-app
   ```

3. **Create environment:**
   ```bash
   eb create fastfashion-env
   ```

4. **Set environment variables:**
   ```bash
   eb setenv SECRET_KEY=your-key DEBUG=False ALLOWED_HOSTS=your-domain.com
   ```

5. **Deploy:**
   ```bash
   eb deploy
   ```

**Create `.ebextensions/django.config`:**
```yaml
option_settings:
  aws:elasticbeanstalk:container:python:
    WSGIPath: fastfashion.wsgi:application
  aws:elasticbeanstalk:environment:proxy:staticfiles:
    /static: staticfiles
```

#### Option B: AWS EC2 + Nginx + Gunicorn

1. **Install Gunicorn:**
   ```bash
   pip install gunicorn
   ```

2. **Add to requirements.txt:**
   ```
   gunicorn>=21.2.0
   ```

3. **Create systemd service** (`/etc/systemd/system/gunicorn.service`):
   ```ini
   [Unit]
   Description=gunicorn daemon
   After=network.target

   [Service]
   User=ubuntu
   Group=www-data
   WorkingDirectory=/home/ubuntu/fastfashion-sitegit
   ExecStart=/home/ubuntu/venv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/run/gunicorn.sock fastfashion.wsgi:application

   [Install]
   WantedBy=multi-user.target
   ```

4. **Configure Nginx** to serve static files and proxy to Gunicorn

#### Option C: AWS App Runner (Serverless)

1. Create `Procfile`:
   ```
   web: gunicorn fastfashion.wsgi:application --bind 0.0.0.0:$PORT
   ```

2. Deploy via AWS App Runner console or CLI

### 5. Security Checklist

- [ ] Set `DEBUG=False` in production
- [ ] Set a strong `SECRET_KEY` (never commit it!)
- [ ] Configure `ALLOWED_HOSTS` with your domain
- [ ] Enable HTTPS (`SECURE_SSL_REDIRECT=True`)
- [ ] Use environment variables for sensitive data
- [ ] Set up database backups (if using RDS)
- [ ] Configure security groups (firewall rules)
- [ ] Set up CloudWatch logging

### 6. Static Files with S3 (Optional but Recommended)

For better performance, serve static files from S3:

1. Install `django-storages`:
   ```bash
   pip install django-storages boto3
   ```

2. Add to `INSTALLED_APPS`:
   ```python
   INSTALLED_APPS = [
       # ... existing apps ...
       'storages',
   ]
   ```

3. Add to settings.py:
   ```python
   AWS_STORAGE_BUCKET_NAME = 'your-bucket-name'
   AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
   STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
   ```

### 7. Pre-Deployment Checklist

- [ ] Run `python manage.py collectstatic`
- [ ] Run `python manage.py migrate`
- [ ] Test locally with `DEBUG=False`
- [ ] Check `ALLOWED_HOSTS` is set correctly
- [ ] Verify environment variables are set
- [ ] Test error pages (404, 500)
- [ ] Review security settings
- [ ] Set up domain name (if applicable)
- [ ] Configure SSL certificate (for HTTPS)

### 8. Post-Deployment

1. **Create superuser:**
   ```bash
   eb ssh
   source /var/app/venv/*/bin/activate
   cd /var/app/current
   python manage.py createsuperuser
   ```

2. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

3. **Load initial data** (if needed):
   ```bash
   python manage.py loaddata initial_data.json
   ```

## Troubleshooting

### Static files not loading
- Ensure `collectstatic` runs during deployment
- Check `STATIC_ROOT` and `STATIC_URL` settings
- Verify static files are in the correct directory

### Database connection errors
- Check `DATABASE_URL` is set correctly
- Verify security groups allow database access
- Check database credentials

### 500 errors
- Check CloudWatch logs: `eb logs`
- Verify `DEBUG=False` and error pages exist
- Check environment variables are set

## Additional Resources

- [Django Deployment Checklist](https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/)
- [AWS Elastic Beanstalk Django Guide](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html)
- [Django on AWS Best Practices](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html)

