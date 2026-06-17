import datetime
import mimetypes
from pathlib import Path
from django.conf import settings
from django.http import FileResponse, Http404
from django.utils.http import http_date

class MediaMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 1. Ignore anything that isn't a media request
        if not request.path.startswith("/media/"):
            return self.get_response(request)

        # 2. Get the relative path
        rel_path = request.path[len("/media/"):]
        
        # 3. Basic security check: Prevent directory traversal 
        if '..' in rel_path or rel_path.startswith('/'):
            raise Http404

        # 4. Resolve the full path and check if the file exists
        full = Path(settings.MEDIA_ROOT) / rel_path
        if not full.is_file():
            raise Http404

        # 5. Serve the file directly
        return self.serve_file(full, request)

    def serve_file(self, file_path, request):
        # Swapped to Python's built-in mimetypes library for simplicity
        mime_type, _ = mimetypes.guess_type(str(file_path))
        file_size = file_path.stat().st_size
        
        response = FileResponse(
            file_path.open('rb'),
            content_type=mime_type or 'application/octet-stream'
        )
        
        # Always include these security headers
        response['Content-Length'] = file_size
        response['Content-Security-Policy'] = "default-src 'none'"
        response['X-Content-Type-Options'] = 'nosniff'
        
        # Handle download flag
        if request.GET.get('download', '').lower() in ('true', '1', 'yes'):
            response['Content-Disposition'] = f'attachment; filename="{file_path.name}"'
        
        # Smart caching based on file type
        if mime_type:
            if mime_type.startswith('image/'):
                # Cache images aggressively
                expiration = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=3)
                response['Cache-Control'] = 'public, max-age=259200'  # 3 days
                response['Expires'] = http_date(expiration.timestamp())
            elif mime_type in ['application/pdf', 'application/msword']:
                response['Cache-Control'] = 'no-store'
            else:
                # Default no-cache for other types
                response['Cache-Control'] = 'no-store'
        else:
            # Unknown file type - be conservative
            response['Cache-Control'] = 'no-store'
        
        return response