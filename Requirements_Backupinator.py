import pkg_resources
import subprocess
import sys

def backup_installed_packages(backup_file='requirements_backup.txt'):
    try:
        with open(backup_file, 'w') as f:
            for dist in pkg_resources.working_set:
                f.write(f"{dist.project_name}=={dist.version}\n")
        print(f"Backup of installed packages saved to {backup_file}")
    except IOError as e:
        print(f"Failed to write the backup file: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred while creating the backup: {e}")
        sys.exit(1)

def uninstall_packages():
    installed_packages = pkg_resources.working_set
    packages = [dist.project_name for dist in installed_packages if dist.project_name != "pip"]

    for package in packages:
        try:
            result = subprocess.run(f"pip uninstall -y {package}", shell=True, check=True)
            if result.returncode != 0:
                print(f"Failed to uninstall {package}")
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while trying to uninstall {package}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred during the uninstallation of {package}: {e}")

def main():
    backup_installed_packages()
    uninstall_packages()

if __name__ == "__main__":
    main()
