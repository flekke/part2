import os
import shutil
import re
from modules.logger import log_error, log_info
from modules.config import *


# 데코레이터 정의
def add_missing_category(func):
    def wrapper(file_name, root_dir):
        destination_folder = None
        for category, patterns in FILE_CATEGORIES.items():
            # 기존 카테고리 매칭 확인
            if any(re.match(pattern, file_name) for pattern in patterns):
                destination_folder = os.path.join(root_dir, "..", category)
                break

        if not destination_folder:
            # 카테고리 없으면 확장자 기반으로 추가
            ext = os.path.splitext(file_name)[1][1:]
            if ext:  # 확장자가 있으면 동적 카테고리 생성
                category_name = ext
                FILE_CATEGORIES[category_name] = [rf".*\.{ext}$"]
                destination_folder = os.path.join(root_dir, "..", category_name)
                log_info(f"Added new category: {category_name}")
            else:
                # 확장자가 없으면 기본 폴더로 이동
                destination_folder = os.path.join(root_dir, "..", DEFAULT_FOLDER)

        return func(file_name, root_dir, destination_folder)

    return wrapper

# 파일 처리 함수 (데코레이터 적용)
@add_missing_category
def move_file(file_name, root_dir, destination_folder):
    file_path = os.path.join(root_dir, "..", "files", file_name)
    os.makedirs(destination_folder, exist_ok=True)
    try:
        shutil.move(file_path, os.path.join(destination_folder, file_name))
        log_info(f"Moved: {file_name} -> {destination_folder}")
    except PermissionError:
        log_error(f"Permission denied: {file_path}")
    except Exception as e:
        log_error(f"Error moving {file_name}: {str(e)}")

# 파일 정리 함수
def organize_files():
    # 루트 디렉토리 및 files 폴더 설정
    root_dir = os.path.dirname(os.path.abspath(__file__))
    files_dir = os.path.join(root_dir, "..", "files")

    # 파일 처리
    for file_name in os.listdir(files_dir):
        file_path = os.path.join(files_dir, file_name)
        if not os.path.isfile(file_path):  # 파일만 처리
            continue
        move_file(file_name, root_dir)  # 데코레이터 적용된 함수 호출

    print("File organization complete.")
    return True

if __name__ == "__main__":
    organize_files()



'''
def organize_files():
    # 루트 디렉토리 및 files 폴더 설정
    root_dir = os.path.dirname(os.path.abspath(__file__))
    files_dir = os.path.join(root_dir, "..", "files")

    # 파일 처리
    for file_name in os.listdir(files_dir):
        file_path = os.path.join(files_dir, file_name)

        # 파일만 처리
        if not os.path.isfile(file_path):
            continue

        # 분류 폴더 결정
        destination_folder = None
        for category, patterns in FILE_CATEGORIES.items():
            # 정규표현식으로 파일 이름 확인
            if any(re.match(pattern, file_name) for pattern in patterns):
                destination_folder = os.path.join(root_dir, "..", category)
                break

        if not destination_folder:
            # 기존 카테고리에 맞지 않으면 확장자 기반 폴더 생성
            ext = os.path.splitext(file_name)[1][1:]  # 확장자 추출 (e.g., "txt")
            if ext:  # 확장자가 있으면 해당 확장자 이름의 폴더 생성
                destination_folder = os.path.join(root_dir, "..", ext)
            else:
                # 확장자가 없으면 기본 폴더로 이동
                destination_folder = os.path.join(root_dir, "..", DEFAULT_FOLDER)

        # 폴더 생성 및 파일 이동
        os.makedirs(destination_folder, exist_ok=True)
        try:
            print('there')
            shutil.move(file_path, os.path.join(destination_folder, file_name))
            log_info(f"Moved: {file_name} -> {destination_folder}")
        except PermissionError:
            log_error(f"Permission denied: {file_path}")
        except Exception as e:
            log_error(f"Error moving {file_name}: {str(e)}")

    print("File organization complete.")
    return True


if __name__ == "__main__":
    organize_files()
'''
'''
def organize_files():
    # 루트 디렉토리 및 files 폴더 설정
    root_dir = os.path.dirname(os.path.abspath(__file__))
    files_dir = os.path.join(root_dir, "..", "files")

    # 파일 처리
    for file_name in os.listdir(files_dir):
        file_path = os.path.join(files_dir, file_name)

        # 파일만 처리
        if not os.path.isfile(file_path):
            continue

        # 분류 폴더 결정
        destination_folder = None
        for category, patterns in FILE_CATEGORIES.items():
            # 정규표현식으로 파일 이름 확인
            if any(re.match(pattern, file_name) for pattern in patterns):
                destination_folder = os.path.join(root_dir, "..", category)
                break

        if not destination_folder:
            # 기본 폴더 설정
            destination_folder = os.path.join(root_dir, "..", DEFAULT_FOLDER)

        # 폴더 생성 및 파일 이동
        os.makedirs(destination_folder, exist_ok=True)
        try:
            shutil.move(file_path, os.path.join(destination_folder, file_name))
            log_info(f"Moved: {file_name} -> {destination_folder}")
        except PermissionError:
            log_error(f"Permission denied: {file_path}")
        except Exception as e:
            log_error(f"Error moving {file_name}: {str(e)}")

    print("File organization complete.")
    return True

if __name__ == "__main__":
    organize_files()
'''
'''
def organize_files():
    # 루트 디렉토리 및 files 폴더 설정
    root_dir = os.path.dirname(os.path.abspath(__file__))
    files_dir = os.path.join(root_dir, "..", "files")

    # 동적 카테고리 로드
    dynamic_categories = get_dynamic_categories()

    # 파일 처리
    for file_name in os.listdir(files_dir):
        file_path = os.path.join(files_dir, file_name)

        # 파일만 처리
        if not os.path.isfile(file_path):
            continue

        # 분류 폴더 결정
        destination_folder = None
        for category, patterns in {**FILE_CATEGORIES, **dynamic_categories}.items():
            if any(re.match(pattern, file_name) for pattern in patterns):
                destination_folder = os.path.join(root_dir, "..", category)
                break

        if not destination_folder:
            destination_folder = os.path.join(root_dir, "..", DEFAULT_FOLDER)

        # 폴더 생성 및 파일 이동
        os.makedirs(destination_folder, exist_ok=True)
        try:
            shutil.move(file_path, os.path.join(destination_folder, file_name))
            log_info(f"Moved: {file_name} -> {destination_folder}")
        except PermissionError:
            log_error(f"Permission denied: {file_path}")
        except Exception as e:
            log_error(f"Error moving {file_name}: {str(e)}")

    print("File organization complete.")
    return True

if __name__ == "__main__":  
    organize_files()    
'''

'''
source_folder = r"D:\공부 관련\OsloMet\24 1학기\4200\final\part2"
destination_folder = ""

for target_file in os.listdir(source_folder):
    if target_file.endswith(".txt"):
        file_path = os.path.join(source_folder, target_file)
        destination_folder=r"D:\공부 관련\OsloMet\24 1학기\4200\final\part2\txtfiles"
        print(file_path)
        shutil.move(file_path, os.path.join(destination_folder, target_file))   
    elif target_file.endswith(".pdf"):
        file_path = os.path.join(source_folder, target_file)
        destination_folder=r"D:\공부 관련\OsloMet\24 1학기\4200\final\part2\pdffiles"
        shutil.move(file_path, os.path.join(destination_folder, target_file)) 
    elif target_file.endswith(".png"):
        file_path = os.path.join(source_folder, target_file)
        destination_folder=r"D:\공부 관련\OsloMet\24 1학기\4200\final\part2\pngfiles"
        shutil.move(file_path, os.path.join(destination_folder, target_file)) 
    else:
        file_path = os.path.join(source_folder, target_file)
        destination_folder=r"D:\공부 관련\OsloMet\24 1학기\4200\final\part2\others"
        shutil.move(file_path, os.path.join(destination_folder, target_file)) 

'''