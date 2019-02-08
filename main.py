import subprocess

def mount(remote_directory, local_directory):
    retcode = subprocess.call(["/sbin/mount", "-t", "smbfs", remote_directory, local_directory])

def unmount(local_directory):
    """Unmounts the local SMB directory"""
    retcode = subprocess.call(["/sbin/umount", local_directory])

local_directory = 'path_to_local_dir'
smb_location = 'smb location'

mount(smb_location, local_directory)

input("Press any key to unmount: ")
unmount(local_directory)
