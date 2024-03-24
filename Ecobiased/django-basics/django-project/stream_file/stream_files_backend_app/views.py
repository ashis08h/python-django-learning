from django.shortcuts import render
from django.views import View
import os
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from stream_files_backend_app.dao.stored_file import StoredFileDao
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from datetime import datetime
import concurrent.futures
# Create your views here.


@method_decorator(csrf_exempt, name='dispatch')
class StreamFileView(View):
    """
    Responsible to store data into folder as well as database.
    """
    MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB

    def validate_file(self, file):
        """
        Validates file size and type.
        :param file: Uploaded file object
        :return: Tuple (valid, error_message)
        """
        if file.size > self.MAX_FILE_SIZE:
            return False, 'File size should not exceeds from 10 MB.'

        allowed_types = ['image/jpeg', 'image/png', 'application/pdf']
        if file.content_type not in allowed_types:
            return False, 'Invalid file type. Allowed types: JPEG, PNG, PDF.'

        return True, None

    def store_files_in_db(self, file_path, file_name):
        """
        Logic to store the file in the database
        :param file_path:
        :param file_name:
        :return:
        """
        StoredFileDao().stored_file(file_name, file_path)

    def post(self, request):
        """
        Post method store data into folder as well as database.
        :param request:
        :return:
        """
        if request.FILES.get('file'):
            file = request.FILES.get('file')

            # Validate the file
            is_valid, error_message = self.validate_file(file)
            if not is_valid:
                return JsonResponse({'error': error_message}, status=400)
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            file_name_with_timestamp = f"{timestamp}_{file.name}"
            file_path = os.path.join(settings.MEDIA_ROOT, file_name_with_timestamp)

            # Logic to write the file in to destination
            try:
                with open(file_path, 'wb+') as destination:
                    for chunk in file.chunks():
                        destination.write(chunk)
            except PermissionError:
                return JsonResponse({'error': 'Permission denied while writing the file.'}, status=500)
            except Exception as e:
                return JsonResponse({'error': 'Failed to write the file to the destination.', 'detail': str(e)},
                                    status=500)

            # Execute the file processing task asynchronously
            with concurrent.futures.ThreadPoolExecutor() as executor:
                executor.submit(self.store_files_in_db, file_path, file_name_with_timestamp)
            return JsonResponse({'message': 'File streamed successfully.'}, status=200)
        return JsonResponse({'error': 'No file provided.'}, status=400)

