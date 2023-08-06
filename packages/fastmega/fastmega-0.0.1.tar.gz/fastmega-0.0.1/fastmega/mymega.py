from mega import Mega

"""
https://www.geeksforgeeks.org/how-to-use-mega-nz-api-with-python/
https://github.com/odwyersoftware/mega.py/blob/master/src/mega/mega.py
"""

class MyMega:
    def __int__(self, username: str, password: str) -> None:
        self.username=username
        self.password=password
        self.mega = Mega()
        self.mega = self.mega.login(
            self.username,
            self.password
        )
        self.root = self.mega.find("workspace")[0]

    def mkdir(self, dirname: str, dest: str) -> str:
        """
        Make a directory
        args:
            - dirname: directory's name
            - dest: destination path on cloud
        """
        self.mega.create_folder(
            dirname,
            dest=dest
        )
        newdir_path = self.mega.find(dirname)[0]
        return newdir_path

    def upload_file(self, src: str, dest: str):
        """
        Upload file from your local to the cloud
        args:
            - src: filename path local path
            - dest: directory path on the cloud 
        """
        resp = self.mega.upload(
            src,
            dest
        )
        file_path = self.mega.get_upload_link(resp)
        return file_path