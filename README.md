## tensor2tensorHL

1. gym install for windows
* MSYS install(mingw terminal 실행하기 위한 패키지) minsgw(리눅스 프로그램 윈도우 빌드용)<br>
  > MSYS2 MSYS terminal<br>
  > pacman -Syu<br>
  > pacman -Su<br>
  > 환경변수 Path 추가<br>
  > C:\msys64\mingw64\bin<br>
  > C:\msys64\usr\bin
* Xming install<br>
  > 환경변수 DISPLAY 추가<br>
  > DISPLAY -> :0<br>
* Git install<br>
* python terminal<br>
  > conda create -n py36 python=3.6<br>
  > activate py36<br>
  > git clone https://github.com/j8lp/atari-py<br>
  > cd atari-py && make && python setup.py install && pip install "gym[atari]"<br>
  > 환경변수 PYTHONPATH 추가<br>
  > PYTHONPATH -> C:\atari-py:$PYTHONPATH<br>
2. problem 생성
  
  ```
  myproblem = registry.problem('my_problem2')
  myproblem.generate_data(data_dir, temp_dir, None)
  ```
3. sample 데이터 입력
  * my_problem2.py
4. hyperparameter 수정 후 training evaluation
  12시간 돌렸는데.. 번역 상태가...pc 업그레이드가 필요한듯
