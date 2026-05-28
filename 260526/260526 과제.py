import filecmp  
import os 


def get_file_info_dict(dir_path):
    """지정한 디렉토리 내 파일들의 {이름: 크기} 딕셔너리를 반환하는 함수"""
    file_data = {}
    with os.scandir(dir_path) as entries:
        for entry in entries:
            if entry.is_file():
                file_data[entry.name] = entry.stat().st_size

    return file_data

def compare_directories():
    dir1 = input("첫 번째 디렉토리 이름을 입력하세요: ")
    dir2 = input("두 번째 디렉토리 이름을 입력하세요: ")

    if not os.path.exists(dir1) or not os.path.exists(dir2):
        print("입력하신 디렉토리 중 존재하지 않는 곳이 있습니다.")
        return

    dir1_files = get_file_info_dict(dir1)
    dir2_files = get_file_info_dict(dir2)

    print("\n--- 비교 결과 보고서 ---")

    if len(dir1_files) != len(dir2_files):
        print(
            f"❌ 파일 개수가 다릅니다. ({dir1}: {len(dir1_files)}개, {dir2}: {len(dir2_files)}개)"
        )
        return 

    if set(dir1_files.keys()) != set(dir2_files.keys()):
        print("❌ 두 디렉토리의 파일 구성(이름)이 서로 다릅니다.")
        return 

    for file_name, size1 in dir1_files.items():
        size2 = dir2_files[file_name] 

        if size1 != size2:
            print(
                f"❌ [{file_name}] 파일의 크기가 다릅니다. ({size1} Bytes vs {size2} Bytes)"
            )
            return 

        path1 = os.path.join(dir1, file_name)  
        path2 = os.path.join(dir2, file_name)  

        if not filecmp.cmp(path1, path2, shallow=False):
            print(f"❌ [{file_name}] 파일의 내부 내용이 서로 다릅니다.")
            return 

    print("✅ 두 디렉토리의 파일 개수, 이름, 크기, 내용이 모두 완벽히 일치합니다!")


if __name__ == "__main__":
    compare_directories()
