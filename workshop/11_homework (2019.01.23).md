## 11_homework (2019.01.23)

1. 다음은 부트스트랩의 어떤 component 이며 아래와 같이 만들려면 어떤 class를 주어야 하는가.



```html
<button type="button" class="btn btn-danger">Danger</button>
```



2. 다음은 부트스트랩의 어떤 component이며 아래와 동일하게 만들어 보시오.

```html
<div class="alert alert-info" role="alert">
  Hello SSAFY ?!
```



3. 다음 빈칸을 채우시오.

"부트스트랩 그리드 시스템은 레이아웃을 ( 12 )개의 column 으로, ( 5 ) 개의 반응형 사이즈 조건을 사용하여 구축한다."



4. 아래와 같은 분할을 grid system 을 활용하여 만들어 보시오.

```html
<p></p><!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS"
        crossorigin="anonymous">
    <style>
        div {
            border: solid 1px black;
        }
        .row {
            background-color: moccasin;
        }
    </style><p></p>
</head>

<body>
    <div class="row">
        <div class="col-3">25%</div>
        <div class="col-6">50%</div>
        <div class="col-3">25%</div>
    </div>


    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"
        crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js" integrity="sha384-wHAiFfRlMFy6i5SRaxvfOCifBUQy1xHdJ/yoi7FRNXMRBu5WHdZYu1hA6ZOblgut"
        crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js" integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k"
        crossorigin="anonymous"></script>
</body>

</html>
```

