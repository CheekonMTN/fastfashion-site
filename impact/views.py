# impact/views.py

from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from pathlib import Path
from .models import HeadlineStat

def home(request):
    stats = HeadlineStat.objects.all()
    return render(request, "impact/home.html", {"stats": stats})

def sitemap(request):
    """Generate sitemap.xml for SEO"""
    sitemap_xml = render_to_string("sitemap.xml", {
        "domain": request.build_absolute_uri("/").rstrip("/")
    })
    return HttpResponse(sitemap_xml, content_type="application/xml")

def security_txt(request):
    """Serve security.txt file"""
    base_dir = Path(__file__).resolve().parent.parent.parent
    security_txt_path = base_dir / "impact" / "static" / "impact" / ".well-known" / "security.txt"
    try:
        with open(security_txt_path, 'r') as f:
            content = f.read()
        return HttpResponse(content, content_type="text/plain")
    except FileNotFoundError:
        return HttpResponse("Contact: mailto:security@yourdomain.com\n", content_type="text/plain", status=404)
