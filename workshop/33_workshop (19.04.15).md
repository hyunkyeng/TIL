# 33_workshop (19.04.15)
일반적인 REST API에서 게시글(Post)에 대한 각각의 CRUD에 대응되는 HTTP methods 와 Url을 작성하시오.
기본 url : /posts/
| CRUD                | HTTP method | URL                     |
| ------------------- | ----------- | ----------------------- |
| 리소스의 목록       | GET         | `list/`                 |
| 리소스 생성         | POST        | `create/`               |
| 리소스 중 하나 표시 | GET         | `<int:post_pk>/detail/` |
| 리소스 수정         | PUT         | `<int:post_pk>/update/` |
| 리소스 삭제         | DELETE      | `<int:post_pk>/delete/` |