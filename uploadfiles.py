#importing dropbox
import dropbox
import os

from dropbox.files import WriteMode

#class
class TransferData():

    #creating function
    def upload_files(self,copy_file,paste_file):

        #initializing dropbox
        dbx = dropbox.Dropbox(self.access_token)
        f = open(copy_file,'rb')
        dbx.files_upload(f.read(),paste_file)

        #using os.walk
        for root,dirs,files in os.walk(copy_file):
            print(files)
            print(root)

        #creating local path
        local_path = "/Users/win10/"

        #creating path to dropbox
        relative_path = os.path.relpath(local_path,copy_file)
        dropbox_path = os.path.join(paste_file,relative_path)

        #uploading the file
        with open(local_path,'rb') as f:
            dbx.files_upload(f.read(),dropbox_path,mode = WriteMode('overwrite'))

#creating main function
def main(self,access_token):

    #setting access token to its variable
    self.access_token = access_token

    #accepting file path from the user
    file_from = input("Enter your file path to be copied")
    file_to = input("Enter you file path to be pasted")

    #calling upload files function from transfer data class
    TransferData.upload_files(file_from,file_to)
    print("File moved successfully!")