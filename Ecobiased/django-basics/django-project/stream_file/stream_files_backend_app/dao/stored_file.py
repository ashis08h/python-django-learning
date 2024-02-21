from stream_files_backend_app.models import StoredFile


class StoredFileDao:
    """
    This class to perform CRUD operations to StoredFile.
    """

    def stored_file(self, name=None, file_path=None):
        """
        This method is used to save file name in database.
        :param name:
        :param file_path:
        :return:
        """
        if name and file_path:
            store_file_obj = StoredFile()
            store_file_obj.name = name
            store_file_obj.file_path = file_path
            store_file_obj.save()
