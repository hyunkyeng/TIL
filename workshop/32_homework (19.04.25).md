### 32_homework (19.04.25)

##### 데이터베이스 시딩

1. Django에서 모델의 기초 데이터베이스의 값을 제공하기 위해서는 Fixtures를 사용한다. 해당 파일은 기본적으로 각각의 app에 fixtures 폴더에 있어야하며, 파일 형식은 [       ] 이거나 [       ] 이다.

   ```python
   json, xml, yaml
   ```

2. 워크샵처럼 실제 Django에 데이터가 저장되어 있을 때, 아래의 fixtures 파일을 만들고자 한다. 사용해야하는 명령어를 작성하라.

   ```bash
   $ pip install pyyaml
   $ python manage.py dumpdata myapp.musician --format yaml > final.yaml
   ```

   ```
   python manage.py dumpdata dump_sample.json : 모델 전체 출력
   python manage.py dumpdata myapp.musician > dump_sample.json : 특정모델 출력 
   ```